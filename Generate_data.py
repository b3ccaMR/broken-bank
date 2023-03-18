# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:05:12 2023

@author: Becca
"""

import csv
import random
import string

# Generate random names for customers and employees
def random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Generate random addresses
def random_address():
    address = ['123 Main St', '456 Elm St', '789 Oak St', '555 Maple Ave','122 Apple Way','5511 Tree Ave']
    city = ['New York', 'Los Angeles', 'Chicago', 'Houston','Seattle','Orlando']
    state = ['NY', 'CA', 'IL', 'TX','WA','FL']
    zip_code = ['10001', '90001', '60601', '77001','98404','55322']
    return random.choice(address) + ',' + random.choice(city) + ',' + random.choice(state) + ',' + random.choice(zip_code)

# Generate random phone numbers
def random_phone():
    return '555-' + '{:03}'.format(random.randint(0, 999)) + '-' + '{:04}'.format(random.randint(0, 9999))

# Generate random email addresses
def random_email(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length)) + '@example.com'

# Generate random account numbers
def random_account_number(length):
    return ''.join(random.choice(string.digits) for i in range(length))

# Generate random transaction amounts
def random_transaction_amount():
    return round(random.uniform(-1000, 1000), 2)

# Generate random loan amounts
def random_loan_amount():
    return round(random.uniform(1000, 100000), 2)

# Generate random credit card balances
def random_credit_card_balance():
    return round(random.uniform(0, 5000), 2)

# Generate random employee IDs
def random_employee_id():
    return random.randint(1000, 9999)

# Generate random branch IDs
def random_branch_id():
    return random.randint(1, 10)

# Generate customer data
customers = []
for i in range(100000):
    customer_id = i + 1
    name = random_name(10)
    address = random_address()
    phone = random_phone()
    email = random_email(8)
    customers.append([customer_id, name, address, phone, email])

# Write customer data to a CSV file
with open('customers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['customer_id', 'name', 'address', 'phone', 'email'])
    for customer in customers:
        writer.writerow(customer)

# Generate account data
accounts = []
for i in range(100000):
    account_id = i + 1
    customer_id = random.randint(1, 100000)
    account_number = random_account_number(10)
    account_type = random.choice(['Checking', 'Savings'])
    balance = round(random.uniform(0, 10000), 2)
    interest_rate = round(random.uniform(0, 0.1), 4)
    accounts.append([account_id, customer_id, account_number, account_type, balance, interest_rate])

# Write account data to a CSV file
with open('accounts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['account_id', 'customer_id', 'account_number', 'account_type', 'balance', 'interest_rate'])
    for account in accounts:
        writer.writerow(account)

# Generate transaction data
transactions = []
for i in range(100000):
    transaction_id = i + 1
    account_id = random.randint(1, 100000)
    transaction_type = random.choice(['Deposit', 'Withdrawal', 'Transfer'])
    amount = random_transaction_amount()
    date = '2023-03-' + '{:02}'.format(random.randint(1, 31))
    transactions.append([transaction_id, account_id, transaction_type, amount, date])


# Write transaction data to a CSV file
with open('transactions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_id', 'account_id', 'transaction_type', 'transaction_amount','transaction_date'])
    for transaction in transactions:
        writer.writerow(transaction)

# Generate loan data
loans = []
for i in range(50000):
    loan_id = i + 1
    customer_id = random.randint(1, 100000)
    loan_amount = random_loan_amount()
    interest_rate = round(random.uniform(0.05, 0.1), 4)
    repayment_term = random.randint(1, 5)
    loans.append([loan_id, customer_id, loan_amount, interest_rate, repayment_term])

# Write loan data to a CSV file
with open('loans.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['loan_id', 'customer_id', 'loan_amount', 'interest_rate', 'repayment_term'])
    for loan in loans:
        writer.writerow(loan)

# Generate credit card data
credit_cards = []
for i in range(50000):
    credit_card_id = i + 1
    customer_id = random.randint(1, 100)
    credit_card_number = random_account_number(16)
    credit_limit = round(random.uniform(1000, 5000), 2)
    balance = random_credit_card_balance()
    credit_cards.append([credit_card_id, customer_id, credit_card_number, credit_limit, balance])

# Write credit card data to a CSV file
with open('credit_cards.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['credit_card_id', 'customer_id', 'credit_card_number', 'credit_limit', 'balance'])
    for credit_card in credit_cards:
        writer.writerow(credit_card)

# Generate employee data
employees = []
for i in range(10000):
    employee_id = random_employee_id()
    name = random_name(10)
    address = random_address()
    phone = random_phone()
    email = random_email(8)
    branch_id = random_branch_id()
    employees.append([employee_id, name, address, phone, email, branch_id])

# Write employee data to a CSV file
with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['employee_id', 'name', 'address', 'phone', 'email', 'branch_id'])
    for employee in employees:
        writer.writerow(employee)

# Generate branch data
branches = []
for i in range(1000):
    branch_id = i + 1
    address = random_address()
    phone = random_phone()
    branches.append([branch_id, address, phone])

# Write branch data to a CSV file
with open('branches.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['branch_id', 'address', 'phone'])
    for branch in branches:
        writer.writerow(branch)

