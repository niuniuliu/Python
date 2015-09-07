# # coding: utf-8

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# import time
# import os

# # for i in os.environ.items():
# # 	print i

# if 'HTTP_PROXY'in os.environ:
#     print os.environ['HTTP_PROXY']
#     del os.environ['HTTP_PROXY']


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



dict_srt = {
    "http://zhuwei.me/youtube/cc/v=Lx7ycjC8qjE.srt" : "AngularJS - 01 Binding.srt" , 
"http://zhuwei.me/youtube/cc/v=MEmC0QH8ATQ.srt" : "AngularJS - 02 Controllers.srt" , 
"http://zhuwei.me/youtube/cc/v=DTx23w4z6Kc.srt" : "AngularJS - 03 The Dot.srt" , 
"http://zhuwei.me/youtube/cc/v=HXpHV5gWgyk.srt" : "AngularJS - 04 Sharing Data Between Controllers.srt" , 
"http://zhuwei.me/youtube/cc/v=Powr9vzqMac.srt" : "AngularJS - 05 Defining a Method on the Scope.srt" , 
"http://zhuwei.me/youtube/cc/v=FX5TwV2ZKqc.srt" : "AngularJS - 06 Filters.srt" , 
"http://zhuwei.me/youtube/cc/v=wFYID8eYQLs.srt" : "AngularJS - 07 Testing Overview.srt" , 
"http://zhuwei.me/youtube/cc/v=bLohP9mh8ks.srt" : "AngularJS - 08 ngFilter.srt" , 
"http://zhuwei.me/youtube/cc/v=D4NyA-SFnZg.srt" : "AngularJS - 09 Built-in Filters.srt" , 
"http://zhuwei.me/youtube/cc/v=xoIHkM4KpHM.srt" : "AngularJS - 10 First Directive.srt" , 
"http://zhuwei.me/youtube/cc/v=AoDh1T_0Obg.srt" : "AngularJS - 11 Directive Restrictions.srt" , 
"http://zhuwei.me/youtube/cc/v=W82ztvDY_Po.srt" : "AngularJS - 12 Basic Behaviors.srt" , 
"http://zhuwei.me/youtube/cc/v=IfUyUeYHffk.srt" : "AngularJS - 13 Useful Behaviors.srt" , 
"http://zhuwei.me/youtube/cc/v=LJmZaxuxlRc.srt" : "AngularJS - 14 Directives Talking to Controllers.srt" , 
"http://zhuwei.me/youtube/cc/v=rzMrBIVuxgM.srt" : "AngularJS - 15 Directive to Directive Communication.srt" , 
"http://zhuwei.me/youtube/cc/v=fYgdU7u2--g.srt" : "AngularJS - 16 Understanding Isolate Scope.srt" , 
"http://zhuwei.me/youtube/cc/v=7X5vx-n7Nxs.srt" : "AngularJS - 17 Isolate Scope @.srt" , 
"http://zhuwei.me/youtube/cc/v=O9iVkfQJauQ.srt" : "AngularJS - 18 Isolate Scope =.srt" , 
"http://zhuwei.me/youtube/cc/v=mZGgNPTHc2Q.srt" : "AngularJS - 19 Isolate Scope &.srt" , 
"http://zhuwei.me/youtube/cc/v=97pv_kiYhv4.srt" : "AngularJS - 20 Isolate Scope Review.srt" , 
"http://zhuwei.me/youtube/cc/v=cjrBTjMvruI.srt" : "AngularJS - 21 Transclusion Basics.srt" , 
"http://zhuwei.me/youtube/cc/v=L9-c2NvCuf4.srt" : "AngularJS - 22 An Alternative Approach to Controllers.srt" , 
"http://zhuwei.me/youtube/cc/v=bz-yhpaFElI.srt" : "AngularJS - 23 Thinking Differently About Organization.srt" , 
"http://zhuwei.me/youtube/cc/v=JeuhhPlOZs0.srt" : "AngularJS - 24 Building Zippy.srt" , 
"http://zhuwei.me/youtube/cc/v=_6ijcqI5fi8.srt" : "AngularJS - 25 angular.element.srt" , 
"http://zhuwei.me/youtube/cc/v=NnB2NBtoeAY.srt" : "AngularJS - 26 $scope vs. scope.srt" , 
"http://zhuwei.me/youtube/cc/v=_23TfKY8If4.srt" : "AngularJS - 27 templateUrl.srt" , 
"http://zhuwei.me/youtube/cc/v=boBm3AU-uX4.srt" : "AngularJS - 28 $templateCache.srt" , 
"http://zhuwei.me/youtube/cc/v=nZrbZ_sYShU.srt" : "AngularJS - 29 ng-view.srt" , 
"http://zhuwei.me/youtube/cc/v=TT31mYUEAPs.srt" : "AngularJS - 30 The config function.srt" , 
"http://zhuwei.me/youtube/cc/v=gNtnxRzXj8s.srt" : "AngularJS - 31 $routeProvider api.srt" , 
"http://zhuwei.me/youtube/cc/v=T10gr1Leq6g.srt" : "AngularJS - 32 $routeParams.srt" , 
"http://zhuwei.me/youtube/cc/v=LGPXW-NgHCs.srt" : "AngularJS - 33 redirectTo.srt" , 
"http://zhuwei.me/youtube/cc/v=o84ryzNp36Q.srt" : "AngularJS - 34 Promises.srt" , 
"http://zhuwei.me/youtube/cc/v=Kr1qZ8Ik9G8.srt" : "AngularJS - 35 Resolve.srt" , 
"http://zhuwei.me/youtube/cc/v=vIDvluer97A.srt" : "AngularJS - 36 resolve conventions.srt" , 
"http://zhuwei.me/youtube/cc/v=rbqRJQZBF3Q.srt" : "AngularJS - 37 resolve $routeChangeError.srt" , 
"http://zhuwei.me/youtube/cc/v=-bv4Tp06Lxg.srt" : "AngularJS - 38 Directive for Route Handling.srt" , 
"http://zhuwei.me/youtube/cc/v=0uvAseNXDr0.srt" : "AngularJS - 39 Route Life Cycle.srt" , 
"http://zhuwei.me/youtube/cc/v=HvTZbQ_hUZY.srt" : "AngularJS - 40 Providers.srt" , 
"http://zhuwei.me/youtube/cc/v=OnSb4ebdjrk.srt" : "AngularJS - 41 Injectors.srt" , 
"http://zhuwei.me/youtube/cc/v=UCn7CwS5fKg.srt" : "AngularJS - 42 Components and Containers.srt" , 
"http://zhuwei.me/youtube/cc/v=jEpbjve5iHk.srt" : "AngularJS - 43 $index, $event, $log.srt" , 
"http://zhuwei.me/youtube/cc/v=tTihyXaz4Bo.srt" : 'AngularJS - 44 Experimental "Controller as" Syntax.srt' , 
"http://zhuwei.me/youtube/cc/v=2CdivtU5ytY.srt" : "AngularJS - 45 Directive Communication.srt" , 
"http://zhuwei.me/youtube/cc/v=ZvWftlp7TKY.srt" : "AngularJS - 46 ngmin.srt" , 
"http://zhuwei.me/youtube/cc/v=WX03ODuzkSY.srt" : "AngularJS - 47 ng-repeat-start .srt" , 
"http://zhuwei.me/youtube/cc/v=Bcv46xKJH98.srt" : "AngularJS - 48 animation basics .srt" , 
"http://zhuwei.me/youtube/cc/v=ni0N8dmxiio.srt" : "AngularJS - 49 Animating with JavaScript.srt" , 
"http://zhuwei.me/youtube/cc/v=2-xcoaba7_o.srt" : "AngularJS - 50 Animating the Angular Way.str" 
    }

for x, y in dict_srt.items():
    print x, y

    