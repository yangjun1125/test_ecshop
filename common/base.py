import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(browser="chrome"):
    # 打开浏览器
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        driver = None
        print("请输入正确的浏览器,例如'chrome','firefox','ie'")
    return driver


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """
        打开网址
        :return:
        """
        self.driver.get(url)
        # 窗口最大化
        self.driver.maximize_window()

    def find_element(self, locator, timeout=10):
        """定位一个元素"""
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=10):
        """定位一组元素"""
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator, timeout=10):
        """
        点击元素
        :return:
        """
        element = self.find_element(locator=locator, timeout=timeout)
        element.click()

    def send_keys(self, locator, text, timeout=10):
        """
        写入数据
        :return:
        """
        element = self.find_element(locator=locator, timeout=timeout)
        element.clear()
        element.send_keys(str(text))

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本是否存在于文本中
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout=timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value, timeout=10):
        """
        判断value属性值是否相同
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout=timeout).until(
                EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()


if __name__ == '__main__':
    # 调用方法打开浏览器
    driver = open_browser()
    # 实例化对象
    base = Base(driver)
    # 打开网站
    url = "http://localhost:8080/ecshop/user.php"
    base.open_url(url)
    time.sleep(2)
    # 输入用户名
    locator = ("name", "username")
    base.send_keys(locator=locator, text="yangjun")
    time.sleep(2)
    # 输入密码
    locator = ("name", "password")
    base.send_keys(locator=locator, text="123456")
    time.sleep(2)
    # 点击立即登录
    locator = ("name", "submit")
    base.click(locator=locator)
    time.sleep(2)
    # 关闭
    base.close_browser()
    base.close_browser()
    base.close_browser()
