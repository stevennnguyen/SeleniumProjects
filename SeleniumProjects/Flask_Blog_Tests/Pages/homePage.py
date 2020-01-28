class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.login_link_linkText = "Login"
        self.account_link_linkText = "Account"

    def click_login(self):
        self.driver.find_element_by_link_text(self.login_link_linkText).click()

    def click_account(self):
        self.driver.find_element_by_link_text(self.account_link_linkText).click()