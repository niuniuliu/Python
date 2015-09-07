
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


UserName = '//*[@name="Email"]';
Pwd = '//*[@name="Password"]';
LoginButton = '//*[@id="FormLogin"]/button';


url = "https://devidmadmin.ctp.dev.com/IdmFirmAdminWeb/"

dr = webdriver.Chrome()
dr.get(url)
sleep(1)
# get popup link
dr.find_element_by_xpath(UserName).clear()
dr.find_element_by_xpath(UserName).send_keys("helenjing2012+620@gmail.com")
dr.find_element_by_xpath(Pwd).clear()
dr.find_element_by_xpath(Pwd).send_keys("Atlas2012")
dr.find_element_by_xpath(LoginButton).click()

sleep(3)
original_window = dr.current_window_handle
# popup_link.click()

TermsOfUseLink = '//div[@class="tos-text"]//a'

print "Current title:" + dr.title
print len(dr.window_handles)
print dr.current_window_handle
# print dr.page_source

dr.find_element_by_xpath(TermsOfUseLink).click()
# print len(dr.window_handles)
# print dr.current_window_handle

# dr.switch_to_window(dr.window_handles[1])
# print "Current title:" + dr.title

# dr.close()
# sleep(2)
# dr.switch_to_window(original_window)

# dr.find_element_by_xpath(TermsOfUseLink).click()

# dr.switch_to_window

dr.close()