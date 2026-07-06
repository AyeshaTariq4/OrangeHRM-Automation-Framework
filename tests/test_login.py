from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.logout_page import LogoutPage

# Chrome Options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

# Browser Launch
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Browser Settings
driver.maximize_window()

# Open Website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for page to load
time.sleep(10)

# Login Object
login = LoginPage(driver)

login.login("Admin", "admin123")

time.sleep(5)

dashboard = DashboardPage(driver)

if dashboard.verify_dashboard():
    print("Dashboard Verified Successfully!")

# Admin Object
admin = AdminPage(driver)

# Open Admin Menu
admin.open_admin()
time.sleep(3)

# Search User
admin.search_user("Admin")
time.sleep(2)

# Click Search
admin.click_search()
time.sleep(3)

# Verify Search Result
if admin.verify_user():
    print("User Search Successful!")


# PIM Object
pim = PIMPage(driver)

# Open PIM
pim.open_pim()
time.sleep(5)
driver.save_screenshot("Screenshots/PIM_Page.png")

# Open Add Employee
pim.click_add_employee()
time.sleep(3)

# Employee Details
pim.enter_first_name("Ayesha")
pim.enter_last_name("Tariq")

time.sleep(2)

# Save Employee
pim.save_employee()

time.sleep(5)

print("Employee Added Successfully!")

# Logout Object
logout = LogoutPage(driver)

# Open Profile
logout.open_profile()
time.sleep(2)

# Click Logout
logout.click_logout()
time.sleep(3)

print("Logout Successful!")
input("Press Enter to Close Browser...")

driver.quit()