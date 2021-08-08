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
        counter_break = 0

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
                # print(image_elements)
                if (i == 0):
                    for image_element in image_elements:
                        image_link = image_element.get_attribute('src')
                        temp1.append(image_link)
                else:
                    temp2 = []
                    for image_element in image_elements:
                        image_link = image_element.get_attribute('src')
                        temp2.append(image_link)
                    for j in (temp2):
                        temp1.append(j)
                    temp1 = list(set(temp1))
                
                print(f'Urls: {len(temp1)}')
                
                if(len(temp1) > 1000):
                    print(f'number of urls saved: {len(temp1)}')
                    with open(f'image_url_list_part'+{str(counter_break)}+'.txt', 'w') as f:
                        for item in img_list:
                            f.write("%s\n" % item)
                    print('Images link successfully saved! Please check '+{str(counter_break)}+'.txt'')
                    temp1 = []
                    counter_break+=1
                
                if (counter_break == 9):
                    break

            self.driver.quit()

        except:
            self.driver.quit()
            print(f'number of urls saved: {len(temp1)}')
            with open(f'image_url_list_part'+{str(counter_break)}+'.txt', 'w') as f:
                for item in img_list:
                    f.write("%s\n" % item)
            print('Images link successfully saved! Please check '+{str(counter_break)}+'.txt'')


if __name__ == '__main__':
    vdisplay = Xvfb(width=800, height=1280)
    vdisplay.start()
    Crawl = WebDriverChrome()
    Crawl.save_txt()
    vdisplay.stop()

