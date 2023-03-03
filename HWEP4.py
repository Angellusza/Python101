from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from datetime import datetime

###################### csv
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist)
        
def readcsv():
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
####################csv


GUI = Tk()  #นี่คือหน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อของโปรแกรม
GUI.geometry('650x400') #นี่คือขนาดของโปรแกรม

LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลที่ต้องการ')
LF1.place(x=200,y=100)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความ GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(padx=10,pady=10)


def SaveData():
    t = datetime.now().strftime('%Y:%m:%d   %H:%M:%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    messagebox.showinfo('บันทึกสำเร็จเวลา',t)
    

B1 = ttk.Button(LF1,text='บันทึกข้อมูล',command=SaveData) #นี่คื่อชื่อปุ่ม
B1.pack(ipadx=20,ipady=20)



'''
def ShowData():
    t = datetime.now().strftime('%d:%m:%Y,%H:%M:%S')
    messagebox.showinfo('เวลาปัจจุบัน',t)
    
    
    
LF2 = Frame(GUI) 
LF2.place(x=600,y=200)

B2 = ttk.Button(LF2,text='เวลาปัจจุบัน',command=ShowData) #นี่คื่อชื่อปุ่ม
B2.pack(ipadx=10,ipady=10)
    '''
GUI.mainloop()
