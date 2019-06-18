# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("http://www.baidu.com")

# 4. 业务操作
# 测试账号：itest2018  test123456
# 添加cookie
cookie_data = {
    "name": "BDUSS",
    "value": "5peTlkTklqbGJnaC10NVFzZWdBTExxNU4tNzc5dHJuWnBFdDk4LVphUmZBTU5iQVFBQUFBJCQAAAAAAAAAAAEAAAAlASDSaXRlc3QyMDE4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF9zm1tfc5tbeE"
}
driver.add_cookie(cookie_data)

# 刷新一下页面
driver.refresh()

# 获取cookie数据
c = driver.get_cookie("BAIDUID")
print(c)

# 获取所有的cookie数据
print(driver.get_cookies())

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
