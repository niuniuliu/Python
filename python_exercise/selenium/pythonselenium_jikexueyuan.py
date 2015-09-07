# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

# for i in os.environ.items():
# 	print i

# if 'HTTP_PROXY'in os.environ:
#     print os.environ['HTTP_PROXY']
#     del os.environ['HTTP_PROXY']


# dr = webdriver.Chrome()
# dr.close()
dr = webdriver.Chrome()
# dr.maximize_window()
# file_path = 'file:///' + os.path.abspath('a.html')
file_path = 'http://www.jikexueyuan.com/path/csharp/'
# dr.set_window_size(800, 600)

# $x('/html/body/div[6]/div[2]/div[2]/ul//h2/a')
# $x('//*[@id="path"]/section[4]/ul/li//a')


# dr.get('http://www.jikexueyuan.com/course/482.html')
# y = dr.find_elements_by_xpath('/html/body/div[5]//ul//h2/a')
# # y = dr.find_elements_by_xpath('//ul//h2/a')
# # $x('//ul//h2/a')

# for x in y:
#     print x.get_attribute('innerHTML')
#     # print x.is_displayed()
#     # z = x.find_element_by_tag_name('a')
#     # print z.get_attribute('href')



#################
dr.get(file_path)
time.sleep(1)



# # dr.find_element_by_link_text('Link1').click()

# x = dr.find_elements_by_xpath('//*[@id="path"]/section[3]/ul/li//a')
# urls = []

# for item in x:
#     # item.click()
#     # $x('/html/body/div[6]/div[2]/div[2]/ul//h2/a')
#     url = item.get_attribute("href")
#     urls.append(url)

# print urls

# for url in urls:
#     # $x('/html/body/div[5]//ul//h2/a')
#     dr.get(url)
#     y = dr.find_elements_by_xpath('/html/body/div[5]//ul//h2/a')
    
#     for item in y:
#         # print item.text
#         print item.get_attribute('innerHTML')
#     print 
#     print
################

# for path in xrange(1,5):
#     xpath = '//*[@id="path"]/section[' + str(x) + ']/ul/li//a'
#     x = dr.find_elements_by_xpath(xpath)
#     urls = []

#     for item in x:
#         # item.click()
#         # $x('/html/body/div[6]/div[2]/div[2]/ul//h2/a')
#         url = item.get_attribute("href")
#         urls.append(url)

#     print urls

#     for url in urls:
#         # $x('/html/body/div[5]//ul//h2/a')
#         dr.get(url)
#         y = dr.find_elements_by_xpath('/html/body/div[5]//ul//h2/a')
        
#         for item in y:
#             # print item.text
#             print item.get_attribute('innerHTML')
#         print 
#         print
#     #################


# $x('//*[@id="path"]/section[4]/ul/li//a')

# WebDriverWait(dr, 10).until(lambda the_driver: the_driver.find_element_by_id("dropdown1").is_displayed())

# menu = dr.find_element_by_id('dropdown1').find_element_by_link_text("Another action")

# webdriver.ActionChains(dr).move_to_element(menu).perform()

# time.sleep(2)
# # dr.quit()


# print dr.title
# print dr.current_url


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# import os

# if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

# dr = webdriver.Chrome()
# file_path = 'file:///' + os.path.abspath('c.html')

# dr.get(file_path)

# sleep(1)

# # 定位text是second的按钮
# buttons = dr.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
# for btn in buttons:
#     if btn.text == 'second': print 'find second button'

# sleep(1)
# # dr.quit()

