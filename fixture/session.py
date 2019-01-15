class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # driver.find_element_by_link_text(u"Выйти").click()
        self.app.driver.find_element_by_name("userName").clear()
        self.app.driver.find_element_by_name("userName").send_keys(username)
        self.app.driver.find_element_by_name("password").clear()
        self.app.driver.find_element_by_name("password").send_keys(password)
        self.app.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Вход'])[1]/following::button[1]").click()

    def logout(self):
        self.app.driver.find_element_by_link_text(u"Выйти").click()