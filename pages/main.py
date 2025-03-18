from selenium.webdriver.common.by import By
from pages.contacts import ContactsPage

class MainPage:
    url = "https://saby.ru"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def contacts(self):
        self.driver.find_element(By.CLASS_NAME, 'sbisru-Header__menu-item-1').click()

    def offices(self):
        self.driver.find_element(By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon').click()
        return ContactsPage(self.driver)
