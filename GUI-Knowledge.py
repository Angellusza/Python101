from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import tkinter as tk



GUI = Tk()  #นี่คือหน้าจอหลัก
GUI.title('โปรแกรมเช็คข้อมูล') #นี่คือชื่อของโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดของโปรแกรม

L1=Label(GUI,text="โปรแกรมบันทึกข้อมูล",font=("Angsana New",30),fg=('green'))
L1.place(x=120,y=20)



def Button():
    text = 'บันทึกสำเร็จแล้ว'
    messagebox.showinfo('สถานะข้อมูล',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=50,y=200)

B1 = ttk.Button(FB1,text='ข้อมูลถูกต้อง',command=Button) #นี่คื่อชื่อปุ่ม
B1.pack(ipadx=2,ipady=2)  #จัดให้ปุ่มอยู่ตรงกลาง


def Button():
    text = 'บันทึกไม่สำเร็จแล้ว'
    messagebox.showinfo('สถานะข้อมูล',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=200,y=200)

B2 = ttk.Button(FB2,text='ข้อมูลผิดพลาด',command=Button) #นี่คื่อชื่อปุ่ม
B2.pack(ipadx=2,ipady=2)

def Button():
    text = 'แก้ไขข้อมูลแล้ว'
    messagebox.showinfo('สถานะข้อมูล',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=350,y=200)

B3 = ttk.Button(FB3,text='แก้ไขข้อมูล',command=Button) #นี่คื่อชื่อปุ่ม
B3.pack(ipadx=2,ipady=2)



GUI.mainloop()
