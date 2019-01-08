from selenium import webdriver
import  unittest
# 测试账号：
# 用户名：testuser01
# 密码：123456
# nrl = "http://39.107.96.138:3000/"
class Cnode(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
    
    def test_register(self):#注册 固定写法 用test开始
        self.driver.find_element_by_css_selector('a[href="//signup"]').click()
        self.driver.find_element_by_id("loginname").send_keys("wangyou")
        self.driver.find_element_by_id("pass").send_keys("123456")
        self.driver.find_element_by_id("re_pass").send_keys("123456")
        self.driver.find_element_by_id("email").send_keys("123456@163.com")
        self.driver.find_element_by_class_name("span-primary").click()
    def test_login(self):#登录
        self.driver.find_element_by_css_selector('a[href="/signin"]').click()
        self.driver.find_element_by_id("name").send_keys("user1")
        self.driver.find_element_by_id("pass").send_keys("123456")
        self.driver.find_element_by_class_name("span-primary").click()

    def tearDown(self):
        self.driver.save_screenshot("./01.png")
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()