
import random
from re import L
import mysql
import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import re
class Banking:
    def __init__(self,fname,lname,mobile,email,dob,adhar):
        self.fname = fname
        self.lname = lname
        self.mobile = mobile
        self.email = email
        self.dob=dob
        self.adhar = adhar
    
    def opnacct():
        #create a new account for customer
        try:
            mydb = mysql.connector.connect(host="localhost",user = "root",password="1133",database="account")
            fname = input("Enter your first name:\n")
            lname = input("Enter your last name:\n")
            while True:
                mobile = input("Enter your mobile number:\n")
                if re.match(r'[789]\d{9}$',mobile):
                    break
                else:
                    print("Invalid mobile number!Please enter valid mobile number.")
            while True:
                email = input("Enter your Email:\n")
                if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
                    break
                else:
                    print("Invalid Email. Please enter an valid email!")
            dob = input("Enter your date of birth in format(dd/mm/yyyy):\n")
            adhar = input("Enter your adhar id:\n")
            op_balance = int(input("Enter opening balance:\n"))
            accountnumber = random.randrange(1111111111,9999999999)
            pin = int(input("Enter Your secret pin:\n"))
            print("First Name:",fname)
            print("Last Name:",lname)
            print("Mobile:",mobile)
            print("Email:",email)
            print("DateofBirth:",dob)
            print("Adhar:",adhar)
            print("Account number:",accountnumber) #generates a account number automatically
            mycursor = mydb.cursor()
            mycursor.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s,%s)",(fname,lname,mobile,email,dob,adhar,accountnumber,op_balance))
            mycursor.execute("insert into amount values(%s,%s,%s)",(fname,accountnumber,op_balance))#Opening account balance
            mycursor.execute("insert into usersaccount values(%s,%s,%s)",(fname,accountnumber,pin)) #inserts into the databases
            mydb.commit()
            mydb.close()
            
        except Error as e:
            print(e)
    def depo():
        #to deposit ammount
        try:
            x=PrettyTable()
            x.field_names = ['Name','AccountNo','Balance']
            mydb = mysql.connector.connect(host="localhost",user="root",password="1133",database = "account")
            amount = input("Enter the Amount you want to deposit:\n")
            account_no = input("Enter account number:")
            a = "select Balance from amount where AccountNo =%s"
            data=(account_no,)
            c=mydb.cursor()
            c.execute(a,data)
            myresult = c.fetchall()
            #tam = myresult[0] +inam)
            sql = "update amount set Balance = Balance+%s where AccountNo=%s"
            d = (amount,account_no)
            c.execute(sql,d)
            c.execute("select * from amount where AccountNo=%s"%account_no)
            
            myresult = c.fetchall()
            mydb.commit()
            print(amount,"credited to",account_no)
            for row in myresult:
                x.add_row([row[0],row[1],row[2]])
            print(x)
        except Error as e:
            print(e)
    def withdrw():
        #withdraw from account
        try:
            x=PrettyTable()
            x.field_names = ["Name","AccountNo","Balance"]
            mydb = mysql.connector.connect(host="localhost",user="root",password="1133",database="account")
            from users import secret
            secret.check()
            

        except Error as e:
            print(e)
    def chkblnce():
        try:
            x=PrettyTable()
            x.field_names = ["Name","AccountNo","Balance"]
            mydb = mysql.connector.connect(host="localhost",user="root",password="1133",database="account")
            mycursor = mydb.cursor()
            account_no = input("Enter Account number:\n")
            mycursor.execute("select * from amount where AccountNo=%s"%account_no)
            myresult = mycursor.fetchall()
            mydb.commit()
            for row in myresult:
                x.add_row([row[0],row[1],row[2]])
            print(x)
        except Error as e:
            print(e)

    def close():
        try:
            x=PrettyTable()
            x.field_names = ["Name","AccountNo","Balance"]
            mydb = mysql.connector.connect(host="localhost",user="root",password="1133",database="account")
            from users import secret
            secret.checkcls()
            

        except Error as e:
            print(e)
    


print("Welcome to banking management system:")
print("1.Create a new account")
print("2.Withdraw")
print("3.Desposit")
print("4.Check Balance")
print("5.Close Account")
print("6. exit")
n = int(input("Enter your choice:\n"))
if(n==1):
    Banking.opnacct()
elif(n==2):
    Banking.withdrw()
elif(n==3):
    Banking.depo()
elif(n==4):
    Banking.chkblnce()
elif(n==5):
    Banking.close()
elif(n==6):
    print("Thank you for banking with us!")
    exit()

