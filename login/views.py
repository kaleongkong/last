from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.http import Http404
from django.utils import simplejson as json
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
#from login.models import Poll, Choice
from login.models import Users
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from login.UsersModel import UsersModel
import subprocess
from login.tests import AllLoginTest
import unittest


#11
#import pdb;pdb.set_trace()


SUCCESS = 1;
ERR_BAD_CREDENTIALS = -1;
ERR_USER_EXISTS = -2;
ERR_BAD_USERNAME = -3;
ERR_BAD_PASSWORD  = -4;

@csrf_exempt
def add(request):
    #print "add"
    data = None
    uname = None
    pword = None
    user = None
    errCode = "errCode"
    count = 0
    err_code = SUCCESS
    
    if request.method == "POST":
	if not('application/json' in request.META['CONTENT_TYPE']):
	    return client(request)
        data = json.loads(request.body)
        print 'Raw Data: "%s"' % data
        uname = data['user']
	pword = data['password']
	usermodel = UsersModel()
	add_result = usermodel.add(uname, pword)
	#print add_result
	err_code = add_result[0]
	count = add_result[1]
        if err_code == SUCCESS:
    	    jsonresponse = json.dumps({errCode:err_code, 'count': count})
    	    return HttpResponse(jsonresponse, content_type="application/json");
        else:
	    jsonresponse = json.dumps({errCode:err_code})
    	    return HttpResponse(jsonresponse, content_type="application/json");
    else:
	print "OMG"
	return client(request)

@csrf_exempt
def login(request):
    #print "login"
    data = None
    input_name = None
    input_pw = None
    existed_user = None
    jsonreponse = None
    errCode = "errCode"
    err_code = SUCCESS
    count = 0
    if request.method == "POST":
	print request
	print "isPost"
	if not('application/json' in request.META['CONTENT_TYPE']):
	    return client(request)
	data = json.loads(request.body)
        #print 'Raw Data: %s"' % data
	input_name = data['user']
        input_pw = data['password']
	#print input_name
	#print input_pw
	usermodel = UsersModel()
	add_result = usermodel.login(input_name, input_pw)
	#print "finish usermodel login"
	err_code = add_result[0]
	count = add_result[1]
	#print err_code
	#print count    
        if err_code == SUCCESS:
	    print "success"
    	    jsonresponse = json.dumps({errCode:err_code, 'count': count})
    	    return HttpResponse(jsonresponse, content_type="application/json");
        else:
	    print "not success"
	    jsonresponse = json.dumps({errCode:err_code})
    	    return HttpResponse(jsonresponse, content_type="application/json");
    return client(request)


def client(request):
    #print "yes"
    #print request.is_ajax()
    #print request.method
    return render(request, 'login/client.html', {})

@csrf_exempt
def reset(request):
    if request.method == "POST":
	if request.META['CONTENT_TYPE']=='application/json':
    	    Users.objects.all().delete()
            return HttpResponse( json.dumps({"errCode":1}), content_type="application/json")
    
    return client(request)

@csrf_exempt
def unittests(request):
    response = {}
    if request.method == "POST":
	
	p = subprocess.Popen(["python","manage.py", "test", "login"], stdout= subprocess.PIPE, stderr = subprocess.PIPE, stdin =subprocess.PIPE)
	out, err = p.communicate()
	num_tests_break_list = err.split("Ran ")
	totalTests = num_tests_break_list[1].split()[0]
	nrFailed = 0
	if "failures=" in err:
	    nrFailed_break_list = err.split("failures=")
	    nrFailed = nrFailed_break_list[1].split(")")[0]
	    
	response = {"totalTests":int(totalTests), "nrFailed": int(nrFailed), "output":err}
	print response
    return HttpResponse( json.dumps(response), content_type="application/json")
    














