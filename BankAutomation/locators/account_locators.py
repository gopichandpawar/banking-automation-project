class AccountLocator:
    ACCOUNT = "//div[@class='hidden md:block']//a[@href='/bank/accounts']"
    ADD_ACCOUNT = "(//div[@data-testid='accounts-page']//button)[1]"
    ACCOUNT_NAME = "//input[@id='account-form-name']"
    ACCOUNT_TYPE = "//button[@id='account-form-type-trigger']"
    PICK_UP_ACC_TYPE = "(//div//div[text()='Savings'])[1]"
    STARTING_BALANCE = "//div[@class='relative']//input[@id='base-ui-_r_f_']"
    ACCEPT_CONDITION = "//input[@id='account-form-accept-terms']"
    ADD_ACCOUNT1 = "(//div[@data-slot='dialog-footer']//button)[2]"