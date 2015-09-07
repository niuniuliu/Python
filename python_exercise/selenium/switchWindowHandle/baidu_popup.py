
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

url = "file:///C:/Users/tliu/Data/GitHub/zZZzzZZzz/Python/python_exercise/selenium/switchWindowHandle/baidu.html"

dr = webdriver.Chrome()
dr.get(url)
sleep(1)
# get popup link
# popup_link = dr.find_element_by_xpath("/html/body/a[5]")
popup_link = dr.find_element_by_xpath("/html/body/a[6]")


original_window = dr.current_window_handle
popup_link.click()

print len(dr.window_handles)
print dr.current_window_handle
# print dr.page_source
print "Current Browser Name:" + dr.name
print "Current title:" + dr.title
all_handles = dr.window_handles
print all_handles
print 

dr.switch_to_window(dr.window_handles[1])
print "Current Browser Name:" + dr.name
print "Current title:" + dr.title
