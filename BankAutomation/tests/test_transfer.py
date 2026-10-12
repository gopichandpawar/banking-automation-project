from pages.login_page import LoginPage
from pages.transfer_page import TransferPage
from test_data.test_data1 import LOGIN

def test_transfer(driver):
    try:
        login = LoginPage(driver)
        login.Login_Details(LOGIN)

        transfer = TransferPage(driver)
        transfer.Transfer_Details()

    except Exception as e:
        driver.save_screenshot("reports/screenshorts/abc.png")
        print(f"script failed {e}")

