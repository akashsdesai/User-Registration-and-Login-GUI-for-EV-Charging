import tkinter as tk
import time
import csv
import serial
import pandas as pd
import RPi.GPIO as GPIO

rel = 21
check = False
from tkinter import messagebox

count = int(0)
minn = int(0)
import board
import busio
import time

i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)
ads.gain = 1
v = 0
maxc = 0
rfd = False


def relayon1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(rel, GPIO.OUT)
    GPIO.output(rel, True)


root = tk.Tk()
root.geometry('800x416')
root.configure(bg='#305F72')
user_frame = tk.Frame(root, bg='#F1D1B5')
user_frame.pack(side=tk.BOTTOM)
user_frame.pack_propagate(False)
user_frame.configure(height=161, width=800)
voltage = 0
current = 0
vb = 0
current1 = 0
maxc = 0


def show():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)

        ser.reset_input_buffer()
    port1 = tk.Label(user_frame)
    labelv1 = tk.Label(user_frame)
    labelv11 = tk.Label(user_frame)
    labelc1 = tk.Label(user_frame)
    labelc11 = tk.Label(user_frame)
    port2 = tk.Label(user_frame)
    labelv2 = tk.Label(user_frame)
    labelv22 = tk.Label(user_frame)
    labelc2 = tk.Label(user_frame)
    labelc22 = tk.Label(user_frame)

    def measure():
        global check
        global voltage
        global current
        global vb
        global current1
        global maxc
        chan1 = AnalogIn(ads, ADS.P0)
        c = chan1.value
        if (c > maxc):
            maxc = c
        if (vb == 60):
            current1 = (maxc * 100) / 164673.3333
            current1 = round(current1, 3)
            vb = 0
            maxc = 0
        vb = vb + 1
        v = ser.readline().decode('utf-8').rstrip()
        voltage = v
        print(voltage)
        if (check):
            current = current1
        else:
            current = "0"
        print(current)
        voltage = str(voltage)
        current = str(current)
        port1.config(text='Port 1', font=40, bg='#F1D1B5', fg='Black')
        port1.place(y=15, relx=0.25, anchor='center')
        labelv1.config(text='Voltage = ', font=25, bg='#F1D1B5', fg='Black')
        labelv1.place(y=30, x=150)
        labelv11.config(text=(voltage + 'V'), font=25, bg='#F1D1B5', fg='Black')
        labelv11.place(y=30, x=220)
        labelc1.config(text='Current = ', font=25, bg='#F1D1B5', fg='Black')
        labelc1.place(y=60, x=150)
        labelc11.config(text=(current + 'A'), font=25, bg='#F1D1B5', fg='Black')
        labelc11.place(y=60, x=220)

        port2.config(text='Port 2', font=40, bg='#F1D1B5', fg='Black')
        port2.place(y=15, relx=0.75, anchor='center')
        labelv2.config(text='Voltage = ', font=25, bg='#F1D1B5', fg='Black')
        labelv2.place(y=30, x=550)
        labelv22.config(text=(voltage + 'V'), font=25, bg='#F1D1B5', fg='Black')
        labelv22.place(y=30, x=620)
        labelc2.config(text='Current = ', font=25, bg='#F1D1B5', fg='Black')
        labelc2.place(y=60, x=550)
        labelc22.config(text=(current + 'A'), font=25, bg='#F1D1B5', fg='Black')
        labelc22.place(y=60, x=620)
        labelv1.after(1, measure)

    # stop2=tk.Button(user_frame,text='❌',font=40,bg='White',fg='Red')
    # stop2.place(relx=0.75,y=135,anchor='center')
    measure()


show()
work_frame1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
work_frame1.pack(side=tk.LEFT)
work_frame1.propagate(False)
work_frame1.configure(height=255, width=400)
work_frame2 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
work_frame2.pack(side=tk.RIGHT)
work_frame2.propagate(False)
work_frame2.configure(height=255, width=400)


