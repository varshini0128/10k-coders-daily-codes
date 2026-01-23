import random
class BANK:
    holder_details=[]
    def create_account(self):
        print("==========Welcome==============")
        self.add_holder={}

        self.add_holder['holder_name']=input("enter holdername: ")
        self.add_holder['Aadhar']=int(input("enter Aadhar: "))
        self.add_holder['Mobile no']=int(input("enter mobile no: "))
        self.add_holder['IFSC']='SBI012345'
        self.add_holder['Acc_num']=random.randint(00000000000000,999999999999999999)
        
        n1=input('select type of account /zero/savings').lower()
        while True:
            if n1=='zero':
                n2=int(input('deposit 500 rupees'))
                if n2>=500:
                    self.add_holder['balance']=n2
                    break
                else:
                    print("******deposit 500 rupees*********")
            elif n1=='saving':
                n3=int(input('deposit 1000 rupees'))
                if n3>=1000:
                    self.add_holder['balance']=n3
                    break
                else:
                    print("*******deposit 1000 rupees************")
        print("=================Your account created====================")

        BANK.holder_details.append(self.add_holder)

        print(BANK.holder_details)


    def Deposit(self):
        print("======welcome to deposit=======")

        user_name = input("enter holder name: ")
        acc_no = int(input('enter account number: '))
        Deposit_Amount = int(input('enter deposit amount: '))

        for x in BANK.holder_details:
            if x['Acc_num'] == acc_no:
                x['balance']+=Deposit_Amount

    def withdraw(self):
        w1=input('enter holder name: ')
        w2=int(input('enter account number: '))
        acc_found=False
        for x in BANK.holder_details:
            if x['Acc_num']==w2:
                acc_found=True
                w3=int(input('enter withdraw amount'))

                if  x['balance']>w3:
                    x['balance']-=w3
                    print('withdraw completed successfully')
                else:
                    print('check account number')
                return

        if not acc_found:
            print("invalid account number")     



    def check_details(self):
        c1=input("enter holder name: ")
        c2=int(input('enter account number: '))

        for x in BANK.holder_details:
            if x['Acc_num']==c2:
                for k,v in x.items():
                    print(k,v)  
            else:
                print('check your acc number') 

    def check_balance(self):
        print("welcome to check balance")   
        b1=int(input('enter acc  number: '))
        print()
        print('*****balance*****')
        for x in BANK.holder_details:
            if x['Acc_num']==b1:
                print('your balance:',x['balance'])
            else:
                print('check your account number')
obj =BANK()

while True:
    print("""
          1) 1 for create account
          2) Deposit
          3)check details
          4)withdraw
          5)check balance
          6)exit
          """)
    n4=input('enter option:')
    if n4=='1':
        obj.create_account()
    elif n4=='2':
        obj.Deposit()
    elif n4=='3':
        obj.check_details()
    elif n4=='4':
        obj.withdraw()
    elif n4=='5':
        obj.check_balance()
    elif n4=='6':
        break