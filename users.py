import mysql 
import mysql.connector
from mysql.connector import Error
from prettytable.prettytable import PrettyTable
import re
class secret:
    def check():
        try:
            mydb = mysql.connector.connect(host="localhost",user="root",password ="1133",database="account")
            accountno = input("Enter Account Number:")
            pin = input("Enter Your Pin number:")
            mycursor = mydb.cursor()
            mycursor.execute("select * from usersaccount where AccountNumber=%s and PIN=%s",(accountno,pin))
            row = mycursor.fetchone()
            if row==None:
                print("Invalid please check your accounnt no and PIN")
            else:
                secret.withdraw()
            
        except Error as e:
            print(e)
    
    def withdraw():
        x=PrettyTable()
        x.field_names = ['Name','AccountNo','Balance']
        mydb = mysql.connector.connect(host="localhost",user="root",password ="1133",database="account")
        print("Enter the ammount to be witdrawn")
        account_no = input("Enter the Account No:\n")
        amount = input("Enter the Amount:\n")
        a = "select Balance from amount where AccountNo =%s"
        data = (account_no,)
        c=mydb.cursor()
        c.execute(a,data)
        myresult = c.fetchall()
            #tam = myresult[0] +inam)
        sql = "update amount set Balance = Balance-%s where AccountNo=%s"
        d=(amount,account_no)
        c.execute(sql,d)
        c.execute("select * from amount where AccountNo=%s"%account_no)
        myresult = c.fetchall()
        mydb.commit()
        print(amount,"Has been debited from",account_no)
        for row in myresult:
            x.add_row([row[0],row[1],row[2]])
        print(x)

    def checkcls():
        try:
            mydb = mysql.connector.connect(host="localhost",user="root",password ="1133",database="account")
            accountno = input("Enter Account Number:")
            pin = input("Enter Your Pin number:")
            mycursor = mydb.cursor()
            mycursor.execute("select * from usersaccount where AccountNumber=%s and PIN=%s",(accountno,pin))
            row = mycursor.fetchone()
            if row==None:
                print("Invalid please check your accounnt no and PIN")
            else:
                secret.close()

        except Error as e:
            print(e)

    def close():
        try:
            x=PrettyTable()
            x.field_names = ["Name","AccountNo","Balance"]
            mydb = mysql.connector.connect(host="localhost",user="root",password="1133",database="account")
            mycursor = mydb.cursor()
            account_no=input("Enter your account number:")
            mobile = input("Enter your mobile number:\n")
            while True:
                mobile = input("Enter your mobile number:\n")
                if re.match(r'[789]\d{9}$',mobile):
                    break
                else:
                    print("Invalid mobile number!Please enter valid mobile number.")
            mycursor.execute("delete from amount where AccountNo=%s"%account_no)
            mycursor.execute("delete from usersaccount where AccountNumber=%s"%account_no)
            mycursor.execute("delete from user where mobile=%s"%mobile)
            mydb.commit()
            print("Your account has been Deleted! Thank You")
        except Error as e:
            print(e)