# user one
def adminlogin1():
    admin1_txt = 'evcharger'
    pass1_txt = 'DSCE'
    work_frame1.pack_forget()
    admin_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
    admin_window1.pack(side=tk.LEFT)
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
            register_window1.pack(side=tk.LEFT)
            register_window1.propagate(False)
            register_window1.configure(height=255, width=400)

            def new_user():
                register_window1.pack_forget()
                newuser_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                newuser_window1.pack(side=tk.LEFT)
                newuser_window1.propagate(False)
                newuser_window1.configure(height=255, width=400)
                name = tk.Label(newuser_window1, text='Name', bg='#305F72', fg='White')
                name.place(y=10, relx=0.5, anchor='center')
                name1 = tk.Entry(newuser_window1)
                name1.place(y=30, relx=0.5, anchor='center')
                num = tk.Label(newuser_window1, text='Phone Number', bg='#305F72', fg='White')
                num.place(y=55, relx=0.5, anchor='center')
                num1 = tk.Entry(newuser_window1)
                num1.place(y=75, relx=0.5, anchor='center')
                email = tk.Label(newuser_window1, text='Email', bg='#305F72', fg='White')
                email.place(y=100, relx=0.5, anchor='center')
                email1 = tk.Entry(newuser_window1)
                email1.place(y=120, relx=0.5, anchor='center')
                password = tk.Label(newuser_window1, text='Password', bg='#305F72', fg='White')
                password.place(y=145, relx=0.5, anchor='center')
                password1 = tk.Entry(newuser_window1)
                password1.place(y=165, relx=0.5, anchor='center')

                def add_user():
                    name = name1.get()

                    num = num1.get()
                    email = email1.get()
                    pas = password1.get()
                    newuser_window1.pack_forget()
                    confirm_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                    confirm_window.pack(side=tk.LEFT)
                    confirm_window.propagate(False)
                    confirm_window.configure(height=255, width=400)

                    def confirm1():
                        if __name__ == '__main__':
                            rfid = serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
                            rfid.reset_input_buffer()
                        while (1):
                            if (rfid.in_waiting > 0):
                                rf = rfid.readline().decode('utf-8').rstrip()
                                rfiddata = int(rf[4:11])
                                confirm_window.pack_forget()
                                register_window1.pack(side=tk.LEFT)
                                res = pd.read_csv('data.csv')
                                userid = len(res) + 1
                                id = str(userid) + name
                                with open('data.csv', 'a', newline='') as file:
                                    writer = csv.writer(file)
                                    amnt = int(200)
                                    writer.writerow([userid, id, name, num, email, pas, rfiddata, amnt])
                                    break
                        messagebox.showinfo(message=('your User ID = ' + id))

                    confirm = tk.Button(confirm_window, text='Scan New Card', font=15, background='#32FCA7',
                                        command=confirm1)
                    confirm.place(relx=0.5, rely=0.5, anchor='center')

                reg = tk.Button(newuser_window1, text='Register', command=add_user, background='#FFCCCB')
                reg.place(y=220, relx=0.35, anchor='center')

                def back1():
                    newuser_window1.pack_forget()
                    register_window1.pack(side=tk.LEFT)

                back1 = tk.Button(newuser_window1, text='   Back   ', command=back1, background='Orange')
                back1.place(y=220, relx=0.65, anchor='center')

            new_reg = tk.Button(register_window1, text='Register New User', command=new_user)
            new_reg.place(y=25, relx=0.5, anchor='center')

            def update_info():
                register_window1.pack_forget()
                update_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                update_window1.pack(side=tk.LEFT)
                update_window1.propagate(False)
                update_window1.configure(height=255, width=400)
                num = tk.Label(update_window1, text='Phone Number', bg='#305F72', fg='White')
                num.place(rely=0.1, relx=0.5, anchor='center')
                num1 = tk.Entry(update_window1)
                num1.place(rely=0.19, relx=0.5, anchor='center')
                email = tk.Label(update_window1, text='Email', bg='#305F72', fg='White')
                email.place(rely=0.29, relx=0.5, anchor='center')
                email1 = tk.Entry(update_window1)
                email1.place(rely=0.37, relx=0.5, anchor='center')
                password = tk.Label(update_window1, text='Password', bg='#305F72', fg='White')
                password.place(rely=0.46, relx=0.5, anchor='center')
                password1 = tk.Entry(update_window1)
                password1.place(rely=0.54, relx=0.5, anchor='center')
                name = tk.Label(update_window1, text='UserID', bg='#305F72', fg='White')
                name.place(rely=0.64, relx=0.5, anchor='center')
                userID = tk.Entry(update_window1)
                userID.place(rely=0.73, relx=0.5, anchor='center')

                def op():
                    df = pd.read_csv('data.csv')
                    num = userID.get()
                    num = num[0:1]
                    num = int(num)
                    n = num1.get()
                    e = email1.get()
                    p = password1.get()
                    df.loc[num - 1, 'Phone'] = n
                    df.loc[num - 1, 'email'] = e
                    df.loc[num - 1, 'Password'] = p
                    df.to_csv('data.csv', index=False)
                    update_window1.pack_forget()
                    register_window1.pack(side=tk.LEFT)

                update = tk.Button(update_window1, text='Update ', command=op, background='#FFCCCB')
                update.place(rely=0.92, relx=0.35, anchor='center')

                def back1():
                    update_window1.pack_forget()
                    register_window1.pack(side=tk.LEFT)

                back1 = tk.Button(update_window1, text='Back ', command=back1, background='Orange')
                back1.place(rely=0.92, relx=0.65, anchor='center')

            update1 = tk.Button(register_window1, text='Update', command=update_info)
            update1.place(y=65, relx=0.5, anchor='center')

            def recharge():
                register_window1.pack_forget()
                recharge_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                recharge_window.pack(side=tk.LEFT)
                recharge_window.propagate(False)
                recharge_window.configure(height=255, width=400)
                amnt = tk.Label(recharge_window, text='Amount', bg='#305F72', fg='White')
                amnt.place(rely=0.1, relx=0.5, anchor='center')
                amnt1 = tk.Entry(recharge_window)
                amnt1.place(rely=0.2, relx=0.5, anchor='center')
                name = tk.Label(recharge_window, text='UserID', bg='#305F72', fg='White')
                name.place(rely=0.3, relx=0.5, anchor='center')
                userID = tk.Entry(recharge_window)
                userID.place(rely=0.4, relx=0.5, anchor='center')

                def addamnt():
                    df = pd.read_csv('data.csv')
                    amnt = int(amnt1.get())
                    num = userID.get()
                    num = num[0:1]
                    num = int(num)
                    amnt = amnt + df.loc[num - 1, 'amount']
                    df.loc[num - 1, 'amount'] = amnt
                    df.to_csv('data.csv', index=False)
                    recharge_window.pack_forget()
                    register_window1.pack(side=tk.LEFT)

                recharge1 = tk.Button(recharge_window, text='Recharge', command=addamnt)
                recharge1.place(relx=0.2, rely=0.8, anchor='center')

                def back1():
                    recharge_window.pack_forget()
                    register_window1.pack(side=tk.LEFT)

                back1 = tk.Button(recharge_window, text='Back ', command=back1, background='Orange')
                back1.place(rely=0.8, relx=0.65, anchor='center')

            recharge = tk.Button(register_window1, text='Recharge', command=recharge)
            recharge.place(y=105, relx=0.5, anchor='center')

            def cancel1():
                register_window1.pack_forget()
                work_frame1.pack(side=tk.LEFT)

            cancel1 = tk.Button(register_window1, text='Home ', font=15, command=cancel1, background='#FFCCCB')
            cancel1.place(y=220, relx=0.5, anchor='center')
            messagebox.showinfo(message="         Welcome         ", title='Login Success')
        else:
            messagebox.showerror(message="Wrong password or ID", title='Login Failed')

    login1 = tk.Button(admin_window1, text='Log in', font=2, command=Register1, background='#90EE90')
    login1.place(y=180, relx=0.5, anchor='center')

    def cancel1():
        admin_window1.pack_forget()
        work_frame1.pack(side=tk.LEFT)

    cancel1 = tk.Button(admin_window1, text='Cancel', font=15, command=cancel1, background='#FFCCCB')
    cancel1.place(y=220, relx=0.5, anchor='center')


