from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
import cv2,os
from student import Student
from train import Train
from face_recognition import Face_Recognition

class Face_Recognization_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

       #first img
        img=Image.open(r"C:\FaceRecognizationSystem\Images\imgbackgro.jfif")
        img=img.resize((500,130),Image.ANTIALIAS)             #ANTIALIAS convert high lvl img to low lvl
        self.photoimg=ImageTk.PhotoImage(img)

        frst_lbl=Label(self.root,image=self.photoimg)
        frst_lbl.place(x=0,y=0,width=500,height=130)


        #second img
        img1=Image.open(r"C:\FaceRecognizationSystem\Images\grpimg.jfif")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        

        frst_lbl=Label(self.root,image=self.photoimg1)
        frst_lbl.place(x=500,y=0,width=500,height=130)


        #third img
        img2=Image.open(r"C:\FaceRecognizationSystem\Images\backimge.jfif")
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
        title_lbl=Label(bg_img,text="Face Recognization Attendence System",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student button
        img4=Image.open(r"C:\FaceRecognizationSystem\Images\studentinfo.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=280,width=200,height=40)


        #detect face button
        img5=Image.open(r"C:\FaceRecognizationSystem\Images\faceDetectorimg.jfif")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=200,height=200)
        
        b1_1=Button(bg_img,text="Face Dectetor",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=280,width=200,height=40)

        
        #Attendence button
        img6=Image.open(r"C:\FaceRecognizationSystem\Images\attendenceimg.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=200,height=200)
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=280,width=200,height=40)


         
        #help button
        img7=Image.open(r"C:\FaceRecognizationSystem\Images\helppp.jfif")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=200,height=200)
        
        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=280,width=200,height=40)


        #train button
        img8=Image.open(r"C:\FaceRecognizationSystem\Images\trainingdata.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=370,width=200,height=200)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=550,width=200,height=40)

        #Photos face button
        img9=Image.open(r"C:\FaceRecognizationSystem\Images\boyimg.jfif")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=370,width=200,height=200)
        
        b1_1=Button(bg_img,text="Faces",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=550,width=200,height=40)

        #Developer button
        img10=Image.open(r"C:\FaceRecognizationSystem\Images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=370,width=200,height=200)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=550,width=200,height=40)

        #Exit button
        img11=Image.open(r"C:\FaceRecognizationSystem\Images\exite.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=370,width=200,height=200)
        
        b1_1=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=550,width=200,height=40)




    def open_img(self):
        os.startfile("data")


    #------------CLcIK ON IMAGE FUNCTION BUTTON-----------------------------------

    def student_details(self):
          self.new_window=Toplevel(self.root)
          self.app=Student(self.new_window)

    def train_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Train(self.new_window)

    def face_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Face_Recognition(self.new_window)





            

    

        





if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognization_System(root)
    root.mainloop()