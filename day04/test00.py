# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作






# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
