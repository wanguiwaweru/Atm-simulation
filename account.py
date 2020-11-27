import os
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 

atm = tkinter.Tk()
atm.title ("ATM")
atm.resizable(False,False)
image1 = ImageTk.PhotoImage(Image.open ("conceptual-business-illustration-words-core-260nw-1015011430.jpg.webp"))
Label(atm,image= image1).grid(row = 0,sticky= 'W')
#functions
def register_done():
    name = temp_name.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    if name =="" or password =="":
        messagebox.showinfo('Empty Entry',"All fields required*")
        return
    for account in all_accounts:
        if name == account:
            notification.config(fg="tomato2",text="Account already exists")
            return
        else:

            new_account = open(name,"w")
            new_account.write(name + '\n')
            new_account.write(password +'\n')
            new_account.write('0') 
            new_account.close()
            notification.config(fg="spring green", text="Account has been created")

        
#create pop up window to register user
def register():
    register_screen = Toplevel(atm)
    register_screen.title("Register")
    register_screen.geometry("500x350")
    register_screen.configure(bg ="bisque")
    register_screen.resizable(False,False)
    
    global temp_name
    global temp_password
    global notification
    temp_name = StringVar()
    temp_password = StringVar()
    regLabel = Label(register_screen,text="Enter your bank details.",font=('Verdana',14), bg= "white",fg="black").grid(row=0,sticky=N,pady=10)
    nameLabel = Label(register_screen,text="Name",font=('Verdana',14),bg= "white",fg="black",width=15).grid(row=1,sticky=W,pady=15)
    nameInput = Entry(register_screen,width=20,bd=2, font=('Verdana',14),textvariable=temp_name).grid(row=1,column=1,pady=15)
    pinLabel = Label(register_screen,text="Enter PIN",font=('Verdana',14),bg= "white",fg="black",width=15).grid(row=2,sticky=W,pady=10)
    pinInput = Entry(register_screen,width=20,bd=2, font=('Verdana',14), textvariable=temp_password, show ="*").grid(row=2,column=1)
    finishRegButton = Button(register_screen,text="Register",font=('Verdana',14), bg= "white",fg="black",command=register_done).grid(row=3,column = 0,pady=15)
    notification = Label(register_screen, font=('Verdana',12))
    notification.grid(row=6,column=0,pady=10)

def login_done():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for account in all_accounts:
        if account == login_name:
            login_screen.destroy()
            file = open(account,"r")
            account_info = file.read()
            account_info = account_info.split('\n')
            password  = account_info[1] #password at index 1 of the file
            if login_password == password:
                account_interface = Toplevel(atm)
                account_interface.title('Account')
                account_interface.configure(bg ="bisque")
                account_interface.geometry("450x350")
    
                welcomeLabel = Label(account_interface, text="Welcome "+ login_name +'!', font=('Verdana',14)).grid(row=1,sticky=N,pady=15,padx=10)
                depositBtn = Button(account_interface, text="Deposit",font=('Verdana',14),width=30,command=deposit).grid(row=2,column=0,padx=10,pady=10)
                withdrawBtn = Button(account_interface, text="Withdraw",font=('Verdana',14),width=30,command=withdraw).grid(row=3,column=0,padx=10,pady=10)
                return
            else:
                messagebox.showinfo('Empty Entry',"Incorrect password!!")
                return
    messagebox.showinfo('Unavailable Account',"Account does not exist!!")
                

def login():
    global login_screen
    global temp_login_name
    global temp_login_password
    global login_notification
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    login_screen = Toplevel(atm)
    login_screen.title("Login")
    login_screen.geometry("500x350")
    login_screen.configure(bg ="bisque")
    login_screen.resizable(False,False)

    regLabel = Label(login_screen,text="Login",font=('Verdana',14), bg= "white",fg="black").grid(row=0,sticky=N,pady=10)
    nameLabel = Label(login_screen,text="Name",font=('Verdana',14),bg= "white",fg="black",width=15).grid(row=1,column=0,pady=15)
    nameInput = Entry(login_screen,width=20,bd=2, font=('Verdana',14),textvariable=temp_login_name).grid(row=1,column=1,pady=15)
    pinLabel = Label(login_screen,text="Enter PIN",font=('Verdana',14),bg= "white",fg="black",width=15).grid(row=2,column=0,pady=10)
    pinInput = Entry(login_screen,width=20,bd=2, font=('Verdana',14), textvariable=temp_login_password, show ="*").grid(row=2,column=1)
    finishRegButton = Button(login_screen,text="Login",font=('Verdana',14), bg= "white",fg="black",command=login_done).grid(row=3,column = 0,pady=15)
    notification = Label(login_screen, font=('Verdana',12))
    notification.grid(row=6,column=0,pady=10)

