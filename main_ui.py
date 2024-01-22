from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import font,colorchooser,filedialog,messagebox
from googletrans import Translator 
import vlc,pafy,math,os,wikipedia
import webbrowser



      


main_ui=tk.Tk()
main_ui.title('Student Needs')
main_ui.geometry('862x610')
main_ui.iconbitmap('student_needs.ico')
main_ui.resizable(0,0)
url=''
current_font_family='Arial'    
current_font_size= 12
text_changed=False
translator=Translator()

def study_material():
   study=tk.Toplevel(main_ui)
   study.title('Study Material')
   study.geometry('530x450')
   study.iconbitmap('study_head.ico')
   study.resizable(0,0)
   study_P1=tk.PhotoImage(file='study_P1.png')
   #Labels
   study_L1=tk.Label(study,text='Study Material',font=('Colonna MT',28,'bold'))
   study_L1.grid(row=0,columnspan=5,padx=170)
   study_L2=tk.Label(study,image=study_P1)
   study_L2.grid(row=0,column=0,padx=69)

   #buttons
   study_B1_P1=tk.PhotoImage(file='python_btn.png')
   study_B1_P2=tk.PhotoImage(file='java_btn.png')
   study_B1_P3=tk.PhotoImage(file='c++_btn.png')
   study_B1_P4=tk.PhotoImage(file='c_btn.png')

   def python():
      url = "https://youtu.be/RAwntanK4wQ"
      video = pafy.new(url)
      best = video.getbest()
      media = vlc.MediaPlayer(best.url)
      media.play()
      
      
   study_B1=tk.Button(study,image=study_B1_P1,highlightthickness=0,bd=0,cursor='hand2',command=python)
   study_B1.grid(row=1,column=0,pady=30)

   def java():
      url = "https://youtu.be/kToBR6JBANc"
      video = pafy.new(url)
      best = video.getbest()
      media = vlc.MediaPlayer(best.url)
      media.play()
      


   study_B2=tk.Button(study,image=study_B1_P2,highlightthickness=0,bd=0,cursor='hand2',command=java)
   study_B2.grid(row=1,column=1,pady=30)

   def c_plus():
      url = "https://youtu.be/j8nAHeVKL08"
      video = pafy.new(url)
      best = video.getbest()
      media = vlc.MediaPlayer(best.url)
      media.play()
      

   study_B3=tk.Button(study,image=study_B1_P3,highlightthickness=0,bd=0,cursor='hand2',command=c_plus)
   study_B3.grid(row=2,column=0,pady=30)
   
   def c_lan():
      url = "https://youtu.be/7Dh73z3icd8"
      video = pafy.new(url)
      best = video.getbest()
      media = vlc.MediaPlayer(best.url)
      media.play()
      

   study_B4=tk.Button(study,image=study_B1_P4,highlightthickness=0,bd=0,cursor='hand2',command=c_lan)
   study_B4.grid(row=2,column=1,pady=30)

   study.mainloop()

def web_site():
    webbrowser.open('https://sites.google.com/view/studentneeds/home')
    

