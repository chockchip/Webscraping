from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import page

# Google element
class GoogleElements():
    search_box_element = (By.XPATH, "//input[@name='q']")
    search_button_element = (By.XPATH,"//input[@name='btnK']")

class GoogleHome(page.Page):
    def open(self):
        self.url = 'https://www.google.com'
        self.open_browser(self.url)

    def search_text(self,msg):
        search_box = self.find_element(*GoogleElements.search_box_element)
        self.wait_element_visible(search_box)
        search_box.send_keys(msg)
        search_box.send_keys(Keys.ENTER)
    
    def button_search_click(self):
        search_button = self.find_element(*GoogleElements.search_button_element)
        self.wait_element_visible(search_button)
        search_button.click()
