from selenium import webdriver
import time

class web_driver(object):
    def funcname(self):
        browser = webdriver.Chrome()
        browser.get('http://www.baidu.com/')

        time.sleep(20)

        browser.back()
        time.sleep(2)
        browser.forward()
        time.sleep(3)

        browser.quit()
