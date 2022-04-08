from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql 

class Student():

    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")
        title =Label(self.root,text = 'Student Management Systems',bd=9,relief=GROOVE, font=("times new roman",50,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #########All Variable##########
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()





        #########MANAGEFRAME##########
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=585)

        m_title = Label(Manage_Frame,text="Manage Student",bg="yellow",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=1,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Roll No", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=2, column=0, pady=1, padx=1,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_Roll.grid(row=2,column=1, pady=10, padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=3, column=0, pady=1, padx=1, sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_name.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email ID", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=4, column=0, pady=1, padx=1, sticky="w")
        txt_email = Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_email.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="GENDER", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=5, column=0, pady=1, padx=1, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']= ("male","female","others")
        combo_gender.grid(row=5,column=1,padx=20,pady=10,sticky='w')

        lbl_contact = Label(Manage_Frame, text="Contact ", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=6, column=0, pady=1, padx=1, sticky="w")
        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="DOB", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=7, column=0, pady=1, padx=1, sticky="w")
        txt_dob = Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_dob.grid(row=7, column=1, pady=10, padx=20, sticky="w")


        lbl_Address = Label(Manage_Frame,text='Address:',bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=8,column=0,pady=1,padx=1,sticky="w")
        self.txt_Address = Text(Manage_Frame,width=30,height=3,font=("times new roman",10,"bold"))
        self.txt_Address.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        #####Button Frame###########

        btn_frame = Frame(self.root, bd=3, relief=RIDGE, bg="black")
        btn_frame.place(x=30, y=620, width=420)

        Addbtn = Button(btn_frame,text="ADD",width=10,command=self.add_students).grid(row=12,column=0,padx=10,pady=10)

        updatebtn = Button(btn_frame,text="UPDATE",width=10,command=self.update_data).grid(row=12,column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame,text="DELETE",width=10,command=self.delete_data).grid(row=12,column=2,padx=10,pady=10)
        clearbtn = Button(btn_frame,text="CLEAR",width=10,command=self.clear).grid(row=12,column=3,padx=10,pady=10)

        #########DETAILFRAME##########
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg="blue", fg="white",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=1, column=0, pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(Details_Frame,textvariable=self.search_by,font=("times new roman", 13, "bold"),width=10, state='readonly')
        combo_search['values'] = ("roll_no","name","email")
        combo_search.grid(row=1, column=2, padx=1, pady=1, sticky='w')
        txt_search = Entry(Details_Frame,textvariable=self.search_txt,font=("times new roman", 10, "bold"),width =20,bd=5,relief=GROOVE)
        txt_search.grid(row=1, column=3, pady=10, padx=20, sticky="w")

        searchbtn = Button(Details_Frame, text="Search", width=10,command=self.search_data).grid(row=1, column=4, padx=10, pady=10)
        Showallbtn = Button(Details_Frame, text="Show All", width=10,command=self.fetch_data).grid(row=1, column=5, padx=10, pady=10)

        #########TABLEFRAME##########

        Table_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Table_Frame.place(x=550, y=170, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("roll","name", "email","gender","contact", "dob", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll NO")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email ID")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("Address",text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>" ,self.get_cursor)
        self.fetch_data()



    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" or self.txt_Address.get('1.0',END)=="":
            messagebox.showerror("Error","Please fill all the fields")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="sms1")
            cur = con.cursor()
            cur.execute("INSERT into students values (%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_Address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("SUCCESS","Result are successfull added to your database")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows :
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row =  contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[6])





    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)


    def update_data(self):

        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no =%s",(
                                                                           self.name_var.get(),
                                                                           self.email_var.get(),
                                                                           self.gender_var.get(),
                                                                           self.contact_var.get(),
                                                                           self.dob_var.get(),
                                                                           self.txt_Address.get('1.0', END),
                                                                           self.Roll_No_var.get()))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("SUCCESS", "Result are successfull added to your database")


    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        cur = con.cursor()
        cur.execute("select * from students where " + str(self.search_by.get()) +" Like '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()




class Student():
    pass
    root= Tk()
    obj=Student(root)
    root.mainloop()
