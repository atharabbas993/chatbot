#________________________Libraries_____________________

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#____________________Creating class________________________

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open('chat1.png')
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT,
                            image=self.photoimg, text='CHAT ME', font=('arial', 30, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=('arial', 15, 'bold'), width=8, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_btn = Button(btn_frame, text="Clear Data", command=self.clear, font=('arial', 15, 'bold'), width=8,
                                bg='red', fg='white')
        self.clear_btn.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

        self.responses = {
            "Hi": "Hello",
            "How are you?": "Fine and you?",
            "What is your name?": "I am a ChatBot. How can I help you?",
            "I'm fine": "Nice to hear you are fine",
            "Who created you?": "I was created by Mr. Athar Abbas",
            "What do you do?": "I am a chatbot designed to help answer your questions and provide information.",
            "How can I contact you?": "You can contact Athar Abbas at atharabbas993@gmail.com",
            "What are your working hours?": "I am available 24/7 to assist you.",
            "What languages can you speak?": "I understand only English for communication.",
            "Do you have any hobbies?": "As a chatbot, I don't have hobbies, but I can help you find hobbies and activities that you might enjoy!"
        }

    #===============Function Declarations===============

    def enter_func(self, event):
        self.send.invoke()
        self.entry.set("")

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        user_input = self.entry.get().strip()
        send = f'\t\t\tYou: {user_input}'
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if not user_input:
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')
            response = self.responses.get(user_input, "Sorry, I did not get it")
            self.text.insert(END, f'\n\nBot: {response}')
            self.entry.set('')


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
