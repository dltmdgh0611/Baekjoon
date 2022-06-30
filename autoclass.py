from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
import time

driver = webdriver.Chrome("C:\\Users\\chromedriver.exe")
driver.set_window_size(1000, 3000)

driver.get("https://seumedu.kr/member/login.html")
driver.find_element_by_id('login_ID').send_keys('a06114171')
driver.find_element_by_id('login_PW').send_keys('ghqks0805!')
driver.find_element_by_xpath('//*[@id="section"]/div[3]/div/div[1]/form/fieldset/p[4]/input').click()
time.sleep(2)
try:
    result = driver.switch_to_alert()
    result.dismiss()
except: pass
studystartbtn = driver.find_element_by_xpath('//*[@id="section"]/div[4]/div[1]/table/tbody/tr[3]/td[10]/a')
studystartbtn.click()
time.sleep(1)
classcount = driver.find_elements_by_class_name("num")

for i in range(26,len(classcount)):
    driver.refresh()
    classStartbtn = driver.find_element_by_xpath('//*[@id="section"]/div[4]/div[4]/div[2]/ul/li[{0}]/div[4]/a'.format(i+2))
    classStartbtn.click()
    time.sleep(1)
    driver.switch_to_window( driver.window_handles[1] )
    time.sleep(5)
    try : 
        xbtn = driver.find_element_by_xpath('/html/body/div[3]/div[1]/button/span[1]')
        xbtn.click()
    except : pass
    iframe = driver.find_elements_by_id('frame')[0]
    driver.switch_to.frame(iframe)
    for j in range(1,14):
        time.sleep(10)
        try:
            # driver.execute_script("changeFile('next')")
            try:
                driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/table/tbody/tr/td[6]/a').click()
            except:
                driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/table/tbody/tr/td[6]/a').click()
        except:
            print("end or error")
            break
    time.sleep(1000)
    driver.switch_to_window( driver.window_handles[0] )
    driver.refresh()
    pass