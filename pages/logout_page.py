from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_profile(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "oxd-userdropdown-tab")
            )
        ).click()

    def click_logout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Logout']")
            )
        ).click()