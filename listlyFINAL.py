import tkinter as tk
from tkinter import simpledialog, messagebox

class ListlyApp(tk.Tk):
    # Creating a main menu
    def __init__(self):
        super().__init__()

        # Configuring the window
        self.title("Listly - Task Manager")
        self.geometry("900x900")

        # Task storage (dictionary list)
        self.tasks = []  # Task list initializing

        # Label Creation for Listly
        self.label = tk.Label(self, text="Listly!", font=("Impact", 48), bg="#ADD8E6", fg="#FFFFFF")
        self.label.pack(expand=True)

        # Adding a description below the title for the program
        self.label = tk.Label(self, text="The quick and easy task master!", font=("Impact",24), bg="#ADD8E6", fg="#FFFFFF")
        self.label.pack(expand=True)

        # Putting a picture on the main menu
        self.logo = tk.PhotoImage(file="greentick.png")
        self.logo_label = tk.Label(self, image=self.logo, bg="#ADD8E6")
        self.logo_label.pack(pady=0)

        # Changing the background color to light blue
        self.config(bg="#ADD8E6")

        # Creating the New Task button
        self.new_task_button = tk.Button(self, text="Make a New Task", width=40, height=2, command=self.new_task)
        self.new_task_button.pack(side=tk.BOTTOM, pady=10)

        # Creating the View Task button
        self.view_task_button = tk.Button(self, text="View Current Tasks", width=40, height=2, command=self.view_task)
        self.view_task_button.pack(side=tk.BOTTOM)

        # Creating the Close Program button
        self.close_button = tk.Button(self, text="Close Program", width=40, height=2, command=self.close_program)
        self.close_button.pack(side=tk.BOTTOM, pady=10)

    def new_task(self):
        # Creating a new window for task input
        self.new_task_window = tk.Toplevel(self)
        self.new_task_window.title("New Task")
        self.new_task_window.geometry("500x900")

        # Task description creation
        self.task_label = tk.Label(self.new_task_window, text="Task Description:")
        self.task_label.pack(pady=5)
        self.task_entry = tk.Entry(self.new_task_window, width=30)
        self.task_entry.pack(pady=5)

        # Creating a due date
        self.due_date_label = tk.Label(self.new_task_window, text="Due Date (Day):")
        self.due_date_label.pack(pady=5)
        self.due_date_entry = tk.Entry(self.new_task_window, width=30)
        self.due_date_entry.pack(pady=5)

        # Making a task category selection
        self.category_label = tk.Label(self.new_task_window, text="Category:")
        self.category_label.pack(pady=5)
        self.category_var = tk.StringVar()
        self.category_var.set("Personal")  # Default selection
        self.category_menu = tk.OptionMenu(self.new_task_window, self.category_var, "Personal", "Work", "Social")
        self.category_menu.pack(pady=5)

        # Save button that saves the task in Listly
        self.save_button = tk.Button(self.new_task_window, text="Save Task", width=20, height=2, command=self.save_task)
        self.save_button.pack(pady=20)

        # Go back button
        self.go_back_button = tk.Button(self.new_task_window, text="Go Back", width=20, height=2, command=self.go_back_new_task)
        self.go_back_button.pack(pady=10)

        # Adding a picture
        self.image = tk.PhotoImage(file="tasklist.png")
        self.image_label = tk.Label(self.new_task_window, image=self.image)
        self.image_label.pack(pady=10)

    def go_back_new_task(self):
        # Closes the New Task window
        self.new_task_window.destroy()

    def save_task(self):
        # Saves a new task
        task_description = self.task_entry.get()
        due_date = self.due_date_entry.get()
        category = self.category_var.get()

        # Stores the task as a dictionary
        if task_description and due_date:
            task = {
                "description": task_description,
                "due_date": due_date,
                "category": category
            }
            self.tasks.append(task)  # Correctly adding to the instance variable `self.tasks`
            messagebox.showinfo("Task Saved", "Your task has been saved successfully!")
            self.new_task_window.destroy()  # Close the input window
        else:
            messagebox.showerror("Error", "Please enter a description and due date.")

    def view_task(self):
        # Creates a new window to display the tasks
        self.view_window = tk.Toplevel(self)
        self.view_window.title("View Tasks")
        self.view_window.geometry("500x400")

        # Creates a list to store the checkboxes
        self.check_buttons = []

        # Displays tasks with checkboxes
        if self.tasks:
            for idx, task in enumerate(self.tasks):
                # Creates a variable to link each checkbox to the task's completion state
                var = tk.BooleanVar(value=False)
                self.check_buttons.append(var)

                task_info = f"Task {idx + 1}:\nDescription: {task['description']}\nDue Date: {task['due_date']}\nCategory: {task['category']}\n"
                task_label = tk.Label(self.view_window, text=task_info, anchor="w", justify="left", font=("Helvetica", 12))
                task_label.pack(pady=5)

                # Adds a checkbox to mark the task as complete
                checkbox = tk.Checkbutton(self.view_window, text="Completed", variable=var)
                checkbox.pack(pady=5)

        else:
            messagebox.showinfo("No Tasks", "No tasks available to view.")

        # Creates a button to delete completed tasks
        self.delete_button = tk.Button(self.view_window, text="Delete Completed Tasks", width=30, height=2, command=self.delete_completed)
        self.delete_button.pack(pady=10)

        # Go back button
        self.go_back_button = tk.Button(self.view_window, text="Go Back", width=20, height=2, command=self.go_back_view_task)
        self.go_back_button.pack(pady=10)

    def go_back_view_task(self):
        # Close the View Tasks window
        self.view_window.destroy()

    def delete_completed(self):
        # Removes tasks that have been ticked as complete
        completed_tasks = [task for idx, task in enumerate(self.tasks) if self.check_buttons[idx].get()]

        # Removes completed tasks from the main task list
        self.tasks = [task for idx, task in enumerate(self.tasks) if not self.check_buttons[idx].get()]

        # Shows a confirmation message
        if completed_tasks:
            messagebox.showinfo("Deleted", f"Deleted {len(completed_tasks)} task(s).")
        else:
            messagebox.showinfo("No Tasks Deleted", "No tasks were marked as completed.")

    def close_program(self):
        # Closes the program
        self.destroy()

if __name__ == "__main__":
    app = ListlyApp()
    app.mainloop()