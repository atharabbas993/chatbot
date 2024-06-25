

#________________________Libraries_____________________



from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



#____________________Creating class________________________


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()


        img_chat=Image.open('chat1.png')
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()    


        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)


        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)


        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='green',)
        self.send.grid(row=0,column=2,padx=5,sticky=W)


        self.clare=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clare.grid(row=1,column=0,padx=5,sticky=W)


        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)


    #===============Function Decleration===============

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set("")


    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)




        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')
        
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')





        if (self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=="How are you?"):
            self.text.insert(END,'\n\n'+'Bot: Fine and you')

        elif (self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n\n'+'Bot: I am a ChatBot. How i can help you?')
    
        elif (self.entry.get()=="I\'m fine"):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear! you fine')

        elif (self.entry.get()=="Who created you?"):
            self.text.insert(END,'\n\n'+'Bot: By Mr.Athar Abbas')

        elif (self.entry.get()=="What do you do?"):
            self.text.insert(END,'\n\n'+'Bot: I am a chatbot designed to help answer your questions and provide information.')

        elif (self.entry.get()=="How can I contact you?"):
            self.text.insert(END,'\n\n'+'Bot: I Will provide the email address of Athar Abbas which is (atharabbas993@gmail.com)')

        elif (self.entry.get()=="What are your working hours?"):
            self.text.insert(END,'\n\n'+'Bot: I am available 24/7 to assist you.')

        elif (self.entry.get()=="What languages can you speak?"):
            self.text.insert(END,'\n\n'+'Bot: Now I understand only English languge for commucation')

        elif (self.entry.get()=="Do you have any hobbies?"):
            self.text.insert(END,'\n\n'+'Bot: As a chatbot, I don\'t have hobbies, but I can help you find hobbies and activities that you might enjoy!')

        elif (self.entry.get()=="Who created you?"):
            self.text.insert(END,'\n\n'+'Bot: By Mr.Athar Abbas')    
        

        else:
            self.text.insert(END,'\n\n'+'Bot:Sorry i did not get it')




if __name__ == '__main__':
    root = Tk()
    obj=ChatBot(root)
    root.mainloop()
    

