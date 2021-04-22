from common import browser_factory
from project.Shopee import home

driver_path = "driver/chromedriver"
is_option = True
is_headless = False

web = browser_factory.Browser(driver_path, is_option, is_headless)

shopee_home = home.ShopeeHome(web.driver)
shopee_home.open()
shopee_home.close_language_selection()
shopee_home.wait(2)
shopee_home.close_popup()
shopee_home.wait(2)
shopee_home.search_items("iphone")
shopee_home.wait(2)
shopee_home.get_search_results()
shopee_home.wait(1)
shopee_home.close_browser()