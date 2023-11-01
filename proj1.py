from tkinter import *
from tkinter import ttk

class Student:
    # -------------- انشاء نافذة الرنامج ---------------------
    def __init__(self, root): 
        self.root =root
        self.root.geometry('1350x690+1+1')
        self.root.title('برنامج اداره المدارس ')
        self.root.configure(background='silver')
        self.root.resizable(False,True)
        title = Label(self.root,
           text = '[نظام تسجيل الطلاب]'  ,         
           bg = '#1AAECB' ,
           font = ('monospace',14,'bold'),
           fg = 'WHITE'          
                      )
        title.pack(fill=X)
#-----------------ادوات التحكم بالبرنامج-------------
        Manage_Frame = Frame(self.root,bg='white')
        Manage_Frame.place(x=1137,y=30,width=210,height=400)
        lb1_ID = Label(Manage_Frame,text='الرقم التسلسلي',bg='white')
        lb1_ID.pack()
        ID_Entery = Entry(Manage_Frame,bd=2,justify='center')
        ID_Entery.pack()
        lb1_Name = Label(Manage_Frame,text='اسم الطالب',bg='white')
        lb1_Name.pack()
        Name_Entery = Entry(Manage_Frame,bd=2,justify='center')
        Name_Entery.pack()
        lb1_email = Label(Manage_Frame,text='ايميل الطالب',bg='white')
        lb1_email.pack()
        email_Entery = Entry(Manage_Frame,bd=2,justify='center')
        email_Entery.pack()
        lb1_phone = Label(Manage_Frame,text='هاتف الطالب',bg='white')
        lb1_phone.pack()
        phone_Entery = Entry(Manage_Frame,bd=2,justify='center')
        phone_Entery.pack()
        lb1_certi = Label(Manage_Frame,text='موهلات الطالب',bg='white')
        lb1_certi.pack()
        certi_Entery = Entry(Manage_Frame,bd=2,justify='center')
        certi_Entery.pack()
        lbl_gender = Label(Manage_Frame,text='جنس الطالب',bg='white')
        lbl_gender.pack()
        combo_gender = ttk.Combobox(Manage_Frame)
        combo_gender['value']=('ذكر','انثى')
        combo_gender.pack()

        lb1_address = Label(Manage_Frame,text='عنوان الطالب',bg='white')
        lb1_address.pack()
        address_Entery = Entry(Manage_Frame,bd=2,justify='center')
        address_Entery.pack()
        
        lb1_delete = Label(Manage_Frame,text='حذف طالب بالاسم ',bg='white',fg='red')
        lb1_delete.pack()
        delete_Entery = Entry(Manage_Frame,bd=2,justify='center')
        delete_Entery.pack()






root = Tk()
ob = Student(root)
root.mainloop()