def Dictionary():
   new_window_1=tk.Toplevel(main_ui)
   new_window_1.title('Dictionary')
   new_window_1.iconbitmap('dictionary_logo.ico')
   new_window_1.geometry('550x290')
   new_window_1.resizable(0,0)
   Dic_1=tk.PhotoImage(file='dict_head.png')
   Dic_2=tk.PhotoImage(file='search_btn.png')
   
   main_label=tk.Label(new_window_1,image=Dic_1)
   main_label.grid(row=0,column=0,padx=130)

   main_label_1=tk.Label(new_window_1,text='Dictionary',font=('Colonna MT','30','bold'))
   main_label_1.grid(row=0,columnspan=5,padx=220)

   search_box=tk.Label(new_window_1,text='Search:',font=('Colonna MT','20','bold'))
   search_box.grid(row=1,column=0,sticky=tk.W,pady=39)

   var=tk.StringVar()
   search_box_entry=tk.Entry(new_window_1,width=43,textvariable=var,bg='#2c3e50',fg='White')
   search_box_entry.grid(row=1,columnspan=3,padx=100,ipadx=60,ipady=3,sticky=tk.E)
   


   ans_label=tk.Label(new_window_1,text='Meaning:',font=('Colonna MT','18','bold'))
   ans_label.grid(row=2,column=0,sticky=tk.W,pady=30)

   text=tk.Entry(new_window_1,width=62,bg='#2c3e50',fg='White')
   text.grid(row=2,columnspan=8,sticky=tk.W,padx=110,ipady=3)
   def ans():
     a=var.get() 
     lm='en'
     b='hi'
   
     try:
        if a:
         text.delete(0,tk.END)
         text.insert(tk.END,f'{a.upper()}:{translator.translate(a,src=lm,dest=b).text}')
     except:
        messagebox.showwarning('Connection','Internet is now working')

   sumbit_btn=tk.Button(new_window_1,image=Dic_2,cursor='hand2',highlightthickness=0,bd=0,command=ans)
   sumbit_btn.grid(row=1,column=2,sticky=tk.E,padx=33)  
   new_window_1.mainloop()
    


