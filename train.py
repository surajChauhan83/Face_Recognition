from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2, os
import csv
import numpy as np



class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")



        title_top=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_top.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"Images\trainimag.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)


        top_lbl=Label(self.root,image=self.photoimg_top)
        top_lbl.place(x=0,y=45,width=1530,height=325)

        #button---------------------
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=0,y=370,width=1530,height=50)
        

        
        img_bottom=Image.open(r"Images\morefacess.jpeg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)


        bottom_lbl=Label(self.root,image=self.photoimg_bottom)
        bottom_lbl.place(x=0,y=420,width=1530,height=350)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Convert in Gray scale image
            imageNp=np.array(img,'uint8')  # 'uint8'--data type in array
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
         #---------------------------Train the Classifier and Save-----------------------------------------------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!")








if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()