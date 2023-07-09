from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2, os
import csv
import sys
 

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        #----------------------create variables-----------------------------------------------------
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stud_id=StringVar()
        self.var_stud_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_addres=StringVar()
        self.var_teacher=StringVar()  

        
       #first img
        img=Image.open(r"C:\FaceRecognizationSystem\Images\studentimgeeee.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        frst_lbl=Label(self.root,image=self.photoimg)
        frst_lbl.place(x=0,y=0,width=500,height=130)


        
        #second img
        img1=Image.open(r"C:\FaceRecognizationSystem\Images\studentgroup.jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        frst_lbl=Label(self.root,image=self.photoimg1)
        frst_lbl.place(x=500,y=0,width=500,height=130)


        #third img
        img2=Image.open(r"C:\FaceRecognizationSystem\Images\studentgrp.jfif")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        frst_lbl=Label(self.root,image=self.photoimg2)
        frst_lbl.place(x=1000,y=0,width=550,height=130)


        
        #background img
        img3=Image.open(r"C:\FaceRecognizationSystem\Images\trainedata.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title label
        title_lbl=Label(bg_img,text="Student Managment System",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=650)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=0,width=705,height=600)


        img_left=Image.open(r"C:\FaceRecognizationSystem\Images\studentstudy.jfif")
        img_left=img_left.resize((680,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)


        frst_lbl=Label(self.root,image=self.photoimg_left)
        frst_lbl.place(x=30,y=220,width=680,height=120)


        #current course information  
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),)
        current_course_frame.place(x=5,y=135,width=685,height=120)


        # Department
        dep_label=Label(current_course_frame,text="Department",bg="white",font=("times new roman",12,"bold") )
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department   --","CSE","IT","Civil","Mechanical","Chemical","Electronics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # course
        course_label=Label(current_course_frame,text="Course",bg="white",font=("times new roman",12,"bold") )
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course   --","BE/Btech.","Polythecnic","M.tech","TE","FE","SE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_label=Label(current_course_frame,text="Year",bg="white",font=("times new roman",12,"bold") )
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year   --","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        sem_label=Label(current_course_frame,text="Semester",bg="white",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Semester   --","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)





        #class studetn information   
        class_stud_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_stud_frame.place(x=5,y=260,width=685,height=310)

        # student id
        student_Id=Label(class_stud_frame,text="StudentID:",bg="white",font=("times new roman",11,"bold") )
        student_Id.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_stud_frame,textvariable=self.var_stud_id,width=20,font=("times new roman",11,"bold") )
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_name=Label(class_stud_frame,text="Student Name:",bg="white",font=("times new roman",11,"bold") )
        student_name.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_stud_frame,textvariable=self.var_stud_name,width=20,font=("times new roman",11,"bold") )
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class Division
        division=Label(class_stud_frame,text="Section :",bg="white",font=("times new roman",11,"bold") )
        division.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_stud_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo["values"]=("Select Section   --","0","1","2","3","4")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        #roll no
        rollNo_label=Label(class_stud_frame,text="Roll No:",bg="white",font=("times new roman",11,"bold") )
        rollNo_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollNo_entry=ttk.Entry(class_stud_frame,textvariable=self.var_roll,width=20,font=("times new roman",11,"bold") )
        rollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender=Label(class_stud_frame,text="Gender :",bg="white",font=("times new roman",11,"bold") )
        gender.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gen_combo=ttk.Combobox(class_stud_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gen_combo["values"]=("Select Gender   --","Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob
        dob_label=Label(class_stud_frame,text="DOB:",bg="white",font=("times new roman",11,"bold") )
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_stud_frame,textvariable=self.var_dob,width=20,font=("times new roman",11,"bold") )
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label=Label(class_stud_frame,text="E-mail:",bg="white",font=("times new roman",11,"bold") )
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_stud_frame,textvariable=self.var_email,width=20,font=("times new roman",11,"bold") )
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no.
        phone_label=Label(class_stud_frame,text="Mobile No:",bg="white",font=("times new roman",11,"bold") )
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_stud_frame,textvariable=self.var_phone,width=20,font=("times new roman",11,"bold") )
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label=Label(class_stud_frame,text="Address:",bg="white",font=("times new roman",11,"bold") )
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_stud_frame,textvariable=self.var_addres,width=20,font=("times new roman",11,"bold") )
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher no.
        teacher_label=Label(class_stud_frame,text="Teacher Name:",bg="white",font=("times new roman",11,"bold") )
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_stud_frame,textvariable=self.var_teacher,width=20,font=("times new roman",11,"bold") )
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio button--
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_stud_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)


        #button frame  
        button_frame=LabelFrame(class_stud_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=5,y=210,width=670,height=35)

        #delete button
        delete_btn=Button(button_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=0,)

        #save button
        save_btn=Button(button_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=1,)

        #reset button
        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=2,)

        #update button
        update_btn=Button(button_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="orange",fg="white")
        update_btn.grid(row=0,column=3,)


        #button frame 1
        button_frame1=LabelFrame(class_stud_frame,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=5,y=245,width=670,height=35)

        #take button
        take_photo_btn=Button(button_frame1,command=self.genrate_dataset,text="Take Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,)

        #update button
        update_photo_btn=Button(button_frame1,text="Update Photo Sample",width=33,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,)



        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=720,y=0,width=765,height=600)

        img_right=Image.open(r"C:\FaceRecognizationSystem\Images\studentwo.jfif")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_label=Label(Right_frame,image=self.photoimg_right)
        f_label.place(x=5,y=0,width=720,height=130)


        #----------Search Frame----

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Data:",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=750,height=70)

        search_label=Label(search_frame,text="Search By:",bg="red",fg="white",font=("times new roman",11,"bold") )
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select Year   --","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="orange",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        show_all_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="orange",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4)

        
        #----table frame--
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=750,height=360)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year/Batch")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Mob No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=130)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=110)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=110)
        self.student_table.column("address",width=120)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=110)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    #------------------------------FUNCTION DECLARATION FOR ENTRY FIELD-----------------------------------------

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stud_name.get()=="" or self.var_stud_id.get()=="":
            messagebox.showerror("Error","All Fields are required!!",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="suraj@24",database="face_recognizer")
                my_cursor=con.cursor()
                my_cursor.execute("INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                                 self.var_dep.get(),
                                                                                                                 self.var_course.get(),
                                                                                                                 self.var_year.get(),
                                                                                                                 self.var_sem.get(),
                                                                                                                 self.var_stud_id.get(),
                                                                                                                 self.var_stud_name.get(),
                                                                                                                 self.var_div.get(),
                                                                                                                 self.var_roll.get(),
                                                                                                                 self.var_gender.get(),
                                                                                                                 self.var_dob.get(),
                                                                                                                 self.var_email.get(),
                                                                                                                 self.var_phone.get(),
                                                                                                                 self.var_addres.get(),
                                                                                                                 self.var_teacher.get(), 
                                                                                                                 self.var_radio1.get()                                             
                                                                                                                                                   
                                                                                                                                    ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","Student Detail has been added Succesfully!!",parent=self.root)                                                                                                                   
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
 
    #---------------------------fetch data---------------------------------------------------------------------------------

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",username="root",password="suraj@24",database="face_recognizer")
        my_cursor=con.cursor()
        my_cursor.execute("SELECT  * FROM student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            con.commit()
        con.close()

    #----------------------Get Cursor-------------------------------------------------------------------------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stud_id.set(data[4]),
        self.var_stud_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_addres.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #------update function on clk button----------------------------------------------------------------------
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stud_name.get()=="" or self.var_stud_id.get()=="":
            messagebox.showerror("Error","All Fields are required!!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detail!!",parent=self.root)
                if Update>0:
                    con=mysql.connector.connect(host="localhost",username="root",password="suraj@24",database="face_recognizer")
                    my_cursor=con.cursor()
                    my_cursor.execute("UPDATE student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_Id=%s",(
                                              
                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                 self.var_year.get(),
                                                                                                                                                                 self.var_sem.get(),
                                                                                                                                                                 self.var_stud_name.get(),
                                                                                                                                                                 self.var_div.get(),
                                                                                                                                                                 self.var_roll.get(),
                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                 self.var_addres.get(),
                                                                                                                                                                 self.var_teacher.get(),
                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                 self.var_stud_id.get()
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                             ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","student details successfully update completed!!",parent=self.root) 
                con.commit()
                self.fetch_data()
                con.close()                                                                                                                                            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #--------------------Delete Function--------------------------------------------------------------------
    def delete_data(self):
        if self.var_stud_id.get()=="":
            messagebox.showerror("Error","Student Id must be required!!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this details!!",parent=self.root)
                if delete>0:
                    con=mysql.connector.connect(host="localhost",username="root",password="suraj@24",database="face_recognizer")
                    my_cursor=con.cursor()
                    sql="DELETE from student where Student_Id=%s"
                    val=(self.var_stud_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                con.commit()
                self.fetch_data()
                con.close()  
                messagebox.showinfo("Delete","Successfully Deleted Student Details!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    
    #-------------------------Reset--------------------------------------------------------------------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stud_id.set("")
        self.var_stud_name.set("")
        self.var_div.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_addres.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    #=======================Generate data set take a photo sample===================================================
    def genrate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stud_name.get()=="" or self.var_stud_id.get()=="":
            messagebox.showerror("Error","All Fields are required!!",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="suraj@24",database="face_recognizer")
                my_cursor=con.cursor()
                my_cursor.execute("SELECT * FROM student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1

                my_cursor.execute("UPDATE student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_Id=%s",(
                                              
                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                 self.var_year.get(),
                                                                                                                                                                 self.var_sem.get(),
                                                                                                                                                                 self.var_stud_name.get(),
                                                                                                                                                                 self.var_div.get(),
                                                                                                                                                                 self.var_roll.get(),
                                                                                                                                                                 self.var_gender.get(),
                                                                                                                                                                 self.var_dob.get(),
                                                                                                                                                                 self.var_email.get(),
                                                                                                                                                                 self.var_phone.get(),
                                                                                                                                                                 self.var_addres.get(),
                                                                                                                                                                 self.var_teacher.get(),
                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                 self.var_stud_id.get() 
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                             ))

                con.commit()
                self.fetch_data()
                self.reset_data()
                con.close()

                #---------------------------Load predefined data on face frontals from opencv-------------------------------------------------------------
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crooped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3     min neighbour=5

                    for (x,y,w,h) in faces:
                        face_crooped=img[y:y+h,x:x+w]
                        return face_crooped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_crooped(my_frame) is not None:
                        img_id += 1
                        face=cv2.resize(face_crooped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+'.jpg'
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break 
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genrating data sets completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                    
                                                                                                                                                            
     
     

    

         
            



if __name__ == "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()