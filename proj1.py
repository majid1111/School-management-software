from tkinter import *
from tkinter import ttk
import tkinter  as tk

class Student:
    # -------------- انشاء نافذة الرنامج ---------------------
    def __init__(self, root): 
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('برنامج اداره المدارس ')
        self.root.configure(background='silver')
        self.root.resizable(False,False)
        title = Label(self.root,
           text = '[نظام تسجيل الطلاب]'  ,         
           bg = '#1AAECB' ,
           font = ('monospace',14,'bold'),
           fg = 'WHITE'          
                      )
        title.pack(fill=X)
        #--------------  variable  -----------

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.moahel_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.del_var = StringVar
        self.search_var = StringVar()





#-----------------ادوات التحكم بالبرنامج-------------
        Manage_Frame = Frame(self.root,bg='white')
        Manage_Frame.place(x=1137,y=30,width=210,height=400)
        lb1_ID = Label(Manage_Frame,text='الرقم التسلسلي',bg='white')
        lb1_ID.pack()
        ID_Entery = Entry(Manage_Frame,textvariable=self.id_var,bd=2,justify='center')
        ID_Entery.pack()
        lb1_Name = Label(Manage_Frame,text='اسم الطالب',bg='white')
        lb1_Name.pack()
        Name_Entery = Entry(Manage_Frame,textvariable= self.name_var,bd=2,justify='center')
        Name_Entery.pack()
        lb1_email = Label(Manage_Frame,text='ايميل الطالب',bg='white')
        lb1_email.pack()
        email_Entery = Entry(Manage_Frame,textvariable=self.email_var,bd=2,justify='center')
        email_Entery.pack()
        lb1_phone = Label(Manage_Frame,text='هاتف الطالب',bg='white')
        lb1_phone.pack()
        phone_Entery = Entry(Manage_Frame,textvariable=self.phone_var,bd=2,justify='center')
        phone_Entery.pack()
        lb1_certi = Label(Manage_Frame,text='موهلات الطالب',bg='white')
        lb1_certi.pack()
        certi_Entery = Entry(Manage_Frame,textvariable=self.moahel_var,bd=2,justify='center')
        certi_Entery.pack()
        lbl_gender = Label(Manage_Frame,text='جنس الطالب',bg='white')
        lbl_gender.pack()
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var)
        combo_gender['value']=('ذكر','انثى')
        combo_gender.pack()

        lb1_address = Label(Manage_Frame,text='عنوان الطالب',bg='white')
        lb1_address.pack()
        address_Entery = Entry(Manage_Frame,textvariable= self.address_var,bd=2,justify='center')
        address_Entery.pack()
        
        lb1_delete = Label(Manage_Frame,text='حذف طالب بالاسم ',bg='white',fg='red')
        lb1_delete.pack()
        delete_Entery = Entry(Manage_Frame,textvariable= self.del_var,bd=2,justify='center')
        delete_Entery.pack()

#----------- الازرار buttons-------------
        btn_Frame = Frame(self.root,bg='white')
        btn_Frame.place(x=1137,y=435,width=210,height=250)
        title1 =Label(btn_Frame, text = 'لوحة التحكم',font=('Deco',14),fg='white',bg='#2980B9')
        title1.pack(fill=X)

        add_btn = Button(btn_Frame, text = 'اضافةطالب' , bg='#0000FF')
        add_btn.place(x=33,y=33,width=150,height=30)

        del_btn = Button(btn_Frame, text = 'حذف طالب' , bg='red')
        del_btn.place(x=33,y=65,width=150,height=30)

        update_btn = Button(btn_Frame, text = 'تعديل بيانات طالب',bg='red')
        update_btn.place(x=33,y=97,width=150,height=30)

        clear_btn = Button(btn_Frame, text = 'افراغ الحقول' , bg='blue')
        clear_btn.place(x=33,y=129,width=150,height=30)

        about_btn = Button(btn_Frame, text='من نحن', bg='red')
        about_btn.place(x=33,y=161,width=150,height=30)
 
        extie_btn = Button(btn_Frame, text = 'اغلاق البرنامج',bg='black')
        extie_btn.place(x=33,y=193,width=150,height=30)


       #-------search manage البحث----------------
        search_Frame = Frame(self.root,bg='white') 
        search_Frame.place(x=1,y=30,width=1134,height=50)

        lb1_search = Label(search_Frame,text='البحث عن طالب',bg='white')
        lb1_search.place(x=1034,y=12)
         
        combo_search = ttk.Combobox(search_Frame,justify='right')
        combo_search['value']=('id','name','email','phone')
        combo_search.place(x=880,y=12)

        search_Entery = Entry(search_Frame,textvariable=self.search_var,justify='right',bd=2)
        search_Entery.place(x=680,y=12)


        se_btn = Button(search_Frame, text = 'بحث' , bg='green',fg='blue')
        se_btn.place(x=620,y=12,width=60,height=30)
        #------- detals عرض النتائج والبيانات---------
        Detals_Frame = Frame(self.root,bg='#F2F4F4')
        Detals_Frame.place(x=1,y=82,width=1134,height=605)
           #---scroll---
        scroll_x= Scrollbar(Detals_Frame,orient=HORIZONTAL)
        scroll_y =Scrollbar(Detals_Frame,orient=VERTICAL)
         
          #-----treeveiw------
        self.studen_table= ttk.Treeview(Detals_Frame,
           columns=('address','gender','certi','phone','email','name','id') ,                            
           xscrollcommand= scroll_x.set,
           yscrollcommand=scroll_y.set) 
        
        self.studen_table.place(x=18,y=1,width=1130,height=587)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.studen_table.xview)
        scroll_y.config(command=self.studen_table.yview)

        self.studen_table['show']='headings'
        self.studen_table.heading('address',text='عنوان الطالب')
        self.studen_table.heading('gender',text='جنس الطالب')
        self.studen_table.heading('certi',text='مؤهلات الطالب')
        self.studen_table.heading('phone',text='هاتف الطالب')
        self.studen_table.heading('email',text='البريد الالكتروني')
        self.studen_table.heading('name',text='اسم الطالب')
        self.studen_table.heading('id',text='الرقم التسلسلي')

        self.studen_table.column('address',width=125)
        self.studen_table.column('gender',width=30)
        self.studen_table.column('certi',width=65)
        self.studen_table.column('phone',width=65)
        self.studen_table.column('email',width=70)
        self.studen_table.column('name',width=100)
        self.studen_table.column('id',width=14)







root = Tk()
ob = Student(root)
root.mainloop()