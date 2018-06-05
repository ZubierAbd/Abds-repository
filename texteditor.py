import tkinter

import random

#Create Root window

root = tkinter.Tk()

root.configure(bg = "white")
root.title('My super To-Do list')
root.geometry('200x500')

#create an empty list

tasks = []

#for testing purposes
tasks = ['Call mom', 'Buy Guitar', 'Establish Communism']


######################################
def update_listbox():
    for task in tasks:
        lb_tasks.insert("end",task)

def add_task():
    update_listbox()

def delete_all():
    pass

def del_one():
    pass

def sort_ascending():
    pass

def sort_descending():
    pass

def choose_random():
    pass

def number_of_tasks():
    pass


#########################
lbl_title = tkinter.Label(root, text = "To-Do-List",bg = "white")
lbl_title.pack()

lbl_display = tkinter.Label(root, text = "",bg = "white")
lbl_title.pack()

lbl_input = tkinter.Entry(root, width = 15)
#1
btn_add_task = tkinter.Button(root,text = "Add Task", fg = "green", bg = "white", command = add_task)
btn_add_task.pack()
#2
btn_delete_all = tkinter.Button(root,text = "Delete All", fg = "green", bg = "white", command =delete_all)
btn_delete_all.pack()
#3
btn_del_one = tkinter.Button(root,text = "Delete one ", fg = "green", bg = "white", command = del_one)
btn_del_one.pack()
#4
btn_sort_asc = tkinter.Button(root,text = "Sort Ascending", fg = "green", bg = "white", command = sort_ascending)
btn_sort_asc.pack()

#5
btn_sort_dsc = tkinter.Button(root,text = "Sort descending", fg = "green", bg = "white", command = sort_descending)
btn_sort_dsc.pack()

#6
btn_choose_random = tkinter.Button(root,text = "Choose Random", fg = "green", bg = "white", command = choose_random)
btn_choose_random.pack()

#7
btn_number_of_tasks = tkinter.Button(root,text = "Show Number of Tasks", fg = "green", bg = "white", command = number_of_tasks)
btn_number_of_tasks.pack()

#8
btn_quit = tkinter.Button(root,text = "Exit", fg = "green", bg = "white", command = exit())
btn_quit.pack()

#
lb_tasks = tkinter.Listbox(root)

#start the main events loop

root.mainloop()

