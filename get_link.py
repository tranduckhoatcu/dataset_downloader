import time
import undetected_chromedriver.v2 as webdriver
import secrets
from xvfbwrapper import Xvfb

class WebDriverChrome(object):

    def __init__(self):
        self.driver = self.StartWebdriver()

    def StartWebdriver(self):
        options = webdriver.ChromeOptions()
        # options.add_argument(f'user-agent={secrets.choice(articles.user_agent)}')
        options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        options.add_argument('--user-data-dir=/home/test1/.config/google-chrome/Default')
        options.add_argument(f"--no-sandbox")
        options.add_argument(f"--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        return driver


    def save_txt(self):
        img_list = []
        temp1 = []

        URL = "https://unsplash.com/s/photos/fire"

        print('Openning Chrome...', end='\n\n')
        
        self.driver.get(URL)
        print('Please wait...', end="\n\n")
        time.sleep(2)


        scroll_counter = 0
        for i in range(20):
            print(f'{scroll_counter} scroll times')
            scroll_counter += 1
            self.driver.execute_script("window.scrollBy(0,"+str(secrets.SystemRandom().uniform(1800,2000))+");")
            time.sleep(secrets.SystemRandom().uniform(1,1.25))
            self.driver.execute_script("window.scrollBy(0,-"+str(secrets.SystemRandom().uniform(800,1000))+");")
            time.sleep(secrets.SystemRandom().uniform(1,1.25))
            image_elements = self.driver.find_elements_by_class_name('oCCRx')
            # print(image_elements)
            if (i == 0):
                for image_element in image_elements:
                    image_link = image_element.get_attribute('src')
                    temp1.append(image_link)
            else:
                temp2 = []
                temp3 = []
                for image_element in image_elements:
                    image_link = image_element.get_attribute('src')
                    temp2.append(image_link)
                temp3 = list(set(temp2) - set(temp1))
                for j in temp3:
                    temp1.append(j)
        
        
        
        
            # image_name = image_element.get_attribute('alt')
            # if image_name == '':
            #     image_name = 'demo name'
            

            # print('get image link %s...' % image_name)
            # img_list.append(image_link)

        self.driver.quit()
        print(f'number of urls: {len(temp1)}')
        with open('image_url_list.txt', 'w') as f:
            for item in temp1:
                f.write("%s\n" % item)

        print('Images link successfully saved! Please check image_url_list.txt!')


if __name__ == '__main__':
    vdisplay = Xvfb(width=1920, height=1080)
    vdisplay.start()
    Crawl = WebDriverChrome()
    Crawl.save_txt()
    vdisplay.stop()

