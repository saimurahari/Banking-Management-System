import mysql
import mysql.connector
from mysql.connector import Error
import re
import getpass

class Register:
    def __init__(self,username,email,mobile,password,confirmpassword):
        self.username=username
        self.email = email
        self.mobile = mobile
        self.password = password
        self.confirmpassword= confirmpassword
    
    def register(self):
        #for a new user register here1
        try:
            mydb = mysql.connector.connect(host="localhost",user = "root",password="1133",database="login")
            mycursor=mydb.cursor()
            mycursor.execute("select * from register where email='%s'",self.email)
            row = mycursor.fetchone()
            if row!=None:
                print("user already exist")
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s);",(self.username,self.email,self.mobile,self.password,self.confirmpassword))
                mydb.commit()
                mydb.close
                print("successfully registered")                

        except Error as e:
            print(e)

class Login:
    def __init__(self,email,password):
        self.email = email
        self.password=password
    def login(self):
        #login for existing user 
        if self.email=="" or self.password=="":
            print("All fields are required please enter valid email/password!")
        else:
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="1133",database="login")
                mycursor=mydb.cursor()

                mycursor.execute("select * from register where email = %s and password=%s",(self.email,self.password))
                row = mycursor.fetchone()

                if row==None:
                    print("Error,Invalid email/ Password")
                else:
                    self.banking()
                    mydb.close()
            except Error as e:
                print(e)
    
    def banking(self):
        print("#---------------------Welcome to Banking Management System-------------------------#")
        from Banking import Banking

print("Hello Welcome! to Banking management system")
print("1.Login")
print("2.Register")

n = int(input("Enter your preference:\n"))
if(n==1):
    while True:
        email = input("Enter your Email:\n")
        if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
            break
        else:
            print("Invalid Email. Please enter an valid email!")
    password = getpass.getpass("Enter Password")
    s1 = Login(email,password)
    s1.login()

elif(n==2):
    username = input("Enter your username:\n")
    while True:
        email = input("Enter your Email:\n")
        if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
            break
        else:
            print("Invalid Email. Please enter an valid email!")
    while True:
        mobile = input("Enter your mobile number:\n")
        if re.match(r'[789]\d{9}$',mobile):
            break
        else:
            print("Invalid mobile number!Please enter valid mobile number.")
    password = getpass.getpass("Enter your password:\n")
    confirmpassword = getpass.getpass("Renter your password:\n")
    if password != confirmpassword:
        print("password and confirm password should be same")
    s = Register(username,email,mobile,password,confirmpassword)
    s2=Login(email,password)
    s.register()