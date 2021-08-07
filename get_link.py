import time
import undetected_chromedriver.v2 as webdriver
from xvfbwrapper import Xvfb
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb

class WebDriverChrome(object):

    def __init__(self):
        # self.url_article = articles.daily_url
        # self.url_home = ['/xem-mua-luon.chn','/hello-genz.html','/nhom-chu-de/emagazine.chn']
        self.driver = self.StartWebdriver()

    def StartWebdriver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("start-maximized")
        # options.add_argument("--incognito")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        # options.add_argument(f'user-agent={secrets.choice(articles.user_agent)}')
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument('--user-data-dir=/home/test1/.config/google-chrome/Default')
        options.add_argument(f"--no-sandbox")
        options.add_argument(f"--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        return driver


def save_txt(self):
    img_list = []
    URL = "https://unsplash.com/s/photos/fire"

    # options = Options()
    # options.headless = True

    print('Openning Chrome...', end='\n\n')

    # browser = webdriver.Chrome(options=options)
    self.driver.get(URL)

    # time.sleep(1)
    print('Please wait...', end="\n\n")

    # browser.get(URL)
    time.sleep(2)

    # result_page = self.driver.find_element_by_tag_name("body")
    
    no_of_pagedowns = 10

    print('Please wait...', end="\n\n")
    scroll_counter = 0
    while no_of_pagedowns:
        print(f'{scroll_counter} scroll times')
        scroll_counter += 1
        self.driver.execute_script("window.scrollBy(0,"+str(5000)+");")
        time.sleep(2)
        no_of_pagedowns -= 1

    image_elements = self.driver.find_elements_by_class_name('oCCRx')
    for image_element in image_elements:

        image_name = image_element.get_attribute('alt')
        if image_name == '':
            image_name = 'demo name'
        image_link = image_element.get_attribute('src')

        print('get image link %s...' % image_name)
        img_list.append(image_link)

    self.driver.quit()

    with open('image_url_list.txt', 'w') as f:
        for item in img_list:
            f.write("%s\n" % item)

    print('Images link successfully saved! Please check image_url_list.txt!')


if __name__ == '__main__':
    vdisplay = Xvfb(width=800, height=1280)
    vdisplay.start()
    Crawl = WebDriverChrome()
    Crawl.save_txt()
    vdisplay.stop()