def Notepad():
    main_application=tk.Toplevel()
    main_application.geometry('1200x800')
    main_application.title('Notepad')
    main_application.iconbitmap('icon.ico')
    
    ################################################# main menu ####################################################################################################

    main_menu=tk.Menu()
    #file icons
    new_icon=tk.PhotoImage(file='icons2/new.png')
    open_icon=tk.PhotoImage(file='icons2/open.png')
    save_icon=tk.PhotoImage(file='icons2/save.png')
    save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
    exit_icon=tk.PhotoImage(file='icons2/exit.png')

    file=tk.Menu(main_menu,tearoff=False)

    # edit icons
    copy_icon=tk.PhotoImage(file='icons2/copy.png')
    paste_icon=tk.PhotoImage(file='icons2/paste.png')
    cut_icon=tk.PhotoImage(file='icons2/cut.png')
    clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
    find_icon=tk.PhotoImage(file='icons2/find.png')

    edit=tk.Menu(main_menu,tearoff=False)

    


    ## color theme icon
    light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
    light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
    dark_icon=tk.PhotoImage(file='icons2/dark.png')
    red_icon=tk.PhotoImage(file='icons2/red.png')
    monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
    night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')

    color_theme=tk.Menu(main_menu,tearoff=False)
    theme_choice=tk.StringVar()
    color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
    color_dict={
      'Light Default':('#000000','#ffffff'),
      'Light Plus':('#474747','#e0e0e0'),
      'Dark':('#c4c4c4','#2d2d2d'),
      'Red':('#2d2d2d','#ffe8e8'),
      'Monokai':('#d3b774','#474747'),       
      'Night Blue':('#ededed','#6b9dc2')
    }
    #cascade
    main_menu.add_cascade(label='File',menu=file)
    main_menu.add_cascade(label='Edit',menu=edit)
    main_menu.add_cascade(label='Color Theme',menu=color_theme)

    # #---------------------------&&&&&&&&&&&&&&&&&&&&& End main menu &&&&&&&&&--------------------------------------------------------------------------------------


    # ################################################# toolbar #####################################################################################

    tool_bar=ttk.Label(main_application)
    tool_bar.pack(side=tk.TOP,fill=tk.X)

    #font box
    font_tuple=tk.font.families()
    font_family=tk.StringVar()
    font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
    font_box['values']=font_tuple
    font_box.current(font_tuple.index('Arial'))
    font_box.grid(row=0,column=0,padx=5)

    #size box
    size_var=tk.IntVar()
    font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
    font_size['values']=tuple(range(8,81))
    font_size.current(4)
    font_size.grid(row=0,column=1,padx=5)
    
    #bold button
    bold_icon=tk.PhotoImage(file='icons2/bold.png')
    bold_btn=ttk.Button(tool_bar,image=bold_icon)
    bold_btn.grid(row=0,column=2,padx=5)

    #italic button
    italic_icon=tk.PhotoImage(file='icons2/italic.png')
    italic_btn=ttk.Button(tool_bar,image=italic_icon)
    italic_btn.grid(row=0,column=3,padx=5)

    #underline button
    underline_icon=tk.PhotoImage(file='icons2/underline.png')
    underline_btn=ttk.Button(tool_bar,image=underline_icon)
    underline_btn.grid(row=0,column=4,padx=5)

    # font color button
    font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
    font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
    font_color_btn.grid(row=0,column=5,padx=5)

    # align left button
    align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
    align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
    align_left_btn.grid(row=0,column=6,padx=5)

    #align center button
    align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
    align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
    align_center_btn.grid(row=0,column=7,padx=5)

    #align right button
    align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
    align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
    align_right_btn.grid(row=0,column=8,padx=5)

    #----------------------------&&&&&&&&&&&&&&&&&&&& End toolbar &&&&&&&&&&&-----------------------------------------------------------------------
    

    ##################################################text editor ##################################################################################
    text_editor=tk.Text(main_application)
    text_editor.config(wrap='word',relief=tk.FLAT)

    scrool_bar=tk.Scrollbar(main_application)
    text_editor.focus_set()
    scrool_bar.pack(side=tk.RIGHT,fill=tk.Y)
    text_editor.pack(fill=tk.BOTH,expand=True)
    scrool_bar.config(command=text_editor.yview)
    text_editor.config(yscrollcommand=scrool_bar.set)
    
    # font family and font size functionality
    

    def change_font(event=None): # aap chye to yaha main_application bhi pass kra sakte hai
        global current_font_family
        current_font_family=font_family.get()
        text_editor.configure(font=(current_font_family,current_font_size))

    def change_fontsize(event=None): #  yaha pr bhiaap chye to yaha main_application bhi pass kra sakte hai
        global current_font_size
        current_font_size=size_var.get()
        text_editor.configure(font=(current_font_family,current_font_size))

    font_box.bind("<<ComboboxSelected>>",change_font)
    font_size.bind("<<ComboboxSelected>>",change_fontsize)

    text_editor.configure(font=('Arial',12))

    ## buttons functionality

    # bold button functionality
    def change_bold():
        text_property_bold=tk.font.Font(font=text_editor['font'])
        if text_property_bold.actual()['weight']=='normal':
            text_editor.configure(font=(current_font_family,current_font_size,'bold'))
        
        if text_property_bold.actual()['weight']=='bold':
            text_editor.configure(font=(current_font_family,current_font_size,'normal'))

    bold_btn.configure(command=change_bold)  

    # italic button functionality
    def change_italic():
        text_property_italic=tk.font.Font(font=(text_editor['font']))
        if text_property_italic.actual()['slant']=='roman':
            text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    
        if text_property_italic.actual()['slant']=='italic':
            text_editor.configure(font=(current_font_family,current_font_size,'roman'))

    italic_btn.configure(command=change_italic)
    
    # underline button functionality
    def change_underline():
        text_property_underline=tk.font.Font(font=(text_editor['font']))
        if text_property_underline.actual()['underline']==0:
            text_editor.configure(font=(current_font_family,current_font_size,'underline'))
        if text_property_underline.actual()['underline']==1:
            text_editor.configure(font=(current_font_family,current_font_size,'normal'))

    underline_btn.configure(command=change_underline) 

    
    # font color functionality    
    def change_font_color():
        color_var=tk.colorchooser.askcolor()
        text_editor.configure(foreground=color_var[1])

    font_color_btn.configure(command=change_font_color) 

    ## align functionality

    # align left button functionality

    def align_left():
        text_content=text_editor.get(1.0,'end')
        text_editor.tag_config('left',justify=tk.LEFT)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(tk.INSERT,text_content,'left')

        align_left_btn.configure(command=align_left)

    # align center button functionality
    def align_center():
        text_context=text_editor.get(1.0,'end')
        text_editor.tag_config('center',justify=tk.CENTER)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(tk.INSERT,text_context,'center')

    align_center_btn.configure(command=align_center) 

    # align right button functionality
    def align_right():
        text_context=text_editor.get(1.0,'end')
        text_editor.tag_config('right',justify=tk.RIGHT)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(tk.INSERT,text_context,'right')

    align_right_btn.configure(command=align_right)
    # #-------------------------------------------&&&&& End text editor &&&&&&&&&&&&&&&&&&&&&&&&&&&------------------------------------------------------------------------------------
    
    # #################################################  status bar ###############################################################################

    status_bar=ttk.Label(main_application,text='Status Bar')
    status_bar.pack(side=tk.BOTTOM)

    text_changed=False
    def changed(event=0):
        global text_changed
        if text_editor.edit_modified():
            text_changed=True
            words=len(text_editor.get(1.0,'end-1c').split())
            characters=len(text_editor.get(1.0,'end-1c').replace(" ",''))
            status_bar.config(text=f'Chracters : {characters} Words : {words}')
            text_editor.edit_modified(False)

    text_editor.bind('<<Modified>>',changed) 

