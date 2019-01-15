from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        self.driver.get("http://playtogether-001-site1.htempurl.com/login")

    def create_new_vacancy(self, vacancy):
        self.driver.find_element_by_link_text(u"Мои вакансии").click()
        self.driver.find_element_by_link_text(u"Создать вакансию").click()
        self.driver.find_element_by_name("title").click()
        self.driver.find_element_by_name("title").clear()
        self.driver.find_element_by_name("title").send_keys(vacancy.title)
        self.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кого вы ищете *'])[1]/following::span[2]").click()
        self.driver.find_element_by_xpath("//html").click()

        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='x'])[1]/following::span[2]").click()

        self.driver.find_element_by_name("description").clear()
        self.driver.find_element_by_name("description").send_keys(vacancy.description)
        self.driver.find_element_by_name("minExperience").clear()
        self.driver.find_element_by_name("minExperience").send_keys(vacancy.minExperience)

        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='triphop'])[1]/following::button[1]").click()



    def destroy(self):
        self.driver.quit()