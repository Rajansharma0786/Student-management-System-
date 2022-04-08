from tkinter import *
from tkinter import ttk

class student():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")
        title =Label(self.root,text = 'Student Management System',bd=9,relief=GROOVE, font=("times new roman",50,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #########MANAGEFRAME##########
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=585)

        m_title = Label(Manage_Frame,text="Manage Student",bg="yellow",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=1,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Roll No", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=2, column=0, pady=1, padx=1,sticky="w")
        txt_Roll = Entry(Manage_Frame,font=("times new roman",15,"bold"),relief=GROOVE)
        txt_Roll.grid(row=2,column=1, pady=10, padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=3, column=0, pady=1, padx=1, sticky="w")
        txt_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_name.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email ID", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=4, column=0, pady=1, padx=1, sticky="w")
        txt_email = Entry(Manage_Frame, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_email.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="GENDER", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=5, column=0, pady=1, padx=1, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']= ("male","female","others")
        combo_gender.grid(row=5,column=1,padx=20,pady=10,sticky='w')

        lbl_contact = Label(Manage_Frame, text="Contact ", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=6, column=0, pady=1, padx=1, sticky="w")
        txt_contact = Entry(Manage_Frame, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="DOB", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=7, column=0, pady=1, padx=1, sticky="w")
        txt_dob = Entry(Manage_Frame, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_dob.grid(row=7, column=1, pady=10, padx=20, sticky="w")


        lbl_Address = Label(Manage_Frame,text='Address:',bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=8,column=0,pady=1,padx=1,sticky="w")
        self.txt_Address = Text(Manage_Frame,width=30,height=3,font=("times new roman",10,"bold"))
        self.txt_Address.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        #####ButtonFrame###########

        btn_frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="black")
        btn_frame.place(x=15, y=525, width=420)

        Addbtn = Button(btn_frame,text="ADD",width=10).grid(row=0,column=0,padx=10,pady=10)

        updatebtn = Button(btn_frame,text="UPDATE",width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame,text="DELETE",width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn = Button(btn_frame,text="CLEAR",width=10).grid(row=0,column=3,padx=10,pady=10)

        #########DETAILFRAME##########
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg="blue", fg="white",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=1, column=0, pady=10,padx=20,sticky="w")

        







class student():
    pass
    root= Tk()
    obj=student(root)
    root.mainloop()
