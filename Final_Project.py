import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import messagebox


################################################# lists





Question_Five=[]





########################################################第一个窗口#########################################################
def listbox_window_show(Question_One):
    """
    listbox_window_show is the first page
    """
    #  list_box show
    listbox_window = tk.Tk()
    listbox_window.title('Question one')
    listbox_window.geometry('1000x1000')
    listbox_window.configure(bg='white')

    # Create a label
    title = tk.Label(listbox_window, text = "Which of the following is least likely to be included in the Voting database ?",
                     font = "40" )
    title.place(x = 180, y = 40)

    list_box = tk.Listbox(listbox_window, selectmode = tk.EXTENDED,width=20,border=0)
    list_box.place(x = 100, y = 150)

    for name in Question_One:
        list_box.insert(tk.END, name)

    # do loop until choose Steven
    def lb_click(event):
        # print(event)
        chosen_name = str(list_box.get(list_box.curselection()[0]))
        if chosen_name == 'C. Email address of Voter':
            messagebox.showinfo(title=None, message = "You are Right" )
            Question_Second=["A.By providing high_bandwidth connections between devices,enabling data packets to be transmitted as qucikly as possible.","\n",
                             "B.By providing multiple paths between devices, enabling routing to occur even in the presence of a failed component. ","\n",
                             "C.By providing open network protocols, ensuring that all devices on the network are interacting in a standard way.","\n",
                             "D.By providing software to monitor all network traffic, ensure that data packets are sent and received in the proper odrer."]
            listbox_window_second_show(Question_Second)
            listbox_window.destroy()
        else:
            messagebox.showinfo(title=None, message = chosen_name + " is wrong choice")

    list_box.bind("<Double-1>", lb_click)


#######################################################第二题##############################################

def listbox_window_second_show(Question_Second):

    listbox_window_second = tk.Tk()
    listbox_window_second.title('Question two')
    listbox_window_second.geometry('1000x1000')
    listbox_window_second.configure(bg='white')

    # Create a label
    title = tk.Label(listbox_window_second, text = "Which of the following best explains how fault tolerance in a network is achieved\"?",
                     font = "40" )
    title.place(x = 180, y = 40)

    list_box_second = tk.Listbox(listbox_window_second, selectmode = tk.EXTENDED,width=100,border=0)
    list_box_second.place(x = 100, y = 150)

    for answer in Question_Second:
        list_box_second.insert(tk.END, answer)

    # do loop until choose Steven
    def lb_click_Second(event):
        chosen_answer_second = str(list_box_second.get(list_box_second.curselection()[0]))
        if chosen_answer_second == "B.By providing multiple paths between devices, enabling routing to occur even in the presence of a failed component. ":
            messagebox.showinfo(title=None, message = "You are Right")
            Question_Third=["A.The ability to use a hierarchical naming system to avoid naming conflicts","\n",
                            "B. The ability to provide data transmission even when some connections have have failed","\n",
                            "C. The ability to resolve errors in domain name system (DNS) lookups","\n",
                            "D. The ability to use muliple protocols such as HTTP, IP and SMTP to transfer data"]
            combox_window_show(Question_Third)
            listbox_window_second.destroy()
        else:
            messagebox.showinfo(title=None, message = chosen_answer_second + " is wrong choice")

    list_box_second.bind("<Double-1>", lb_click_Second)



################################################第三踢#######################################################
def combox_window_show(Question_Third):
    #  list_box show
    combox_window = tk.Tk()
    combox_window.title('Question three')
    combox_window.geometry('1000x1000')
    combox_window.configure(bg='white')

    title = tk.Label(combox_window, text = "Which of the following is a characteristic of the failt-tolerant nature of routing on the internet?")
    title.place(x = 80, y = 40)
    # cmbx_value = tk.StringVar()
    combox = ttk.Combobox(combox_window, width = 60)
    combox.place(x = 20, y = 150)
    combox['value'] = Question_Third
    combox.current(0)

    def selectcmbx(event):
        chosen_answer_second_one = combox.get()
        if chosen_answer_second_one == 'B. The ability to provide data transmission even when some connections have have failed':
            messagebox.showinfo(title="YES", message = "You are Right!" )
            Question_Four=["A. Copyright information for the image","\n",
                           "B. The data and time the image was created","\n",
                           "C. The dimensions (number of rows and columns of pixels) of the image","\n",
                           "D. A duplicate copy of the data","\n"]
            combox_windows_second_show(Question_Four)
            combox_window.destroy()
        else:
            messagebox.showinfo(title=None, message = chosen_answer_second_one + " is not the answer!")
    combox.bind("<<ComboboxSelected>>", selectcmbx)


