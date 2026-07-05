from selenium.webdriver.common.by import By


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def open_admin(self):
        self.driver.find_element(By.XPATH, "//span[text()='Admin']").click()

    def search_user(self, username):
        self.driver.find_element(
            By.XPATH,
            "(//input[@class='oxd-input oxd-input--active'])[2]"
        ).send_keys(username)

    def click_search(self):
        self.driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def verify_user(self):
        return self.driver.find_element(
            By.XPATH,
            "//div[@role='table']"
        ).is_displayed()