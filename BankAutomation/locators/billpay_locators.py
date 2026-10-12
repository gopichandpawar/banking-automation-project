class BillPayLocators:
    BILL_PAY = "//a[@href='/bank/bill-pay']"
    FROM_ACCOUNT = "//button[@id='bill-pay-from-trigger']"
    PICK_UP_FROM_ACC = "(//div//div[text()='Everyday Checking'])[1]"
    BILLER = "//input[@id='biller-search-input']"
    PICK_UP_BILLER = "(//div[@id='biller-search-results']//button)[1]"
    AMOUNT = "//input[@id='bill-amount']"
    MEMO = "//input[@id='bill-memo']"
    REVIEW_PAYMENT = "//button[@type='submit']"

