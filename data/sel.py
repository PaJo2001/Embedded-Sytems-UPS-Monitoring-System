import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import getpass
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import time

# chrome_options = Options()

# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# #Change chrome driver path accordingly
# chrome_driver = "/usr/bin/google-chrome"
# driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
# print(driver.title)
driver=webdriver.Firefox()
driver.get("http:onem2m.iiit.ac.in:443/webpage")
driver.find_element_by_tag_name('button').click()
time.sleep(25)
# list=driver.find_element_by_id('_in-cse')
# items=list.find_elements_by_tag_name("li")
# for item in items:
# 	text=item.text
# 	print(item.text)
# 	if text=="Team40_DG_performance_monitoring":
# 		item.click()
# list=driver.find_element_by_id("_in-cse_CAE241922113")
items2=driver.find_elements_by_tag_name("li")
for item2 in items2:
	# print("hello")
	text1=item2.text
	if "cin" in text1:
		# print("hello")
		item2.click()
		x=''
		try:
			x=print(driver.find_element_by_id("cont").text)
		except:
			print(x)
		# print(text1)
	# print(driver.find_element_by_id("cont").text)
	# if text1=="pr_2_esp32_1":
	# 	item2.click()
	# 	list=driver.find_element_by_id("_in-cse_cnt-831483825")
	# 	items3=list.find_elements_by_tag_name("li")
	# 	for item3 in items3:
	# 		text2=item3.text
	# 		print(text2)
# 					if text2=="oe":
# 						item3.click()
# 						list=driver.find_element_by_id("_in-cse_cnt-835644480")
# 						items4=list.find_elements_by_tag_name("li")
# 						for item4 in items4:
# 							if item4.text=="oe_1_temperature":
# 								item4.click()
# 								# print("hello")
# 								# driver.implicitly_wait(120000)
# 								list=driver.find_element_by_id("_in-cse_cnt-169647129")
# 								# print(list.size())
# 								items5=list.find_elements_by_tag_name("li")
# 								# print(len(list))
# 								# for item5 in items5:
# 									# if "cin" in item5.text:
# 									# print(item5.text)
# 										# item5.click()
# 										# con=driver.find_element_by_id("cont")
# 										# print(con.text)
# 	# 				# print(text2)				
# 	# 				# if "cin" in text2:
# 	# 				# 	item3.click()
# 	# 				# 	print(text2)
# 	# 					# con=driver.find_element_by_id("cont")
# 	# 					# print(con.text)