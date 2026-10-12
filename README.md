# banking-automation-project
# 🏦 Banking Automation Project

This project automates end-to-end workflows of a demo banking application using **Selenium + Pytest**.  
Modules covered:
- Login
- Account Add
- Send Money
- Transfer
- Apply Loan
- Bill Pay
- Transactions

---

## 📂 Project Structure

BankAutomation/
│
├── tests/                # Automated test cases
│   ├── test_login.py
│   ├── test_account.py
│   ├── test_sendmoney.py
│   ├── test_transfer.py
│   ├── test_applyloan.py
│   ├── test_billpay.py
│   └── test_transactions.py
│
├── pages/                # Page Object Model classes
│   ├── login_page.py
│   ├── account_page.py
│   ├── sendmoney_page.py
│   ├── transfer_page.py
│   ├── loan_page.py
│   ├── billpay_page.py
│   └── transactions_page.py
│
├── locators/             # Element locators (one per module)
│   ├── login_locators.py
│   ├── account_locators.py
│   ├── sendmoney_locators.py
│   ├── transfer_locators.py
│   ├── loan_locators.py
│   ├── billpay_locators.py
│   └── transactions_locators.py
│
├── data/                 # Test data
│   ├── testdata.json
│   └── testdata.csv
│
├── reports/              # Execution reports
│   ├── html_reports/
│   └── screenshots/
│
├── requirements.txt      # Python dependencies
├── conftest.py           # Pytest configuration
└── README.md             # Project documentation

Code



---
## 📊 Test Closure Summary Report


| **Module**             | **Planned** | **Executed** | **Passed** | **Failed** | **Pass %** |
|-------------------------|-------------|--------------|------------|------------|------------|
| Login Module            | 10          | 10           | 10         | 0          | 100%       |
| Add Account Module      | 10          | 10           | 10         | 0          | 100%       |
| Transfer Module         | 10          | 10           | 10         | 0          | 100%       |
| Send Money Module       | 10          | 10           | 10         | 0          | 100%       |
| Transaction Module      | 10          | 10           | 10         | 0          | 100%       |
| Apply Loan Module       | 10          | 10           | 10         | 0          | 100%       |
| Bill Pay Module         | 10          | 10           | 10         | 0          | 100%       |

---

### 📈 Execution Overview
- **Total Test Cases Written:** 70  
- **Total Test Cases Executed:** 70  
- **Total Test Cases Passed:** 70 
- **Total Test Cases Failed:** 00  
- **Pass Percentage:** 100% ✅

---
## 🛠️ Tools & Technologies Used

- **Selenium with Python** → Browser automation  
- **Pytest** → Test execution framework  
- **Page Object Model (POM)** → Maintainable test design  
- **Jira** → Bug tracking & test management  
- **Git & GitHub** → Version control & collaboration  
- **SQL** → Backend data validation  
- **Manual Testing** → Functional, regression, UI validation  
- **API Testing (Postman)** → REST API validation  


## 🚀 How to Run Tests
pytest -v -s


1. Install dependencies:
   ```

   
   bash
   pip install -r requirements.txt


👨‍💻 Author
QA Engineer: Gopichand Pawar

Focus: End-to-end automation, defect tracking, and reporting for BankApp project.
