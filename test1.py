from tkinter import*
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
root = Tk()
root.title("Contact Information")
root.maxsize(1150,650)

#function to close login window
def logclose():
	log.destroy()

#function to check login details in database
def login_check():
	if num.get()=="" or passwd.get()=="":
		messagebox.showwarning("Warning","Please enter the details")
	else:
		mycon = mysql.connector.connect(host="localhost",user="root",password="aryanmahale21",database="aryan")
		crsr=mycon.cursor()
		sql = "select * from members where mobile = %s and password=%s"
		crsr.execute(sql,[(num.get()),(passwd.get())])
		results = crsr.fetchall()
		if results:
			messagebox.showinfo("Information","Entered in the System")
			logclose()
		else:
			messagebox.showinfo("Information","No details found")


#function for login page
def login():
	global log
	log = Tk()
	log.title("Login")
	log.maxsize(1150,650)
	#global variable to store values from entry box
	global num
	global passwd

	passwd = StringVar()
	num = IntVar()

	#label for heading
	L1 = Label(log, text=" Login Page",font=("Helvetica 35 bold"))
	L1.place(x= 290,y=190)

	#labels for number and password
	L2 = Label(log, text="Number :",font=("25")).place(x=300,y=300)
	L3 = Label(log, text="Password :" ,font=("25")).place(x=300,y=350)

	#entry box to write information by user 
	Entry(log, textvariable=num).place(x=420,y=303)
	Entry(log, textvariable=passwd).place(x=420,y=353)

	#buttons to login and cancel the page
	Button(log, text="Cancel" , command=logclose).place(x=330,y=420)
	Button(log, text="Login" ,command=login_check).place(x=430,y=420)
	log.mainloop()

#function to close root window
def quit():
        root.destroy()

#function to store data in our database
def storedata():
	if  fname.get() == "" or lname.get() == "" or radio.get() == "" or email.get() == "" or number.get() == "" or passwd.get() == "" or address.get() =="":
		messagebox.showinfo("Info", "Please fill all the fields first.")
	elif len(str(number.get())) >10: 
		messagebox.showwarning("Warning","Please enter valid number")
	elif len(str(number.get())) <10 :
		messagebox.showwarning("Warning","Please enter valid number")

	else:
		mycon = mysql.connector.connect(host="localhost",user="root",password="aryanmahale21",database="aryan")
		crsr=mycon.cursor()
		sql = "select * from members where mobile = %s"
		crsr.execute(sql,[(number.get())])
		results = crsr.fetchall()
		if results:
			messagebox.showinfo("information","This number already registered")
		else:
			crsr.execute(" insert into members values('%s','%s','%s','%s','%s','%s','%s')" %(fname.get(),lname.get(),radio.get(),email.get(),number.get(),passwd.get(),address.get()))
			crsr.close()
			mycon.commit()
			mycon.close()
			messagebox.showinfo("Information","Data saved")
			close()
    

#register window
def register():
	mycon = mysql.connector.connect(host="localhost",user="root",password="aryanmahale21",database="aryan")
	crsr=mycon.cursor()
	crsr.execute(''' CREATE TABLE if not exists members (Fname text, Lname text,Gender integer(2),Email varchar(255),Mobile integer(20),password varchar(255),Address varchar(255))''')
	crsr.close()
	mycon.commit()
	mycon.close()
	global top
	top = Tk()
	top.title("Register")
	top.maxsize(1150,650)

	#variables to store values of entry
	global fname
	global lname
	global radio
	global email
	global number
	global passwd
	global address

	fname =StringVar()
	lname =StringVar()
	radio =IntVar()
	email =StringVar()
	number =IntVar()
	passwd =StringVar()
	address =StringVar()

	#label for heading
	Label(top,text="Sign Up Page",font="Helvetica 35 bold").place(x=350,y=50)
	#labels nd entry for details
	Label(top, text="Firstname :",font="Helvetica 18").place(x=100,y=150)
	Entry(top,textvariable=fname).place(x=250,y=155)

	Label(top, text="Lastname :",font="Helvetica 18").place(x=100,y=200)
	Entry(top,textvariable=lname).place(x=250,y=205)

	Label(top, text="Gender :",font="Helvetica 18").place(x=100,y=250)
	#radio button for gender
	Radiobutton(top, text = "Male", variable = radio,value = 1).place(x=250,y=255)
	Radiobutton(top, text = "Female", variable = radio,value = 2).place(x=310,y=255)

	Label(top, text="Email :",font="Helvetica 18").place(x=100,y=300)
	Entry(top,textvariable=email).place(x=250,y=305)

	Label(top, text="Mobile No. :",font="Helvetica 18").place(x=100,y=350)
	Entry(top,textvariable=number).place(x=250,y=355)

	Label(top, text="Password :",font="Helvetica 18").place(x=100,y=400)
	Entry(top,textvariable=passwd,show="*").place(x=250,y=405)

	Label(top, text="Address :",font="Helvetica 18").place(x=100,y=450)
	Entry(top,textvariable=address).place(x=250,y=455)

	#button for cancel and submit the details
	Button(top, text="Close", command=close).place(x=140,y=520)
	Button(top, text="Submit",command=storedata).place(x=240,y=520)

	


	top.mainloop()
#function to close top window means register window
def close():
	top.destroy()
   
#label for heading          
L1 = Label(root, text=" Welcome To Interface",font=("Helvetica 35 bold"))
L1.place(x= 290,y=190)
#label for image
img=PhotoImage(file='management.png')

L2 =Label(root,image=img).place(x=500,y=250)

#label for text below the image
L3= Label(root,text="Management System", font=("Helvetica 16")).place(x=450,y=340)

#button to add new data
btn1 = Button(root, text= "Register", command=lambda:[quit(),register()])
btn1.place(x=400,y=400)

#button to cancel or end the root window
btn2 = Button(root, text="Close", command=quit)
btn2.place(x=500,y=400)
#button to login for already registered members
btn3 = Button(root, text="Login",command=lambda:[quit(),login()]).place(x=600,y=400)
root.mainloop()