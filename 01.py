import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
"""
�����˻�:
�û�����user1  
���룺123456
"""

class Cnode(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
        # ��½�û�
        self.driver.find_element_by_css_selector('a[href="/signin"]').click()
        # �û���
        self.driver.find_element_by_id('name').send_keys('user1')
        # ����
        self.driver.find_element_by_id('pass').send_keys('123456')
        # ��½
        self.driver.find_element_by_css_selector('input[type="submit"]').click()
# """
# ��½�ɹ���,ҳ�浼������ҳ
# ��������Ĳ���
# 1.��ҳ�����������--���ⷢ��ҳ��
# 2.ѡ��һ�����
# 3.�������
# 4.�����ı�
# 5.�ύ
# �뽫����5������������test_post��ʵ��

    def test_post_topic(self):
        driver = self.driver
        driver.find_element_by_class_name("span-success").click()
        driver.find_element_by_css_selector("select#tab-value").click()
        driver.find_element_by_css_selector("select#tab-value>option:nth-child(2)").click()
        driver.find_element_by_css_selector(".span9").send_keys("����Բ���һ��һ����һ��")

        menu = driver.find_element_by_css_selector('div.CodeMirror-scroll')
        #hidden_submenu = driver.find_element_by_css_selector("div.CodeMirror-scroll")

        action = ActionChains(driver)
        action.move_to_element(menu)
        action.click(menu).send_keys("���Բ���һ��һ�²��Բ���һ��һ��")
        action.perform()

        driver.find_element_by_css_selector('input[type="submit"]').click()
        sleep(4)



    def tearDown(self):
        self.driver.save_screenshot('./posttopic.png')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()