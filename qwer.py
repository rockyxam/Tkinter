from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image,ImageOps
from tkinter.font import Font
import random
from pygame import mixer
tries=0
tryr=0
class Menu(Tk):
     def __init__(self):
          Tk.__init__(self)
          self.frame=Frame(self,width="1020",height="720")
          self.open_image=Image.open("image_E.jpg")
          self.open_image=self.open_image.resize((1020,720),Image.ANTIALIAS)
          self.open_image2=Image.open("bender.jpg")
          self.open_image2=self.open_image2.resize((1020,720),Image.ANTIALIAS)
          self.open_image3=Image.open("wp.jpg")
          self.get_game_image=ImageTk.PhotoImage(self.open_image3)
          self.get_image=ImageTk.PhotoImage(self.open_image)
          self.get_info_image=ImageTk.PhotoImage(self.open_image2)
          self.main_background=Label(image=self.get_image)
          self.info_background=Label(image=self.get_info_image)
          self.game_background=Label(image=self.get_game_image)
          self.frame.pack()
          self.result_msg=0
          self.number=random.randrange(1000,9999)
          self.active=True
          self.escape_active=False
          self.submit=False
          self.qwerty=True
          self.qwerty2=True
          self.label_text ="Enter numbers"
          self.label_result_screen=Label(self,text=self.label_text ,font=("Times",25,"bold"),fg="white",bg="grey",height=2,width=12)
          self.label_result_screen.place(in_=self.game_background,x=22,y=160)
          self.escape_frame=Frame(self,height=300,bg="dimgray",relief=RAISED,width=200,bd=10)

          #TIMER
          self.timer=ttk.Progressbar(self,length=400)
          self.timer.place(in_=self.game_background,x=370,y=60)
          self.timer_label=Label(self,text="GAME OVER",font=("TIMES",25,"bold"),fg="red",bg="gray15",height=2,width=12)
          
          
          #INITIALIZATION BUTTONS FOR MAIN_BACKGROUND
          self.button_start=Button(self,font="Courier" "bold",text="START GAME",fg="white",bg="grey",width=15,command=self.start)
          self.button_info=Button(self,font="Courier" "bold",text="HELP",fg="white",bg="grey",width=15,command=self.info)
          self.button_back=Button(self,font="Courier" "bold",text="BACK",fg="white",bg="grey",width=15,command=self.back)
          self.button_back_2=Button(self,font="Courier" "bold",text="BACK",fg="white",bg="grey",width=15,command=self.back_2)
          self.button_exit=Button(self,font="Courier" "bold",text="EXIT",fg="white",bg="grey",width=15,command=self.exit_t)
          
          #PACKING BUTTONS FOR MAIN_BACKGORUND
          self.main_background.pack(in_=self.frame)
          self.button_start.place(in_=self.main_background,x=410,y=250)
          self.button_info.place(in_=self.main_background,x=410,y=300)
          self.button_exit.place(in_=self.main_background,x=410,y=350)


          #INITIALIZATION BUTTONS FOR GAME_BACKGROUND
          self.button_1=Button(self,font="Courier" "bold",text="1",fg="white",bg="grey",width=5,command = lambda x = "1", y = self.label_result_screen : self.set_value(x, y))
          self.button_2=Button(self,font="Courier" "bold",text="2",fg="white",bg="grey",width=5,command = lambda x = "2", y = self.label_result_screen : self.set_value(x, y))
          self.button_3=Button(self,font="Courier" "bold",text="3",fg="white",bg="grey",width=5,command = lambda x = "3", y = self.label_result_screen : self.set_value(x, y))#,command=self.button_1)
          self.button_4=Button(self,font="Courier" "bold",text="4",fg="white",bg="grey",width=5,command = lambda x = "4", y = self.label_result_screen : self.set_value(x, y))#,command=self.button_1)
          self.button_5=Button(self,font="Courier" "bold",text="5",fg="white",bg="grey",width=5,command = lambda x = "5", y = self.label_result_screen : self.set_value(x, y))#,command=self.button_1)
          self.button_6=Button(self,font="Courier" "bold",text="6",fg="white",bg="grey",width=5,command = lambda x = "6", y = self.label_result_screen : self.set_value(x, y))#,command=self.button_1)
          self.button_7=Button(self,font="Courier" "bold",text="7",fg="white",bg="grey",width=5,command = lambda x = "7", y = self.label_result_screen : self.set_value(x, y))#,command=self.button_1)
          self.button_8=Button(self,font="Courier" "bold",text="8",fg="white",bg="grey",width=5,command = lambda x = "8", y = self.label_result_screen : self.set_value(x, y))#,command=self.button_1)
          self.button_9=Button(self,font="Courier" "bold",text="9",fg="white",bg="grey",width=5,command = lambda x = "9", y = self.label_result_screen : self.set_value(x, y))#,command=self.button_1)
          self.button_0=Button(self,font="Courier" "bold",text="0",fg="white",bg="grey",width=18,command = lambda x = "0", y = self.label_result_screen : self.set_value(x, y))
          self.button_resume=Button(self,font="Courier" "bold",text="Reset",fg="white",bg="grey",width=7,command=self.reset)
          self.button_submit=Button(self,font="Courier" "bold",text="Submit",fg="white",bg="grey",width=7,command=self.reveal)
          self.button_clear=Button(self,font="Courier" "bold",text="Clear",fg="white",bg="grey",width=7,command=self.clear)
          self.button_restart=Button(self,font="Courier" "bold",text="RESTART",fg="white",bg="grey",width=15,command=self.restart)

          #LABELS IN GAME_BACKGROUND
          self.label_error=Label(self,text="" ,font=("Times", 20,"bold"),fg="white",bg="grey",width=21,height=4)
          self.label_error.place(in_=self.game_background,x=20,y=20)

          
          #PACKING BUTTONS FOR GAME_GROUND
          self.button_1.place(in_=self.game_background,x=30,y=250)
          self.button_2.place(in_=self.game_background,x=110,y=250)
          self.button_3.place(in_=self.game_background,x=190,y=250)
          self.button_4.place(in_=self.game_background,x=30,y=300)
          self.button_5.place(in_=self.game_background,x=110,y=300)
          self.button_6.place(in_=self.game_background,x=190,y=300)
          self.button_7.place(in_=self.game_background,x=30,y=350)
          self.button_8.place(in_=self.game_background,x=110,y=350)
          self.button_9.place(in_=self.game_background,x=190,y=350)
          self.button_0.place(in_=self.game_background,x=32,y=400)
          self.button_resume.place(in_=self.game_background,x=270,y=200)
          self.button_submit.place(in_=self.game_background,x=270,y=200)
          self.button_clear.place(in_=self.game_background,x=270,y=160)
          

     def reveal(self):
          self.submit = True
          if not self.active:
               return  
          global tries,tryr,number 
          guess=self.label_text
          guess=str(guess)
          number=str(self.number)
          if len(guess)<4:
               self.label_error.config(text="Not enough numbers")
               return
          elif len(guess)>4:
               self.label_error.config(text="Too much numbers")
               return


          for i in range(len(number)):
               if guess[i]==number[i]:
                    tries+=1
               elif number[i] in guess:
                    tryr+=1
                    
          self.active=False
          if tries==4:
               self.label_error.config(text="You won! :) ")
               self.button_submit.place_forget()
               self.button_resume.place(in_=self.game_background,x=270,y=200)
               
               
               
          else:
               self.result_msg="Your Score","+",tries, "-",tryr
               self.label_error.config(text=self.result_msg)
          tries=0
          tryr=0

     def game_over(self):
          mixer.music.stop()
          self.timer.stop()
          self.timer_label.place(in_=self.game_background,x=400,y=200)
          self.button_resume.lower()
          self.button_submit.lower()
          self.button_clear.lower()
          self.button_1.lower()
          self.button_2.lower()
          self.button_3.lower()
          self.button_4.lower()
          self.button_5.lower()
          self.button_6.lower()
          self.button_7.lower()
          self.button_8.lower()
          self.button_9.lower()
          self.button_0.lower()
          self.label_error.lower()
          self.label_result_screen.lower()
          self.timer.lower()
          self.button_back.lower()
          self.button_restart.place(in_=self.game_background,x=430,y=300)
          
     def info(self):
         self.main_background.pack_forget()
         self.info_background.pack(in_=self.frame)
         self.button_back_2.place(in_=self.info_background,x=0,y=680)

     def exit_t(self):
          self.destroy()

     def start(self):
          mixer.init()
          mixer.music.load('main.mp3')
          mixer.music.play()
          self.main_background.pack_forget()
          self.game_background.pack(in_=self.frame)
          self.button_back.place(in_=self.game_background,x=850,y=680)
          self.button_back.lift(self.game_background)

          
     def restart(self):
          self.qwerty=True
          if self.qwerty:
               self.timer["value"]=0
               self.timer["maximum"]=1200
               self.timer.start()
               self.after(60000,self.game_over)
               self.qwerty=False
          mixer.init()
          mixer.music.load('main.mp3')
          mixer.music.play()
          self.button_resume.lift()
          self.button_submit.lift()
          self.button_clear.lift()
          self.button_1.lift()
          self.button_2.lift()
          self.button_3.lift()
          self.button_4.lift()
          self.button_5.lift()
          self.button_6.lift()
          self.button_7.lift()
          self.button_8.lift()
          self.button_9.lift()
          self.button_0.lift()
          self.label_error.lift()
          self.label_result_screen.lift()
          self.timer.lift()
          self.button_back.lift()
          self.timer_label.place_forget()
          self.button_restart.place_forget()
          self.label_text=""
          self.label_result_screen.config(text="Enter numbers")
          self.label_error.config(text="")
          self.result_msg=""

          
          
     def back(self):
          self.game_background.pack_forget()
          self.main_background.pack(in_=self.frame)
          self.button_start.place(in_=self.main_background)
          self.button_info.place(in_=self.main_background)
          self.button_back.lower(self.main_background)
          mixer.music.stop()
          
          

     def back_2(self):
          self.info_background.pack_forget()
          self.main_background.pack(in_=self.frame)
          self.button_back_2.pack_forget()

     def reset(self):
          if self.qwerty2:
               self.timer.stop()
               self.qwerty2=False
               if self.qwerty2==False:
                    self.timer["value"]=0
                    self.timer["maximum"]=1200
                    self.timer.start()
                    self.after(60000,self.game_over)
          self.number=random.randrange(1000,9999)
          self.button_resume.place_forget()
          self.button_submit.place(in_=self.game_background,x=270,y=200)
          self.label_text=""
          self.label_result_screen.config(text="")
          self.label_error.config(text="")
          self.result_msg=""
          mixer.init()
          mixer.music.load('main.mp3')
          mixer.music.play()
          

          
     def set_value(self, a, label):
          if self.qwerty:
               self.timer["value"]=0
               self.timer["maximum"]=1200
               self.timer.start()
               self.after(60000,self.game_over)
               self.qwerty=False
          if self.submit:
               self.label_text = ''
               self.submit = False
          if self.label_text == 'Enter numbers':
               self.label_text = ''
          self.label_text+=a
          label.config(text=self.label_text)
          self.active=True
          

     def clear(self):
          self.label_text=""
          self.label_result_screen.config(text="")
          self.label_error.config(text="")
          self.result_msg=""


          
          
     



root=Menu()
root.title("Number+")
root.maxsize(width="1020",height="720")
root.config(bg="green")

root.mainloop()
