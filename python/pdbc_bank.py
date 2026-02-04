import mysql.connector
import random

# ------------------ DATABASE CONNECTION ------------------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="varsh789"
)
cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS pdbc_bank")
cursor.execute("USE pdbc_bank")

cursor.execute("""
CREATE TABLE IF NOT EXISTS holder_details (
    holder_name VARCHAR(50),
    aadhar_no BIGINT,
    mobile BIGINT,
    ifsc VARCHAR(20),
    account_type VARCHAR(20),
    account_no BIGINT PRIMARY KEY,
    balance INT
)
""")

# ------------------ BANK CLASS ------------------
class BANK:

    # CREATE ACCOUNT
    def create_account(self):
        name = input("Enter holder name: ")
        aadhar = int(input("Enter Aadhar number: "))
        mobile = int(input("Enter mobile number: "))
        acc_type = input("Account type (saving/zero): ").lower()
        ifsc = "IFSC12345"

        acc_no = random.randint(10000000000, 99999999999)
        balance = 500 if acc_type == "saving" else 100

        sql = """
        INSERT INTO holder_details
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        values = (name, aadhar, mobile, ifsc, acc_type, acc_no, balance)
        cursor.execute(sql, values)
        con.commit()

        print("\n✅ Account created successfully!")
        print("Account Number:", acc_no)

    # DEPOSIT
    def deposit(self):
        acc_no = int(input("Enter account number: "))
        amount = int(input("Enter deposit amount: "))

        cursor.execute(
            "UPDATE holder_details SET balance = balance + %s WHERE account_no = %s",
            (amount, acc_no)
        )
        con.commit()
        print("✅ Amount deposited successfully")

    # WITHDRAW
    def withdraw(self):
        acc_no = int(input("Enter account number: "))
        amount = int(input("Enter withdraw amount: "))

        cursor.execute(
            "SELECT balance FROM holder_details WHERE account_no = %s",
            (acc_no,)
        )
        data = cursor.fetchone()

        if data is None:
            print("❌ Account not found")
            return

        balance = data[0]

        if amount > balance:
            print("❌ Insufficient balance")
        else:
            cursor.execute(
                "UPDATE holder_details SET balance = balance - %s WHERE account_no = %s",
                (amount, acc_no)
            )
            con.commit()
            print("✅ Withdrawal successful")

    # CHECK BALANCE
    def check_balance(self):
        acc_no = int(input("Enter account number: "))

        cursor.execute(
            "SELECT holder_name, balance FROM holder_details WHERE account_no = %s",
            (acc_no,)
        )
        data = cursor.fetchone()

        if data:
            print("\nAccount Holder:", data[0])
            print("Current Balance: ₹", data[1])
        else:
            print("❌ Account not found")

        def check_details(self):
            acc_no = int(input("Enter account number: "))

            cursor.execute(
                "SELECT * FROM holder_details WHERE account_no = %s",
                (acc_no,)
            )
            data = cursor.fetchone()

            if data:
                print("\n===== ACCOUNT DETAILS =====")
                print("Holder Name   :", data[0])
                print("Aadhar No     :", data[1])
                print("Mobile No     :", data[2])
                print("IFSC Code     :", data[3])
                print("Account Type :", data[4])
                print("Account No   :", data[5])
                print("Balance      : ₹", data[6])
            else:
                print("❌ Account not found")



# ------------------ MENU ------------------
bank = BANK()

while True:
    print("\n====== BANK MENU ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        print("Thank you for using our bank 🏦")
        break
    else:
        print("❌ Invalid choice")
