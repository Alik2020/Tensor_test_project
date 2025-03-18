from selenium.webdriver.common.by import By

class AboutPage:
    def __init__(self, driver):
        self.driver = driver
    
    def check_url(self, url):
        return url == self.driver.current_url

    def get_image_sizes(self):
        imgs = self.driver.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image-filter')
        return [img.size for img in imgs]
    
