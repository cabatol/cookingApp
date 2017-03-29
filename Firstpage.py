import sys
from tkinter import *

def addRecipe():
    mlabel1= Label(mGui, text='you cant do this yet').pack()

mGui = Tk()

mGui.geometry('325x500')
mGui.title('My Cooking App')

mlabel = Label(mGui, text='My Cooking App').place(relx=0.5, rely=.1, anchor=CENTER)
btn1 = Button(mGui, text='Add Recipe', command = addRecipe).place(relx=0.5, rely=0.2, anchor=CENTER)
btn2 = Button(mGui, text='Search Recipe', command = addRecipe).place(relx=0.5, rely=0.3, anchor=CENTER)
btn3 = Button(mGui, text='Learn to Cook', command = addRecipe).place(relx=0.5, rely=0.4, anchor=CENTER)
btn4 = Button(mGui, text='More...', command = addRecipe).place(relx=0.5, rely=0.5, anchor=CENTER)

