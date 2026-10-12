class TransactionLocators:
    TRANSACTION = "//a[@href='/bank/transactions']"
    CREDITS = "(//div[@data-testid='all-txn-type-filter']//button)[2]"
    DEBITS = "(//div[@data-testid='all-txn-type-filter']//button)[3]"
