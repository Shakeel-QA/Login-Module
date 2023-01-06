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

from lib.Resources import LoginModuleResources
from lib.Pag import LoginPage

def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = 'w' if new else 'a'
    with open(filename, mode, newline='') as f:
        f.writelines(data)

USER_NAME = "Shakeel_QA_Admin"
PASS_WORD = "AA@@1122"



def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    login = LoginPage(driver)
    login.enter_username(LoginModuleResources.username, 'Shakeel_QA_Admin')
    login.enter_password(LoginModuleResources.password, 'PAA@@##44')
    url = (driver.current_url)
    login.submit_btn(LoginModuleResources.submit_button)
    time.sleep(0.5)
    today = date.today()
    pop = driver.find_element(By.ID,"popUpMessage").text  
    make_csv('Login Report.csv',f'Test Case,Scenario, Result{today}, URL,Fail/Pass\n', new=True)
    make_csv('Login Report.csv',f'Login Module,Login With Correct Username and Wrong Password,{pop},{url}\n', new=False)
    time.sleep(3)
    
    login1 = LoginPage(driver)
    login1.enter_username(LoginModuleResources.username, 'Shakeel_QA_Admin')
    login1.enter_password(LoginModuleResources.password, 'AA@@1122324')
    login.submit_btn(LoginModuleResources.submit_button)
    time.sleep(0.5)
    pop1 = driver.find_element(By.ID,"popUpMessage").text  
    make_csv('Login Report.csv',f'Login Module,Login With Wrong Username and Wrong Password,{pop1},{url}\n', new=False)
    time.sleep(3)
   
    login2 = LoginPage(driver)
    login2.enter_username(LoginModuleResources.username, USER_NAME)
    login2.enter_password(LoginModuleResources.password, PASS_WORD)
    url = (driver.current_url)
    login.submit_btn(LoginModuleResources.submit_button)
    url_s = (driver.current_url)                                                           
    time.sleep(0.5)
    
    make_csv('Login Report.csv',f'Login Module,Login With Correct Username and Password,Login Successfully,{url_s}\n', new=False)
    time.sleep(3)


    make_csv('Login Report.csv',f'Login Credential,Username:{USER_NAME},Password:{PASS_WORD},\n', new=False)

if __name__ == '__main__':
    main()