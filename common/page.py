from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

class Page():
    def __init__(self, driver):
        self.driver = driver

    def maximize_window(self):
        self.driver.maximize_window()

    def open_browser(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

    def close_tab(self):
        self.driver.close()

    def wait(self, waiting_time=5):
        # Waiting time in seconds
        time.sleep(waiting_time)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def maximize_window(self):
        self.driver.maximize_window()

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)

    # def find_child_element(self, element, *locator):
    #     return element.find_element(*locator)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element_visible(self,element):
        wait = WebDriverWait(self.driver,10)
        wait = wait.until(ec.visibility_of(element))

    def wait_element_clickable(self, element):
        wait = WebDriverWait(self.driver,10)
        wait = wait.until(ec.element_to_be_clickable(element))

    def wait_element_selected(self, element):
        wait = WebDriverWait(self.driver,10)
        wait = wait.until(ec.element_to_be_selected(element))

    def select_dropdown_item(self,option,dropdown):
        pass

    def check_element_exist(self,*locator):
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_slow_to_end(self):
        height = self.driver.execute_script("return document.body.scrollHeight")
        
        for step in range(0, height, int(height/30)):
            self.driver.execute_script(f"window.scrollTo(0, {step});")
            self.wait(0.5)