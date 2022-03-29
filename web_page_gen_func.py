
import webbrowser
import os.path
from tkinter import *
from tkinter import messagebox
import tkinter as tk


import web_page_gen_gui
import web_page_gen_main


#Defining function called "main"

def main(self):
    contents = self.txtContent.get() #assigning a variable called "contents" and using the get()
    #method on the entry box to get the input the user put in.
    browserLocal(contents)#pass this content in to the "browserLocal" function.
    
def strToFile(contents,filename): #function that puts the content on to the file. 
    output = open(filename,"w") #assigning variable called "output", making it equal to open method
    #syntax open(file,mode). "w" means opens a file for writing, creates the file if it does not exist
    output.write(contents) #write the contents to file
    output.close() #close the file

#Defining the function and giving it parameters of "contents" and filename.
def browserLocal(contents, filename='web_gen_challenge.html'):
    strToFile(contents, filename)  #call function directly above which writes string to file.
    webbrowser.open_new_tab("file:///" + os.path.abspath(filename)) #using the webbrowser module and the open_new_tab function open
    #default webbrowser by concatenation "file:/// plus the absolute path of filename

def ask_quit(self):

#"messagebox module is used to display message boxes. Askokcancel() function shows a confirmation dialog that has two buttons: OK and Cancel. 
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy() #destroy() method destroys widget (our main window), frees the memory and clears the screen. 
        os._exit(0)#using the os module (that allows interaction with os), exit the program. The "0" means a clean exit without
        #any errors/problems.  

if __name__ == "__main__":
   pass




