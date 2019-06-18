# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册实例.html")

# 4. 业务操作
# 1. 填写主页面的注册信息
driver.find_element_by_id("user").send_keys("admin")

# frame切换
# driver.switch_to.frame("idframe1")
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))


# 2. 填写注册页面A中的注册信息
driver.find_element_by_id("userA").send_keys("admin")

# 切换到主页面
driver.switch_to.default_content()

# frame切换
driver.switch_to.frame("myframe2")

# 3. 填写注册页面B中的注册信息
driver.find_element_by_id("userB").send_keys("admin")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
