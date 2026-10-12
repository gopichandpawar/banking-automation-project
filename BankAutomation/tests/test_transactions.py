from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.transactions_page import TransactionsPage
from test_data.test_data1 import LOGIN

def test_transaction(driver):
    try:
        login = LoginPage(driver)
        login.Login_Details(LOGIN)

        transaction = TransactionsPage(driver)
        transaction.Transactions_Details()

    except Exception as e:
        driver.save_screenshot("reports/screenshorts/abc.png")
        print(f"script failed {e}")