# #-----------------------------------------------&&&&& End  status bar &&&&&&&&&--------------------------------------------------------------

# ############################################### main menu functionality ######################################################################
# variable


    #new_file functionality
    def new_file(event=None):
        global url
        url=''
        text_editor.delete(1.0,tk.END)

    file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

    #open functionality
    def open_file(event=None):
        global url
        url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*'))) 
        try:
            with open(url,'r') as fr:
                text_editor.delete(1.0,tk.END)
                text_editor.insert(1.0,fr.read())
        except FileNotFoundError:
            return
        except:
            return
        main_application.title(os.path.basename(url))

    file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

    # save_file functionality
    def save_file(event=None):
        global url
        try:
            if url:
                content=str(text_editor.get(1.0,tk.END))
                with open(url,'w',encoding='utf-8') as fw:
                    fw.write(content)
            else:
                url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                content2=text_editor.get(1.0,tk.END)
                url.write(content2)
                url.close()
        except:
            return                 

    file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

    # save_as_file functionality

    def save_as(event=None):
        global url
        try:
            content=text_editor.get(1.0,tk.END)
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            url.write(content)
            url.close()
        except:
            return    


    file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as)

    # exit functionality

    def exit_func(event=None):
        global url ,text_changed
        try:
            if text_changed:
                mbox=messagebox.askyesnocancel('Warning','Do you want to save te file ?')
                if mbox is True:
                    if url:
                        content=text_editor.get(1.0,tk.END)
                        with open(url,'w',encoding='utf-8') as fw:
                            fw.write(content)
                            main_application.destroy()
                    else:
                        content2=str(text_editor.get(1.0,tk.END))
                        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                        url.write(content2)
                        url.close()
                        main_application.destroy()
                elif mbox is False:
                    main_application.destroy()
            else:
                main_application.destroy()
        except:
            return                        

    file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)


    ### find_button functionality
    def find_func(event=None):
        def find():
            word =find_input.get()
            text_editor.tag_remove('match','1.0',tk.END)
            matches=0
            if word:
                start_pos='1.0'
                while True:
                    start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                    if not start_pos:
                        break
                    end_pos = f'{start_pos}+{len(word)}c'
                    text_editor.tag_add('match',start_pos,end_pos)
                    matches+=1
                    start_pos=end_pos
                    text_editor.tag_config('match',foreground='red',background='yellow')

        def replace():
            word=find_input.get()
            replace_text=replace_input.get()
            content=text_editor.get(1.0,tk.END)
            new_content=content.replace(word,replace_text)
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,new_content)



        find_dialogue=tk.Toplevel()
        find_dialogue.geometry('450x250+500+200')
        find_dialogue.title('Find')
        find_dialogue.resizable(0,0)
        # frame
        find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
        find_frame.pack(pady=20)
  
        #lables
        text_find_label=ttk.Label(find_frame,text='Find')
        text_replace_label=ttk.Label(find_frame,text='Replace')

        # entry
        find_input=ttk.Entry(find_frame,width=30)
        replace_input=ttk.Entry(find_frame,width=30)

        # button  
        find_button=ttk.Button(find_frame,text='Find',command=find)
        replace_button=ttk.Button(find_frame,text='replace',command=replace)

    # label grid
        text_find_label.grid(row=0,column=0,padx=4,pady=4)
        text_replace_label.grid(row=1,column=0,padx=4,pady=4)

        # entry grid
        find_input.grid(row=0,column=1,padx=4,pady=4)
        replace_input.grid(row=1,column=1,padx=4,pady=4)

        # button grid
        find_button.grid(row=2,column=0,padx=8,pady=4)
        replace_button.grid(row=2,column=1,padx=8,pady=4)
        find_dialogue.mainloop()
    
    # edit command
    edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda :text_editor.event_generate("<Control c>"))
    edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
    edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
    edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
    edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)
    
    # color theme
    def change_theme():
     choose_theme=theme_choice.get()
     color_tuple=color_dict.get(choose_theme)
     fg_color,bg_color=color_tuple[0],color_tuple[1]
     text_editor.config(background=bg_color,foreground=fg_color)
    
    count=0
    for i in color_dict:
      color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
      count+=1
    
    
    main_application.config(menu=main_menu)
    ## bind shortcut keys
    main_application.bind('<Control-n>',new_file)
    main_application.bind('<Control-o>',open_file)
    main_application.bind('<Control-s>',save_file)
    main_application.bind('<Control-Alt-s>',save_as)
    main_application.bind('<Control-q>',exit_func)
    main_application.bind('<Control-f>',find_func)

    main_application.mainloop()

