from tkinter import *
from tkinter import messagebox

import mysql.connector

class bank:
    __name = ''
    __balance = 0
    __acc_no = 0
    __pin = 0
    __mobile_no = 0
    con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Idris@123',
    database = 'bank',
    auth_plugin = 'mysql_native_password')
    cur = con.cursor()   
    
    def create_acc(self):
        self.__name = name.get()
        self.__acc_no = acc_no.get()
        self.__pin = pin.get()
        self.__balance = balance.get()
        self.__mobile_no = mobile_no.get()
        query = 'insert into acc_detail( name ,acc_no, pin , balance , mobile_no) values (%s,%s,%s,%s,%s)'
        val = (self.__name,self.__acc_no,self.__pin,self.__balance,self.__mobile_no)
        self.cur.execute(query,val)
        self.con.commit()
        messagebox.showinfo('Account' ,"Your Account is succesfully created")
        
    def __check_pin(self , acc_no1 , pin1 ):
        query = f'select pin from acc_detail where acc_no = {acc_no1}'
        self.cur.execute(query)
        data = self.cur.fetchall()
        if data !=[]:
            if data[0][0] == pin1:
                h = True
            else:
                messagebox.showinfo('Pin' ,'Incorrect pin')
                h = False
        else: 
            messagebox.showinfo('Account Number' ,'Enter the correct account number')
            h = False
        return h
        
    def show_balance(self):
        acc_no1 = acc_no.get()
        pin1 = pin.get()
        if self.__check_pin(acc_no1,pin1) == True :
            query = f'select balance from acc_detail where acc_no = {acc_no1}'
            self.cur.execute(query)
            data = self.cur.fetchall()
            print(f'your balance is {data[0][0]} of acc_no: {acc_no1}')
            messagebox.showinfo('Your Balance' ,f'your balance is {data[0][0]} of acc_no: {acc_no1}')
            
    def deposite(self):
        acc_no1 = acc_no.get()
        amount1 = amount.get()
        query = f'select balance from acc_detail where acc_no = {acc_no1}'
        self.cur.execute(query)
        data = self.cur.fetchall()
        if data != []:
            new_balance = data[0][0] + amount1
            query = f'update acc_detail set balance = {new_balance} where acc_no = {acc_no1} '
            self.cur.execute(query)
            self.con.commit()
            messagebox.showinfo("Deposite",f'The amount {amount} rs is succesfully credited to your acc_ no =  {acc_no1}')
            messagebox.showinfo("Deposite",f'Now your balance is {new_balance}')
        else:
            messagebox.showinfo("Deposite",'Enter correct account number')
    
    
    
    def withdrawl(self ):
        acc_no1 = acc_no.get()
        pin1 = pin.get()
        amount1 = amount.get()
        if self.__check_pin(acc_no1 ,pin1) == True :
            query = f'select balance from acc_detail where acc_no = {acc_no1}'
            self.cur.execute(query)
            data = self.cur.fetchall()
            if data != []:
                new_balance = data[0][0] - amount1
                query = f'update acc_detail set balance = {new_balance} where acc_no = {acc_no1} '
                self.cur.execute(query)
                self.con.commit()
                messagebox.showinfo("Withdrawl",f'The amount {amount1} rs is succesfully debitted from your acc_ no =  {acc_no1}')
                messagebox.showinfo("Withdrawl",f'Now your balance is {new_balance}')
            else:
                messagebox.showinfo("Withdrawl",'Enter correct account number')
        
    def acc_detail(self):
        query = f'select * from acc_detail '
        self.cur.execute(query)
        data = self.cur.fetchall()
        for i in data:
            print(f'{i[0]} - {i[1]} - {i[3]} - {i[4]}')

    # getter method
    def getName(self):
        acc_no1 = acc_no.get()
        query = f'select name from acc_detail where acc_no = {acc_no1}'
        self.cur.execute(query)
        data = self.cur.fetchall()
        if data != []:
            messagebox.showinfo("GetName",f'The name for account number : {acc_no1} is {data[0][0]} ')
        else:
            messagebox.showinfo("GetName",'Enter correct account number')
        

    # setter method
    def setName(self):
        acc_no1= acc_no.get()
        pin1= pin.get()
        name1= name.get()
        if self.__check_pin(acc_no1,pin1) == True:
            query = f"update acc_detail set name = '{name1}'  where pin = {pin1}"
            self.cur.execute(query)
            self.con.commit()
            messagebox.showinfo("SetName",f"You name is succesfully changed to {name1}")
        else:
            messagebox.showinfo("SetName","Incorrect Pin!!!!")

    def changePin(self, acc_no , old_pin , New_pin):
        if self.__check_pin(acc_no , old_pin) == True:
            query = f'update acc_detail set pin = {New_pin} where acc_no = {acc_no}'
            self.cur.execute(query)
            self.con.commit()
            print(f"Your PIN is succesfully changed")

    def SetMobilleNo(self):
        acc_no1 = acc_no.get() 
        pin1 = pin.get() 
        mobile_no1 = mobile_no.get()
        if self.__check_pin(acc_no1 , pin1) == True:
            query = f"update acc_detail set mobile_no = '{mobile_no1}'  where acc_no = {acc_no1}"
            self.cur.execute(query)
            self.con.commit()
            messagebox.showinfo("SetMobileNo",f"Your mobile no is  succesfully set to {mobile_no1}")
        else:
            messagebox.showinfo("SetMobileNo","Incorrect Pin!!!!")

o = bank()
root = Tk()
root.geometry("600x600")

root.title("Banking System")

label1 = Label(root , text = "Idris Banking Systum" , )
label1.grid()

acc_no = IntVar()
pin = IntVar()
balance = IntVar()
amount = IntVar()
mobile_no = IntVar()
name = StringVar()


L1 = Label(root, text = "Account Number")
E1 = Entry(root,textvariable=acc_no)
L2 = Label(root, text = "Pin")
E2 = Entry(root,textvariable=pin ,show='*')
L3 = Label(root, text = "balance")
E3 = Entry(root,textvariable=balance)
L4 = Label(root, text = "amount")
E4 = Entry(root,textvariable=amount)
L5 = Label(root, text = "mobile_no")
E5 = Entry(root,textvariable=mobile_no)
L6 = Label(root, text = "Account Name")
E6 = Entry(root,textvariable=name)

L1.grid(row=1 , column=1)
E1.grid(row=1 , column=2)
L2.grid(row=2 , column=1)
E2.grid(row=2 , column=2)
L3.grid(row=3 , column=1)
E3.grid(row=3 , column=2)
L4.grid(row=4 , column=1)
E4.grid(row=4 , column=2)
L5.grid(row=5 , column=1)
E5.grid(row=5 , column=2)
L6.grid(row=6 , column=1)
E6.grid(row=6 , column=2)
Button(root, text ="Create_acc" , command=o.create_acc).grid(row=7,column=1)
Button(root, text ="acc_detail" , command=o.acc_detail).grid(row=7,column=2)
Button(root, text ="withdrawl" , command=o.withdrawl).grid(row=7,column=3)
Button(root, text ="Deposite" , command=o.deposite).grid(row=7,column=4)
Button(root, text ="GetName" , command=o.getName).grid(row=8,column=1)
Button(root, text ="SetName" , command=o.setName).grid(row=8,column=2)
Button(root, text ="ShowBalance" , command=o.show_balance).grid(row=8,column=3)
Button(root, text ="SetMobileNo" , command=o.SetMobilleNo).grid(row=8,column=4)
root.mainloop()