Admin1 = tk.Button(work_frame1, text=' Admin ', font=15, command=adminlogin1)
Admin1.place(y=120, relx=0.3, anchor='center')


def user1():
    work_frame1.pack_forget()
    user_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
    user_window.pack(side=tk.LEFT)
    user_window.propagate(False)
    user_window.configure(height=255, width=400)
    id = tk.Label(user_window, text='USER ID', bg='#305F72', fg='White')
    id.place(y=40, relx=0.5, anchor='center')
    userid1 = tk.Entry(user_window)
    userid1.place(y=60, relx=0.5, anchor='center')
    pass1 = tk.Label(user_window, text='Password', bg='#305F72', fg='White')
    pass1.place(y=90, relx=0.5, anchor='center')
    userpass1 = tk.Entry(user_window, show='*')
    userpass1.place(y=110, relx=0.5, anchor='center')

    def login():
        global rfd
        if (rfd == True):
            if __name__ == '__main__':
                rfid = serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
                rfid.reset_input_buffer()
            while (1):
                if (rfid.in_waiting > 0):
                    rf = rfid.readline().decode('utf-8').rstrip()
                    rfiddata = rf[4:]
                    break
        print(rfiddata)
        iden = False
        df = pd.read_csv('data.csv')
        print(len(df))
        for i in range(0, len(df)):
            if ((str(df.loc[i, 'user_id']) == str(userid1.get()) or str(df.loc[i, 'rfid1']) == rfiddata) and str(
                    df.loc[i, 'Password']) == str(userpass1.get())):
                iden = True
                messagebox.showinfo(message=('Welcome ' + df.loc[i, 'Name']))
                break
        if (iden):
            user_window.pack_forget()
            login_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
            login_window.pack(side=tk.LEFT)
            login_window.propagate(False)
            login_window.configure(height=255, width=400)
            data = pd.DataFrame(
                [[2890, 60, 750, ], [3970, 60, 750], [3400, 51.1, 720], [2250, 52, 650], [1536, 51.2, 130],
                 [3240, 72, 720], [2500, 60, 672], [2295, 60, 450], [2000, 72, 840], [1152, 48, 546]],
                index=['Ola S1', 'Ola S1 Pro', 'Ather 450X', 'TVS iQube', 'Hero Electric', 'Revolt rv400', 'Epluto 7G',
                       'Ampere Magnus Ex', 'Okinawa PraisePro', 'From battre with loev'],
                columns=['Usable Capacity', 'Volt', 'Output'])
            vehicle = tk.StringVar(login_window)
            vehicle.set('Select')
            drop = tk.OptionMenu(login_window, vehicle, *data.index)
            drop.place(relx=0.5, rely=0.1, anchor='center')

            def Next():
                selected = str(vehicle.get())
                print(selected)
                if (selected == 'Select'):
                    messagebox.showerror(message='Select your Vehicle', title='Error')
                else:
                    Next.destroy()
                    scale = tk.Scale(login_window, from_=0, to=100, orient='horizontal')
                    scale.place(relx=0.5, rely=0.4, anchor='center')

                    def pro():
                        selected = str(vehicle.get())
                        val = scale.get()
                        if (val == 0):
                            messagebox.showerror(message='Select Charging %')
                        else:
                            login_window.pack_forget()
                            charge_window = tk.Frame(root, bg='#305F72', highlightbackground='White',
                                                     highlightthickness=5)
                            charge_window.pack(side=tk.LEFT)
                            charge_window.propagate(False)
                            charge_window.configure(height=255, width=400)
                            cost = tk.Label(charge_window, text='your approx Cost is', bg='#305F72', fg='White')
                            cost.place(relx=0.5, rely=0.35, anchor='center')
                            capacity = ((data.loc[selected, 'Usable Capacity'] / 100) * val)
                            price = ((capacity / 1000) * 8.75)
                            cost1 = tk.Label(charge_window, text=('₹', price), bg='#305F72', fg='White')
                            cost1.place(relx=0.5, rely=0.43, anchor='center')

                            def charge():
                                global check
                                check = True
                                relayon1()
                                global count

                                charge_window.pack_forget()
                                ani_window = tk.Frame(root, bg='#305F72', highlightbackground='White',
                                                      highlightthickness=5)
                                ani_window.pack(side=tk.LEFT)
                                ani_window.propagate(False)
                                ani_window.configure(height=255, width=400)
                                charge = tk.Label(ani_window, text='⚡', font=50, bg='#305F72', fg='#FFD700')
                                charge.place(relx=0.5, rely=0.5, anchor='center')

                                def stop():
                                    # clock.destroy()
                                    global check
                                    check = False
                                    GPIO.output(rel, False)
                                    GPIO.cleanup(rel)
                                    stop1.destroy()
                                    ani_window.pack_forget()
                                    work_frame1.pack(side=tk.LEFT)

                                stop1 = tk.Button(user_frame, text='❌', font=40, bg='White', fg='Red', command=stop)
                                stop1.place(relx=0.25, y=135, anchor='center')

                            charge = tk.Button(charge_window, text='Charge', background='#FFCCCB', font=15,
                                               command=charge)
                            charge.place(relx=0.5, rely=0.67, anchor='center')

                            def cancel1():
                                charge_window.pack_forget()
                                login_window.pack(side=tk.RIGHT)

                            cancel1 = tk.Button(charge_window, text='Cancel ', font=15, command=cancel1,
                                                background='#FFCCCB')
                            cancel1.place(rely=0.85, relx=0.5, anchor='center')

                    proceed = tk.Button(login_window, text='Proceed', background='#FFCCCB', font=15, command=pro)
                    proceed.place(relx=0.5, rely=0.7, anchor='center')

            Next = tk.Button(login_window, text='Next', background='#FFCCCB', command=Next, font=15)
            Next.place(relx=0.5, rely=0.7, anchor='center')

            def cancel1():
                login_window.pack_forget()
                work_frame1.pack(side=tk.RIGHT)

            cancel1 = tk.Button(login_window, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
            cancel1.place(y=220, relx=0.5, anchor='center')
        else:
            messagebox.showerror(message='Wrong id or Password', title='Error')

    loginbt = tk.Button(user_window, text='   Log in   ', background='#90EE90', command=login)
    loginbt.place(rely=0.6, relx=0.3, anchor='center')

    def rfdd():
        global rfd
        rfd = True
        login()

    rfid = tk.Button(user_window, text='RFID login', background='#90EE90', command=rfdd)
    rfid.place(rely=0.6, relx=0.7, anchor='center')

    def cancel1():
        user_window.pack_forget()
        work_frame1.pack(side=tk.RIGHT)

    cancel1 = tk.Button(user_window, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
    cancel1.place(y=220, relx=0.5, anchor='center')


user1 = tk.Button(work_frame1, text='  User  ', font=15, command=user1)
user1.place(y=120, relx=0.7, anchor='center')


# user two
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
                name = tk.Label(newuser_window1, text='Name', bg='#305F72', fg='White')
                name.place(y=10, relx=0.5, anchor='center')
                name1 = tk.Entry(newuser_window1)
                name1.place(y=30, relx=0.5, anchor='center')
                num = tk.Label(newuser_window1, text='Phone Number', bg='#305F72', fg='White')
                num.place(y=55, relx=0.5, anchor='center')
                num1 = tk.Entry(newuser_window1)
                num1.place(y=75, relx=0.5, anchor='center')
                email = tk.Label(newuser_window1, text='Email', bg='#305F72', fg='White')
                email.place(y=100, relx=0.5, anchor='center')
                email1 = tk.Entry(newuser_window1)
                email1.place(y=120, relx=0.5, anchor='center')
                password = tk.Label(newuser_window1, text='Password', bg='#305F72', fg='White')
                password.place(y=145, relx=0.5, anchor='center')
                password1 = tk.Entry(newuser_window1)
                password1.place(y=165, relx=0.5, anchor='center')

                def add_user():
                    name = name1.get()

                    num = num1.get()
                    email = email1.get()
                    pas = password1.get()
                    newuser_window1.pack_forget()
                    confirm_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                    confirm_window.pack(side=tk.RIGHT)
                    confirm_window.propagate(False)
                    confirm_window.configure(height=255, width=400)

                    def confirm1():
                        if __name__ == '__main__':
                            rfid = serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
                            rfid.reset_input_buffer()
                        while (1):
                            if (rfid.in_waiting > 0):
                                rf = rfid.readline().decode('utf-8').rstrip()
                                rfiddata = int(rf[4:11])
                                confirm_window.pack_forget()
                                register_window1.pack(side=tk.RIGHT)
                                res = pd.read_csv('data.csv')
                                userid = len(res) + 1
                                id = str(userid) + name
                                with open('data.csv', 'a', newline='') as file:
                                    writer = csv.writer(file)
                                    amnt = int(200)
                                    writer.writerow([userid, id, name, num, email, pas, rfiddata, amnt])
                                    break
                        messagebox.showinfo(message=('your User ID = ' + id))

                    confirm = tk.Button(confirm_window, text='Scan New Card', font=15, background='#32FCA7',
                                        command=confirm1)
                    confirm.place(relx=0.5, rely=0.5, anchor='center')

                reg = tk.Button(newuser_window1, text='Register', command=add_user, background='#FFCCCB')
                reg.place(y=220, relx=0.35, anchor='center')

                def back1():
                    newuser_window1.pack_forget()
                    register_window1.pack(side=tk.RIGHT)

                back1 = tk.Button(newuser_window1, text='   Back   ', command=back1, background='Orange')
                back1.place(y=220, relx=0.65, anchor='center')

            new_reg = tk.Button(register_window1, text='Register New User', command=new_user)
            new_reg.place(y=25, relx=0.5, anchor='center')

            def update_info():
                register_window1.pack_forget()
                update_window1 = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                update_window1.pack(side=tk.RIGHT)
                update_window1.propagate(False)
                update_window1.configure(height=255, width=400)
                num = tk.Label(update_window1, text='Phone Number', bg='#305F72', fg='White')
                num.place(rely=0.1, relx=0.5, anchor='center')
                num1 = tk.Entry(update_window1)
                num1.place(rely=0.19, relx=0.5, anchor='center')
                email = tk.Label(update_window1, text='Email', bg='#305F72', fg='White')
                email.place(rely=0.29, relx=0.5, anchor='center')
                email1 = tk.Entry(update_window1)
                email1.place(rely=0.37, relx=0.5, anchor='center')
                password = tk.Label(update_window1, text='Password', bg='#305F72', fg='White')
                password.place(rely=0.46, relx=0.5, anchor='center')
                password1 = tk.Entry(update_window1)
                password1.place(rely=0.54, relx=0.5, anchor='center')
                name = tk.Label(update_window1, text='UserID', bg='#305F72', fg='White')
                name.place(rely=0.64, relx=0.5, anchor='center')
                userID = tk.Entry(update_window1)
                userID.place(rely=0.73, relx=0.5, anchor='center')

                def op():
                    df = pd.read_csv('data.csv')
                    num = userID.get()
                    num = num[0:1]
                    num = int(num)
                    n = num1.get()
                    e = email1.get()
                    p = password1.get()
                    df.loc[num - 1, 'Phone'] = n
                    df.loc[num - 1, 'email'] = e
                    df.loc[num - 1, 'Password'] = p
                    df.to_csv('data.csv', index=False)
                    update_window1.pack_forget()
                    register_window1.pack(side=tk.RIGHT)

                update = tk.Button(update_window1, text='Update ', command=op, background='#FFCCCB')
                update.place(rely=0.92, relx=0.35, anchor='center')

                def back1():
                    update_window1.pack_forget()
                    register_window1.pack(side=tk.RIGHT)

                back1 = tk.Button(update_window1, text='Back ', command=back1, background='Orange')
                back1.place(rely=0.92, relx=0.65, anchor='center')

            update1 = tk.Button(register_window1, text='Update', command=update_info)
            update1.place(y=65, relx=0.5, anchor='center')

            def recharge():
                register_window1.pack_forget()
                recharge_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
                recharge_window.pack(side=tk.RIGHT)
                recharge_window.propagate(False)
                recharge_window.configure(height=255, width=400)
                amnt = tk.Label(recharge_window, text='Amount', bg='#305F72', fg='White')
                amnt.place(rely=0.1, relx=0.5, anchor='center')
                amnt1 = tk.Entry(recharge_window)
                amnt1.place(rely=0.2, relx=0.5, anchor='center')
                name = tk.Label(recharge_window, text='UserID', bg='#305F72', fg='White')
                name.place(rely=0.3, relx=0.5, anchor='center')
                userID = tk.Entry(recharge_window)
                userID.place(rely=0.4, relx=0.5, anchor='center')

                def addamnt():
                    df = pd.read_csv('data.csv')
                    amnt = int(amnt1.get())
                    num = userID.get()
                    num = num[0:1]
                    num = int(num)
                    amnt = amnt + df.loc[num - 1, 'amount']
                    df.loc[num - 1, 'amount'] = amnt
                    df.to_csv('data.csv', index=False)
                    recharge_window.pack_forget()
                    register_window1.pack(side=tk.RIGHT)

                recharge1 = tk.Button(recharge_window, text='Recharge', command=addamnt)
                recharge1.place(relx=0.2, rely=0.8, anchor='center')

                def back1():
                    recharge_window.pack_forget()
                    register_window1.pack(side=tk.RIGHT)

                back1 = tk.Button(recharge_window, text='Back ', command=back1, background='Orange')
                back1.place(rely=0.8, relx=0.65, anchor='center')

            recharge = tk.Button(register_window1, text='Recharge', command=recharge)
            recharge.place(y=105, relx=0.5, anchor='center')

            def cancel1():
                register_window1.pack_forget()
                work_frame2.pack(side=tk.RIGHT)

            cancel1 = tk.Button(register_window1, text='Home ', font=15, command=cancel1, background='#FFCCCB')
            cancel1.place(y=220, relx=0.5, anchor='center')
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
Admin2 = tk.Button(work_frame2, text='Admin', font=15, command=adminlogin2)
Admin2.place(y=120, relx=0.3, anchor='center')
def user2():
    work_frame2.pack_forget()
    user_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
    user_window.pack(side=tk.RIGHT)
    user_window.propagate(False)
    user_window.configure(height=255, width=400)
    id = tk.Label(user_window, text='USER ID', bg='#305F72', fg='White')
    id.place(y=40, relx=0.5, anchor='center')
    userid1 = tk.Entry(user_window)
    userid1.place(y=60, relx=0.5, anchor='center')
    pass1 = tk.Label(user_window, text='Password', bg='#305F72', fg='White')
    pass1.place(y=90, relx=0.5, anchor='center')
    userpass1 = tk.Entry(user_window, show='*')
    userpass1.place(y=110, relx=0.5, anchor='center')

    def login():
        global rfd
        if (rfd == True):
            if __name__ == '__main__':
                rfid = serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
                rfid.reset_input_buffer()
            while (1):
                if (rfid.in_waiting > 0):
                    rf = rfid.readline().decode('utf-8').rstrip()
                    rfiddata = rf[4:]
                    break
        print(rfiddata)
        iden = False
        df = pd.read_csv('data.csv')
        print(len(df))
        for i in range(0, len(df)):
            if ((str(df.loc[i, 'user_id']) == str(userid1.get()) or str(df.loc[i, 'rfid1']) == rfiddata) and str(
                    df.loc[i, 'Password']) == str(userpass1.get())):
                iden = True
                messagebox.showinfo(message=('Welcome ' + df.loc[i, 'Name']))
                break
        if (iden):
            user_window.pack_forget()
            login_window = tk.Frame(root, bg='#305F72', highlightbackground='White', highlightthickness=5)
            login_window.pack(side=tk.RIGHT)
            login_window.propagate(False)
            login_window.configure(height=255, width=400)
            data = pd.DataFrame(
                [[2890, 60, 750, ], [3970, 60, 750], [3400, 51.1, 720], [2250, 52, 650], [1536, 51.2, 130],
                 [3240, 72, 720], [2500, 60, 672], [2295, 60, 450], [2000, 72, 840], [1152, 48, 546]],
                index=['Ola S1', 'Ola S1 Pro', 'Ather 450X', 'TVS iQube', 'Hero Electric', 'Revolt rv400', 'Epluto 7G',
                       'Ampere Magnus Ex', 'Okinawa PraisePro', 'From battre with loev'],
                columns=['Usable Capacity', 'Volt', 'Output'])
            vehicle = tk.StringVar(login_window)
            vehicle.set('Select')
            drop = tk.OptionMenu(login_window, vehicle, *data.index)
            drop.place(relx=0.5, rely=0.1, anchor='center')

            def Next():
                selected = str(vehicle.get())
                print(selected)
                if (selected == 'Select'):
                    messagebox.showerror(message='Select your Vehicle', title='Error')
                else:
                    Next.destroy()
                    scale = tk.Scale(login_window, from_=0, to=100, orient='horizontal')
                    scale.place(relx=0.5, rely=0.4, anchor='center')

                    def pro():
                        selected = str(vehicle.get())
                        val = scale.get()
                        if (val == 0):
                            messagebox.showerror(message='Select Charging %')
                        else:
                            login_window.pack_forget()
                            charge_window = tk.Frame(root, bg='#305F72', highlightbackground='White',
                                                     highlightthickness=5)
                            charge_window.pack(side=tk.RIGHT)
                            charge_window.propagate(False)
                            charge_window.configure(height=255, width=400)
                            cost = tk.Label(charge_window, text='your approx Cost is', bg='#305F72', fg='White')
                            cost.place(relx=0.5, rely=0.35, anchor='center')
                            capacity = ((data.loc[selected, 'Usable Capacity'] / 100) * val)
                            price = ((capacity / 1000) * 8.75)
                            cost1 = tk.Label(charge_window, text=('₹', price), bg='#305F72', fg='White')
                            cost1.place(relx=0.5, rely=0.43, anchor='center')

                            def charge():
                                global check
                                check = True
                                relayon2()
                                global count

                                charge_window.pack_forget()
                                ani_window = tk.Frame(root, bg='#305F72', highlightbackground='White',
                                                      highlightthickness=5)
                                ani_window.pack(side=tk.RIGHT)
                                ani_window.propagate(False)
                                ani_window.configure(height=255, width=400)
                                charge = tk.Label(ani_window, text='⚡', font=50, bg='#305F72', fg='#FFD700')
                                charge.place(relx=0.5, rely=0.5, anchor='center')

                                def stop():
                                    # clock.destroy()
                                    global check
                                    check = False
                                    GPIO.output(rel2, False)
                                    GPIO.cleanup(rel2)
                                    stop2.destroy()
                                    ani_window.pack_forget()
                                    work_frame1.pack(side=tk.RIGHT)

                                stop2 = tk.Button(user_frame, text='❌', font=40, bg='White', fg='Red', command=stop)
                                stop2.place(relx=0.75, y=135, anchor='center')

                            charge = tk.Button(charge_window, text='Charge', background='#FFCCCB', font=15,
                                               command=charge)
                            charge.place(relx=0.5, rely=0.67, anchor='center')

                            def cancel1():
                                charge_window.pack_forget()
                                login_window.pack(side=tk.RIGHT)

                            cancel1 = tk.Button(charge_window, text='Cancel ', font=15, command=cancel1,
                                                background='#FFCCCB')
                            cancel1.place(rely=0.85, relx=0.5, anchor='center')

                    proceed = tk.Button(login_window, text='Proceed', background='#FFCCCB', font=15, command=pro)
                    proceed.place(relx=0.5, rely=0.7, anchor='center')

            Next = tk.Button(login_window, text='Next', background='#FFCCCB', command=Next, font=15)
            Next.place(relx=0.5, rely=0.7, anchor='center')

            def cancel1():
                login_window.pack_forget()
                work_frame2.pack(side=tk.RIGHT)

            cancel1 = tk.Button(login_window, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
            cancel1.place(y=220, relx=0.5, anchor='center')
        else:
            messagebox.showerror(message='Wrong id or Password', title='Error')

    loginbt = tk.Button(user_window, text='   Log in   ', background='#90EE90', command=login)
    loginbt.place(rely=0.6, relx=0.3, anchor='center')

    def rfdd():
        global rfd
        rfd = True
        login()

    rfid = tk.Button(user_window, text='RFID login', background='#90EE90', command=rfdd)
    rfid.place(rely=0.6, relx=0.7, anchor='center')

    def cancel1():
        user_window.pack_forget()
        work_frame2.pack(side=tk.RIGHT)

    cancel1 = tk.Button(user_window, text='Cancel ', font=15, command=cancel1, background='#FFCCCB')
    cancel1.place(y=220, relx=0.5, anchor='center')

user2 = tk.Button(work_frame2, text='  User  ', font=15,command=user2)
user2.place(y=120, relx=0.7, anchor='center')
root.mainloop()
