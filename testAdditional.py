"""
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib

class TestUnit(testLib.RestTestCase):
    """Issue a REST API request to run the unit tests, and analyze the result"""
    def testUnit(self):
        respData = self.makeRequest("/TESTAPI/unitTests", method="POST")
        self.assertTrue('output' in respData)
        print ("Unit tests output:\n"+
               "\n***** ".join(respData['output'].split("\n")))
        self.assertTrue('totalTests' in respData)
        print "***** Reported "+str(respData['totalTests'])+" unit tests. nrFailed="+str(respData['nrFailed'])
        # When we test the actual project, we require at least 10 unit tests
        minimumTests = 10
        if "SAMPLE_APP" in os.environ:
            minimumTests = 4
        self.assertTrue(respData['totalTests'] >= minimumTests,
                        "at least "+str(minimumTests)+" unit tests. Found only "+str(respData['totalTests'])+". use SAMPLE_APP=1 if this is the sample app")
        self.assertEquals(0, respData['nrFailed'])


        
class TestAddUser(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)

class TestLoginUser(testLib.RestTestCase):

    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):

        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 2)


class TestAddExistedUser(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_USER_EXISTS)


class TestLoginBadCredentialsUser(testLib.RestTestCase):
    def assertResponse(self, respData, errCode = testLib.RestTestCase.SUCCESS):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'wordpass'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

class TestAddNullUsername(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	respData=self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)


class TestAddTooLongUsername(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	longname = 'a'*129
	respData=self.makeRequest("/users/add", method="POST", data = { 'user' : longname, 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)


class TestAddNullUserpassword(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	respData=self.makeRequest("/users/add", method="POST", data = { 'user' : 'username', 'password' : ''} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)

class TestAddTooLongUserpassword(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	longname = 'a'*129
	respData=self.makeRequest("/users/add", method="POST", data = { 'user' : 'username', 'password' : longname} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)



class TestLoginNullUsername(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	respData=self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)


class TestLoginTooLongUsername(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	longname = 'a'*129
	respData=self.makeRequest("/users/login", method="POST", data = { 'user' : longname, 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)


class TestLoginNullUserpassword(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	respData=self.makeRequest("/users/login", method="POST", data = { 'user' : 'username', 'password' : ''} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)

class TestLoginTooLongUserpassword(testLib.RestTestCase):
    def assertResponse(self, respData, errCode):

        expected = { 'errCode' : errCode }
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
	longname = 'a'*129
	respData=self.makeRequest("/users/login", method="POST", data = { 'user' : 'username', 'password' : longname} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)










    
