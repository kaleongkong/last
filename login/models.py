from django.db import models
import datetime
from django.utils import timezone

SUCCESS = 1;
ERR_BAD_CREDENTIALS = -1;
ERR_USER_EXISTS = -2;
ERR_BAD_USERNAME = -3;
ERR_BAD_PASSWORD  = -4;
MAX_USERNAME_LENGTH =128
MAX_PASSWORD_LENGTH =128

class Users(models.Model):
    
    username = models.CharField(max_length = MAX_USERNAME_LENGTH, primary_key= True)
    password = models.CharField(max_length = MAX_PASSWORD_LENGTH)
    count = models.IntegerField(default = 1)
    
    def __str__(self):
	return self.username

    def printuserlist(self):
	userlist = Users.objects.all()
	for u in userlist:
	    print u
    
    def increment(self):
	self.count +=1
	self.save()

