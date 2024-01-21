from tkinter import *
import tkinter as tk 

def addTask():
    task = entry.get()
    if task != "":
        task_number = listbox.size() + 1
        listbox.insert(tk.END, f"{task_number}. {task}")
        entry.delete(0, tk.END)

def delTask():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
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
    except FileNotFoundError:
        pass

window = tk.Tk()
window.title("To-Do List")
window.geometry("500x500")
window.configure(bg="gray")  # Set the background color of the window to gray

frame_main = tk.Frame(window, bg="gray")
frame_main.pack(fill=tk.BOTH, expand=True)

frame_buttons = tk.Frame(frame_main, bg="gray")
frame_buttons.pack(side=tk.LEFT, padx=10)

text_title = tk.Label(frame_buttons, text="To-Do List", font=("Script", 40), bg="gray", fg="black")
text_title.pack(pady=10)

entry = tk.Entry(frame_buttons, font=("Helvetica", 12), justify=tk.CENTER, bg="gray", fg="black")
entry.pack(pady=10)

button_add_task = tk.Button(frame_buttons, text="Adicionar Tarefa", width=25, command=addTask, bg="gray", fg="black", activebackground="gray", activeforeground="black")
button_add_task.pack(pady=5)

button_del_task = tk.Button(frame_buttons, text="Deletar Tarefa", width=25, command=delTask, bg="gray", fg="black", activebackground="gray", activeforeground="black")
button_del_task.pack(pady=5)

button_del_all_tasks = tk.Button(frame_buttons, text="Deletar Todas as Tarefas", width=25, command=lambda: listbox.delete(0, tk.END), bg="gray", fg="black", activebackground="gray", activeforeground="black")
button_del_all_tasks.pack(pady=5)

button_exit = tk.Button(frame_buttons, text="Sair", width=25, command=window.destroy, bg="gray", fg="black", activebackground="gray", activeforeground="black")
button_exit.pack(pady=5)

frame_listbox = tk.Frame(frame_main, bg="gray")
frame_listbox.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame_listbox, height=15, width=25, font=("Helvetica", 12), justify=tk.CENTER, bg="gray", fg="black")
listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_listbox, bg="gray")
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox.yview)

window.mainloop()