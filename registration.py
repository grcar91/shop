import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re

def registration():
    window1=tk.Tk()
    window1.geometry("500x450")
    window1.title("Registration")
    window1.configure(bg="silver")
    window1.eval('tk::PlaceWindow . center')

    table=sqlite3.connect("customers.db")
    con=table.cursor()
    con.execute('''CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT NOT NULL, last_name TEXT NOT NULL, address TEXT, email TEXT)''')
    table.commit()

    window1.resizable(False,False)
    window1.grid_columnconfigure(2, weight=1)

    text1=tk.Label(window1,text="Welcome!",bg="silver")
    text1.pack() 

    text2 = tk.Label(window1,text="We need you to trust us with some data!",bg="silver")
    text2.pack()

    insert1 = tk.Label(window1,text="Please enter your first name",bg="silver")
    insert1.pack()

    first_name_entry = tk.Entry(window1,width=15,justify="center")
    first_name_entry.pack()

    insert2 = tk.Label(window1,text="Please enter your last name",bg="silver")
    insert2.pack()

    last_name_entry = tk.Entry(window1,width=15,justify="center")
    last_name_entry.pack()

    text3 = tk.Label(window1,text="Please enter your address",bg="silver")
    text3.pack()

    address_entry = tk.Entry(window1,width=15,justify="center")
    address_entry.pack()

    text4=tk.Label(window1,text="Please enter your email",bg="silver")
    text4.pack()

    email_entry = tk.Entry(window1,width=15,justify="center")
    email_entry.pack()

    text5=tk.Label(window1,text="Thank you for trusting us with your data.",bg="silver")
    text5.pack()

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    def save():
        first_name = first_name_entry.get()            
        last_name = last_name_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        if first_name =="":
            ok = messagebox.showerror("","Name is missing!")
            return                          
        if last_name == "":
            ok = messagebox.showerror("","Last name is missing!")
            return                   
        if address == "":
            ok = messagebox.showerror("","Address is missing!")
            return
        if email == "":
            ok = messagebox.showerror("","Email is missing!")
            return
        if not (re.fullmatch(regex,email)):       
            ok = messagebox.showerror("","Please inserte email!")
            return
      

        sql="INSERT INTO customers(first_name, last_name, address, email) VALUES(?,?,?,?)"
        data=(first_name,last_name,address,email)
        con.execute(sql,data)
        table.commit()
        return True

    def delete():
        first_name_entry.delete(0,tk.END)
        last_name_entry.delete(0,tk.END)
        address_entry.delete(0,tk.END)
        email_entry.delete(0,tk.END)
   
    def show_customer():
        con.execute("SELECT * FROM customers")
        all_customers=con.fetchall()
        sorted_customers=sorted(all_customers,reverse=True)

        customer_window=tk.Toplevel(window1)
        customer_window.geometry("300x300")
        customer_window.title("Customers")
        listbox=tk.Listbox(customer_window,width=40,border=3)
        listbox.grid(row=2,column=0)

        for customer in sorted_customers:
            listbox.insert(0,customer)

        def delete_customer():
            try:
                selected_index=listbox.curselection()[0]
                selected_customer=listbox.get(selected_index)
                selected_id=selected_customer[0]
                listbox.delete(selected_index)
                cursor=table.cursor()
                cursor.execute("DELETE FROM customers WHERE id = ?",(selected_id,))
                table.commit()
            except:
                pass 

        def confirm_delete():     
            sure=messagebox.askyesno("Delete","Are you sure?")
            if sure:
                delete_customer()
            else:
                pass    

        delete_button=tk.Button(customer_window,text="Delete",width=5,command=confirm_delete)
        delete_button.grid(row=1,column=3)

    def jump_next(event,next_field):
        next_field.focus()

    first_name_entry.bind("<Return>",lambda x:jump_next(x,last_name_entry))
    last_name_entry.bind("<Return>",lambda x:jump_next(x,address_entry))
    address_entry.bind("<Return>",lambda x:jump_next(x,email_entry))
    email_entry.bind("<Return>",lambda x:jump_next(x,save_button))

    def save_success():
        if save():
          delete()
          messagebox.showinfo(" ","Saved")
          first_name_entry.focus()
        
    def open_shop():
        window1.destroy()
        from Shop import shop
        shop()
        

    save_button=tk.Button(window1,text="SAVE",width=10,bg="#0c6b2d",fg="gold",command=save_success)
    save_button.pack()

    show_button=tk.Button(window1,text="Show clients",width=10,fg="gold",bg="#0c0f6b",command=show_customer)
    show_button.pack()

    delete_button=tk.Button(window1,text="Delete",width=10,fg="gold",bg="#70110d",command=delete)
    delete_button.pack()

    shop_button=tk.Button(window1,text="Back to Shop",width=10,fg="gold",bg="#70110d",command=open_shop)
    shop_button.pack()

    window1.mainloop()

registration()
