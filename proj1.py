from tkinter import *


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
        ID_Entery = Entry(Manage_Frame,bd=2)
        ID_Entery.pack()
        lb1_Name = Label(Manage_Frame,text='اسم الطالب',bg='white')
        lb1_Name.pack()









root = Tk()
ob = Student(root)
root.mainloop()