import unittest
from selenium import webdriver


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost")

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys("13012345678")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_name("sbtbutton").click()

        msg = self.driver.find_element_by_css_selector(".layui-layer-content").text
        print("msg=", msg)
