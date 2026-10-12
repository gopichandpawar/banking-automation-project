from pages.login_page import LoginPage
from test_data.test_data1 import LOGIN

def test_login_page(driver):
    try:
        login = LoginPage(driver)
        login.Login_Details(LOGIN)

    except Exception as e:
        driver.save_screenshot("reports/screenshorts/abc.png")
        print(f"script failed {e}")