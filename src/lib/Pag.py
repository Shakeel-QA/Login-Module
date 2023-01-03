from selenium.webdriver.common.by import By

# OOP Python
# object or Class
# Inharitance
# self key word

class HomePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(HomePage):
    url = "https://staging.brandsignals.io/campaign/"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)

    def enter_username(self, xpath: str, username: str):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, xpath).send_keys(username)


    def enter_password(self, xpath: str, password: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(password)


    def submit_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()