# # coding: utf-8

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import time
import os

# for i in os.environ.items():
#     print i

if 'HTTP_PROXY'in os.environ:
    print os.environ['HTTP_PROXY']
    del os.environ['HTTP_PROXY']


# # dr = webdriver.Chrome()
# # dr.close()
# dr = webdriver.Chrome()
# # dr.maximize_window()
# file_path = 'file:///' + os.path.abspath('a.html')
# dr.set_window_size(800, 600)

# dr.get(file_path)
# time.sleep(1)


# dr.find_element_by_link_text('Link1').click()


# WebDriverWait(dr, 10).until(lambda the_driver: the_driver.find_element_by_id("dropdown1").is_displayed())

# menu = dr.find_element_by_id('dropdown1').find_element_by_link_text("Another action")

# webdriver.ActionChains(dr).move_to_element(menu).perform()

# time.sleep(2)
# # dr.quit()


# # print dr.title
# # print dr.current_url

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

url = "http://webapplog.com/giveaways/sublime/?lucky=574"

dr = webdriver.Chrome()
dr.get("http://webapplog.com/giveaways/sublime/?lucky=574")
sleep(1)
# 定位text是second的按钮
ddl = dr.find_element_by_id("giveaways_answer")

ddl.click()

ddls = dr.find_elements_by_id("giveaways_answer")

for option in ddls:
    
    if option.text == "Sublime Text":
        print "good"
        option.click() # select() in earlier versions of webdriver
        break



# for option in ddls:
#     if option.text == 'Sublime Text':
#         option.click() # select() in earlier versions of webdriver
#         break

# dr.find_element_by_xpath('//*[@id="giveaways_answer"]/option[4]')

dr.find_element_by_name("giveaways_email").click()

dr.find_element_by_name("giveaways_email").send_keys()

# dr.quit()

'''