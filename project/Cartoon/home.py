from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common import page
from common import helper
import time
import random

class CartoonElements():
    # Kingsmanga
    # images = (By.XPATH, "//img[contains(@loading,'lazy')]")

    # Manghwa 1
    # images = (By.XPATH, "//img[contains(@id,'image')]")
    # button_popup = (By.XPATH,"//button[contains(@class,'btn btn-primary btn-adult-confirm')]")

    # Manghwa 2
    # images = (By.XPATH,"//img[contains(@rel,'noreferrer')]")

    # Manghwa 3
    images = (By.XPATH, "//img[contains(@id,'image')]")

class CartoonHome(page.Page):
    def open(self,index):
        #self.url = 'https://www.kingsmanga.net/one-piece-1019/'
        self.url = "https://dootoon18.com/manga/a-wonderful-new-world/ตอนที่-"+ str(index) +"/"
        #self.url = "https://www.niceoppai.net/A-Wonderful-New-World/" + str(index) + "/"
        #self.url = "https://catzaa.com/manga/a-wonderful-new-world/ตอนที่-" + str(index) + "/"
        self.open_browser(self.url)
        self.image_list = []

    # Close popup of dootoon18.com
    def close_popup(self):
        if(self.check_element_exist(*CartoonElements.button_popup)):
            button_close = self.find_element(*CartoonElements.button_popup)
            button_close.click()
        else:
            print("Don't found the button")


    def get_images(self):
        if(self.check_element_exist(*CartoonElements.images)):

            images = self.find_elements(*CartoonElements.images)

            for idx,i in enumerate(images):
                self.image_list.append(i.get_attribute("src"))
                print(f'save image {i}')
        else:
            print("Don't found any image from this cartoon page")

    def save_image(self):

        image_directory = './project/Cartoon/images/'

        print("*"*30)
        print(self.image_list)
        print("*"*30)
        for idx, url in enumerate(self.image_list):
            
            if url is None:
                continue

            print("*"*30)
            print(url)
            print("*"*30)
            helper.save_image_url(image_directory +"image" + str(idx) + ".png", url)
            self.random_waitting(3)
            # time.sleep(1)
        print('save finished')

    def create_pdf(self, index):

        image_directory = './project/Cartoon/images/'
        images_path = []

        images = helper.get_files_from_directory(image_directory)
        
        images_sort = helper.sort_text_with_number(images)
        print("*"*30)
        print(images_sort)
        print("*"*30)
        for file in images_sort:
            if "image" in file:
                images_path.append(image_directory+file)
                
        helper.create_pdf(images_path, "a-wonderful-new-world " + str(index))

    def delete_images(self):
        path = "./project/Cartoon/images"
        images = helper.get_files_from_directory(path)
        for file in images:
            if "image" in file:
                helper.remove_files_from_directory(path + "/" , file)

    def random_waitting(self, max_waiting:int):
        sleeping_time = random.randint(1, max_waiting)
        time.sleep(sleeping_time)    
    