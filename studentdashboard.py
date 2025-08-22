from tkinter import *
from datetime import datetime
import ttkthemes
from tkinter import ttk,messagebox
import mysql.connector
from datetime import datetime
# ttk for buttons
#functionality
def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        student_table.insert('',END,values=data)
def delete_student():
    indexing=student_table.focus()
    content=student_table.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,(content_id,))#tuple format
    mydb.commit()
    messagebox.showinfo('Deleted',f'This id {content_id} is deleted successfully.')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        student_table.insert('',END,values=data)
def search_student():
    search_student_window=Toplevel()
    search_student_window.title('Search Student')
    search_student_window.resizable(False,False)
    search_student_window.grab_set()
    search_student_id_label=Label(search_student_window,text='Id',font=('times new roman',20,'bold'))
    search_student_id_label.grid(row=0,column=0,padx=20,pady=10)
    search_student_id_Entry=Entry(search_student_window,font=('times new roman',15,'bold'))
    search_student_id_Entry.grid(row=0,column=1,padx=10,pady=10)
    search_student_name_label=Label(search_student_window,text='Name',font=('times new roman',20,'bold'))
    search_student_name_label.grid(row=1,column=0,padx=10,pady=10)
    search_student_name_Entry=Entry(search_student_window,font=('times new roman',15,'bold'))
    search_student_name_Entry.grid(row=1,column=1,padx=20,pady=10)
    search_student_phone_label = Label(search_student_window, text='phone', font=('times new roman', 20, 'bold'))
    search_student_phone_label.grid(row=2, column=0, padx=10, pady=10)
    search_student_phone_Entry = Entry(search_student_window, font=('times new roman', 15, 'bold'))
    search_student_phone_Entry.grid(row=2, column=1, padx=20, pady=10)
    search_student_email_label = Label(search_student_window, text='Email', font=('times new roman', 20, 'bold'))
    search_student_email_label.grid(row=3, column=0, padx=10, pady=10)
    search_student_email_Entry = Entry(search_student_window, font=('times new roman', 15, 'bold'))
    search_student_email_Entry.grid(row=3, column=1, padx=20, pady=10)
    search_student_address_label = Label(search_student_window, text='Address', font=('times new roman', 20, 'bold'))
    search_student_address_label.grid(row=4, column=0, padx=10, pady=10)
    search_student_address_Entry = Entry(search_student_window, font=('times new roman', 15, 'bold'))
    search_student_address_Entry.grid(row=4, column=1, padx=20, pady=10)
    search_student_gender_label = Label(search_student_window, text='Gender', font=('times new roman', 20, 'bold'))
    search_student_gender_label.grid(row=5, column=0, padx=10, pady=10)
    search_student_gender_Entry = Entry(search_student_window, font=('times new roman', 15, 'bold'))
    search_student_gender_Entry.grid(row=5, column=1, padx=20, pady=10)
    search_student_birth_label = Label(search_student_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    search_student_birth_label.grid(row=6, column=0, padx=10, pady=10)
    search_student_birth_Entry = Entry(search_student_window, font=('times new roman', 15, 'bold'))
    search_student_birth_Entry.grid(row=6, column=1, padx=20, pady=10)
    #functions
    def search_student_data():
        query='select * from student where id=%s or name=%s or Email=%s'
        mycursor.execute(query,(search_student_id_Entry.get(),search_student_name_Entry.get(),search_student_email_Entry.get(),))#the comma is must at end in queries because the op is in tuple format not as list
        student_table.delete(*student_table.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            #datalist=list(data)
            student_table.insert('',END,values=data)

    search_student_button = ttk.Button(search_student_window, text='Search Student', command=search_student_data)
    search_student_button.grid(row=7, columnspan=2)
def add_student():
    add_student_window=Toplevel()
    add_student_window.resizable(False,False)
    add_student_window.grab_set()#it helps only click  one webiste and it doesnot support other window to open
    add_student_id_label=Label(add_student_window,text='Id',font=('times new roman',20,'bold'))
    add_student_id_label.grid(row=0,column=0,padx=20,pady=10)
    add_student_id_Entry=Entry(add_student_window,font=('times new roman',15,'bold'))
    add_student_id_Entry.grid(row=0,column=1,padx=10,pady=10)
    add_student_name_label=Label(add_student_window,text='Name',font=('times new roman',20,'bold'))
    add_student_name_label.grid(row=1,column=0,padx=10,pady=10)
    add_student_name_Entry=Entry(add_student_window,font=('times new roman',15,'bold'))
    add_student_name_Entry.grid(row=1,column=1,padx=20,pady=10)
    add_student_phone_label = Label(add_student_window, text='phone', font=('times new roman', 20, 'bold'))
    add_student_phone_label.grid(row=2, column=0, padx=10, pady=10)
    add_student_phone_Entry = Entry(add_student_window, font=('times new roman', 15, 'bold'))
    add_student_phone_Entry.grid(row=2, column=1, padx=20, pady=10)
    add_student_email_label = Label(add_student_window, text='Email', font=('times new roman', 20, 'bold'))
    add_student_email_label.grid(row=3, column=0, padx=10, pady=10)
    add_student_email_Entry = Entry(add_student_window, font=('times new roman', 15, 'bold'))
    add_student_email_Entry.grid(row=3, column=1, padx=20, pady=10)
    add_student_address_label = Label(add_student_window, text='Address', font=('times new roman', 20, 'bold'))
    add_student_address_label.grid(row=4, column=0, padx=10, pady=10)
    add_student_address_Entry = Entry(add_student_window, font=('times new roman', 15, 'bold'))
    add_student_address_Entry.grid(row=4, column=1, padx=20, pady=10)
    add_student_gender_label = Label(add_student_window, text='Gender', font=('times new roman', 20, 'bold'))
    add_student_gender_label.grid(row=5, column=0, padx=10, pady=10)
    add_student_gender_Entry = Entry(add_student_window, font=('times new roman', 15, 'bold'))
    add_student_gender_Entry.grid(row=5, column=1, padx=20, pady=10)
    add_student_birth_label = Label(add_student_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    add_student_birth_label.grid(row=6, column=0, padx=10, pady=10)
    add_student_birth_Entry = Entry(add_student_window, font=('times new roman', 15, 'bold'))
    add_student_birth_Entry.grid(row=6, column=1, padx=20, pady=10)
   #always write the functions  after the enteries of data.
    def add_student_data():
        if add_student_id_Entry.get()==''\
                or add_student_name_Entry.get()==''\
                or add_student_email_Entry.get()==''\
                or add_student_address_Entry.get()=='' \
                or add_student_birth_Entry.get()==''\
                or add_student_gender_Entry.get()==''\
                or add_student_phone_Entry.get()=='':
                messagebox.showerror('Error','All fields must required',parent=add_student_window)
        else:
            try:
                today_datetime=datetime.now()
                current_date =today_datetime.strftime('%d/%m/%Y')
                current_time=today_datetime.strftime('%H:%M:%S')
                query = 'INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (
                    add_student_id_Entry.get(),
                    add_student_name_Entry.get(),
                    add_student_phone_Entry.get(),
                    add_student_email_Entry.get(),
                    add_student_address_Entry.get(),
                    add_student_gender_Entry.get(),
                    add_student_birth_Entry.get(),
                    current_date,
                    current_time
                ))
                mydb.commit()
                res=messagebox.askyesno('Confirm','Data added Successfy.Do you want to clean form?')
                if res:#if want to clean form the res is been true and the below lines of code is executed.
                        add_student_id_Entry.delete(0,END)
                        add_student_name_Entry.delete(0,END)
                        add_student_phone_Entry.delete(0,END)
                        add_student_email_Entry.delete(0,END)
                        add_student_address_Entry.delete(0,END)
                        add_student_gender_Entry.delete(0,END)
                        add_student_birth_Entry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=add_student_window)
            query='select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())#clear all existing data from tree view.
            for data in fetched_data:
                datalist=list(data)
                student_table.insert('',END,values=datalist)#adds a new row at the bottom of your Treeview table, with the data from datalist.

    #button have function so it must be written after the function
    add_student_button = ttk.Button(add_student_window, text='Add Student', command=add_student_data)
    add_student_button.grid(row=7, columnspan=2)
