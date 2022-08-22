from unittest import result
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import page
import json
import time

# Shopee elements
class ShopeeElements():
    logo = (By.XPATH, "//svg[contains(@class,'icon-shopee-logo')]")
    button_language = (By.XPATH, "//button[contains(text(), 'English')]")
    button_popup = (By.XPATH, "//div[@class = 'shopee-popup__close-btn']")
    #button_popup = (By.XPATH, ".//div[contains(@class,'shopee-popup__close-btn')]")
    search_box = (By.XPATH, "//input[contains(@class,'shopee-searchbar-input__input')]")
    button_search = (By.XPATH, "//button[contains(@class,'btn btn-solid-primary btn--s btn--inline')]")
    shadow_host_root = (By.XPATH, "//shopee-banner-popup-stateful[contains(@spacekey, 'PC-TH-HOME')]")
    
    # Have to use .// for find a child element
    search_results = (By.XPATH, "//div[contains(@class,'result__items')]")
    product_name = (By.XPATH, ".//div[contains(@class, '_10Wbs- _2STCsK _3IqNCf')]")
    ## search_results = (By.XPATH, "//div[contains(@class, 'col-xs-2-4 shopee-search-item-result__item')]")
    images = (By.XPATH, ".//img[contains(@class, 'mxM4vG _2GchKS')]")
    prices = (By.XPATH, ".//span[contains(@class, '_29R_un')]")

class ShopeeHome(page.Page):
    def open(self):
        self.url = 'https://shopee.co.th/'
        self.maximize_window()
        self.open_browser(self.url)

    def close_language_selection(self):
        if(self.check_element_exist(*ShopeeElements.button_language)):
            button_select_language = self.find_element(*ShopeeElements.button_language)
            self.wait_element_visible(button_select_language)
            button_select_language.click()
        else:
            print("Does not found the select language page")

    def close_popup(self):
        # It's in shadow root.
        try:
            close_btn = self.driver.execute_script('return document.querySelector("#main shopee-banner-popup-stateful").shadowRoot.querySelector("div.home-popup__close-area div.shopee-popup__close-btn")')
            close_btn.click()
            print('Clicked successfully')
        except:
            print('Could not clicked')
            pass

    def close_popup_shadow(self):
        # shadow_host = self.find_element(*(By.XPATH, "//shopee-banner-popup-stateful"))
        
        # shadow_root = self.find_root_shadow(shadow_host)
        # print(shadow_root)
        # button = shadow_root.find_element(By.CSS_SELECTOR, 'div.shopee-popup__close-btn') 
        # print(button)
        # a = 1
        # button.click()

        button = self.find_shadow_element('div.shopee-popup__close-btn')
        button.click()

    def search_items(self,msg):
        search_box = self.find_element(*ShopeeElements.search_box)
        self.wait_element_visible(search_box)
        search_box.send_keys(msg)
        search_box.send_keys(Keys.ENTER)

    def get_search_results(self):

        price_list = []
        image_list = []

        # Slow scroll to the end of the page to load all elements properly
        self.scroll_slow_to_end()

        results = self.find_element(*ShopeeElements.search_results)

        print(results.get_attribute("class"))
        
        # names = [item.find_element(*ShopeeElements.product_name).text for item in results]

        names = results.find_elements(*ShopeeElements.product_name)

        for name in names:
            print(name.text)

        
        for item in results:
            image = item.find_element(*ShopeeElements.images)
            image_list.append(image.get_attribute("src"))
            # image_list.append(image.get_attribute("src"))
            

            prices = item.find_elements(*ShopeeElements.prices)
            price_list.append(prices[-1].text)

        print(image_list)
        


        # for item in results:
            
        #     name = self.find_element(item, *ShopeeElements.product_name)
        #     print(name.text)
        ##

        # item_names = []
        # self.scroll_slow_to_end()
        # names = self.find_elements(*ShopeeElements.product_name)
        # item_names = [name.text for name in names]
        # print(item_names)            

    def get_products_name(self):
        product_names = self.find_elements(*ShopeeElements.product_name)
        print(len(product_names))
        for name in product_names:
            print(name.text)

    def read_items(self, path):
        with open(path) as data_json:
            data = json.load(data_json)
            print(data)