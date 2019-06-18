# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作
# 1>浏览器窗口最大化
# driver.maximize_window()
# time.sleep(1)

# 2>改变窗口的大小
# driver.set_window_size(500, 400)
# time.sleep(1)

# 3>改变窗口的位置
# driver.set_window_position(300, 300)


# 后退
# driver.find_element_by_link_text("AA 新浪 网站").click()
# driver.back()
# time.sleep(2)

# 前进
# driver.forward()
# time.sleep(2)

# 刷新
# driver.refresh()


# 打开新的窗口
# driver.find_element_by_link_text("访问 新浪 网站").click()
# time.sleep(2)

# 关闭当前窗口（一个窗口）
# driver.close()

# 获取当前的标题
print("title=", driver.title)

# 获取当前页面的url
print("url=", driver.current_url)


# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
