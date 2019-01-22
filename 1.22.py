from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https:www.baidu.com")
time.sleep(2)
driver.get('https:www.taobao.com')
#最大化
driver.maximize_window()
#设置窗口大小为多少
driver.set_window_size(456,333)
#刷新页面
driver.refresh()
#返回到上一页
driver.back()
#切换到下一页
driver.forward()
#截屏后设置制定的保存路径+文件名称+后缀
driver.get_screenshot_as_file('Q\\python\\1.jpg')
#close用于关闭当前窗口，当打开的窗口较多时，就可以用close关闭部分窗口
#quit用于结束进程，关闭所有的窗口
# driver.close()
# driver.quit()



