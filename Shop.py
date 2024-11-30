import tkinter as tk
from tkinter import *

def shop():

 window = tk.Tk()
 window.geometry("500x500")
 window.title("Shop")
 window.config(bg="#91c1db")
 window.eval('tk::PlaceWindow . center')

 label = tk.Label(window,text="Welcome to Shop",font=('Times New Roman', 25, 'bold') ,bg="#91c1db")
 label.grid(row=0,column=1,pady=50)
 
 def registrationwindow():
   window.destroy()
   from registration import registration       
   registration()
         
 def additemswindow():
   window.destroy()
   from additems import additems
   additems()
    
 def calculatorwindow():  
   window.destroy()
   from calculator import calculator
   calculator()
   
 more = tk.Button(window,text="Customers",bg="#59c94f", command = registrationwindow)
 more.grid(row=1,column=0,padx=15,pady=10)

 more1 = tk.Button(window,text="Items",bg="#bf5252", command = additemswindow)
 more1.grid(row=1,column=1,padx=10,pady=10)

 more2 = tk.Button(window,text="calculator",bg="#bfa952", command = calculatorwindow  )
 more2.grid(row=1, column=2,padx=10,pady=10)


 window.mainloop()
if __name__ == "__main__":
 shop() 
