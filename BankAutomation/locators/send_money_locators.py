class SendMoneyLocators:
    SEND_MONEY = "//a[@href='/bank/send-money']"
    FROM_ACC = "//button[@id='send-from-trigger']"
    PICK_UP_FROM_ACC = "(//div//div[text()='Everyday Checking'])[1]"
    PAYEE_ACC = "//button[@id='payee-select-trigger']"
    PICK_UP_PAYEE_ACC = "(//div//div[text()='Amit Verma'])[1]"
    AMOUNT = "//input[@id='send-amount']"
    NOTE = "//input[@id='send-note']"
    REVIEW_AND_SEND = "//button[@type='submit']"