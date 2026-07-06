from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_admin(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Admin']")
            )
        ).click()

    def search_user(self, username):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
            )
        ).send_keys(username)

    def click_search(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        ).click()

    def verify_user(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@role='table']")
            )
        ).is_displayed()