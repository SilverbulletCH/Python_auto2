from datetime import datetime
from time import sleep

from selenium import webdriver
import yaml

class TestLinks:


    def test_demo6(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        driver = webdriver.Chrome(options=option)
        driver.implicitly_wait(10)
        j = 0
        a = True
        url_list = []
        while a == True:
            list01 = {}
            url = 'https://www.baidu.com/s?wd=site:ceshiren.com&pn='+ str(0 + j * 10)
            driver.get(url)
            sleep(3)
            element = driver.find_elements_by_xpath('//*[@class="result c-container new-pmd"]')
            for i in range(1, len(element) + 1):
                element0 = driver.find_element_by_xpath(
                    f'(//*[@class="result c-container new-pmd"])[{i}]').get_attribute('id')
                ele1 = element0
                element2 = driver.find_element_by_xpath(f'(//*[@class="c-tools c-gap-left"])[{i}]').get_attribute(
                    "data-tools")
                element3 = driver.find_element_by_xpath(
                    f'(//*[@class="result c-container new-pmd"])[{i}]').get_attribute("outerText")
                ele2 = eval(element2)
                ele4 = element3.split('\n')
                list01[ele1] = [ele2['url'], ele2['title'], ele4[2]]

            url_list.append(list01)
            print(list01)
            a = True if len(list01) >= 9 else False
            j += 1
            continue

        f = open(datetime.now().date().isoformat()+'.yml', 'w')
        print(url_list,file=f)
        print(len(url_list))

if __name__ == '__main__':
    print(TestLinks().test_demo6())