exp=' '
def calculator():
    
   root = Toplevel()    
   root.title("Scientific Calculator")
   root.iconbitmap('calulator_logo.ico')
   root.configure(background = 'white')
   root.resizable(width=False, height=False)
   root.geometry("480x568+450+90") 

   calc = Frame(root)
   calc.grid()
   class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
      
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
    
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)
   
   added_value = Calc()
   
   txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),bg='black',fg='white', bd=30,width=28,justify=RIGHT)
   txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
   txtDisplay.insert(0,"0")
   
   # Here is the code for NUMBER PAD in Calculator.

   numberpad = "789456123"
   i=0
   btn = []
   for j in range(2,5):
      for k in range(3):
         btn.append(Button(calc, width=6, height=2, bg='white',fg='black', font=('Helvetica',20,'bold'),bd=4,text=numberpad[i]))
         btn[i].grid(row=j, column= k, pady = 1)
         btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
         i+=1
   
   # Here is the code for Button of Standard Calulator.   

   btnClear = Button(calc, text=chr(67),width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4, command=added_value.Clear_Entry).grid(row=1, column= 0, pady = 1)

   btnAllClear = Button(calc, text=chr(67)+chr(69),width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=added_value.All_Clear_Entry).grid(row=1, column= 1, pady = 1)

   btnsq = Button(calc, text="\u221A",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=added_value.squared).grid(row=1, column= 2, pady = 1)

   btnAdd = Button(calc, text="+",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.operation("add")).grid(row=1, column= 3, pady = 1)

   btnSub = Button(calc, text="-",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.operation("sub")).grid(row=2, column= 3, pady = 1)

   btnMul = Button(calc, text="x",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.operation("multi")).grid(row=3, column= 3, pady = 1)

   btnDiv = Button(calc, text="/",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.operation("divide")).grid(row=4, column= 3, pady = 1)

   btnZero = Button(calc, text="0",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.numberEnter(0)).grid(row=5, column= 0, pady = 1)

   btnDot = Button(calc, text=".",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.numberEnter(".")).grid(row=5, column= 1, pady = 1)
   
   btnPM = Button(calc, text=chr(177),width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=added_value.mathPM).grid(row=5, column= 2, pady = 1)

   btnEquals = Button(calc, text="=",width=6, height=2,bg='black',fg='white', font=('Helvetica',20,'bold'),bd=4,command=added_value.sum_of_total).grid(row=5, column= 3, pady = 1)
   
   # Here is the code for Buttons of Scientific Calulator.
   # ROW 1 :

   btnPi = Button(calc, text="pi",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.pi).grid(row=1, column= 4, pady = 1)

   btnCos = Button(calc, text="Cos",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.cos).grid(row=1, column= 5, pady = 1)

   btntan = Button(calc, text="tan",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),   
                  bd=4,command=added_value.tan).grid(row=1, column= 6, pady = 1)

   btnsin = Button(calc, text="sin",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.sin).grid(row=1, column= 7, pady = 1)

  # ROW 2 :

   btn2Pi = Button(calc, text="2pi",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.tau).grid(row=2, column= 4, pady = 1)

   btnCosh = Button(calc, text="Cosh",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.cosh).grid(row=2, column= 5, pady = 1)

   btntanh = Button(calc, text="tanh",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.tanh).grid(row=2, column= 6, pady = 1)

   btnsinh = Button(calc, text="sinh",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.sinh).grid(row=2, column= 7, pady = 1)

   
   # ROW 3 :

   btnlog = Button(calc, text="log",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log).grid(row=3, column= 4, pady = 1)

   btnExp = Button(calc, text="exp",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.exp).grid(row=3, column= 5, pady = 1)

   btnMod = Button(calc, text="Mod",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=lambda:added_value.operation("mod")
                ).grid(row=3, column= 6, pady = 1)

   btnE = Button(calc, text="e",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.e).grid(row=3, column= 7, pady = 1)


   # ROW 4 :

   btnlog10 = Button(calc, text="log10",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold')
                  ,bd=4,command=added_value.log10).grid(row=4, column= 4, pady = 1)

   btncos = Button(calc, text="log1p",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log1p).grid(row=4, column= 5, pady = 1)

   btnexpm1 = Button(calc, text="expm1",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold')
                  ,bd=4,command=added_value.expm1).grid(row=4, column= 6, pady = 1)

   btngamma = Button(calc, text="gamma",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold')
                  ,bd=4,command=added_value.lgamma).grid(row=4, column= 7, pady = 1)



   # ROW 5 :

   btnlog2 = Button(calc, text="log2",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log2).grid(row=5, column= 4, pady = 1)

   btndeg = Button(calc, text="deg",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.degrees).grid(row=5, column= 5, pady = 1)

   btnacosh = Button(calc, text="acosh",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.acosh).grid(row=5, column= 6, pady = 1)

   btnasinh = Button(calc, text="asinh",width=6, height=2,bg='white',fg='black', font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.asinh).grid(row=5, column= 7, pady = 1)

   lblDisplay = Label(calc, text = "Scientific Calculator",font=('Helvetica',30,'bold'),
                   bg='black',fg='white',justify=CENTER)
   lblDisplay.grid(row=0, column= 4,columnspan=4)


   # Here are the fucntions for ManuBar.

   def iExit():
     iExit = tkinter.messagebox.askyesno("Scientific Calculator","Do you want to exit ?")
     if iExit>0:
        root.destroy()
        return

   def Scientific():
      root.resizable(width=False, height=False)
      root.geometry("944x568+0+0")


   def Standard():
      root.resizable(width=False, height=False)
      root.geometry("480x568+0+0")



   menubar = Menu(calc)

   # ManuBar 1 :

   filemenu = Menu(menubar, tearoff = 0)
   menubar.add_cascade(label = 'File', menu = filemenu)
   filemenu.add_command(label = "Standard", command = Standard)
   filemenu.add_command(label = "Scientific", command = Scientific)
   filemenu.add_separator()
   filemenu.add_command(label = "Exit", command = iExit)

   # ManuBar 2 :

   editmenu = Menu(menubar, tearoff = 0)
   menubar.add_cascade(label = 'Edit', menu = editmenu)
   editmenu.add_command(label = "Cut")
   editmenu.add_command(label = "Copy")
   editmenu.add_separator()
   editmenu.add_command(label = "Paste")

   root.config(menu=menubar)


