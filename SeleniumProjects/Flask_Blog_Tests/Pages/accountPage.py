class AccountPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "username"
        self.email_textbox_id = "email"

    def check_valid_username(self):
        return self.driver.find_element_by_id(self.username_textbox_id).get_attribute("value")

    def check_valid_email(self):
        return self.driver.find_element_by_id(self.email_textbox_id).get_attribute("value")