import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import font,colorchooser,filedialog,messagebox
import wikipedia

wiki_home=tk.Tk()
wiki_home.title('Wikipedia')
wiki_home.geometry('854x480')
wiki_home.resizable(0,0)

# Icons
head_icon=tk.PhotoImage(file='wiki_icon.png')
search_icon=tk.PhotoImage(file='search_icon.png')
search_btn_icon=tk.PhotoImage(file='search_btn.png')
##icons end...........

#label
main_label=ttk.Label(wiki_home,text='Wikipedia',font=('Colonna MT',30,'bold'))
main_label.grid(row=0,columnspan=3,padx=359)
main_label_1=tk.Label(wiki_home,image=head_icon)
main_label_1.grid(row=0,column=0,padx=220)

search_label=tk.Label(wiki_home,text='Search :',font=('Colonna MT',20,'bold'))
search_label.grid(row=1,column=0,sticky=tk.W,pady=30,padx=70)
search_label_1=tk.Label(wiki_home,image=search_icon)
search_label_1.grid(row=1,column=0,sticky=tk.W,pady=40)
## label end........

#SearchEntry
search_data=tk.StringVar()
search_entry=tk.Entry(wiki_home,width=48,textvariable=search_data,bg='#2c3e50',fg='White',font=('Comic Sans MS',14))
search_entry.grid(row=1,columnspan=10,ipady=5,padx=185)
##SearchEntry end....





# Ans_Text
Ans_Text=tk.Text(wiki_home,width=67,height=9,bg='#2c3e50',fg='White',font=('Comic Sans MS',14))
Ans_Text.grid(rowspan=3,columnspan=3,sticky=tk.W,padx=22,ipady=8)
## Ans_Text end....

#SearchEntry_button

def pi():
    new_data=search_data.get()
    
    try:
        if new_data:
            Ans_Text.delete('1.0','end')
            Ans_Text.insert(tk.END,wikipedia.summary(new_data,sentences=4,auto_suggest=False))
    except:
          messagebox.showwarning('Connection','Internet is not working')


search_button=tk.Button(wiki_home,image=search_btn_icon,highlightthickness=0,bd=0,cursor='hand2',command=pi)
search_button.grid(row=1,columnspan=3,sticky=tk.E,padx=65)

#SearchEntry_button end....


wiki_home.mainloop()
