class VacancyHelper:

    def __init__(self, app):
        self.app = app


    def create(self, vacancy):
        self.app.driver.find_element_by_link_text(u"Мои вакансии").click()
        self.app.driver.find_element_by_link_text(u"Создать вакансию").click()
        self.app.driver.find_element_by_name("title").click()
        self.app.driver.find_element_by_name("title").clear()
        self.app.driver.find_element_by_name("title").send_keys(vacancy.title)
        self.app.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Кого вы ищете *'])[1]/following::span[2]").click()
        self.app.driver.find_element_by_xpath("//html").click()

        self.app.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='x'])[1]/following::span[2]").click()

        self.app.driver.find_element_by_name("description").clear()
        self.app.driver.find_element_by_name("description").send_keys(vacancy.description)
        self.app.driver.find_element_by_name("minExperience").clear()
        self.app.driver.find_element_by_name("minExperience").send_keys(vacancy.minExperience)

        self.app.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='triphop'])[1]/following::button[1]").click()