from pages.login_page import LoginPage
from pages.send_money_page import SendMoneyPage
from test_data.test_data1 import LOGIN

def test_send_money(driver):
    try:
        login = LoginPage(driver)
        login.Login_Details(LOGIN)

        send_money = SendMoneyPage(driver)
        send_money.send_money_detains()

    except Exception as e:
        driver.save_screenshot("reports/screenshorts/abc.png")
        print(f"script failed {e}")