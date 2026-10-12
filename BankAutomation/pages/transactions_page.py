from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.transaction_locators import TransactionLocators

class TransactionsPage:
    def __init__(self,driver):
        self.driver = driver

    def Transactions_Details(self):
        transactions = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, TransactionLocators.TRANSACTION))
        )
        transactions.click()

        credits1 = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,TransactionLocators.CREDITS))
        )
        credits1.click()

        debits = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, TransactionLocators.DEBITS))
        )
        debits.click()