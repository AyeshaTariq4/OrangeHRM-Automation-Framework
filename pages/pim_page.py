from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_pim(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='PIM']")
            )
        ).click()

    def click_add_employee(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Add Employee']")
            )
        ).click()

    def enter_first_name(self, firstname):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "firstName")
            )
        ).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "lastName")
            )
        ).send_keys(lastname)

    def save_employee(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        ).click()