from tkinter import *
from tkinter import messagebox
import tkinter as tk

import web_page_gen_func
import web_page_gen_main


#load gui function which is the function called from web_page_gen_main. It loads the following widgets:
def load_gui(self):


#creating a label widget. Syntax is x = Label(master, option,...)
        self.lblContent = Label(self.master, text='Please enter what you would like to see on the webpage:',font = ("Helvetica", 16),fg='black') 
#placing the label widget using grid manager. Padx means how many pixels to pad widget, horizally and vertically
#OUTSIDE the widget.
        self.lblContent.grid(row=0, column=0, columnspan=3, pady= (30,30))
        

#Creating a button widget. "command =" indicates what function or method to be called when button is clicked. "lambda" is small
#inline function that will be activated if button is pressed. "Sticky" answers question of "What to do if the cell is larger than widget?"
#By default, with sticky='', widget is centered in its cell. Sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE,
#and SW, compass directions indicating the sides and corners of the cell to which widget sticks. 
        


        self.btnSubmit = Button(self.master,text="Submit", width=15, height=5, command=lambda:web_page_gen_func.main(self)) 
        self.btnSubmit.grid(row =2, column=2, padx = (30,0), pady= (30,30), sticky =E)

#Creating "Cancel" button widget and positioning it:
        self.btnCancel = Button(self.master, text = "Cancel", command=lambda:web_page_gen_func.ask_quit(self), width=15, height=5)
        self.btnCancel.grid(row = 2, column= 0, padx = (30,0), pady= (30,30), sticky = W)  

#Creating the content box using the "Entry" widget. The method we will use on this in our function page is the get() method
#which will return the current text as a string. ipadx means "how many pixels to pad widget horizontally or vertically INSIDE
#widget.
        
        self.txtContent = Entry(self.master, font=("Helvetica", 16),fg='black', bg ='lightblue',)
        self.txtContent.grid(row = 1, column= 0, ipady=30, ipadx=255, sticky=W, columnspan=3, padx = (30,0), pady= (10,0))


if __name__ == "__main__":
        pass

#when the "pass" keyword is executed nothing happens, but you avoid getting an error when empty code is not allowed. 

