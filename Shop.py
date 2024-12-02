import tkinter as tk
from tkinter import *
from tkinter import messagebox

def singin():
 singinwindow =tk.Tk()
 singinwindow.geometry("300x300")
 singinwindow.title("Sing-in")
 singinwindow.eval('tk::PlaceWindow . center')
 
 usernname_label = tk.Label(singinwindow,text="Please entry your user name")
 usernname_label.pack(pady=5)
 
 username_entry = tk.Entry(singinwindow,width= 30,justify="center")
 username_entry.pack(pady=5)

 password_label = tk.Label(singinwindow,text="Please entry your password")
 password_label.pack(pady=5)

 password_entry = tk.Entry(singinwindow,width=30,justify="center")
 password_entry.pack(pady=5)
 
 def jump_next(event,next_field):
   next_field.focus()
 username_entry.bind("<Return>",lambda event:jump_next(event,password_entry))
 
 def delete_singin():
   username_entry.delete(0,tk.END)
   password_entry.get(0,tk.END)

 login = False
 def validuser():
  nonlocal login
  username = username_entry.get()
  password = password_entry.get()
  while True:
    try:
       if username =="" and password == "":
        singinwindow.destroy()
        login = True
        return
       else:
        delete_singin()
    except:
      messagebox.showerror("","Invalid username or password!")
      return
 
 singin_button = tk.Button(singinwindow,text="Sing-in",command=validuser)
 singin_button.pack(pady=5)

 singinwindow.mainloop()
 return login
    

def shop():
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Shop")
    window.config(bg="#91c1db")
    window.eval('tk::PlaceWindow . center')

    label = tk.Label(window,text="Welcome to Shop",font=('Times New Roman', 25, 'bold') ,bg="#91c1db")
    label.grid(row=0,column=1,pady=50)
 
    def registrationwindow():
     window.withdraw()
     from registration import registration       
     registration()
           
    def additemswindow():
     window.withdraw()
     from additems import additems
     additems()
   
    def calculatorwindow():  
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
     if singin():
       shop()    
    
