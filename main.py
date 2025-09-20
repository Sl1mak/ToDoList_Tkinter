import tkinter as tk

root = tk.Tk()
root.title("ToDo List")
root.geometry("500x500")

taskList = []
check_vars = []

def RefreshTaskList():
    for widget in taskFrame.winfo_children():
        widget.destroy()

    if len(taskList) == 0:
        emptyLabel = tk.Label(
            taskFrame,
            text="No tasks yet",
            font=("Arial", 15),
            bg="lightblue",
        )
        emptyLabel.pack(anchor="center", pady=175)

    for task in taskList:
        row = tk.Frame(taskFrame)
        row.pack(fill="x", pady=1)

        var = tk.BooleanVar()
        cb = tk.Checkbutton(row, variable=var)
        cb.pack(side="left")
        check_vars.append(var)

        lbl = tk.Label(row, text=task, font=("Arial", 12))
        lbl.pack(side="left")

def NewTask():
    InputTaskWindow = tk.Toplevel(root)
    InputTaskWindow.title("New Task")
    InputTaskWindow.geometry("500x150")

    def AddTask():
        if len(entry.get()) != 0:
            taskList.append(entry.get())
            InputTaskWindow.destroy()
            RefreshTaskList()

    entry = tk.Entry(InputTaskWindow, width=40, font=("Arial", 15))
    entry.pack(pady=20)

    acceptButton = tk.Button(InputTaskWindow, text="Add task", command=AddTask, font=("Arial", 15))
    acceptButton.pack(pady=20)

taskFrame = tk.Frame(
    root,
    width=450,
    height=375,
    bg="lightblue",
    bd=2,
    relief="solid")
taskFrame.pack(side="top", expand=True)
taskFrame.pack_propagate(False)

if len(taskList) == 0:
    emptyLabel = tk.Label(
        taskFrame,
        text="No tasks yet",
        font=("Arial", 15),
        bg="lightblue",
    )
    emptyLabel.pack(anchor="center", pady=175)

addButton = tk.Button(root, text="Add new task", font=("Arial", 20), command=NewTask)
addButton.pack(side="bottom", pady=20)

root.mainloop()