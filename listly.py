import tkinter as tk

class ListlyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting up the window
        self.title("Listly - Task Manager")
        self.geometry("900x600")

        # Creating a Label for the title in the center
        self.label = tk.Label(self, text="Listly!", font=("Impact", 48), bg="#ADD8E6", fg="#FFFFFF")
        self.label.pack(expand=True)

        # Creating a description below the title for the program
        self.label = tk.Label(self, text="The quick and easy task master!", font=("Impact",24), bg="#ADD8E6", fg="#FFFFFF")
        self.label.pack(expand=True)

        # Adding a picture to the main menu
        self.logo = tk.PhotoImage(file="greentick.png")
        self.logo_label = tk.Label(self, image=self.logo, bg="#ADD8E6")
        self.logo_label.pack(pady=0)

        # Setting the background color to light blue
        self.config(bg="#ADD8E6")

        # Creating the New Task button
        self.new_task_button = tk.Button(self, text="Make a New Task", width=40, height=2, command=self.new_task)
        self.new_task_button.pack(side=tk.BOTTOM, pady=10)

        # Creating the View Task button
        self.view_task_button = tk.Button(self, text="View Current Tasks", width=40, height=2, command=self.view_task)
        self.view_task_button.pack(side=tk.BOTTOM)

    def new_task(self):
        # In progress
        print("New Task button clicked")

    def view_task(self):
        # In progress
        print("View Task button clicked")

if __name__ == "__main__":
    app = ListlyApp()
    app.mainloop()