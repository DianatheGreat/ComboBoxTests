#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:33:04 2020

@author: dianasimpson
"""

# Imported packages and files
import tkinter as tk
from tkinter import ttk, Menu

# Global variables for formatting
FT_DOG = 'dark olive green'
FT_GRY = '#E7E7E7'
LB_N16 = ('Times', 16)
LB_B16 = ('Times Bold', 16)
LB_N18 = ('TImes', 18)
LB_N20 = ('TImes', 20)
LB_B20 = ('Times Bold', 20)


# Create GUI class
class VRES_GUI():

    # Initialising class
    def __init__(self):

        # Create instance
        self.win = tk.Tk()

        # Add a title
        self.win.title("Navigability Analysis of Australian University"
                       " Websites")

        # Running method for menu
        self.generateMenu()

        # Initialising Tab1
        self.createTab1()

        # Window placement
        self.winPlacement()

    # Method to generate the menu items for the app
    def generateMenu(self):
        # Creating a Menu Bar
        self.menuBar = Menu(self.win)
        self.win.config(menu=self.menuBar)

        # Add menu items
        fileMenu = Menu(self.menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.win.destroy)
        self.menuBar.add_cascade(label="File", menu=fileMenu)

        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(self.menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        self.menuBar.add_cascade(label="Help", menu=helpMenu)

    # Generating method for window placement
    def winPlacement(self):
        # Updating the base window to get information
        self.win.update()

        # Generate the desired sized window
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()
        print("Screen width: ", screenWidth, "\t Screen height: ",
              screenHeight)
        winW = self.win.winfo_width()
        winH = self.win.winfo_height()
        print("win width: ", winW, "\t win height: ", winH)
        # win.geometry(("%dx%d") % (winW, winH))

        # Position window in the centre of the screen
        posRight = int(screenWidth/2 - winW/2)
        posDown = int(screenHeight/2 - winH/2)
        self.win.geometry("+{}+{}".format(posRight, posDown))

    # ComboBox CallBack alternation requires label update
    def focusCall(self, event):
        print('focusCall initiatied')
        selectedDegree = self.degree.get()
        print(selectedDegree)
        self.focusChoice.configure(foreground=FT_DOG, text=selectedDegree)

    # Generates items for first tab
    def createTab1(self):
        # Create Tab Control
        self.tabControl = ttk.Notebook(self.win)

        # Adding tabs to the window for organisation & asthetic appeal
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Parameters')
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Analysis')
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='Results')
        # self.tabControl.pack(expand=1, fill='both')
        self.tabControl.grid(row=0, column=0, sticky='NSEW')
        self.tabControl.grid_columnconfigure(0, weight=1)
        self.tabControl.grid_rowconfigure(0, weight=1)

        # Creating frame for right side of tab1
        self.focusBox = ttk.Labelframe(self.tab1, text='Parameter Summary')
        self.focusBox.grid(column=1, row=0, padx=10, pady=10, sticky='NS')
        self.focusBox.grid_columnconfigure(1, weight=1)
        self.focusBox.grid_rowconfigure(0, weight=1)

        # Creating a label to show which focus group has been selected
        self.focusChoice = ttk.Label(self.focusBox, text='Make a Choice',
                                     font=LB_B20)
        self.focusChoice.grid(columnspan=2, row=1, padx=5, pady=5)
        self.focusChoice.grid_rowconfigure(1, weight=1)

        # Creating drop-down menu to specify focus group
        focusLabel = ttk.Label(self.focusBox, text='Focus Group:', font=LB_N18)
        focusLabel.grid(column=0, row=0, padx=5, pady=5)
        focusLabel.grid_columnconfigure(0, weight=1)
        focusLabel.grid_rowconfigure(0, weight=1)

        self.degree = tk.StringVar()
        self.groupChosen = ttk.Combobox(self.focusBox, width=30,
                                        textvariable=self.degree,
                                        state='readonly', validate='all',
                                        justify='center')
        self.groupChosen['values'] = ('Undergraduate, International',
                                      'Undergarduate, Domestic',
                                      'Masters, International',
                                      'Masters, Domestic',
                                      'Doctorate, International',
                                      'Doctorate, Domestic')
        self.groupChosen.grid(column=1, row=0, padx=5, pady=5)
        self.groupChosen.grid_columnconfigure(1, weight=1)
        self.groupChosen.grid_rowconfigure(0, weight=1)
        self.groupChosen.current(0)
        print(self.degree.get())
        self.groupChosen.bind("<<ComboboxSelectd>>", self.focusCall)


mainGui = VRES_GUI()
mainGui.win.mainloop()
