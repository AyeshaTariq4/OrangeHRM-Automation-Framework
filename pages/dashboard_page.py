from selenium.webdriver.common.by import By

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard(self):
        return self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()