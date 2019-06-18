# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作
# 1.获取用户名输入框的大小
size = driver.find_element_by_id("userA").size
print("size=", size)

# 2.获取页面上第一个超链接的文本内容
text = driver.find_element_by_tag_name("a").text
print("text=", text)

# 3.获取页面上第一个超链接的地址
href = driver.find_element_by_tag_name("a").get_attribute("href")
print("href=", href)

# 4.判断页面中的span标签是否可见
is_displayed = driver.find_element_by_tag_name("span").is_displayed()
print("is_displayed=", is_displayed)

# 5.判断页面中取消按钮是否可用
is_enabled = driver.find_element_by_id("cancelA").is_enabled()
print("is_enabled==", is_enabled)

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
