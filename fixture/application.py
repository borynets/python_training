from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.vacancy import VacancyHelper

class Application:
    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.vacancy = VacancyHelper(self)

    def open_home_page(self):
        self.driver.get("http://playtogether-001-site1.htempurl.com/login")


    def destroy(self):
        self.driver.quit()