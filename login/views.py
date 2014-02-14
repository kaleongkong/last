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

#11
#import pdb;pdb.set_trace()


SUCCESS = 1;
ERR_BAD_CREDENTIALS = -1;
ERR_USER_EXISTS = -2;
ERR_BAD_USERNAME = -3;
ERR_BAD_PASSWORD  = -4;

@csrf_exempt
def add(request):
    print "add"
    data = None
    uname = None
    pword = None
    user = None
    errCode = "errCode"
    count = 0
    err_code = SUCCESS
    
    if request.is_ajax() and request.method == "POST":
        data = json.loads(request.body)
        print 'Raw Data: "%s"' % data
        uname = data['user']
	pword = data['password']
	usermodel = UsersModel()
	add_result = usermodel.add(uname, pword)
	print add_result
	err_code = add_result[0]
	count = add_result[1]
        if err_code == SUCCESS:
    	    jsonresponse = json.dumps({errCode:err_code, 'count': count})
    	    return HttpResponse(jsonresponse, mimetype="application/json");
        else:
	    jsonresponse = json.dumps({errCode:err_code})
    	    return HttpResponse(jsonresponse, mimetype="application/json");
    else:
	return client(request)

@csrf_exempt
def login(request):
    print "login"
    data = None
    input_name = None
    input_pw = None
    existed_user = None
    jsonreponse = None
    errCode = "errCode"
    err_code = SUCCESS
    count = 0
    if request.is_ajax() and request.method == "POST":
	data = json.loads(request.body)
        print 'Raw Data: %s"' % data
	input_name = data['user']
        input_pw = data['password']
	print input_name
	print input_pw
	usermodel = UsersModel()
	add_result = usermodel.login(input_name, input_pw)
	print "finish usermodel login"
	err_code = add_result[0]
	count = add_result[1]
	print err_code
	print count    
        if err_code == SUCCESS:
    	    jsonresponse = json.dumps({errCode:err_code, 'count': count})
    	    return HttpResponse(jsonresponse, mimetype="application/json");
        else:
	    jsonresponse = json.dumps({errCode:err_code})
    	    return HttpResponse(jsonresponse, mimetype="application/json");
    return client(request)


def client(request):
    print "yes"
    print request.is_ajax()
    print request.method
    return render(request, 'login/client.html', {})

@csrf_exempt
def reset(request):
    Users.objects.all().delete()
    return HttpResponse( json.dumps({"errCode":1, 'count': 1}), mimetype="application/json")

