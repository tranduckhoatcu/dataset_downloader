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
        driver = webdriver.Chrome(version_main=91,options=options)
        return driver


    def save_txt(self):
        temp1 = []
        list_element = []
        URL = "https://unsplash.com/s/photos/fire"

        print('Openning Chrome...', end='\n\n')
        
        self.driver.get(URL)
        print('Please wait...', end="\n\n")
        time.sleep(2)


        scroll_counter = 0
        try:
            for i in range(5000):
                print(f'{scroll_counter} scroll times')
                scroll_counter += 1
                self.driver.execute_script("window.scrollBy(0,"+str(secrets.SystemRandom().uniform(1800,2000))+");")
                time.sleep(secrets.SystemRandom().uniform(1,1.25))
                self.driver.execute_script("window.scrollBy(0,-"+str(secrets.SystemRandom().uniform(800,1000))+");")
                time.sleep(secrets.SystemRandom().uniform(1,1.25))
                image_elements = self.driver.find_elements_by_class_name('oCCRx')
                
                

                print(f'get elements successfully')
                print(f'number of elements extracted: {len(image_elements)}')
                # print(image_elements)
                if (i == 0):
                    for element in image_elements:
                        image_link = element.get_attribute('src')
                        temp1.append(image_link)
                        list_element.append(element)                        
                else:
                    temp_elements = list(set(image_elements) - set(list_element))

                    for element in temp_elements:
                        image_link = element.get_attribute('src')
                        temp1.append(image_link)
                        list_element.append(element)

                    temp1 = list(set(temp1))
                    list_element = list(set(list_element))
                     
                print(f'Urls: {len(temp1)}')
                if(len(temp1) > 9500):
                    break
            
            self.driver.quit()
            print(f'number of urls saved: {len(temp1)}')
            with open('image_url_list.txt', 'w') as f:
                for item in temp1:
                    f.write("%s\n" % item)
        except:
            self.driver.quit()
            print(f'number of urls saved: {len(temp1)}')
            with open('image_url_list.txt', 'w') as f:
                for item in temp1:
                    f.write("%s\n" % item)

        print('Images link successfully saved! Please check image_url_list.txt!')


if __name__ == '__main__':
    vdisplay = Xvfb(width=800, height=1280)
    vdisplay.start()
    Crawl = WebDriverChrome()
    Crawl.save_txt()
    vdisplay.stop()

