from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def Login_Details(self,login_data):
        username = WebDriverWait(self.driver,15).until(
            EC.visibility_of_element_located((By.XPATH,LoginLocators.USERNAME))
        )
        username.send_keys(login_data["username1"])

        password = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.PASSWORD))
        )
        password.send_keys(login_data["password1"])

        remember_me = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, LoginLocators.REMEMBER_ME))
        )
        self.driver.execute_script("arguments[0].click();", remember_me)

        sign_in = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.SIGN_IN))
        )
        sign_in.click()