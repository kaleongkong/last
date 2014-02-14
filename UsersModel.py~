from login.models import Users

SUCCESS = 1;
ERR_BAD_CREDENTIALS = -1;
ERR_USER_EXISTS = -2;
ERR_BAD_USERNAME = -3;
ERR_BAD_PASSWORD  = -4;
MAX_USERNAME_LENGTH =128
MAX_PASSWORD_LENGTH =128
class UsersModel(object):

    def login(self, input_name, input_pw):
	print input_name
        print input_pw
	existed_users = Users.objects
	err_code = SUCCESS
	count = 0
	#print existed_users.get(username = input_name)
	if invalidusername(input_name) or input_name =="" or len(input_name)==0:
	    print "here1"
	    err_code = ERR_BAD_USERNAME
	    return (err_code, count)
	if invalidpassword(input_pw)or input_pw =="" or len(input_pw)==0:
	    print "here2"
	    err_code = ERR_BAD_PASSWORD
	    return (err_code, count)
	try:
	    existed_user= existed_users.get(username = input_name);
	    if input_pw == existed_user.password:
	        existed_user.increment()
	        count = existed_user.count
	    else:
		err_code = ERR_BAD_CREDENTIALS
	except:
	    err_code = ERR_BAD_CREDENTIALS
        return (err_code, count)


    def add(self,uname, pword):
	err_code = SUCCESS
	count = 0
	existed_users = Users.objects
	print "hello"
	print existed_users 
	print invalidusername(uname)
	if invalidusername(uname) or uname =="" or len(uname)==0:
	    err_code = ERR_BAD_USERNAME
	    return (err_code, count)
	if invalidpassword(pword)or pword =="" or len(pword)==0:
	    err_code = ERR_BAD_PASSWORD
	    return (err_code, count)
	print existed_users.filter(username = uname)
        print existed_users.filter(username = uname)==[]
	if len(existed_users.filter(username = uname))==0: # user doesn't exist before  
	   user = Users(username = uname, password = pword)
	   user.save()
	   count = user.count
	else:
	   err_code = ERR_USER_EXISTS
	return (err_code, count)

    def TESTAPI_resetFixture(self):
	Users.objects.all().delete()
	return (SUCCESS, 1)
	
def invalidusername(name):
     if(len(name)>MAX_USERNAME_LENGTH):
	return True
     else:
	return False

def invalidpassword(password):
     if(len(password)>MAX_PASSWORD_LENGTH):
	return True
     else:
	return False
