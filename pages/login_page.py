from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, username, password):

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@name='username']")
            )
        ).send_keys(username)

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@name='password']")
            )
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        ).click()