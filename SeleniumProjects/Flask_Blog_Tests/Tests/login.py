from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Flask_Blog_Tests.Pages.homePage import HomePage
from Flask_Blog_Tests.Pages.loginPage import LoginPage
from Flask_Blog_Tests.Pages.accountPage import AccountPage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/stovin/PycharmProjects/Selenium/Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        """
        1. From the home page, click the Login button.
        2. From the login page, fill out the email and password fields.
        3. Click login.
        4. Validate that you are redirected to the account page, therefore successfully logged in.
        """
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        homepage = HomePage(driver)
        homepage.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("test@test.com")
        login.enter_password("test")
        login.click_login()
        time.sleep(2)

        homepage.click_account()
        time.sleep(2)

        accountpage = AccountPage(driver)
        username = accountpage.check_valid_username()
        self.assertEqual(username, "test1")

        email = accountpage.check_valid_email()
        self.assertEqual(email, "test@test.com1")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/stovin/PycharmProjects/SeleniumProjects/Reports"))
