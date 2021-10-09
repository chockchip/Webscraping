from common import browser_factory
from project.Cartoon import home
import time

driver_path = "driver/chromedriver"
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

for i in range(1, 2):
    cartoon_home.open(i)
    cartoon_home.wait(1)
    cartoon_home.get_images()
    cartoon_home.save_image()
    cartoon_home.create_pdf(i)
    cartoon_home.delete_images()
    cartoon_home.wait(5)
    time.sleep(3)