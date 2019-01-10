from selenium import webdriver
import xlwt
from  datetime import datetime
driver = webdriver.Chrome()
driver.get("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8")
w = driver.find_elements_by_css_selector("li.gl-item div.p-price")
o =driver.find_elements_by_css_selector("div.p-name p-name-type-2")
c = len(w)
wd = xlwt.Workbook()
ws = wd.add_sheet("jd")
ws.write(0,0,"shouji")
ws.write(0,1,"jiage")
for index in range(c):
    ws.write( index+1,0, o[index].text)
    ws.write( index+1,1, w[index].text)
wd.save("p.xls") 
