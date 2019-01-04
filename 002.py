import xlwt
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8")
s  = driver.find_elements_by_css_selector("li.gl-item div.p-price")
print(len(s))
for index in range(len(s)):
    print(s(index).text)