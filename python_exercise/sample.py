# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

# if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

one_dict = {

"http://zhuwei.me/youtube/cc/Lx7ycjC8qjE.srt" : "AngularJS - 01 Binding.srt" , 
"http://zhuwei.me/youtube/cc/MEmC0QH8ATQ.srt" : "AngularJS - 02 Controllers.srt" , 
"http://zhuwei.me/youtube/cc/DTx23w4z6Kc.srt" : "AngularJS - 03 The Dot.srt" , 
"http://zhuwei.me/youtube/cc/HXpHV5gWgyk.srt" : "AngularJS - 04 Sharing Data Between Controllers.srt" , 
"http://zhuwei.me/youtube/cc/Powr9vzqMac.srt" : "AngularJS - 05 Defining a Method on the Scope.srt" , 
"http://zhuwei.me/youtube/cc/FX5TwV2ZKqc.srt" : "AngularJS - 06 Filters.srt" , 
"http://zhuwei.me/youtube/cc/wFYID8eYQLs.srt" : "AngularJS - 07 Testing Overview.srt" , 
"http://zhuwei.me/youtube/cc/bLohP9mh8ks.srt" : "AngularJS - 08 ngFilter.srt" , 
"http://zhuwei.me/youtube/cc/D4NyA-SFnZg.srt" : "AngularJS - 09 Built-in Filters.srt" , 
"http://zhuwei.me/youtube/cc/xoIHkM4KpHM.srt" : "AngularJS - 10 First Directive.srt" , 
"http://zhuwei.me/youtube/cc/AoDh1T_0Obg.srt" : "AngularJS - 11 Directive Restrictions.srt" , 
"http://zhuwei.me/youtube/cc/W82ztvDY_Po.srt" : "AngularJS - 12 Basic Behaviors.srt" , 
"http://zhuwei.me/youtube/cc/IfUyUeYHffk.srt" : "AngularJS - 13 Useful Behaviors.srt" , 
"http://zhuwei.me/youtube/cc/LJmZaxuxlRc.srt" : "AngularJS - 14 Directives Talking to Controllers.srt" , 
"http://zhuwei.me/youtube/cc/rzMrBIVuxgM.srt" : "AngularJS - 15 Directive to Directive Communication.srt" , 
"http://zhuwei.me/youtube/cc/fYgdU7u2--g.srt" : "AngularJS - 16 Understanding Isolate Scope.srt" , 
"http://zhuwei.me/youtube/cc/7X5vx-n7Nxs.srt" : "AngularJS - 17 Isolate Scope @.srt" , 
"http://zhuwei.me/youtube/cc/O9iVkfQJauQ.srt" : "AngularJS - 18 Isolate Scope =.srt" , 
"http://zhuwei.me/youtube/cc/mZGgNPTHc2Q.srt" : "AngularJS - 19 Isolate Scope &.srt" , 
"http://zhuwei.me/youtube/cc/97pv_kiYhv4.srt" : "AngularJS - 20 Isolate Scope Review.srt" , 
"http://zhuwei.me/youtube/cc/cjrBTjMvruI.srt" : "AngularJS - 21 Transclusion Basics.srt" , 
"http://zhuwei.me/youtube/cc/L9-c2NvCuf4.srt" : "AngularJS - 22 An Alternative Approach to Controllers.srt" , 
"http://zhuwei.me/youtube/cc/bz-yhpaFElI.srt" : "AngularJS - 23 Thinking Differently About Organization.srt" , 
"http://zhuwei.me/youtube/cc/JeuhhPlOZs0.srt" : "AngularJS - 24 Building Zippy.srt" , 
"http://zhuwei.me/youtube/cc/_6ijcqI5fi8.srt" : "AngularJS - 25 angular.element.srt" , 
"http://zhuwei.me/youtube/cc/NnB2NBtoeAY.srt" : "AngularJS - 26 $scope vs. scope.srt" , 
"http://zhuwei.me/youtube/cc/_23TfKY8If4.srt" : "AngularJS - 27 templateUrl.srt" , 
"http://zhuwei.me/youtube/cc/boBm3AU-uX4.srt" : "AngularJS - 28 $templateCache.srt" , 
"http://zhuwei.me/youtube/cc/nZrbZ_sYShU.srt" : "AngularJS - 29 ng-view.srt" , 
"http://zhuwei.me/youtube/cc/TT31mYUEAPs.srt" : "AngularJS - 30 The config function.srt" , 
"http://zhuwei.me/youtube/cc/gNtnxRzXj8s.srt" : "AngularJS - 31 $routeProvider api.srt" , 
"http://zhuwei.me/youtube/cc/T10gr1Leq6g.srt" : "AngularJS - 32 $routeParams.srt" , 
"http://zhuwei.me/youtube/cc/LGPXW-NgHCs.srt" : "AngularJS - 33 redirectTo.srt" , 
"http://zhuwei.me/youtube/cc/o84ryzNp36Q.srt" : "AngularJS - 34 Promises.srt" , 
"http://zhuwei.me/youtube/cc/Kr1qZ8Ik9G8.srt" : "AngularJS - 35 Resolve.srt" , 
"http://zhuwei.me/youtube/cc/vIDvluer97A.srt" : "AngularJS - 36 resolve conventions.srt" , 
"http://zhuwei.me/youtube/cc/rbqRJQZBF3Q.srt" : "AngularJS - 37 resolve $routeChangeError.srt" , 
"http://zhuwei.me/youtube/cc/-bv4Tp06Lxg.srt" : "AngularJS - 38 Directive for Route Handling.srt" , 
"http://zhuwei.me/youtube/cc/0uvAseNXDr0.srt" : "AngularJS - 39 Route Life Cycle.srt" , 
"http://zhuwei.me/youtube/cc/HvTZbQ_hUZY.srt" : "AngularJS - 40 Providers.srt" , 
"http://zhuwei.me/youtube/cc/OnSb4ebdjrk.srt" : "AngularJS - 41 Injectors.srt" , 
"http://zhuwei.me/youtube/cc/UCn7CwS5fKg.srt" : "AngularJS - 42 Components and Containers.srt" , 
"http://zhuwei.me/youtube/cc/jEpbjve5iHk.srt" : "AngularJS - 43 $index, $event, $log.srt" , 
"http://zhuwei.me/youtube/cc/tTihyXaz4Bo.srt" : 'AngularJS - 44 Experimental "Controller as" Syntax.srt' , 
"http://zhuwei.me/youtube/cc/2CdivtU5ytY.srt" : "AngularJS - 45 Directive Communication.srt" , 
"http://zhuwei.me/youtube/cc/ZvWftlp7TKY.srt" : "AngularJS - 46 ngmin.srt" , 
"http://zhuwei.me/youtube/cc/WX03ODuzkSY.srt" : "AngularJS - 47 ng-repeat-start .srt" , 
"http://zhuwei.me/youtube/cc/Bcv46xKJH98.srt" : "AngularJS - 48 animation basics .srt" , 
"http://zhuwei.me/youtube/cc/ni0N8dmxiio.srt" : "AngularJS - 49 Animating with JavaScript.srt" , 
"http://zhuwei.me/youtube/cc/2-xcoaba7_o.srt" : "AngularJS - 50 Animating the Angular Way.srt" 
    }


