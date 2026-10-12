class TransferLocators:
    TRANSFER = "//a[@href='/bank/transfer']"
    FROM_ACC = "//button[@id='transfer-from-trigger']"
    PICK_UP_FROM_ACC = "(//div//div[contains(text(),'Everyday Checking')])"
    TO_ACC = "//button[@id='transfer-to-trigger']"
    PICK_UP_TO_ACC = "(//div//div[contains(text(),'High-Yield Savings')])[2]"
    AMOUNT = "//input[@id='transfer-amount']"
    MEMO = "//div[@class='bank-field-row']//input[@id='base-ui-_r_d_']"
    REVIEW_THE_TRANSFER = "//button[@type='submit']"