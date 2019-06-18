# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册实例.html")

# 4. 业务操作
# 填写注册A页面注册信息，填写完毕，截图保存；
driver.switch_to.frame("myframe1")
driver.find_element_by_id("userA").send_keys("admin")

# 截图
now_time = time.strftime("%Y%m%d-%H%M%S")
driver.get_screenshot_as_file("./img/{}.png".format(now_time))

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