file_path = r'/Users/TimLiu/Desktop/sample.txt'
list_urls = open(file_path, 'r').readlines()


# print list_url.strip()

def submit(url):
    dr = webdriver.Chrome()
    dr.get("http://zhuwei.me/youtube/")
    dr.find_element_by_name('url').send_keys(url)
    dr.find_element_by_id('btn1').click()

    try:
        # dr.find_element_by_tag_name('a').click()
        # url =  dr.current_url
        # print url
        ccurl = 'http://zhuwei.me/youtube/cc/' + url[-11:] + '.srt'
        dr.get(ccurl)

        str_content = dr.find_element_by_tag_name('pre').text
        # print str_content
        # print r'/Users/TimLiu/Desktop/' + one_dict[ccurl]
        # print one_dict[ccurl]
        open('/Users/TimLiu/Desktop/' + one_dict[ccurl], 'w').write(str_content)

    except Exception, e:
        # raise
        print e
    else:
        pass
    finally:
        # pass
        dr.quit()

    # dr.quit()
# print one_dict['http://zhuwei.me/youtube/cc/MH58D6XOlqA.srt']
# submit('https://www.youtube.com/watch?v=2-xcoaba7_o')
# print 'https://www.youtube.com/watch?v=MH58D6XOlqA'[-11:]

for x in list_urls:
    y = x.strip()
    # sleep(1)
    print y
    submit(y)

# dr = webdriver.Chrome()
# def save_srt(dictionary):
#     for x, y in dictionary.items():
#         dr.get(x)
#         print x
#         print y

#         try:
#             str_content = dr.find_element_by_tag_name('pre').text
#             open('/Users/TimLiu/Desktop/' + y, 'w').write(str_content)

#         except Exception, e:
#             # raise
#             pass
#         else:
#             pass
#         finally:
#             pass
        
#         # sleep(0.05)

# save_srt(one_dict)

# dr.get('http://zhuwei.me/youtube/cc/2-xcoaba7_o.srt')

# str_content = dr.find_element_by_tag_name('pre').text
# open('/Users/TimLiu/Desktop/1.txt', 'w').write(str_content)
# dr.quit()

# submit('https://www.youtube.com/watch?v=MH58D6XOlqA')

# dr.get(file_path)

# sleep(1)

# # 定位text是second的按钮
# buttons = dr.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
# for btn in buttons:
#     if btn.text == 'second': print 'find second button'

# sleep(1)
# # dr.quit()