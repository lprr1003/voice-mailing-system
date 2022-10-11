from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector as m
import smtplib as s
import speech_recognition as sr

def screen1():
          def CLOSE():
                    window.destroy()
                    screen2()
          window=Tk()
          window.title("Project: Screen 1")
          window.geometry('700x500')
          window.resizable(False,False)
          load=Image.open("D:\propics\mail.webp") #'C:/Users/i am rock/Desktop/Jeet School/dps.jpg'
          render=ImageTk.PhotoImage(load)
          img=Label(window,image=render)    #3 label 1 button
          img.place(x=0,y=0,height=500,width=700)
          l=Label(img,text="Voice Based Mailing System",fg="#3658BE" ,font=("Comic Sans MS",25,'bold')).place(x=130,y=30)
          l1=Label(img,text="Submitted By\n Sakshi Sharma(ECE),Parul(CSE)\n Sakshi(CSE),Preeti(CSE)",font=("Comic Sans MS",12,'bold')).place(relx=0.0,rely=1.0,anchor=SW)
          l2=Label(img,text="Under Guidance of\n Mr. Saurav Ghosh",font=("Comic Sans MS",12,'bold')).place(relx=1.0,rely=1.0,anchor=SE)
          b=Button(img,text='Click To Continue',bg='lightgrey',font=('Comic Sans MS',15,'italic'),command=CLOSE).place(relx=0.5,rely=0.5,anchor='center')
          window.mainloop()
def screen2():
          window=Tk()
          window.title("Project: Screen 2")
          window.geometry('600x400')
          window.resizable(False,False)
        
          load=Image.open("D:\propics\mail.webp")
          render=ImageTk.PhotoImage(load)
          img=Label(window,image=render)
          img.place(x=0,y=0,height=400,width=600)
          l=Label(img,text="Login",fg="#3658BE",bg="white",font=("Comic Sans MS",25,'bold')).place(x=250,y=30)
          l1=Label(img,text="Username:",fg="#3658BE",bg="white",font=("Comic Sans MS",11,'bold')).place(x=180,y=100)
          s1=StringVar()
          e1=Entry(img,textvariable=s1,bg='white',fg='navy',font=("Comic Sans MS",15,'bold')).place(x=180,y=130)
          l2=Label(img,text="Password:",fg="#3658BE",bg="white",font=("Comic Sans MS",11,'bold')).place(x=180,y=200)
          s2=StringVar()
          e2=Entry(img,textvariable=s2,bg='white',fg='navy',font=("Comic Sans MS",15,'bold'),show='*').place(x=180,y=230)
          def EXIT():
                    window.destroy()
          def VERIFYLOGIN():
                    valid=False
                    username=s1.get()
                    password=s2.get()
                    cnx=m.connect(host="localhost",user="root",password="",database="project1")
                    cur=cnx.cursor()
                    cur.execute("select username,password from credentials where username='%s' and password='%s'"%(username,password))
                    for row in cur.fetchall():
                              valid=True
                    cur.close()
                    cnx.close()
                    if not valid:
                              messagebox.showerror(title="Login",message="Invalid Credentials")
                              s1.set("")
                              s2.set("")
                    else:
                              window.destroy()
                              screen3()
          b1=Button(img,text='Login',bg='green',font=('Comic Sans MS',15,'italic'),command=VERIFYLOGIN).place(x=357,y=300) #img
          b2=Button(img,text='Exit',bg='red',font=('Comic Sans MS',15,'italic'),command=EXIT).place(x=180,y=300)  #img
          window.mainloop()
