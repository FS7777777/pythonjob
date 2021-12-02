from selenium import webdriver
from selenium.webdriver.support.select import Select, By
import requests

chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chrome_opt.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(r"F:\tools\chromedriver_win32\chromedriver.exe",chrome_options=chrome_opt)
browser.get("https://www.heavens-above.com/login.aspx")

'''登录'''
browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_UserName"]').send_keys('-')
browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_Password"]').send_keys('-')

browser.find_element_by_xpath('//*[@id="ctl00_cph1_Login1_LoginButton"]').click()

'''选择地理位置'''
Select(browser.find_element_by_xpath('//*[@id="ctl00_ddlLocation"]')).select_by_value("2151038")

'''选择明亮卫星每日预报'''
browser.find_element_by_xpath('//*[@id="aspnetForm"]/table/tbody/tr[3]/td[1]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/div/p[18]/a').click()

'''选择最低亮度3.0'''
browser.find_element_by_xpath('//*[@id="ctl00_cph1_radioButtonsMag_0"]').click()

'''选择傍晚'''
browser.find_element_by_xpath('//*[@id="ctl00_cph1_TimeSelectionControl1_radioAMPM"]/tbody/tr[2]/td/label').click()

'''开始筛选数据'''
tb_tbody = browser.find_element_by_xpath('//*[@id="aspnetForm"]/table/tbody/tr[3]/td[1]/table[3]/tbody').find_elements(By.TAG_NAME,'tr')

print('================================================================================') 
for tr in tb_tbody:
    print(tr.text)
    tr_data=tr.text.split(' ')
    print(tr_data)
print('================================================================================') 

req = requests.Session() #构建Session
cookies = browser.get_cookies() #导出cookie

for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value']) #转换cookies
print(cookies) #打印cookies

browser.quit()