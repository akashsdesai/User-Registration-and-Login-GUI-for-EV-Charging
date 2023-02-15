import tkinter as tk
import time
import csv
import pandas as pd
import numpy as np


from tkinter import messagebox
count = int(0)
root =tk.Tk()
root.geometry('800x416')
root.configure(bg='#305F72')
user_frame =tk.Frame(root,bg='#F1D1B5')
user_frame.pack(side=tk.BOTTOM)
user_frame.pack_propagate(False)
user_frame.configure(height=161,width=800)
voltage = 0
current = 0

def show():


    port1=tk.Label(user_frame)
    labelv1 = tk.Label(user_frame)
    labelv11=tk.Label(user_frame)
    labelc1=tk.Label(user_frame)
    labelc11=tk.Label(user_frame)
    port2=tk.Label(user_frame)
    labelv2=tk.Label(user_frame)
    labelv22=tk.Label(user_frame)
    labelc2=tk.Label(user_frame)
    labelc22=tk.Label(user_frame)
    def measure():
        global voltage
        global current
        voltage=voltage+1
        current=current+1
        port1.config(text='Port 1',font=40,bg='#F1D1B5',fg='Black')
        port1.place(y=15,relx=0.25,anchor='center')
        labelv1.config(text='Voltage = ',font=25,bg='#F1D1B5',fg='Black')
        labelv1.place(y=30,x=150)
        labelv11.config(text=(voltage,'V'),font=25,bg='#F1D1B5',fg='Black')
        labelv11.place(y=30,x=220)
        labelc1.config(text='Current = ',font=25,bg='#F1D1B5',fg='Black')
        labelc1.place(y=60,x=150)
        labelc11.config(text=(current,'A'),font=25,bg='#F1D1B5',fg='Black')
        labelc11.place(y=60,x=220)
        port2.config(text='Port 2',font=40,bg='#F1D1B5',fg='Black')
        port2.place(y=15,relx=0.75,anchor='center')
        labelv2.config(text='Voltage = ',font=25,bg='#F1D1B5',fg='Black')
        labelv2.place(y=30,x=550)
        labelv22.config(text=(voltage,'V'),font=25,bg='#F1D1B5',fg='Black')
        labelv22.place(y=30,x=620)
        labelc2.config(text='Current = ',font=25,bg='#F1D1B5',fg='Black')
        labelc2.place(y=60,x=550)
        labelc22.config(text=(current,'A'),font=25,bg='#F1D1B5',fg='Black')
        labelc22.place(y=60,x=620)
        labelv1.after(1000, measure)
    stop1=tk.Button(user_frame,text='❌',font=40,bg='White',fg='Red')
    stop1.place(relx=0.25,y=135,anchor='center')
    stop2=tk.Button(user_frame,text='❌',font=40,bg='White',fg='Red')
    stop2.place(relx=0.75,y=135,anchor='center')
    measure()

show()


