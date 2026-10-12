from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.billpay_locators import BillPayLocators

class BillPayPage:
    def __init__(self,driver):
        self.driver = driver

    def Bill_Pay_Details(self,bill_data):
        bill_pay = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,BillPayLocators.BILL_PAY))
        )
        bill_pay.click()

        from_account = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,BillPayLocators.FROM_ACCOUNT))
        )
        from_account.click()

        pick_up_from_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,BillPayLocators.PICK_UP_FROM_ACC))
        )
        pick_up_from_acc.click()

        biller = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,BillPayLocators.BILLER))
        )
        biller.click()

        pick_up_biller = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,BillPayLocators.PICK_UP_BILLER))
        )
        pick_up_biller.click()

        amount = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,BillPayLocators.AMOUNT))
        )
        amount.send_keys(bill_data['amount1'])

        memo = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,BillPayLocators.MEMO))
        )
        memo.send_keys(bill_data['memo1'])

        review_payment = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, BillPayLocators.REVIEW_PAYMENT))
        )
        review_payment.click()