def screen3():
          def Close1():  # ye close krne ke liye h mne back button add kiya h or kaam bhi kr rha h nhi nhi esa nhi h
              window.destroy()
              rscreen()
          def Close2():
              window.destroy() # han m bol rhi hu ki ye test.py ka koi kaam nhi h es project me
              sscreen()
          def Close3():
              window.destroy()
              cscreen()
          def Close4():
              window.destroy()



          window=Tk()
          window.title("Project: Screen 3")
          window.geometry('400x600')
          window.resizable(False,False)
          load=Image.open("D:\propics\mail.webp")
          render=ImageTk.PhotoImage(load)
          img=Label(window,image=render)
          img.place(x=0,y=0,height=600,width=400)
          l=Label(img,text="Main Menu",bg="white",fg="#3658BE",font=("Comic Sans MS",25,'bold')).place(x=110,y=20)
          b=Button(img,text='Register Email ID Shortnames',bg='lightgrey',font=('Comic Sans MS',15,'italic'),command=Close1).place(x=60,y=250)
          b1=Button(img,text='Send Mail',bg='lightgrey',font=('Comic Sans MS',15,'italic'),command=Close2).place(x=150,y=350)
          #b2=Button(img,text='Configure SMTP Settings',bg='lightgrey',font=('Comic Sans MS',15,'italic'),command=Close3).place(x=90,y=350)
          b3=Button(img,text='Log Out',bg='maroon',fg='white',font=('Comic Sans MS',15,'italic'),command=Close4).place(relx=0.95,rely=0.95,anchor=SE)
          window.mainloop()

def rscreen():
    def Close():
        root.destroy()
        screen3()

    root = Tk()
    root.title("Project: Reg.Screen")
    root.geometry('500x600')
    root.resizable(False,False)
     ## email register func



    load = Image.open("D:\propics\mail.webp")
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.place(x=0, y=0, height=600, width=500)
    l = Label(img,text="Register Email ID", bg="white", fg="black", font=("Comic Sans MS", 25, 'bold')).place(x=110, y=20)
    l1 = Label(img,text="Enter your email id : ", font=("Comic Sans MS", 13, 'bold')).place(x=40, y=200)
    s1 = StringVar()
    e1 = Entry(img,textvariable=s1, bg='white', fg='navy', font=("Comic Sans MS", 15, 'bold')).place(x=230, y=200)
    l2 = Label(img,text="User name : ",font=("Comic Sans MS",13,'bold')).place(x=40,y=260)
    s2 = StringVar()
    e2 = Entry(img,textvariable=s2,bg='white',fg='navy',font=("Comic Sans MS", 15, 'bold')).place(x=230, y=260)

    def email():
        cnx = m.connect(user="root", host="localhost", database="project1", password="")

        cursor = cnx.cursor()
        try:
            emailAddress = s1.get()
            name = s2.get()

            cursor.execute("insert into emails values('%s','%s')" % (name, emailAddress))
            cnx.commit()
        except:
            messagebox.showerror(title="ERROR",message="Something went wrong!!")
            s1.set("")
            s2.set("")
        else:
            messagebox.showinfo(title="INFO",message="Data Registered Successfully")
        finally:
            cursor.close()
            cnx.close()
            messagebox.showinfo(title="INFO",message="Thanks for registering.\nNow you can send mail..")

    b1 = Button(img,text="Register",bg='green',fg='white',font=("Comic Sans MS", 15, 'bold'),command=email).place(x=360, y=350)# cmd
    b2 = Button(img,text="Back",bg='orange',fg='white',font=("Comic Sans MS", 15, 'bold'),command=Close).place(x=280, y=350)
    root.mainloop()

