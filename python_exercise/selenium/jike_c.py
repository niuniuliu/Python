# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()
# root_url = 'http://www.jikexueyuan.com/path/c/'
# root_url = 'http://www.jikexueyuan.com/path/php/'
root_url = 'http://www.jikexueyuan.com/path/bootstrap/'

dr.get(root_url)

element_sections = dr.find_elements_by_xpath('//*[@id="path"]/section')
# headers = element_sections.find_elements_by_xpath('//*[@id="path"]/section//h2/')
# name_section = element_sections.find_elements_by_xpath('.//ul/a')
# subname_section = ''


def GoAndBack(url, prefix):
    dr_1 = webdriver.Chrome()
    dr_1.get(url)
    time.sleep(1)
    sub_headers = dr_1.find_elements_by_xpath('/html/body/div[5]//ul//h2/a')
    for sub_header in sub_headers:
        print prefix + sub_header.get_attribute('innerHTML')
    # print
    dr_1.back()
    dr_1.quit()
    # time.sleep(1)
    # print


for section in element_sections:
    # print section
    headers = section.find_elements_by_xpath('.//h2')
    url_names = section.find_elements_by_xpath('.//ul//a')
    for header in headers:
        
        print "========================="
        print header.text
        h1 = header.text[0:2]

        for url_name in url_names:
            print '--------------------'
            print url_name.text
            h2 = url_name.text[0:2]
            url = url_name.get_attribute("href")
            print url

            GoAndBack(url, h1+h2)
            # time.sleep(1)

        

    # for url_name in url_names:
    #     print url_name.text
    #     url = url_name.get_attribute("href")
    #     print url

    #     GoAndBack(url)
    #     # time.sleep(1)


dr.quit()

    # section..find_elements_by_xpath('.//ul/a')



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
# ################
