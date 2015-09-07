# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_browser(BrowserName):
    BrowserName = BrowserName.lower()

    if BrowserName == 'chrome':

        return webdriver.Chrome()
    elif BrowserName == 'firefox':
        return webdriver.Firefox()
    elif BrowserName == 'ie':
        return webdriver.Ie("C:\Users\tliu\Data\SoftWare_T\nodejs\IEDriverServer.exe")

br = open_browser('chrome')
browser = br
browser.get('http://www.bing.com')
# br = dir(browser)
# help(browser)
# for i in br:
# print i
# print (browser.title)

assert u'Bing' in browser.title
# assert u'Yahoo' in browser.title

print browser.window_handles

elem = browser.find_element_by_name('q')  # Find the search box
elem.send_keys('selenium' + Keys.RETURN)
# elem.click()
# elem.get_attribute('name')

# x = elem.parent
# print x
# elem.get_attribute('class')
# x.get_attribute(self, name)
# elements = dir(elem)

# for i in elements:
#     print i
# help(elem)

browser.quit()



# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')


# import calendar

# Nov = calendar.month(2014, 11)
# Dec = calendar.month(2014, 12)

# print Nov
# print Dec

# from apihelper import info
# li = []
# info(li)

