# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作
# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
# try:
#     print("start time=", time.strftime("%Y-%m-%d %H:%M:%S"))
#     # 1> 创建WebDriverWait类的对象
#     wait = WebDriverWait(driver, 10, 1)
#     # 2> 调用until方法
#     element = wait.until(lambda x: x.find_element_by_id("userA666"))
#     element.send_keys("admin")
# except Exception as e:
#     print(type(e))
# finally:
#     print("end   time=", time.strftime("%Y-%m-%d %H:%M:%S"))


# 使用隐式等待定位用户名输入框，如果元素存在，就输入admin
try:
    print("start time=", time.strftime("%Y-%m-%d %H:%M:%S"))
    # 设置隐式等待，全局的作用域
    driver.implicitly_wait(10)

    driver.find_element_by_id("userA666").send_keys("admin")
except Exception as e:
    print(type(e))
finally:
    print("end   time=", time.strftime("%Y-%m-%d %H:%M:%S"))

# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
