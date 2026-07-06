from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def verify_dashboard(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Dashboard']")
            )
        ).is_displayed()