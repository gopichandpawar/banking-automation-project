from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.account_locators import AccountLocator

class AccountPage:
    def __init__(self,driver):
        self.driver = driver

    def Account_Details(self):
        account = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,AccountLocator.ACCOUNT))
        )
        account.click()

        add_account = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,AccountLocator.ADD_ACCOUNT))
        )
        add_account.click()

        account_name = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, AccountLocator.ACCOUNT_NAME))
        )
        account_name.send_keys("Gopichand Pawar")

        account_type = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, AccountLocator.ACCOUNT_TYPE))
        )
        account_type.click()

        pick_up_acc_type = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, AccountLocator.PICK_UP_ACC_TYPE))
        )
        pick_up_acc_type.click()

        starting_bal = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, AccountLocator.STARTING_BALANCE))
        )
        starting_bal.send_keys("100")

        accept_condition = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, AccountLocator.ACCEPT_CONDITION))
        )
        self.driver.execute_script("arguments[0].click();", accept_condition)

        add_account1 = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, AccountLocator.ADD_ACCOUNT1))
        )
        add_account1.click()