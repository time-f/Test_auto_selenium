# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册实例.html")

# 4. 业务操作
print("current_window_handle=", driver.current_window_handle)
print("window_handles=", driver.window_handles)
print("-----------------------------")

# 点击‘注册A页面’链接，在打开的页面，填写A页面注册信息；
driver.find_element_by_link_text("注册A网页").click()

print("current_window_handle=", driver.current_window_handle)
print("window_handles=", driver.window_handles)
print("-----------------------------")

# 窗口切换
driver.switch_to.window(driver.window_handles[1])
print("current_window_handle=", driver.current_window_handle)

driver.find_element_by_id("userA").send_keys("admin")

# 关闭当前窗口
driver.close()

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