def wiki():
    wiki_home=tk.Toplevel(main_ui)
    wiki_home.title('Summary Finder')
    wiki_home.iconbitmap('wikipedia_logo.ico')
    wiki_home.geometry('854x480')
    wiki_home.resizable(0,0)

    # Icons
    head_icon=tk.PhotoImage(file='wiki_icon.png')
    search_icon=tk.PhotoImage(file='search_icon.png')
    search_btn_icon=tk.PhotoImage(file='search_btn.png')
    ##icons end...........

    #label
    main_label=ttk.Label(wiki_home,text='Summary Finder',font=('Colonna MT',19,'bold'))
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




#Frame-1

F1_P1=tk.PhotoImage(file='sk.png')
Frame1=tk.LabelFrame(main_ui,bg='black',padx=15, pady=15)
Frame1.grid(rowspan=3,column=1,ipady=214,ipadx=5,sticky=tk.N)

#labels

F1_L1=tk.Label(Frame1,image=F1_P1,bg='black')
F1_L1.grid(rowspan=1,column=0,padx=30,pady=10)

F1_L2=tk.Label(Frame1,text='Student Needs',fg='white',bg='black',font=('Times New Roman',35,'bold'))
F1_L2.grid(row=1,columnspan=2, pady=10)

web_button_img=tk.PhotoImage(file="Web.png")
web_button =tk.Button(Frame1,image=web_button_img,highlightthickness=0,bd=0,cursor='hand2', background="black")
web_button.grid(row=3,column=0,pady=160)


