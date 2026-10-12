from pages.account_page import AccountPage
from pages.login_page import LoginPage
from test_data.test_data1 import LOGIN

def test_add_account(driver):

    try:
        login = LoginPage(driver)
        login.Login_Details(LOGIN)

        acc = AccountPage(driver)
        acc.Account_Details()

    except Exception as e:
        driver.save_screenshot("reports/screenshorts/abc.png")
        print(f"script failed {e}")