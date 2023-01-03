from selenium.webdriver.common.by import By




class BasePage:
    def __init__(self, driver):
        self.driver = driver



class LoginPage(BasePage):
    url = "https://staging.brandsignals.io/campaign/"
    
    def enter_username(self, xpath: str, username: str):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, xpath).send_keys(username)
    def enter_password(self, xpath: str, password: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(password)
    def click_login_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        return 'Invalid Credentials' not in self.driver.page_source


class Click(BasePage):
    def Click_button(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()


class SendKeys(BasePage):
    def send_keys(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)