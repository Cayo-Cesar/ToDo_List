import tkinter as tk
from tkinter import Entry as entry
from tkinter import Listbox as listbox

def addTask():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delTask():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        pass

def saveList():
    with open("tasks.txt", "w") as f:
        tasks = listbox.get(0, listbox.size())
        for task in tasks:
            f.write(task + "\n")

def loadList():
    try:
        with open("tasks.txt", "r") as f:
            for task in f:
                listbox.insert(tk.END, task.strip())
    except:
        pass

window = tk.Tk()
window.title("To-Do List")
window.geometry("300x400")

frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox = tk.Listbox(frame_tasks, height=15, width=25)
listbox.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox.yview)

entry = tk.Entry(window, width=25)
entry.pack()

button_add_task = tk.Button(window, text="Add task", width=25, command=addTask)
button_add_task.pack()
button_del_task = tk.Button(window, text="Delete task", width=25, command=delTask)
button_del_task.pack()
button_save_list = tk.Button(window, text="Save list", width=25, command=saveList)
button_save_list.pack()
button_load_list = tk.Button(window, text="Load list", width=25, command=loadList)
button_load_list.pack()

window.mainloop()


