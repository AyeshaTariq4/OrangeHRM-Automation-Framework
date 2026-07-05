from selenium.webdriver.common.by import By
import time

class PIMPage:

    def __init__(self, driver):
        self.driver = driver

    def open_pim(self):
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()

    def click_add_employee(self):
        self.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()

    def enter_first_name(self, firstname):
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)

    def save_employee(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()