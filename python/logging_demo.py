import random
import logging

# Logging Configuration
logging.basicConfig(
    filename='bank123.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Bank:

    def __init__(self):
        self.Holder_Details = []

    # ------------------ CREATE ACCOUNT ------------------
    def create_new_account(self):
        print("--------- Welcome to Union Bank ------------")

        new_holder = {}

        new_holder['holder_name'] = input('Enter holder name: ')
        new_holder['aadhar_num'] = int(input('Enter Aadhar number: '))
        new_holder['mobile'] = input('Enter mobile number: ')
        new_holder['IFSC_CODE'] = 'IFSC2026'

        account_number = random.randint(1111111111, 9999999999)
        new_holder['account_number'] = account_number

        account_type = input('Select account type (Saving/Zero): ').lower()

        if account_type == 'saving':
            print("You must deposit exactly 500 rupees.")
            amount = int(input("Enter deposit amount: "))

            if amount == 500:
                new_holder['sufficient_balance'] = amount
                self.Holder_Details.append(new_holder)
                logging.info(f"New Saving Account Created: {new_holder}")
                print("Account Created Successfully!")
                print(f"Your Account Number is {account_number}")
            else:
                print("Deposit must be exactly 500 rupees.")

        elif account_type == 'zero':
            print("You must deposit exactly 100 rupees.")
            amount = int(input("Enter deposit amount: "))

            if amount == 100:
                new_holder['sufficient_balance'] = amount
                self.Holder_Details.append(new_holder)
                logging.info(f"New Zero Account Created: {new_holder}")
                print("Account Created Successfully!")
                print(f"Your Account Number is {account_number}")
            else:
                print("Deposit must be exactly 100 rupees.")

        else:
            print("Invalid account type selected.")

    # ------------------ DEPOSIT ------------------
    def deposit(self):
        print("------------ Deposit Option --------------")

        name = input("Enter holder name: ")
        acc_no = int(input("Enter account number: "))
        amount = int(input("Enter amount to deposit: "))

        for holder in self.Holder_Details:
            if holder['holder_name'] == name and holder['account_number'] == acc_no:
                holder['sufficient_balance'] += amount
                logging.info(f"Deposit: {amount} deposited to account {acc_no}")
                print("Deposit Successful!")
                break
        else:
            logging.warning(f"Failed deposit attempt for account {acc_no}")
            print("Account not found!")

    # ------------------ WITHDRAW ------------------
    def withdraw(self):
        print("------------ Withdraw Option --------------")

        name = input("Enter holder name: ")
        acc_no = int(input("Enter account number: "))
        amount = int(input("Enter amount to withdraw: "))

        for holder in self.Holder_Details:
            if holder['holder_name'] == name and holder['account_number'] == acc_no:

                if holder['sufficient_balance'] >= amount:
                    holder['sufficient_balance'] -= amount
                    logging.info(f"Withdraw: {amount} withdrawn from account {acc_no}")
                    print("Withdraw Successful!")
                else:
                    logging.error(f"Insufficient balance for account {acc_no}")
                    print("Insufficient Balance!")

                break
        else:
            logging.warning(f"Withdraw attempt on invalid account {acc_no}")
            print("Account not found!")

    # ------------------ CHECK BALANCE ------------------
    def check_balance(self):
        print("------------ Check Balance Option --------------")

        name = input("Enter holder name: ")
        acc_no = int(input("Enter account number: "))

        for holder in self.Holder_Details:
            if holder['holder_name'] == name and holder['account_number'] == acc_no:
                print(f"Your Current Balance is: {holder['sufficient_balance']}")
                logging.info(f"Balance Checked: Account {acc_no}")
                break
        else:
            logging.warning(f"Balance check attempt on invalid account {acc_no}")
            print("Account not found!")

    # ------------------ CHECK DETAILS ------------------
    def check_details(self):
        print("------------ Check Account Details --------------")

        name = input("Enter holder name: ")
        acc_no = int(input("Enter account number: "))

        for holder in self.Holder_Details:
            if holder['holder_name'] == name and holder['account_number'] == acc_no:

                print(f"Holder Name : {holder['holder_name']}")
                print(f"Aadhar Number : {holder['aadhar_num']}")
                print(f"Mobile Number : {holder['mobile']}")
                print(f"IFSC Code : {holder['IFSC_CODE']}")
                print(f"Account Number : {holder['account_number']}")
                print(f"Balance : {holder['sufficient_balance']}")

                logging.info(f"Account Details Checked: {acc_no}")
                break
        else:
            logging.warning(f"Account details check for invalid account {acc_no}")
            print("Account not found!")


# ------------------ MAIN PROGRAM ------------------

bank = Bank()

while True:
    print("\n------ UNION BANK MENU ------")
    print("1. Create New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Check Details")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        bank.create_new_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        bank.check_details()
    elif choice == "6":
        print("Thank you for using our bank 🏦")
        logging.info("Bank application exited")
        break
    else:
        print("Invalid choice. Please enter 1-6.")
        logging.warning(f"Invalid menu choice: {choice}")