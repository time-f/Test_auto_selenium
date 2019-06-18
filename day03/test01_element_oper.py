# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作
# 1. 通过脚本执行输入 用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
driver.find_element_by_id("userA").send_keys("admin")
driver.find_element_by_id("passwordA").send_keys("123456")
driver.find_element_by_id("telA").send_keys("18611111111")
driver.find_element_by_id("emailA").send_keys("123@qq.com")

# 2. 间隔3秒，修改电话号码为：18600000000
time.sleep(3)
# 修改：先清空再输入新的内容
driver.find_element_by_id("telA").clear()  # 清空
driver.find_element_by_id("telA").send_keys("186000000000")

# 3. 间隔3秒，点击注册用户A
time.sleep(3)
driver.find_element_by_tag_name("button").click()

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
