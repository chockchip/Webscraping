from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import page

# Shopee elements
class ShopeeElements():
    logo = (By.XPATH, "//svg[contains(@class,'icon-shopee-logo')]")
    button_language = (By.XPATH, "//button[contains(@class,'shopee-button-outline shopee-button-outline--primary-reverse ')]")
    button_popup = (By.XPATH, "//div[contains(@class,'shopee-popup__close-btn')]")
    search_box = (By.XPATH, "//input[contains(@class,'shopee-searchbar-input__input')]")
    button_search = (By.XPATH, "//button[contains(@class,'btn btn-solid-primary btn--s btn--inline')]")
    
    # Have to use .// for find a child element
    product_name = (By.XPATH, ".//div[contains(@class, 'yQmmFK _1POlWt _36CEnF')]")
    search_results = (By.XPATH, "//div[contains(@class, 'col-xs-2-4 shopee-search-item-result__item')]")
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
        #if(self.check_element_exist(ShopeeElements.button_popup)):
        
        # *** Have to check why can't find element on the page
        if(True):
            button_close_popup = self.find_element(*ShopeeElements.button_popup)
            self.wait_element_visible(button_close_popup)
            button_close_popup.click()
        else:
            print('Does not found popup')
            body = self.find_element(*ShopeeElements.body)
            body.click()

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

        results = self.find_elements(*ShopeeElements.search_results)
        
        names = [item.find_element(*ShopeeElements.product_name).text for item in results]
        
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