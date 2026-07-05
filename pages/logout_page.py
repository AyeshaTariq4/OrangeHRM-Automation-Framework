from selenium.webdriver.common.by import By
import time

class LogoutPage:

    def __init__(self, driver):
        self.driver = driver

    def open_profile(self):
        self.driver.find_element(
            By.CLASS_NAME,
            "oxd-userdropdown-tab"
        ).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()