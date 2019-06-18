# 1. 导包
from selenium import webdriver
import time

# 2. 创建浏览器驱动对象
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()  # 火狐

# 3. 打开网页
driver.get("D:\\webAutoTest\\page\\注册A.html")

# 4. 业务操作
# 通过定位元素的方式
# 1.选择‘广州’
# driver.find_element_by_css_selector("option[value='gz']").click()
#
# # 2.暂停2秒，选择‘上海’
# time.sleep(2)
# driver.find_element_by_css_selector("option[value='sh']").click()
#
# # 3.暂停2秒，选择‘北京’
# time.sleep(2)
# driver.find_element_by_css_selector("option[value='bj']").click()


# 通过Select类来实现
select = Select(driver.find_element_by_id("selectA"))  # 实例化Select类
# 1.选择‘广州’
select.select_by_index(2)  # 通过索引操作
# 2.暂停2秒，选择‘上海’
time.sleep(2)
select.select_by_value("sh")  # 通过option的value属性值来操作
# 3.暂停2秒，选择‘北京’
time.sleep(2)
select.select_by_visible_text("A北京") # 通过option的文本内容来操作


# 5. 暂停3秒
time.sleep(3)

# 6. 关闭浏览器驱动
driver.quit()
