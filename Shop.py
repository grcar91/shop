import tkinter as tk
from tkinter import *
from tkinter import messagebox
login = False 
def singin():
 global login
 login = False

 singinwindow =tk.Tk()
 singinwindow.geometry("300x350")
 singinwindow.title("Sing-in")
 singinwindow.eval('tk::PlaceWindow . center')

 main_frame = tk.Frame(singinwindow)
 main_frame.pack(fill="both",expand=True)

 def clear():
    for widget in main_frame.winfo_children():
       widget.destroy()
 
 def registration_window(eventi):
    clear()

    def go_next(events,next):
       next.focus()

    name_label = tk.Label(main_frame,text="Please entry your name")
    name_label.pack(pady=5)
 
    name_entry = tk.Entry(main_frame,width= 30,justify="center")
    name_entry.pack(pady=5)
    name_entry.bind("<Return>",lambda events:go_next(events,username_entry))

    usernname_label = tk.Label(main_frame,text="Please entry your user name")
    usernname_label.pack(pady=5)

    username_entry = tk.Entry(main_frame,width= 30,justify="center")
    username_entry.pack(pady=5)
    username_entry.bind("<Return>",lambda events:go_next(events,password_entry))

    password_label = tk.Label(main_frame,text="Please entry your password")
    password_label.pack(pady=5)
  
    password_entry = tk.Entry(main_frame,width=30,justify="center")
    password_entry.pack(pady=5)
    password_entry.bind("<Return>",lambda events:go_next(events,password2_entry))
    

    password2_label = tk.Label(main_frame,text="Please confirm your password")
    password2_label.pack(pady=5)
  

    def save_data():
      name = name_entry.get()
      user_name = username_entry.get()
      password =password_entry.get() 
      password2= password2_entry.get()

      if password == password2:
        with open ("users.txt","a") as file:
          file.write(f" Name:{name},User_name:{user_name}, Password:{password}\n")

      else:
        messagebox.showerror("Error","Passwords not macht! Try agai")
        password_entry.delete(0,tk.END)
        password2_entry.delete(0,tk.END)
        return 

    password2_entry = tk.Entry(main_frame,width=30,justify="center")
    password2_entry.pack(pady=5) 
    password2_entry.bind("<Return>",save_data)

    save = tk.Button(main_frame,text="SAVE",command= save_data)
    save.pack(pady=5)

    back = tk.Button(main_frame,text="Back",command=sinng)
    back.pack(pady= 5)
 
 def sinng():
   clear()
   usernname_label = tk.Label(main_frame,text="Please entry your user name")
   usernname_label.pack(pady=5)
 
   username_entry = tk.Entry(main_frame,width= 30,justify="center")
   username_entry.pack(pady=5)

   password_label = tk.Label(main_frame,text="Please entry your password")
   password_label.pack(pady=5)
  

 
   def jump_next(event,next_field):
    next_field.focus()
   username_entry.bind("<Return>",lambda event:jump_next(event,password_entry))
    
   def delete_singin():
    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
  
   def password_show():
    if password_entry.cget("show") == "":
      password_entry.config(show="*")
      show_button.config(text="show password")
    else:
      password_entry.config(show="")
      show_button.config(text="hide password")
 
   
   def validuser():
      global login
                 
      username = username_entry.get()
      password = password_entry.get()
      try:
          with open("users.txt", "r") as file:
                users = file.readlines()

          for user in users:
              parts = user.strip().split(",")
              if len(parts) == 3:
                  _, User_name, Password = parts
                  if User_name.split(":")[1].strip() == username and Password.split(":")[1].strip() == password:
                      singinwindow.destroy()
                      login = True
                      return login       
                  else:
                       messagebox.showerror("", "Invalid username or password!")
                       delete_singin()
            
      except FileNotFoundError:                 
        messagebox.showerror("", "User file not found!")
      
   password_entry = tk.Entry(main_frame,width=30, show="*",justify="center")
   password_entry.pack(pady=5)
   password_entry.bind("<Return>",validuser) 

   show_button = tk.Button(main_frame,text="Show",command=password_show)
   show_button.pack(pady=5)

   singin_button = tk.Button(main_frame,text="Sing-in",command=validuser)
   singin_button.pack(pady=5)
 
   not_Label = tk.Label(main_frame,text="Not registered?",fg= "blue",cursor = "hand2" )
   not_Label.pack(pady=5)
   not_Label.bind("<Button-1>",registration_window)

 sinng()
 main_frame.mainloop()
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
    
