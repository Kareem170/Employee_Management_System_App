#! /usr/bin/python3

import tkinter as tk

window_obj = tk.Tk(screenName=None,baseName=None,className=" Employee Management System ",useTk=1)
window_obj.geometry("600x400+350+100")
window_obj.config(bg="#405D72")

#-------- Widgets ---------#

L1 = tk.Label(
    window_obj,
    text="Welcome To Employee Managment System",
    font=("Helvetica", 16),
    fg="white",
    bg="#405D72",
    padx=10,
    pady=10,
    borderwidth=2,
    relief="raised"  
    )
L1.pack()










#------ Widgets ----------#




#------- mainLoop --------#
window_obj.mainloop()




