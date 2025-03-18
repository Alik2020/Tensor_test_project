from selenium.webdriver.common.by import By
from pages.tensor import TensorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def tensor(self):
        self.driver.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return TensorPage(self.driver)
    
    def check_region(self):
        region = self.driver.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser")
        return region.text
    
    def check_partners(self):
        partners = self.driver.find_elements(By.CLASS_NAME, "controls-ListViewV__itemsContainer")
        return len(partners) > 0
    
    def get_partners_text(self):
        partners = self.driver.find_elements(By.CLASS_NAME, "controls-ListViewV__itemsContainer")
        return [x.text for x in partners]
    
    def change_region_check(self, xpath, name):
        self.driver.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser__text").click()
        self.driver.find_element(By.XPATH, xpath).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "sbis_ru-Region-Chooser__text"), name))
        region = self.driver.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
        return region.text == name
    
    def check_reg_in_url(self, reg_url_name):
        return reg_url_name in self.driver.current_url
    
    def check_reg_in_title(self, reg_title_name):
        return reg_title_name in self.driver.title


        
