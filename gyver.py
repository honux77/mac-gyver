# simple tkinter app

import tkinter as tk
from tkinter import ttk


# main app
root = tk.Tk()
root.title("MacGyver Utility")
root.geometry("800x600")

# Frame
leftFrame = tk.Frame(root, width=200, height=400, bg="red")
msgFrame = tk.Frame(root, width=200, height=400, bg="blue")
buttonFrame = tk.Frame(root, width=200, height=400, bg="green")
leftFrame.grid(row=0, column=0)
msgFrame.grid(row=0, column=1)
buttonFrame.grid(row=0, column=2)


# main loop
root.mainloop()
