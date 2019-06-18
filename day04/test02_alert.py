# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作
# 1.点击 alert 按钮
driver.find_element_by_id("alerta").click()
time.sleep(2)

# 2.关闭警告框
# 1> 获取到警告框对象
alert = driver.switch_to.alert

# 获取弹出框的提示信息
print(alert.text)

# 2> 调用关闭窗口的方法
# alert.accept()  # 点击确定按钮，建议使用
alert.dismiss()  # 点击取消按钮

# 3.输入用户名：admin
driver.find_element_by_id("userA").send_keys("admin")

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
