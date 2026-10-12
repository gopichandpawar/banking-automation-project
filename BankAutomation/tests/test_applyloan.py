from pages.login_page import LoginPage
from pages.loan_page import ApplyLoanPage
from test_data.test_data1 import LOGIN
from test_data.test_data1 import LOAN_APPLY

def test_apply_loan(driver):

    try:
        login = LoginPage(driver)
        login.Login_Details(LOGIN)

        loan = ApplyLoanPage(driver)
        loan.apply_loan_detains(LOAN_APPLY)

    except Exception as e:
        driver.save_screenshot("reports/screenshorts/abc.png")
        print(f"script failed {e}")

