from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.send_money_locators import SendMoneyLocators

class SendMoneyPage:
    def __init__(self,driver):
        self.driver = driver

    def send_money_detains(self):
        send_money = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,SendMoneyLocators.SEND_MONEY))
        )
        send_money.click()

        from_account = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SendMoneyLocators.FROM_ACC))
        )
        from_account.click()

        pick_up_from_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SendMoneyLocators.PICK_UP_FROM_ACC))
        )
        pick_up_from_acc.click()

        payee_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SendMoneyLocators.PAYEE_ACC))
        )
        payee_acc.click()

        pick_up_payee_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SendMoneyLocators.PICK_UP_PAYEE_ACC))
        )
        pick_up_payee_acc.click()

        amount = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SendMoneyLocators.AMOUNT))
        )
        amount.click()

        note = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SendMoneyLocators.NOTE))
        )
        note.click()

        review_and_send = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SendMoneyLocators.REVIEW_AND_SEND))
        )
        review_and_send.click()

