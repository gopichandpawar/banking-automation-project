from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.transfer_locators import TransferLocators

class TransferPage:
    def __init__(self,driver):
        self.driver = driver

    def Transfer_Details(self):
        transfer = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, TransferLocators.TRANSFER))
        )
        transfer.click()

        from_acc = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,TransferLocators.FROM_ACC))
        )
        from_acc.click()

        pick_up_from_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, TransferLocators.PICK_UP_FROM_ACC))
        )
        pick_up_from_acc.click()

        to_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, TransferLocators.TO_ACC))
        )
        to_acc.click()

        pick_up_to_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, TransferLocators.PICK_UP_TO_ACC))
        )
        pick_up_to_acc.click()

        amount = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, TransferLocators.AMOUNT))
        )
        amount.send_keys("50")

        memo = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, TransferLocators.MEMO))
        )
        memo.send_keys("I want to transfer because i need new car")

        review_transfer = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, TransferLocators.REVIEW_THE_TRANSFER))
        )
        review_transfer.click()