#Frame-1 end...............



#Frame-2
F2_P1=tk.PhotoImage(file='app_icon.png')
Frame2=tk.LabelFrame(main_ui, padx=15, pady=15)
Frame2.grid(row=0,column=3,sticky=tk.N, ipadx=268,ipady=214)


F2_L1=tk.Label(Frame2,image=F2_P1,font=('Colonna MT',30,'bold'))
F2_L1.grid(row=0,column=0)

F2_L2=tk.Label(Frame2,text='Applications',font=('Colonna MT',30,'bold'))
F2_L2.grid(row=1,column=0,padx=120)

  

# buttons
B1_P1=tk.PhotoImage(file='dic_btn.png')
B2_P2=tk.PhotoImage(file='study.png')
B3_P3=tk.PhotoImage(file='Notepad.png')
B4_P4=tk.PhotoImage(file='math_btn.png')
B5_P5=tk.PhotoImage(file='website.png')
B6_P6=tk.PhotoImage(file='cal_btn.png')
B7_P7=tk.PhotoImage(file='book.png')

# buttons
B1=tk.Button(Frame2,image=B1_P1,highlightthickness=0,bd=0,cursor='hand2',command=Dictionary)
B1.grid(row=2,column=0,sticky=tk.W,pady=20)

B2=tk.Button(Frame2,image=B2_P2,highlightthickness=0,bd=0,cursor='hand2',command=study_material)
B2.grid(row=2,column=0,padx=30)


B3=tk.Button(Frame2,image=B3_P3,highlightthickness=0,bd=0,cursor='hand2',command=Notepad)
B3.grid(row=2,column=0,sticky=tk.E)

B4=tk.Button(Frame2,image=B4_P4,highlightthickness=0,bd=0,cursor='hand2',command=wiki)
B4.grid(row=3,column=0,sticky=tk.W,pady=15)

# B4=tk.Button(Frame2,image=B4_P4,highlightthickness=0,bd=0,cursor='hand2',command=wiki)
# B4.grid(row=4,column=0,sticky=tk.W,pady=15)

B5=tk.Button(Frame2,image=B5_P5,highlightthickness=0,bd=0,cursor='hand2',command=web_site)
B5.grid(row=3,column=0)

B5=tk.Button(Frame2,image=B7_P7,highlightthickness=0,bd=0,cursor='hand2',command=web_site)
B5.grid(row=4,column=0)

B6=tk.Button(Frame2,image=B6_P6,highlightthickness=0,bd=0,cursor='hand2',command=calculator)
B6.grid(row=3,column=0,sticky=tk.E)

# B6=tk.Button(Frame2,image=B6_P6,highlightthickness=0,bd=0,cursor='hand2',command=calculator)
# B6.grid(row=4,column=0,sticky=tk.E)
#Frame-2 end...............


main_ui.mainloop()