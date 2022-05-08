import csv
import os,sys,inspect
from numpy.core.arrayprint import DatetimeFormat
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, current_dir) 

from common import browser_factory
from project.Cartoon import home
import time

print(parent_dir)

driver_path = "/Users/watcharapongwongrattanasirikul/Documents/Git/Webscraping/driver/chromedriver"
is_option = True
is_headless = False

web = browser_factory.Browser(driver_path, is_option, is_headless)
cartoon_home = home.CartoonHome(web.driver)

# for i in range(110, 117):
#     cartoon_home.open(i)
#     #cartoon_home.wait(2)
#     #cartoon_home.close_popup()
#     cartoon_home.wait(5)
#     cartoon_home.scroll_slow_to_end()
#     cartoon_home.wait(5)
#     cartoon_home.get_images()
#     cartoon_home.save_image()
#     cartoon_home.create_pdf(i)
#     cartoon_home.delete_images()
#     cartoon_home.wait(5)
#     time.sleep(3)

for i in range(136, 137):
    cartoon_home.open(i)
    cartoon_home.wait(1)
    #cartoon_home.scroll_slow_to_end_v2()
    cartoon_home.wait(3)
    cartoon_home.get_images()
    cartoon_home.save_image()
    cartoon_home.create_pdf(i)
    cartoon_home.delete_images()
    cartoon_home.wait(5)
