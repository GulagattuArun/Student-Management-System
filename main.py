from tkinter import *#tkinter is a simple gui module or library
from tkinter import messagebox#for error msg box
from PIL import ImageTk
#function
def login():
    if UsernameEntry.get()==''or PasswordEntry.get()=='':
        messagebox.showerror('Error','Please Enter the Filed')
    elif UsernameEntry.get()=='Arun' and PasswordEntry.get()=='1234':
            messagebox.showinfo('Success','WELCOME')
            app.destroy()#if accesse to new window the previous window mustbe closed
            import studentdashboard # for to dashboard page we must import those py script with its file name.
    else:
        messagebox.showerror('Error','Please enter correct details')
#this module  used for set bg image
app=Tk()#this class or instance helps us to create window
app.geometry('1980x1080')#geometry is also method in tk() class for window height and width.
app.resizable(True,True)
#background image with imagetk
backgroundImage=ImageTk.PhotoImage(file=r"C:\Users\91799\PycharmProjects\studentmanagement\OIP.jpg")
bg_label=Label(app,image=backgroundImage)
bg_label.place(x=0,y=0)
#container
#WITH FRAME CLASS
loginFrame=Frame(app,bg='white')
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='graduated.png')
logolabel=Label(loginFrame,image=logoImage)
logolabel.grid(row=0,column=0,columnspan=2,pady=10,padx=20)#colspan take 2 column spaces
#username image icon
usernameImage=PhotoImage(file=r"C:\Users\91799\Downloads\user.png")
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0)
#entery field for username
UsernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
UsernameEntry.grid(row=1,column=1,pady=10,padx=20)
#passwordicon
passwordImage=PhotoImage(file='password-icon.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0)
#password entry fo user
PasswordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
PasswordEntry.grid(row=2,column=1,pady=10,padx=20)
#LOGINBUTTON
loginButton=Button(loginFrame,text='Login',command=login,font=('times new roman',15,'bold'),width=15,fg='white',
                   bg='skyblue',activebackground='skyblue',activeforeground='white',cursor='hand2')#fg is a font color
loginButton.grid(row=3,column=1,pady=104)
app.mainloop()#this method is availabel in the obj with the insatnce of tk.
#mainloop method keeps the winodow on a loop so the user can access multiple times.