def deposit():
    global amount
    global current_balance_label
    global deposit_notification
    amount = StringVar()
    file   = open(login_name, "r")
    account_info = file.read()
    user_details = account_info.split('\n')
    current_balance = account_info[2]

    deposit_screen = Toplevel(atm)
    deposit_screen.title('Deposit')
    deposit_screen.configure(bg ="bisque")
    deposit_screen.geometry("500x350")
    deposit_screen.resizable(False,False)
    current_balance_label = Label(deposit_screen,bg= "white",fg="black",text="Current Balance:Ksh"+ current_balance, font=('Verdana',14),width=30)
    current_balance_label.grid(row=1,column=0,pady=10)
    amountLabel = Label(deposit_screen,width=10,bg= "white",fg="black", text="Amount:", font=('Verdana',14)).grid(row=3,column=0)
    depositInput =Entry(deposit_screen, justify = 'right' ,textvariable=amount,width=20).grid(row=3,column=1,pady=15)
    depositButton = Button(deposit_screen,text="Deposit",font=('Verdana',14),command=deposit_done).grid(row=5,sticky=W,pady=5)
    deposit_notification = Label(deposit_screen,font=('Calibri',12))
    deposit_notification.grid(row=4, sticky=N,pady=5)

def deposit_done():
    if amount.get()== "":
        messagebox.showinfo('Empty Entry','Enter amount to be deposited.')
        return
    if float(amount.get()) <= 0:
        messagebox.showinfo('Invalid','Cannot deposit amount')
        return

    file = open(login_name,'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[2]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance:Ksh" + str(updated_balance),fg="green")
    deposit_notofication.config(text='Balance Updated', fg='green')
 
 
def withdraw():
    global withdraw_amount
    global withdraw_notofication
    global current_balance_label
    withdraw_amount = StringVar()
    file   = open(login_name, "r")
    account_info = file.read().split('\n')
    current_balance = account_info[2]

    withdraw_screen = Toplevel(atm)
    withdraw_screen.title('Withdraw')
    withdraw_screen.configure(bg ="bisque")
    withdraw_screen.geometry("500x350")
    withdraw_screen.resizable(False,False)

    #withdrawLabel = Label(withdraw_screen, text="Depos", font=('Verdana',14)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen,bg= "white",fg="black", text="Current Balance:Ksh "+ current_balance, font=('Verdana',14),width=30)
    current_balance_label.grid(row=1,column=0)
    amountLabel = Label(withdraw_screen, text="Amount: ", font=('Verdana',14),bg="white",fg="black").grid(row=3,sticky=W)
    amountInput = Entry(withdraw_screen, textvariable=withdraw_amount,justify='right').grid(row=3,column=1,pady=5,)
    withdrawBtn = Button(withdraw_screen,text="Withdraw",font=('Verdana',14),command=finish_withdraw).grid(row=5,sticky=W,pady=5)
    withdraw_notification = Label(withdraw_screen,font=('Verdane',14))
    withdraw_notification.grid(row=6, sticky=N,pady=5)
def finish_withdraw():
    if withdraw_amount.get() == "":
        messagebox.showinfo('Empty Entry','Enter amount to be withdrawn')
        return
    if float(withdraw_amount.get()) <= 0:
        messagebox.showinfo('Invalid','Cannot withdraw amount')
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[2]

    if float(withdraw_amount.get()) > float(current_balance):
        messagebox.showinfo('Invalid','Insufficient Funds!')
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    current_balance_label.config(text="Current Balance:Ksh"+ str(updated_balance),fg="green")
    withdraw_notification.config(text='Balance Updated', fg='green')
    

registerButton = Button(atm,text= "Register",font=('Verdana',14), bg= "white",fg="black",command = register).place(x=40,y=30,width=150,height=40)
loginButton =  Button(atm,text= "Login",font=('Verdana',14), bg= "white",fg="black",command = login).place(x=40,y=70,width=150,height=40)

atm.mainloop()

