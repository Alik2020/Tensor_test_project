from selenium.webdriver.common.by import By
from pages.about import AboutPage

class TensorPage:
    def __init__(self, driver):
        self.driver = driver

    def force_in_people_search(self):
        elements = self.driver.find_elements(By.XPATH, "//p[text()='Сила в людях']")
        return len(elements) == 1

    def force_about(self):
        links = self.driver.find_elements(By.CLASS_NAME, 'tensor_ru-Index__link')
        links[1].click()
        return AboutPage(self.driver)