def sscreen():
    def Close():
        root.destroy()
        screen3()


    root = Tk()
    root.title("Project: SendMailScreen")
    root.geometry("500x600")
    root.resizable(False,False)
    load = Image.open("D:\propics\mail.webp")  # 'C:/Users/i am rock/Desktop/Jeet School/dps.jpg'
    render=ImageTk.PhotoImage(load)
    img=Label(root,image=render)   # 3 label 1 button
    img.place(x=0,y=0,height=600,width=500)
    r1 = sr.Recognizer()
    l  = Label(img,text="Send Mail", bg="white", fg="black", font=("Comic Sans MS", 25, 'bold')).place(x=160,y=20)

    with sr.Microphone() as source1:
        print("Start speaking emial id")
        l1 = Label(img,text="Your Email Id : ", font=("Comic Sans MS", 12, 'bold')).place(x=45, y=200)
        audio1 = r1.listen(source1)

        print("Start speaking name of receiver") # newly added segment
        l6 = Label(img,text="Name of receiver : ",font=("Comic Sans MS", 12, 'bold')).place(x=45, y=300)
        audio6 = r1.listen(source1)

        print("Start speaking email id of receiver")
        l3 = Label(img,text="Email Id of receiver : ", font=("Comic Sans MS", 12, 'bold')).place(x=45, y=350)
        audio3 = r1.listen(source1)

        print("Subject")
        l4 = Label(img,text="Subject : ", font=("Comic Sans MS", 12, 'bold')).place(x=45, y=400)
        audio4 = r1.listen(source1)

        print("Body")
        l5 = Label(img,text="Enter mail : ", font=("Comic Sans MS", 12, 'bold')).place(x=45, y=450)
        audio5 = r1.listen(source1)

        try:
            text1 = r1.recognize_google(audio1)
            l1_1 = Label(img,text=text1, font=("Comic Sans MS", 12, 'bold')).place(x=250, y=200)

            text6 = r1.recognize_google(audio6) # newly added segment
            l1_6 = Label(img,text=text6, font=("Comic Sans MS", 12, 'bold')).place(x=250, y=300)

            text3 = r1.recognize_google(audio3)
            l1_3 = Label(img,text=text3, font=("Comic Sans MS", 12, 'bold')).place(x=250, y=350)

            text4 = r1.recognize_google(audio4)
            l1_4 = Label(img,text=text4, font=("Comic Sans MS", 12, 'bold')).place(x=250, y=400)

            text5 = r1.recognize_google(audio5)
            l1_5 = Label(img,text=text5, font=("Comic Sans MS", 12, 'bold')).place(x=250, y=450)

        except:
            print("sorry couldn't recognize your voice")

    l2 = Label(img,text="Enter password : ", font=("Comic Sans MS", 12, 'bold')).place(x=45, y=250)
    s2 = StringVar()
    e2 = Entry(img,textvariable=s2, bg='white', fg='navy', font=("Comic Sans MS", 15, 'bold'), show='*').place(x=250, y=250)

    # mailing

    def VERIFYEMAIL():  # newly added segment
         valid = False
         name = str(text6).capitalize()
         emailAddress = str(text3).replace(" ","").lower() + "@gmail.com"
         cnx = m.connect(host="localhost", user="root", password="", database="project1")
         cur = cnx.cursor()
         cur.execute("select name,emailAddress from emails where name='%s' and emailAddress='%s'" % (name, emailAddress))
         for row in cur.fetchall():
             valid = True
         cur.close()
         cnx.close()
         if not valid:
             messagebox.showerror(title="VERIFICATION", message="Data doesn't exist!!")
             # s1.set("")
             # s2.set("")
         else:
             messagebox.showinfo(title="INFO",message="Email is verified successfully..")


    def sndm():
        user = str(text1).replace(" ","").lower()+ "@gmail.com"
        password = s2.get()
        to = [str(text3).replace(" ","").lower() + "@gmail.com"]
        subject = text4
        body = text5
        email_text = """From: %s
                To: %s
                Subject: %s

                %s
                """ % (user, to, subject, body)
        try:
            server = s.SMTP_SSL('smtp.gmail.com', 465)
            server.login(user, password)
            server.sendmail(user, to, email_text)
            server.close()
        except:
            messagebox.showerror(title="ERROR",message="Something went wrong")
        else:
            messagebox.showinfo(message="Mail sent successfully..")

    def all():
        VERIFYEMAIL()
        sndm()


    b1 = Button(text='Send', bg='green', font=('Comic Sans MS', 15, 'italic'), command=all).place(x=280, y=490) # seq , VERIFY
    b2 = Button(text="Back", bg='orange', fg='white', font=("Comic Sans MS", 15, 'bold'), command=Close).place(x=370,y=490)
    root.mainloop()

def cscreen():
    pass

if __name__=='__main__':
          screen1()
          
