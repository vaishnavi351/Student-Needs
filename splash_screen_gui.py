from tkinter.ttk import Progressbar
from tkinter import *
import os,subprocess
import sys
import tkinter as tk
from tkinter import ttk
win=Tk()


width_of_window = 600 
height_of_window = 340 
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
win.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


win.overrideredirect(1)


s = ttk.Style()
s.theme_use('default')
s.configure("red.Horizontal.TProgressbar", background='#ff512f')
progress=Progressbar(win,style='red.Horizontal.TProgressbar',orient=HORIZONTAL,length=600,mode='determinate')


def new_win():
    k=os.system("login_page.py")
    
    # from login_page import login_page
    # root = Tk()
  
     
    # obj = login_page(root)
    # root.mainloop()
  
    sys.path.append(os.path.abspath("\Desktop\new ui\Minor project"))
    import main_ui
    
  

  
    




def bar():

    l4=Label(win,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=0,y=260)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        win.update_idletasks()
        time.sleep(0.03)
        r=r+1
    win.destroy()
    new_win()

progress.place(x=-10,y=320)        
    





a='Black'
f1 = tk.PhotoImage(file="sk.png")
Frame(win,width=600,height=325,bg=a).place(x=0,y=0)  
b1=Button(win,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=250,y=280)


######## Label

l1=tk.Label(win,image=f1,fg='white',bg=a)
l1.place(x=160,y=-10)


l2=Label(win,text='Student Needs',fg='White',bg=a,font=('Times New Roman',30,'bold'))
l2.place(x=168,y=220)


win.mainloop()


