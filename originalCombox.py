#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:44:18 2020

@author: dianasimpson
"""

import tkinter as tk
from tkinter import ttk
from tkinter import Menu

# Create instance
win = tk.Tk()

# Add a title
win.title("Navigability Analysis of Australian University Websites")

# Create Tab Control
tabControl = ttk.Notebook(win)

# Adding tabs to the window for organisation & asthetic appeal
tab1 = ttk.Frame(tabControl)            # Create first tab
tabControl.add(tab1, text='Parameters')  # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Analysis')   # Make second tab visible
tab3 = ttk.Frame(tabControl)            # Add a third tab
tabControl.add(tab3, text='Results')    # Make third tab visible
tabControl.pack(expand=1, fill="both")  # Pack to make all tabs visible

base = ttk.LabelFrame(tab1, text=' Analysis Parameters ')
base.pack(expand=1, fill="both")

# Creating a nameless frame for the right side of the base
focusBox = ttk.LabelFrame(base, text="Parameter Summary")
focusBox.grid(column=1, row=0, padx=10, pady=10, sticky='NS')
focusBox.grid_columnconfigure(1, weight=1)  # , minsize=tab1W*0.25)
focusBox.grid_rowconfigure(0, weight=1)  # , minsize=tab1H*0.5)

# Creating drop-down menu to specify focus group
focusLabel = ttk.Label(focusBox, text="Focus Group:", font=("Times", 16))
focusLabel.grid(column=0, row=0, padx=5, pady=5)
focusLabel.grid_columnconfigure(0, weight=1)
focusLabel.grid_rowconfigure(0, weight=1)

degree = tk.StringVar()
groupChosen = ttk.Combobox(focusBox, width=30, textvariable=degree,
                           state='readonly', validate='all', justify='center')
groupChosen['values'] = ('Undergraduate, International',
                         'Undergraduate, Domestic',
                         'Masters, International',
                         'Masters, Domestic',
                         'Doctorate, International',
                         'Doctorate, Domestic')
groupChosen.grid(column=1, row=0, padx=5, pady=5)
groupChosen.grid_columnconfigure(1, weight=1)  # , minsize=tab1W*0.2)
groupChosen.grid_rowconfigure(0, weight=1)
groupChosen.current(0)

# Creating a label to show which focus group was selected
focusChoice = ttk.Label(focusBox, text="Make a Choice",
                        font=("Times Bold", 20))
focusChoice.grid(columnspan=2, row=1, padx=5, pady=5)
focusChoice.grid_rowconfigure(1, weight=1)
focusChoice.grid_columnconfigure(0, weight=1)


# Combobox callback alteration requires label update
def focusCall(event):
    focusChoice.configure(foreground='dark olive green', text=degree.get())


groupChosen.bind("<<ComboboxSelected>>", focusCall)

# --------------------------------- Menu Bar ---------------------------------

# Creating a Menu Bar
menuBar = Menu(win)
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=win.destroy)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# ----------------------------- Window Placement -----------------------------

# Updating the base window to get information
win.update()

# Generate the desired sized window
screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()
print("Screen width: ", screenWidth, "\t Screen height: ", screenHeight)
winW = win.winfo_width()
winH = win.winfo_height()
print("win width: ", winW, "\t win height: ", winH)
# win.geometry(("%dx%d") % (winW, winH))

# Position window in the centre of the screen
posRight = int(screenWidth/2 - winW/2)
posDown = int(screenHeight/2 - winH/2)
win.geometry("+{}+{}".format(posRight, posDown))

# ------------------------------- Run Program -------------------------------
win.mainloop()
