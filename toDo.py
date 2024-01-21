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
window.configure(bg="gray")  # Set the background color of the window to gray

frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox = tk.Listbox(frame_tasks, height=15, width=25, font=("Helvetica", 12), justify=tk.CENTER, bg="gray", fg="black")
listbox.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks, bg="gray")
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox.yview)

entry = tk.Entry(window, width=20, font=("Helvetica", 12), justify=tk.CENTER, bg="gray", fg="black")
entry.pack()

button_add_task = tk.Button(window, text="Adicionar Tarefa", width=25, command=addTask, bg="gray", fg="black")
button_add_task.pack()
button_del_task = tk.Button(window, text="Deletar Tarefa", width=25, command=delTask, bg="gray", fg="black")
button_del_task.pack()

window.mainloop()