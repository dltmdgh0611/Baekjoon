from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
import time

driver = webdriver.Chrome("C:\\Users\\chromedriver.exe")
driver.get("https://seumedu.kr/member/login.html")
messagebox.showinfo("wait", "로그인하고 ok를 눌러주세요")
studystartbtn = driver.find_element_by_xpath('//*[@id="section"]/div[4]/div[1]/table/tbody/tr[2]/td[9]/a')
studystartbtn.click()
driver.implicitly_wait(1)
classcount = driver.find_elements_by_class_name("num")

for i in range(len(classcount)):
    classStartbtn = driver.find_element_by_xpath('//*[@id="section"]/div[4]/div[4]/div[2]/ul/li[{0}]/div[4]/a'.format(i+1))
    classStartbtn.click()
    driver.implicitly_wait(1)
    driver.switch_to_window( driver.window_handles[1] )
    driver.implicitly_wait(5)
    try : 
        xbtn = driver.find_element_by_xpath('/html/body/div[3]/div[1]/button/span[1]')
        xbtn.click()
    except : pass

    nextbubble = driver.find_element_by_class_name('nextBubblePop')
    while(1):
        driver.implicitly_wait(1)
        if (len(nextbubble.get_attribute("style")) >  1) : break
    nextbtn = driver.find_element_by_xpath('/html/body/div/div[3]/div[18]')
    nextbtn.click()
    pass