from common import browser_factory
import project.Google.home as home

driver_path = "driver/chromedriver"
is_option = True
is_headless = False

web = browser_factory.Browser(driver_path, is_option, is_headless)

google_home = home.GoogleHome(web.driver)
google_home.open()
google_home.wait_title_contains('Google')
google_home.search_text("Hellow selenium world")
google_home.wait()
google_home.close_browser()