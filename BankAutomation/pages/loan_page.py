from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.applyloan_locators import ApplyLoanLocators

class ApplyLoanPage:
    def __init__(self,driver):
        self.driver = driver

    def apply_loan_detains(self,loan_data):
        apply_laon = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,ApplyLoanLocators.APPLY_LOAN))
        )
        apply_laon.click()

        apply_for_loan = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.APPLY_FOR_LOAN))
        )
        apply_for_loan.click()

        loan_type = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.LOAN_TYPE))
        )
        loan_type.click()

        pick_up_loan_type = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.PICK_UP_LOAN_TYPE))
        )
        pick_up_loan_type.click()

        loan_amount = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, ApplyLoanLocators.AMOUNT))
        )
        loan_amount.send_keys(loan_data['loan_amount1'])

        term_len = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.TERM_LEN))
        )
        term_len.click()

        pick_up_term_len = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.PICK_UP_TERM_LEN))
        )
        pick_up_term_len.click()

        interest = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.INTEREST))
        )
        interest.click()

        dis_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.DIS_ACC))
        )
        dis_acc.click()

        pick_up_dis_acc = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.PICK_UP_DIS_ACC))
        )
        pick_up_dis_acc.click()

        purpose = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, ApplyLoanLocators.PURPOSE))
        )
        purpose.send_keys(loan_data['purpose1'])

        review_application = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, ApplyLoanLocators.REVIEW_THE_APP))
        )
        review_application.click()