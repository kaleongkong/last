from django.test import TestCase
from login.models import Users
from login.UsersModel import UsersModel
import unittest
import sys


SUCCESS = 1;
ERR_BAD_CREDENTIALS = -1;
ERR_USER_EXISTS = -2;
ERR_BAD_USERNAME = -3;
ERR_BAD_PASSWORD  = -4;
MAX_USERNAME_LENGTH =128
MAX_PASSWORD_LENGTH =128

class AllLoginTest(TestCase):
    def test_empty_login_user_sting(self):
	print "I'm here"
	usermodel = UsersModel()
	#print usermodel
	self.assertEqual(usermodel.login("","password"), (ERR_BAD_USERNAME,0))
    def test_long_login_user_sting(self):
	usermodel = UsersModel()
	longstring = "d"*129
	print usermodel
	self.assertEqual(usermodel.login(longstring, "password"), (ERR_BAD_USERNAME,0))

    def test_empty_login_password_sting(self):
	usermodel = UsersModel()
	self.assertEqual(usermodel.login("username",""), (ERR_BAD_PASSWORD,0))
    def test_long_login_password_sting(self):
	usermodel = UsersModel()
	longstring = "a"*129
	self.assertEqual(usermodel.login("username", longstring), (ERR_BAD_PASSWORD,0))

    def test_empty_add_user_sting(self):
	usermodel = UsersModel()
	self.assertEqual(usermodel.add("","password"), (ERR_BAD_USERNAME,0))

    def test_long_add_user_sting(self):
	usermodel = UsersModel()
	longstring = "a"*129
	self.assertEqual(usermodel.add(longstring, "password"), (ERR_BAD_USERNAME,0))

    def test_empty_add_password_sting(self):
	usermodel = UsersModel()
	self.assertEqual(usermodel.add("username", ""), (ERR_BAD_PASSWORD,0))

    def test_long_add_password_sting(self):
	usermodel = UsersModel()
	longstring = "a"*129
	self.assertEqual(usermodel.add("username", longstring), (ERR_BAD_PASSWORD,0))

    def test_repetivtive_add_user(self):
	earlieruser = Users(username= "user", password = "password")
	earlieruser.save()
	newuser = UsersModel()
	self.assertEqual(newuser.add("user", "password"), (ERR_USER_EXISTS,0))

    def test_username_password_mismatch_login(self):
	earlieruser = Users(username= "user", password = "password")
	earlieruser.save()
	newuser = UsersModel()
	self.assertEqual(newuser.login("user", "wordpass"), (ERR_BAD_CREDENTIALS,0))

    def test_success_login(self):
	earlieruser = Users(username= "user", password = "password")
	earlieruser.save()
	newuser = UsersModel()
	self.assertEqual(newuser.login("user", "password"), (SUCCESS,2))

    def test_success_add(self):
	newuser = UsersModel()
	self.assertEqual(newuser.add("user", "password"), (SUCCESS,1))










	



