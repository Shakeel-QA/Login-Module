import time, csv
from uuid import uuid1
from typing import List
import pyautogui
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from lib.Resources import LoginModuleResources, UserModuleResources
from lib.Pag import LoginPage, Click, SendKeys

def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = 'w' if new else 'a'
    with open(filename, mode, newline='') as f:
        f.writelines(data)

USER_NAME = "Shakeel_QA_Admin"
PASS_WORD = "AA@@1122"

THREE_CHARACTERS = "ABC"
SPECIAL_CHARACTERS = "@#@@##@#@$#@$"
USERS_NAMES = "Shakeel_9T5q"
WRONG_EMAIL = "Ali@.com"
CORRECT_EMAIL = "ShakeeNineqqT6lD4a@gmail.com"
WRONG_PASSWORD = "AS323232"
CORRECT_PSWD = "AA@@1122"
SCND_WRONG_PSWD = "SDSDASD"
SCND_CORRECT_PSWD  = "AA@@1122"
# SERCH_NAME = "@#@@##@#@$#@$"


def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    
    Login = LoginPage(driver)
    Login.enter_username(LoginModuleResources.username, USER_NAME)
    Login.enter_password(LoginModuleResources.password, PASS_WORD)
    Login.click_login_btn(LoginModuleResources.submit_button)
    url = (driver.current_url)
    time.sleep(0.5)
    today = date.today()
    make_csv('user Report.csv',f'Test Case,Scenario, Result{today}, URL\n', new=True)
    make_csv('user Report.csv',f'Login Credential,Username : {USER_NAME},Password : {PASS_WORD}\n', new=False)
    make_csv('user Report.csv',f'User Module,Login With Correct Username and Password,Login Successfully,{url},\n', new=False)
    time.sleep(1)
    
    
    Username1 = Click(driver)
    Username1.Click_button(UserModuleResources.User_Module)
    url_s = (driver.current_url)
    time.sleep(0.5)

    Add_User = Click(driver)
    Add_User.Click_button(UserModuleResources.Add_New_User_Btn)
    time.sleep(0.5)
    
    
    Username3 = SendKeys(driver)
    Username3.send_keys(UserModuleResources.User_Name, THREE_CHARACTERS)
    time.sleep(1)

    pop_nam2 = driver.find_element(By.XPATH, "//*[@id='usernameuser']").text
    make_csv('user Report.csv',f'User Module,Check User Name Less Than 5 Characters,{pop_nam2},{url_s},\n', new=False)
    time.sleep(0.5)
 

    User_name1 = driver.find_element(By.XPATH, "//input[@id='user_username']").clear()
    time.sleep(0.5)

    Username4 = SendKeys(driver)
    Username4.send_keys(UserModuleResources.User_Name, SPECIAL_CHARACTERS)
    time.sleep(1)

    pop_nam4 = driver.find_element(By.XPATH, "//*[@id='usernamespace']").text
    make_csv('user Report.csv',f'User Module,Check Special Character in User Name,{pop_nam4},{url_s},\n', new=False)

    User_name1 = driver.find_element(By.XPATH, "//input[@id='user_username']").clear()


    Username4 = SendKeys(driver)
    Username4.send_keys(UserModuleResources.User_Name, USERS_NAMES)
    time.sleep(1)
    make_csv('user Report.csv',f'User Module,Add Username as Per Requirement, Username Accepted,{url_s}\n', new=False)

    Position = Click(driver)
    Position.Click_button(UserModuleResources.position)
    time.sleep(0.5)
    make_csv('user Report.csv',f'User Module,Select Position from Drop Down,Position has been Selected,{url_s}\n', new=False)
    time.sleep(0.5)

    Email_1 = SendKeys(driver)
    Email_1.send_keys(UserModuleResources.Email, WRONG_EMAIL)
    time.sleep(1)

    Email_2 = driver.find_element(By.XPATH, "//*[@id='email-pattern']").text
    make_csv('user Report.csv',f'User Module,Add Wrong Email Pattern,{Email_2},{url_s}\n', new=False)
    time.sleep(1)

    User_name4 = driver.find_element(By.XPATH, "//*[@id='email']").clear()

    Email_2 = SendKeys(driver)
    Email_2.send_keys(UserModuleResources.Email, CORRECT_EMAIL)
    time.sleep(1)

    Email_3 = driver.find_element(By.XPATH, "//*[@id='email-pattern']").text
    make_csv('user Report.csv',f'User Module,Add Correct Email Pattern,Email Accepted,{url_s} \n', new=False)
    time.sleep(1)

    Password_1 = SendKeys(driver)
    Password_1.send_keys(UserModuleResources.Password, WRONG_PASSWORD)
    time.sleep(1)

    Password_2 = driver.find_element(By.XPATH, "//*[@id='passwordNotMatch-id-first']").text
    make_csv('user Report.csv',f'User Module,Add Wrong Password,{Password_2},{url_s} \n', new=False)
    time.sleep(1)

    Password_remove = driver.find_element(By.XPATH, "//*[@id='password']").clear()

    Password_3 = SendKeys(driver)
    Password_3.send_keys(UserModuleResources.Password, CORRECT_PSWD)
    time.sleep(1)

    Password_4 = driver.find_element(By.XPATH, "//*[@id='passwordNotMatch-id-first']").text
    make_csv('user Report.csv',f'User Module,Add Correct Password,Password Accepeted,{url_s} \n', new=False)
    time.sleep(1)

    Password_5 = SendKeys(driver)
    Password_5.send_keys(UserModuleResources.Password1, SCND_WRONG_PSWD)
    time.sleep(1)

    Password_6 = driver.find_element(By.XPATH, "//*[@id='error-id-first']").text
    make_csv('user Report.csv',f'User Module,Add Wrong Second Password,{Password_6},{url_s}\n', new=False)
    time.sleep(1)

    Password_remove2 = driver.find_element(By.XPATH, "//*[@id='password1']").clear()

    Password_7 = SendKeys(driver)
    Password_7.send_keys(UserModuleResources.Password1, SCND_CORRECT_PSWD)
    time.sleep(1)

    Password_8 = driver.find_element(By.XPATH, "//*[@id='success-id-first']").text
    make_csv('user Report.csv',f'User Module,Add Correct Second Password,{Password_8},{url_s}\n', new=False)
    time.sleep(1)

    Add_User_btn = Click(driver)
    Add_User.Click_button(UserModuleResources.Add_User_Btn)
    time.sleep(0.5)
    make_csv('user Report.csv',f'User Module,Click on Add User Button, Button is working,{url_s}\n', new=False)

    Creat_User = driver.find_element(By.XPATH, "//*[@id='popUpMessage']").text
    make_csv('user Report.csv',f'User Module,Create User,{Creat_User},{url_s}\n', new=False)
    make_csv('user Report.csv',f'User Module,Created Username,{USERS_NAMES},{url_s}\n', new=False)
   
    time.sleep(1)
    
    Search_Bar = SendKeys(driver)
    Search_Bar.send_keys(UserModuleResources.Search_User, USERS_NAMES)
    time.sleep(2)

    Three_Dots = Click(driver)
    Add_User.Click_button(UserModuleResources.Three_Dots)
    time.sleep(1)
    make_csv('user Report.csv',f'User Module,Click on Three Dots Button, Button is working,{url_s}\n', new=False)
    time.sleep(3)

    
    User_Details = Click(driver)
    Add_User.Click_button(UserModuleResources.User_Details)
    url_t = (driver.current_url)
    time.sleep(1)
    make_csv('user Report.csv',f'User Module,Click on User Details Button,Button is working,{url_t}\n', new=False)
    time.sleep(10)

    

if __name__ == '__main__':
    main()