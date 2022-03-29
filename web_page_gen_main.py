#Project: Webpage Generator

#Author: Vicky Jones-Farias

#Python Version: 3.9.5

#Written and tested on Windows 10

#Minimum project requirements:


#Creates a GUI that allows the user to input text and initiate the web page generation process.
#Generates a web page that sets the user’s input as the body text for the web page.
#Opens the generated web page in the browser..
#Contains comments throughout your Python files explaining your code.

import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk

#import my own files:
import web_page_gen_gui
import web_page_gen_func

#define a class that I called ParentWindow, and make it inherit the parent class attributes
#and method called "Frame". Syntax childclass(parent)

class ParentWindow(Frame):

#def__init__ stands for "initialize". It is a reserved method in python classes. It is automatically called
#every time the class is being used to create a new object. It assigns values to the object properties.
#It creates an instance of the class. It is a "dunder" method (or magic method).

#parameters of init method are always "self" which means the object being created, and then the object properties
#Eg.class Person:
  #def __init__(self, name, age):
    #self.name = name
    #self.age = age

#NB. the use of the period in python connects the attributes or methods to the object. 

    
    def __init__ (self,master):
        
        self.master = master
#Resizable method (if "True") allows user to resize the window object. 
        self.master.resizable(width = True, height = True)
#Geometry method here sets the dimensions of the window object
        self.master.geometry('{}x{}'.format(800,350))
#Title method puts a title on the window object
        self.master.title('Webpage Generator')
#Config method used in this case to change the property of the widget
        self.master.config(bg='lightgray')


#Calling the function "load gui"
        web_page_gen_gui.load_gui(self)


        




if __name__ == "__main__":
        root = Tk() # classes usually start with capital letter. Here we instantiate tkinter and assign it "root"
        App = ParentWindow(root)
        root.mainloop() #makes window stay alive. 

