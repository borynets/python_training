# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from vacancy import Vacancy

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_test_case(self, username="romanovaua189@gmail.com", password ="123456"):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username, password)
        vacancy = Vacancy(title="Test tile", description="Test decsiprtion", minExperience=2);
        self.create_new_vacancy(driver, vacancy) 
        driver.find_element_by_link_text(u"Выйти").click()

    def open_home_page(self, driver):
        driver.get("http://playtogether-001-site1.htempurl.com/login")

    def login(self, driver, username, password):
        # driver.find_element_by_link_text(u"Выйти").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Вход'])[1]/following::button[1]").click()

    def create_new_vacancy(self, driver, vacancy):
        driver.find_element_by_link_text(u"Мои вакансии").click()
        driver.find_element_by_link_text(u"Создать вакансию").click()
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(vacancy.title)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кого вы ищете *'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//html").click()


        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='x'])[1]/following::span[2]").click()

        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys(vacancy.description)
        driver.find_element_by_name("minExperience").clear()
        driver.find_element_by_name("minExperience").send_keys(vacancy.minExperience)


        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='triphop'])[1]/following::button[1]").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