work_frame1=tk.Frame(root,bg='#305F72',highlightbackground='White',highlightthickness=5)
work_frame1.pack(side=tk.LEFT)
work_frame1.propagate(False)
work_frame1.configure(height=255, width=400)
work_frame2 = tk.Frame(root, bg='#305F72',highlightbackground='White',highlightthickness=5)
work_frame2.pack(side=tk.RIGHT)
work_frame2.propagate(False)
work_frame2.configure(height=255, width=400)
#user one
def adminlogin1():
    admin1_txt='evcharger'
    pass1_txt='DSCE'
    work_frame1.pack_forget()
    admin_window1=tk.Frame(root,bg='#305F72',highlightbackground='White',highlightthickness=5)
    admin_window1.pack(side=tk.LEFT)
    admin_window1.propagate(False)
    admin_window1.configure(height=255, width=400)
    id1=tk.Label(admin_window1,text='ADMIN ID',bg='#305F72',fg='White')
    id1.place(y=40,relx=0.5,anchor='center')
    adminid1=tk.Entry(admin_window1)
    adminid1.place(y=60,relx=0.5,anchor='center')
    pass1 = tk.Label(admin_window1, text='Password',bg='#305F72',fg='White')
    pass1.place(y=90,relx=0.5,anchor='center')
    adminpass1=tk.Entry(admin_window1,show='*')
    adminpass1.place(y=110,relx=0.5,anchor='center')
    def Register1():
        a = adminid1.get()
        p = adminpass1.get()
        print(a)
        print(p)
        if(p==pass1_txt and a==admin1_txt):
            admin_window1.pack_forget()
            register_window1=tk.Frame(root,bg='#305F72',highlightbackground='White',highlightthickness=5)
            register_window1.pack(side=tk.LEFT)
            register_window1.propagate(False)
            register_window1.configure(height=255, width=400)
            def new_user():
                register_window1.pack_forget()
                newuser_window1=tk.Frame(root,bg='#305F72',highlightbackground='White',highlightthickness=5)
                newuser_window1.pack(side=tk.LEFT)
                newuser_window1.propagate(False)
                newuser_window1.configure(height=255, width=400)

                name = tk.Label(newuser_window1, text='Name', bg='#305F72', fg='White')
                name.place(y=10, relx=0.2, anchor='center')
                name1=tk.Entry(newuser_window1)
                name1.place(y=30,relx=0.2,anchor='center')
                usn=tk.Label(newuser_window1,text='USN',bg='#305F72',fg='White')
                usn.place(y=55,relx=0.2,anchor='center')
                usn1=tk.Entry(newuser_window1)
                usn1.place(y=75,relx=0.2,anchor='center')
                num=tk.Label(newuser_window1,text='Phone Number',bg='#305F72', fg='White')
                num.place(y=100,relx=0.2,anchor='center')
                num1=tk.Entry(newuser_window1)
                num1.place(y=120,relx=0.2,anchor='center')
                email=tk.Label(newuser_window1,text='Email',bg='#305F72', fg='White')
                email.place(y=145,relx=0.2,anchor='center')
                email1=tk.Entry(newuser_window1)
                email1.place(y=165,relx=0.2,anchor='center')
                def add_user():
                    name = name1.get()
                    usn = usn1.get()
                    num=num1.get()
                    res=pd.read_csv('data.csv')
                    with open('data.csv','a',newline='') as file:
                        writer=csv.writer(file)
                        writer.writerow([len(res)+1,name,usn,num])
                reg=tk.Button(newuser_window1,text='Register',command=add_user, background='#FFCCCB')
                reg.place(y=220,relx=0.35,anchor='center')
                def back1():
                    newuser_window1.pack_forget()
                    register_window1.pack(side=tk.LEFT)
                back1 = tk.Button(newuser_window1, text='   Back   ', command=back1, background='Orange')
                back1.place(y=220, relx=0.65, anchor='center')
            new_reg = tk.Button(register_window1, text='Register New User', command=new_user)
            new_reg.place(y=25,relx=0.2,anchor='center')
            def update_info():
                register_window1.pack_forget()
                update_window1=tk.Frame(root,bg='#305F72',highlightbackground='White',highlightthickness=5)
                update_window1.pack(side=tk.LEFT)
                update_window1.propagate(False)
                update_window1.configure(height=255, width=400)

                def cancel1():
                    update_window1.pack_forget()
                    work_frame1.pack(side=tk.LEFT)
                cancel1 = tk.Button(update_window1, text='Home ', font=15, command=cancel1, background='#FFCCCB')
                cancel1.place(y=220, relx=0.65, anchor='center')
                def back1():
                    update_window1.pack_forget()
                    register_window1.pack(side=tk.LEFT)
                back1 = tk.Button(update_window1, text='Back ', font=15, command=back1, background='Orange')
                back1.place(y=220, relx=0.35, anchor='center')
            update1=tk.Button(register_window1,text='Update',command=update_info)
            update1.place(y=65,relx=0.2,anchor='center')
            def cancel1():
                register_window1.pack_forget()
                work_frame1.pack(side=tk.LEFT)
            cancel1 = tk.Button(register_window1, text='Home ', font=15, command=cancel1,background='#FFCCCB')
            cancel1.place(y=220,relx=0.5,anchor='center')

            messagebox.showinfo(message="         Welcome         ",title='Login Success')
        else:
            messagebox.showerror(message="Wrong password or ID",title='Login Failed')

    login1=tk.Button(admin_window1,text='Log in',font=2,command=Register1,background='#90EE90')
    login1.place(y=180,relx=0.5,anchor='center')
    def cancel1():
        admin_window1.pack_forget()
        work_frame1.pack(side=tk.LEFT)
    cancel1=tk.Button(admin_window1,text='Cancel',font=15,command=cancel1,background='#FFCCCB')
    cancel1.place(y=220,relx=0.5,anchor='center')
