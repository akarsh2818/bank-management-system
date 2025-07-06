import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an error occured as {err}") 
    @staticmethod
    def __update():
        with open(Bank.database,"w") as fs:
            fs.write(json.dumps(Bank.data))

    @staticmethod
    def __accountgenerate():
        alpha=random.choices(string.ascii_letters, k =3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*_",k=1)
        id=alpha +num + spchar
        random.shuffle(id)
        return "".join(id)

    def create_account(self):
        info={
            "name":input("enter your name :"),
            "age":int(input("enter your age ")),
            "email":input("enter your email"),
            "pin":int(input("enter your pin")),
            "accountNo":Bank.__accountgenerate(),
            "balance":0
            }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("you cannot create your account")
        else:
            print("account has been created succesffully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("note down your account number")
            Bank.data.append(info)
            Bank.__update()
    
    def deposit_money(self):
        acctno=input("enter your account number") 
        pinno=int(input("enter your pin")) 
        userdata=[i for i in Bank.data if i['accountNo'] ==acctno and i['pin']==pinno]
        if not userdata:
            print("account not found")
        else:
            amount=int(input("Enter amount  you wanted to  be deposited "))
            if amount>10000 or userdata[0]['balance']<=0:
                print("this amount is too much amount below than 10000 ot more than 0 only be deposited")
            else:
                print(userdata)
                print(f"before deposirt : {userdata[0]['balance']}")
                userdata[0]['balance']+=amount
                
                Bank.__update()
                print(f"after  deposirt : {userdata[0]['balance']}")
                print("amount is succesfully deposited ")
    
    def withdraw_money(self):
        accountno=input("enter account no  ")
        pinno=int(input("enter yout pin number"))
        userdata=[i for i in Bank.data if i['accountNo']==accountno and i['pin']==pinno]
        if not userdata:
            print("you have no account")
        else:
            print(userdata)
            amount=int(input("enter your amaount to be deposited"))
            if amount >userdata[0]['balance'] :
                print(f"you have not sufficient money,have on;y {userdata[0]['balance']}")
            else:
                print(f"before amount : {userdata[0]['balance']}")
                userdata[0]['balance']-=amount
                Bank.__update()
                print(f"after amount : {userdata[0]['balance']}")
                print("you have withdraweh successfully")

    def show_details(self):
        acctno=input("enter your account number") 
        pinno=int(input("enter your pin"))
        userdata=[i for i in Bank.data if i['accountNo']==acctno and i['pin']==pinno] 
        if not userdata:
            print("wrong account number")
        else:
            print(userdata)
            print("your imformation is \n\n\n :")
            for i in userdata[0]:
                print(f"{i}:{userdata[0][i]}")
    def update_details(self):
        acctno=input("enter your account number") 
        pinno=int(input("enter your pin"))
        userdata=[i for i in Bank.data if i['accountNo']==acctno and i['pin']==pinno]
        
        if not userdata:
            print("wrong account no ")
        else:
            print("you can not change the age account number balance")
            print("fill the change or leave it empty if you dont wont to change ")

            new_data={
                "name":input("tell new name or press enter to skip :"),
                "email":input("tell new email or press enter to skip:"),
                "pin":input("tell new pin or press enter to skip:")
            }
            if new_data['name']=="":
                new_data['name']=userdata[0]['name']
            if new_data['email']=="":
                new_data['email']=userdata[0]['email']
            if new_data['pin']=="":
                new_data['pin']=userdata[0]['pin']
            new_data['age']=userdata[0]['age']
            new_data['balance']=userdata[0]['balance']
            new_data['accountNo']=userdata[0]['accountNo']
            if type(new_data['pin'])==str:
                new_data['pin']=int(new_data['pin'])
            for i in new_data:
                if new_data[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=new_data[i]
        
        Bank.__update()
        print("update have been done successfullly")
        print(userdata)
    def delete(self):
        acctno=input("enter your account number") 
        pinno=int(input("enter your pin"))
        userdata=[i for i in Bank.data if i['accountNo']==acctno and i['pin']==pinno]
        if not userdata:
            print("enter no such account")
        else:
            check=input("enter y to delete or n to not delete")
            if check =='n'or check=="N":
                print("bypassed")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
            print("you have succesfully deleted the account")
            Bank.__update()



        

user=Bank()


print("press 1 for  for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money ")
print("press 4 for details ")
print("press 5 for uddating the details ")
print("press 6 for deleting your account")
check=int(input("enter you response "))

if check==1:
    user.create_account()
elif check==2:
    user.deposit_money()
elif check==3:
    user.withdraw_money()
if check==4:
    user.show_details()
if check==5:
    user.update_details()
if check==6:
    user.delete()