def connect_database():
    def connect():
        global mycursor
        global mydb
        try:
            mydb=mysql.connector.connect(
                host='localhost',
                user='root',
                password='Arunsql@123',
                auth_plugin='mysql_native_password'
            )
            mycursor=mydb.cursor()
            messagebox.showinfo('Success','Database is Connected',parent=connect_window)
        except:
            messagebox.showerror('Error','Invalid credits',parent=connect_window)
        #excute queries if database is not exist
        try:
            query='create database students_management_system'
            mycursor.execute(query)
            query='use students_management_system'
            mycursor.execute(query)
            query='create table if not exists student(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(50),Date_of_birth varchar(50),date varchar(20),time varchar(50))'
            mycursor.execute(query)
        #if it is exist it comes to except block
        except:
            query='use students_management_system'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database connection is successful.',parent=connect_window)
        connect_window.destroy()
        student_addButton.config(state=NORMAL)#FOR THE FUNCTION THE BUTTON IS UPDATED TO NORMAL STATE
        student_searchButton.config(state=NORMAL)
        student_updateButton.config(state=NORMAL)
        student_ShowButton.config(state=NORMAL)
        student_deleteButton.config(state=NORMAL)
        student_exportButton.config(state=NORMAL)
        student_exitButton.config(state=NORMAL)
    #new window
    connect_window=Toplevel()#insted of tk() class for a window using toplevel() class
    connect_window.title("Database Connection")
    connect_window.geometry('470x250')
    connect_window.resizable(0,0)
    #hostname
    HostnameLabel=Label(connect_window,text='Hostname',font=('times new roman',20,'bold'))
    HostnameLabel.grid(row=0,column=0,padx=20)
    Hostentry=Entry(connect_window,font=('times new roman',15,'bold'),bd=2)
    Hostentry.grid(row=0,column=1,padx=40,pady=20)
    #username
    UsernameLabel=Label(connect_window,text='Username',font=('times new roman',20,'bold'))
    UsernameLabel.grid(row=1,column=0,padx=20)
    Userentry=Entry(connect_window,font=('times new roman',15,'bold'),bd=2)
    Userentry.grid(row=1,column=1,padx=40,pady=20)
    #password
    PasswordLabel=Label(connect_window,text='Password',font=('times new roman',20,'bold'))
    PasswordLabel.grid(row=2,column=0,padx=20)
    Passwordentry=Entry(connect_window,font=('times new roman',15,'bold'))
    Passwordentry.grid(row=2,column=1,padx=40,pady=20)
    #buttontoconnect
    connectButton=ttk.Button(connect_window,text="Connect",command=connect)
    connectButton.grid(row=3,columnspan=2)