Admin1 = tk.Button(work_frame1, text=' Admin ',font=15, command=adminlogin1)
Admin1.place(y=120,relx=0.3,anchor='center')
def user1():
    work_frame1.pack_forget()
    user_window=tk.Frame(root,bg='#305F72', highlightbackground='White', highlightthickness=5)
    user_window.pack(side=tk.LEFT)
    user_window.propagate(False)
    user_window.configure(height=255, width=400)
    id = tk.Label(user_window, text='USER ID', bg='#305F72', fg='White')
    id.place(y=40, relx=0.5, anchor='center')
    userid=tk.Entry(user_window)
    userid.place(y=60, relx=0.5, anchor='center')
    pass1 = tk.Label(user_window, text='Password', bg='#305F72', fg='White')
    pass1.place(y=90, relx=0.5, anchor='center')
    userpass1 = tk.Entry(user_window, show='*')
    userpass1.place(y=110, relx=0.5, anchor='center')
    loginbt=tk.Button(user_window,text='Log in',font=15,background='#90EE90')
    loginbt.place(y=150,relx=0.5,anchor='center')
    def cancel1():
        user_window.pack_forget()
        work_frame1.pack(side=tk.RIGHT)

    cancel1 = tk.Button(user_window, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
    cancel1.place(y=220, relx=0.5, anchor='center')

user1=tk.Button(work_frame1, text='  User  ',font=15,command=user1)
user1.place(y=120,relx=0.7,anchor='center')
#user two
def adminlogin2():
    admin1_txt = 'evcharger'
    pass1_txt = 'DSCE'
    work_frame2.pack_forget()
    admin_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
    admin_window1.pack(side=tk.RIGHT)
    admin_window1.propagate(False)
    admin_window1.configure(height=255, width=400)
    id1 = tk.Label(admin_window1, text='ADMIN ID', bg='#305F72', fg='White')
    id1.place(y=40, relx=0.5, anchor='center')
    adminid1 = tk.Entry(admin_window1)
    adminid1.place(y=60, relx=0.5, anchor='center')
    pass1 = tk.Label(admin_window1, text='Password', bg='#305F72', fg='White')
    pass1.place(y=90, relx=0.5, anchor='center')
    adminpass1 = tk.Entry(admin_window1, show='*')
    adminpass1.place(y=110, relx=0.5, anchor='center')

    def Register1():
        a = adminid1.get()
        p = adminpass1.get()
        print(a)
        print(p)
        if (p == pass1_txt and a == admin1_txt):
            admin_window1.pack_forget()
            register_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
            register_window1.pack(side=tk.RIGHT)
            register_window1.propagate(False)
            register_window1.configure(height=255, width=400)

            def new_user():
                register_window1.pack_forget()
                newuser_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                newuser_window1.pack(side=tk.RIGHT)
                newuser_window1.propagate(False)
                newuser_window1.configure(height=255, width=400)

                def cancel1():
                    newuser_window1.pack_forget()
                    work_frame1.pack(side=tk.RIGHT)

                cancel1 = tk.Button(newuser_window1, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
                cancel1.place(y=220, relx=0.65, anchor='center')

                def back1():
                    newuser_window1.pack_forget()
                    register_window1.pack(side=tk.RIGHT)

                back1 = tk.Button(newuser_window1, text='Back ', font=15, command=back1, background='Orange')
                back1.place(y=220, relx=0.35, anchor='center')

            new_reg = tk.Button(register_window1, text='Register New User', command=new_user)
            new_reg.place(y=25, relx=0.2, anchor='center')

            def update_info():
                register_window1.pack_forget()
                update_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                update_window1.pack(side=tk.RIGHT)
                update_window1.propagate(False)
                update_window1.configure(height=255, width=400)

                def cancel1():
                    update_window1.pack_forget()
                    work_frame2.pack(side=tk.RIGHT)

                cancel1 = tk.Button(update_window1, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
                cancel1.place(y=220, relx=0.65, anchor='center')

                def back1():
                    update_window1.pack_forget()
                    register_window1.pack(side=tk.RIGHT)

                back1 = tk.Button(update_window1, text='Back ', font=15, command=back1, background='Orange')
                back1.place(y=220, relx=0.35, anchor='center')

            update1 = tk.Button(register_window1, text='Update', command=update_info)
            update1.place(y=65, relx=0.2, anchor='center')

            def cancel1():
                register_window1.pack_forget()
                work_frame2.pack(side=tk.RIGHT)

            cancel1 = tk.Button(register_window1, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
            cancel1.place(y=220, relx=0.65, anchor='center')

            def back1():
                register_window1.pack_forget()
                admin_window1.pack(side=tk.RIGHT)

            back1 = tk.Button(register_window1, text='Back ', font=15, command=back1, background='Orange')
            back1.place(y=220, relx=0.35, anchor='center')
            messagebox.showinfo(message="         Welcome         ", title='Login Success')
        else:
            messagebox.showerror(message="Wrong password or ID", title='Login Failed')

    login1 = tk.Button(admin_window1, text='Log in', font=2, command=Register1, background='#90EE90')
    login1.place(y=180, relx=0.5, anchor='center')

    def cancel1():
        admin_window1.pack_forget()
        work_frame2.pack(side=tk.RIGHT)

    cancel1 = tk.Button(admin_window1, text='Cancel', font=15, command=cancel1, background='#FFCCCB')
    cancel1.place(y=220, relx=0.5, anchor='center')
Admin2 = tk.Button(work_frame2, text='Admin',font=15, command=adminlogin2)
Admin2.place(y=120,relx=0.3,anchor='center')


user2=tk.Button(work_frame2, text='  User  ',font=15)
user2.place(y=120,relx=0.7,anchor='center')

root.mainloop()