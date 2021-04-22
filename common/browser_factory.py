from selenium import webdriver
from fake_useragent import UserAgent

class Browser():
    def __init__(self, driver_path, is_option, is_headless):
        self.option = webdriver.ChromeOptions()

        useragent = UserAgent(verify_ssl=False)

        if(is_option == True):
            self.option.add_argument('--incognito')
            self.option.add_argument('disable-notifications')
            self.option.add_argument('--disable-infobars')
            self.option.add_argument('start-maximized')
            self.option.add_argument('disable-infobars')
            self.option.add_argument(f'user-agent={useragent.random}')
            self.option.add_argument('--disable-gpu') #Why it necessary?

        if(is_headless == True):
            self.option.add_argument('--headless')

        self.driver = webdriver.Chrome(executable_path=r'' + driver_path,options = self.option)     

    def get_driver(self):
        return self.driver   