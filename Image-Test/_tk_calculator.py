# =============================================================================
# This is the script made with baroukh404 app
# =============================================================================

# importing the tkinter module 
import tkinter 
from tkinter import * 
   
# creating a window for the Calculator 
calci = tkinter.Tk() 
calci.title("Calculator")  

# Display screen for result
text_input = StringVar() 
operator=''
t_screen = Entry(calci, textvariable = text_input, bd = 20, insertwidth = 4, font ="italian 20 bold", bg = "Light Blue").grid(columnspan = 7)

def clickbut(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)
# Defining Buttons
b1 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "1", command = lambda:clickbut(1)).grid(row = 3, column = 0)
b2 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "2", command = lambda:clickbut(2)).grid(row = 3, column = 1)
b3 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "3", command = lambda:clickbut(3)).grid(row = 3, column = 2)
bplus = Button(calci, padx = 8, bd = 8, bg = 'blue', fg = "black", font = ("arial", 16, 'bold'), text = "+", command = lambda:clickbut('+')).grid(row = 3, column = 3)

b4 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "4", command = lambda:clickbut(4)).grid(row = 2, column = 0)
b5 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "5", command = lambda:clickbut(5)).grid(row = 2, column = 1)
b6 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "6", command = lambda:clickbut(6)).grid(row = 2, column =2)
bmul = Button(calci, padx = 8, bd = 8, bg = 'blue', fg = "black", font = ("arial", 16, 'bold'), text = "*", command = lambda:clickbut('*')).grid(row = 2, column = 3)

b7 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "7", command = lambda:clickbut(7)).grid(row = 1, column = 0)
b8 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "8", command = lambda:clickbut(8)).grid(row = 1, column = 1)
b9 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "9", command = lambda:clickbut(9)).grid(row = 1, column = 2)
bdiv = Button(calci, padx = 8, bd = 8, bg = 'blue', fg = "black", font = ("arial", 16, 'bold'), text = "/", command = lambda:clickbut("/")).grid(row = 1, column = 3)

b0 = Button(calci, padx = 8, bd = 8, bg = 'red', fg = "black", font = ("arial", 16, 'bold'), text = "0", command =lambda:clickbut(0)).grid(row = 4, column = 0)
bc = Button(calci, padx = 8, bd = 8, bg = 'green', fg = "black", font = ("arial", 16, 'bold'), text = "c", command =lambda:clickbut("C")).grid(row = 4, column = 1)
bequal = Button(calci, padx = 8, bd = 8, bg = 'orange', fg = "black", font = ("arial", 16, 'bold'), text = "=",command = lambda:result()).grid(row = 4, column = 2)

# Function to evaluate the result
def result(): 
    res = str(eval(operator)) 
    text_input.set(res)
    operator=res
    
# Creating an infinite loop for running the application

calci.mainloop()