def date():
    date=datetime.now()
    date=date.strftime('%d/%m/%Y')
    return date
def time():
    current_time=datetime.now()
    time=current_time.strftime('%H:%M:%S')
    return time
count=0
text=''
def slider():
    global text
    global count
    text=text+String[count]
    Sliderlabel.config(text=text)#config() is a method used in Tkinter to modify or update the
    # properties (options) of a widget after it has been created.
    count=count+1
    if count==len(String):
        count=0
        text=''
    else:
        Sliderlabel.after(200,slider)#200millisecons calling slider func
#GUI FOR WINDOW
window=ttkthemes.ThemedTk() #it is similar as tk() for  creating widget but it have some additional themes on buttons
window.get_themes()#to get themes
window.set_theme('radiance')#theme name for buttons
window.geometry('1980x1080')
window.resizable(True,True)
window.title('Student Management System')
#datelabel
dateTimelabel=Label(window,text=f'Date:{date()}\nTime:{time()}',
                    font=('Times new roman',20,'bold'))
dateTimelabel.place(x=5,y=5)
#slider label
String="Student Management System"
Sliderlabel=Label(window,font=('Arial',25,'bold'))
Sliderlabel.place(x=500,y=0)
Sliderlabel.config(text=f'{slider()}')
#connectionButton
connect_button=ttk.Button(window,text="Connect to database",command=connect_database)#its a func
connect_button.place(x=1000,y=0)
#frames in widgets or window
leftFrame=Frame(window,bg='snow',borderwidth=3)
leftFrame.place(x=100,y=100,width=300,height=650)
#adding logo image in left frame
logo_image=PhotoImage(file='logo.png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0,padx=80)
#adding buttons in leftframe
student_addButton=ttk.Button(leftFrame,text='Add Student',command=add_student)
student_addButton.grid(row=1,column=0,pady=20)
#searchbutton in leftframe
student_searchButton=ttk.Button(leftFrame,text='Search Student',command=search_student)
student_searchButton.grid(row=2,column=0,pady=20)
#delete button
student_deleteButton=ttk.Button(leftFrame,text='Delete Student',command=delete_student)
student_deleteButton.grid(row=3,column=0,pady=20)
#update student
student_updateButton=ttk.Button(leftFrame,text='Update Button')
student_updateButton.grid(row=4,column=0,pady=20)
#show student
student_ShowButton=ttk.Button(leftFrame,text='Show Button',command=show_student)
student_ShowButton.grid(row=5,column=0,pady=20)
#exportdata button
student_exportButton=ttk.Button(leftFrame,text='Export Data')
student_exportButton.grid(row=6,column=0,pady=20)
#exit button
student_exitButton=ttk.Button(leftFrame,text='Exit')
student_exitButton.grid(row=7,column=0,pady=20)
#rightframe
right_frame=Frame(window)
right_frame.place(x=350,y=100,width=1000,height=650)
#TREE VIEW
#SCROOLBAR IN FRAME
scrollBar_on_X=Scrollbar(right_frame,orient=HORIZONTAL)#to pass horiz
scrollBar_on_Y=Scrollbar(right_frame,orient=VERTICAL)
scrollBar_on_X.pack(side=BOTTOM,fill=X)
scrollBar_on_Y.pack(side=RIGHT,fill=Y)
student_table=ttk.Treeview(right_frame,
                           columns=('col1','col2','col3','col4','col5','col6','col7','col8'),
                           yscrollcommand=scrollBar_on_Y.set,
                           xscrollcommand=scrollBar_on_X.set)
scrollBar_on_X.config(command=student_table.xview)
scrollBar_on_Y.config(command=student_table.yview)
student_table.heading('col1',text='ID')
student_table.heading('col2',text='Name')
student_table.heading('col3',text='Mobile No')
student_table.heading('col4',text='Address')
student_table.heading('col5',text='Gender')
student_table.heading('col6',text='Address Date')
student_table.heading('col7',text='Address Time')
#heading take two arguemnts the coloumn  and column name to place
#for only given coloumns names
student_table.config(show='headings')
student_table.pack(fill=BOTH,expand=1)#similarly like place or grid to place in window to add whether right or left it is use for simple cases
window.mainloop()