from pages.login_page import LoginPage
from pages.billpay_page import BillPayPage
from test_data.test_data1 import LOGIN
from test_data.test_data1 import BILL_PAY

def test_billpay_page(driver):
    try:
        login = LoginPage(driver)
        login.Login_Details(LOGIN)

        bill = BillPayPage(driver)
        bill.Bill_Pay_Details(BILL_PAY)

    except Exception as e:
        driver.save_screenshot("reports/screenshorts/abc.png")
        print(f"script failed {e}")