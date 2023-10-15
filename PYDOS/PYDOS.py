import tkinter as tk
import random

def create_popup():
    popup = tk.Toplevel(root)
    popup.title("Run")
    popup.geometry(f"200x100+{random.randint(0, 800)}+{random.randint(0, 600)}")
    root.after(1, create_popup)  

root = tk.Tk() 

root.withdraw()  

create_popup()

root.mainloop()
