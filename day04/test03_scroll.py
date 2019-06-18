# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作
# 暂停2秒后，滚动条拉倒最底层
time.sleep(2)
# 编写操作滚动条的js脚本
js = "window.scrollTo(0, 100000)"
# 执行js脚本
driver.execute_script(js)

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
