from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


option = webdriver.ChromeOptions()
option.add_argument("--incognito")
 
browser = webdriver.Chrome()

browser.get("https://finance.yahoo.com/quote/AAPL?ltr=1") 

titles_element = browser.find_elements_by_xpath("//*[@class='C(black)']")
titles = []
for x in titles_element:
 titles.append(x.text)

print "Titles:",titles

values_element = browser.find_elements_by_xpath("//td[@class='Ta(end) Fw(b)']")
values = []
for x in values_element:
 values.append(x.text)

print "values:",values

for title,value in zip(titles,values):
 print title + ':' + value

