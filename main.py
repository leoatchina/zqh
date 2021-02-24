#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : main.py
# Author            : taotao <taotao@myhexin.com>
# Date              : 2021.02.22
# Last Modified Date: 2021.02.22
# Last Modified By  : taotao <taotao@myhexin.com>

import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import messagebox

names = ['Ross', 'Steven', 'Jack', 'Susan', 'Tom', 'Jerry']
def listbox_window_show():
    """
    listbox_window_show is the first page
    """
    #############  list_box show
    listbox_window = tk.Tk()
    listbox_window.title('The listbox window')
    listbox_window.geometry('800x800')
    listbox_window.configure(bg='grey')

    # Create a label
    title = tk.Label(listbox_window, text = "What\" your name? please double click!")
    title.place(x = 40, y = 40)

    ################# add listbox
    # NOTE: https://blog.csdn.net/weixin_42272768/article/details/100796024
    list_box = tk.Listbox(listbox_window, selectmode = tk.EXTENDED)
    list_box.place(x = 40, y = 100)

    for name in names:
        list_box.insert(tk.END, name)

    # do loop until choose Steven
    def lb_click(event):
        # print(event)
        chosen_name = str(list_box.get(list_box.curselection()[0]))
        if chosen_name == 'Steven':
            messagebox.showinfo(title=None, message = chosen_name + " is the one" )
            combox_window_show()
            listbox_window.destroy()
        else:
            messagebox.showinfo(title=None, message = chosen_name + " is wrong choice")

    list_box.bind("<Double-1>", lb_click)


def combox_window_show():
    #############  list_box show
    combox_window = tk.Tk()
    combox_window.title('The combobox window')
    combox_window.geometry('400x256')
    combox_window.configure(bg='grey')

    ###################
    title = tk.Label(combox_window, text = "Who is the author of this program?")
    title.place(x = 40, y = 40)
    ###########################
    # cmbx_value = tk.StringVar()
    ################# add combobox
    combox = ttk.Combobox(combox_window, width = 30)
    combox.place(x = 40, y = 60)
    combox['value'] = names
    combox.current(0)

    def selectcmbx(event):
        chosen_name = combox.get()
        if chosen_name == 'Steven':
            messagebox.showinfo(title="YES", message = chosen_name + " is the author" )
            check_window_show()
            combox_window.destroy()
        else:
            messagebox.showinfo(title=None, message = chosen_name + " is not the author")
    combox.bind("<<ComboboxSelected>>", selectcmbx)


def check_window_show():
    #############  list_box show
    checkbtn_window = tk.Tk()
    checkbtn_window.title('The checkbutton window')
    checkbtn_window.geometry('400x800')
    checkbtn_window.configure(bg='grey')
    #################

    tk.Label(checkbtn_window, text="Please select names").grid(row=0, sticky=tk.W)
    #########3#######
    vars = []
    cnt = 0
    for name in names:
        vars.append(tk.StringVar(value=""))
        tk.Checkbutton(checkbtn_window, text = name, variable = vars[cnt], onvalue = name, offvalue= '').grid(row=cnt + 1, sticky=tk.W)
        cnt += 1

    def selected_show():
        for var in vars:
            print(var.get())
        # messagebox.showinfo(title = None, message = "You have chosen " + message)

    tk.Button(checkbtn_window, text = 'Show names', command=selected_show).grid(row= cnt + 2, sticky=tk.W, pady=4)
    tk.Button(checkbtn_window, text = 'Quit', command=checkbtn_window.quit).grid(row= cnt + 3, sticky=tk.W, pady=4)




def check(name_entry, password_entry, loginwindow):
    password = password_entry.get()
    name     = name_entry.get()
    if True:
    # if name == "Steven" and password == "123":
        messagebox.showinfo("Login Success ", "The Test Start! ")
        # step 1: quit the loginwindow
        # so I did a google search, and found NOTE destroy command
        loginwindow.destroy()
        listbox_window_show()
    else:
        messagebox.showerror("Error","Your name or password is wrong")

    # third step

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