###################################################第四个题#############################################
def combox_windows_second_show(Question_Four):
    #  list_box show
    combox_window_second = tk.Tk()
    combox_window_second.title('Question four')
    combox_window_second.geometry('1000x1000')
    combox_window_second.configure(bg='white')


    title = tk.Label(combox_window_second, text = "A lsit of binary values (0 or 1) is used to represent a black-and-white image. Which of the following is LEAST likely to stored as metadata associated with the image?")
    title.place(x = 80, y = 40)
    # cmbx_value = tk.StringVar()
    combox_second = ttk.Combobox(combox_window_second, width = 60)
    combox_second.place(x = 20, y = 150)
    combox_second['value'] = Question_Four
    combox_second.current(0)

    def selectcmbx(event):
        chosen_answer_second_one = combox_second.get()
        if chosen_answer_second_one == 'C. The dimensions (number of rows and columns of pixels) of the image':
            messagebox.showinfo(title="YES", message ="You are Right!" )
            #combox_windows_second_show() 下一个界面
            combox_window_second.destroy()

        else:
            messagebox.showinfo(title=None, message = chosen_answer_second_one + " is not the answer!")
    combox_second.bind("<<ComboboxSelected>>", selectcmbx)

#####################################第五题#################################################3















''''# 最后一个窗口

def check_window_show():
    #  list_box show
    checkbtn_window = tk.Tk()
    checkbtn_window.title('Question three')
    checkbtn_window.geometry('800x800')
    checkbtn_window.configure(bg='white')


    tk.Label(checkbtn_window, text="Please select Question_One").grid(row=0, sticky=tk.W)

    btns = []
    cnt = 0
    for name in Question_One:
        btn = ttk.Checkbutton(checkbtn_window, text = name, state=['!alternate'])
        btns.append(btn)
        btn.grid(row=cnt + 1, sticky=tk.W)
        cnt += 1

    def selected_show():
        message = ''
        for idx, btn in enumerate(btns):
            # print(idx, btn.state())
            state = btn.state()
            if 'selected' in state:
                message += ' ' + Question_One[idx]
        if message == '':
            messagebox.showinfo(title = None, message = "You have chosen Nobody")
        else:
            messagebox.showinfo(title = None, message = "You have chosen " + message)

    tk.Button(checkbtn_window, text = 'Show Question_One', command=selected_show).grid(row= cnt + 2, sticky=tk.W, pady=4)
    tk.Button(checkbtn_window, text = 'Quit', command=checkbtn_window.quit).grid(row= cnt + 3, sticky=tk.W, pady=4)
'''
################################################login###################################################

def check(name_entry, password_entry, loginwindow):
    password = password_entry.get()
    name     = name_entry.get()
    # if True:
    if name == "Steven" and password == "123":
        messagebox.showinfo("Login Success ", "The Test Start! ")
        # step 1: quit the loginwindow
        # so I did a google search, and found NOTE destroy command
        loginwindow.destroy()
        Question_One = ['A. PIN Voter',"\n",'B. Time of Voter',"\n", 'C. Email address of Voter',"\n", 'D. IP address of voter']
        listbox_window_show(Question_One)
    else:
        messagebox.showerror("Error","Your name or password is wrong")




def login_check():
    mainwindow.withdraw()
    loginwindow = tk.Tk()
    loginwindow.title('Login Window')
    loginwindow.geometry('400x400')
    loginwindow.configure(bg='pink')
    # Create a label
    # TO create a label you can use this label class from tkinter
    name = tk.Label(loginwindow,text='Name:')
    name.place(x=30,y=50)
    name.configure(bg='pink')
    # create another label to display password
    password = tk.Label(loginwindow, text='Password:')
    password.place(x=30, y=90)
    password.configure(bg='pink')

    username_entry = tk.Entry(loginwindow)
    username_entry.place(x=120, y=50)

    password_entry = tk.Entry(loginwindow)
    password_entry.place(x=120, y=90)

    # create tk.Button Object
    #
    login_B = tk.Button(loginwindow, text = 'Login', command = partial(check, username_entry, password_entry, loginwindow)) #
    login_B.place(x=110, y=140)
    Quit_B = tk.Button(loginwindow, text = 'quit', command = exit)
    Quit_B.place(x=240, y=140)


mainwindow = tk.Tk()  # This line will create an object of Tk class
mainwindow.title('Test Login')  # title() function will help to st some title
mainwindow.geometry('800x800')
mainwindow.configure(bg='light GREY')  # configure() function will help to set some basic setting


login = tk.Button(mainwindow,
               bg='blue', text='login', fg='black', font='15', width=18, height=5,
               command=login_check)  # this will create an object of button class
login.pack()
mainwindow.mainloop()  # mianloop() function Will show the window












