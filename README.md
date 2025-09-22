# ToDoList_Tkinter
Small application for personal practice in Python framework Tkinter

# Version 0.1
**Features:**
- Designed the main application layout  
- Implemented adding tasks  
- Added the ability to mark tasks as complete  

<p align="center">
  <img width="400" height="400" alt="изображение" src="https://github.com/user-attachments/assets/256d4acb-c76a-45a5-87d0-a5a443e7e319" />
  <br>
  Image 1.1 - The main window
</p>

A task can be added with the **"Add new task"** button. Clicking it opens a **"New Task"** window where you can write a task and add it to the main window.

<p align="center">
  <img width="501" height="178" alt="изображение" src="https://github.com/user-attachments/assets/cdabaad4-0874-4c46-98fb-1452547687a8" />
  <br>
  Image 1.2 - The "New Task" window
</p>

The task is added through the method **`AddTask`**.  
This method takes the value from the entry field, adds it to the task list, and then calls **`RefreshTaskList`**.  

`RefreshTaskList` works as follows:  
- All tasks are first removed from the main window (but remain in memory).  
- If the task list is empty, the label *"No tasks yet"* is shown.  
- Otherwise, each task is displayed in a separate block.  

You can also mark a task as complete with a check button next to the task text.

---

# Version 0.2
**New features:**
- Added **"Delete"** button to remove tasks  
- Redesigned the task list system  

<p align="center">
  <img width="499" height="525" alt="изображение" src="https://github.com/user-attachments/assets/8b66d9e5-a318-456a-a561-641db8e697e0" />
  <br>
  Image 2.1 - The main window (v0.2)
</p>

In the previous version, tasks and check button values were stored in a simple list.  
Now they are stored in a **dictionary**, where:  
- the key = the task  
- the value = the state of the check button  

The application also now supports task deletion.  
Additionally, if a task is marked as complete, its background is recolored in green.
