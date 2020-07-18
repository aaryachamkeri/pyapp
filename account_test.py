import unittest
import account as AccountClass

class Test(unittest.TestCase):
    accinfo = AccountClass.account()
    
    def test_check_passwd_length(self):
        print("Checking possible passwords")
        passwordList = ["bubbleboy", "tintin123", "agnipath1", "goldengate"]
        
        for passwd in passwordList:
            print("checking password %s" % passwd)
            passinfo = self.accinfo.check_password_length(passwd)
            self.assertTrue(passinfo)

if __name__ == '__main__':
    unittest.main()

