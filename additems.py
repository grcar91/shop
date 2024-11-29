import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def additems():
    windo = tk.Tk()
    windo.geometry("600x350")
    windo.title("Inventory of Materials")
    windo.resizable(False, False)
    windo.eval('tk::PlaceWindow . center')


    database = sqlite3.connect("Inventory.db")
    cursor = database.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Inventory(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 Product_Code INTEGER,
                 Product_Name TEXT,
                 Manufacturer TEXT,
                 Year INTEGER,
                 Stock INTEGER)''')
    database.commit()

    label1 = tk.Label(windo, text="Be careful when entering data!", font="arial,10", justify="center")
    label1.grid(row=0, column=3, sticky=tk.E)

    label_code = tk.Label(windo, font=7, text="Product Code:")
    label_code.grid(row=1, column=0)

    entry_code = tk.Entry(windo, width=30, justify="center")
    entry_code.grid(row=2, column=0)

    label_stock = tk.Label(windo, font=7, text="Product Stock:")
    label_stock.grid(row=2, column=3)

    entry_stock = tk.Entry(windo, width=30, justify="center")
    entry_stock.grid(row=3, column=3)

    label_name = tk.Label(windo, font=7, text="Product Name:")
    label_name.grid(row=1, column=5)

    entry_name = tk.Entry(windo, width=30, justify="center")
    entry_name.grid(row=2, column=5)

    label_manufacturer = tk.Label(windo, font=7, text="Manufacturer:")
    label_manufacturer.grid(row=3, column=0)

    entry_manufacturer = tk.Entry(windo, width=30, justify="center")
    entry_manufacturer.grid(row=4, column=0)

    label_year = tk.Label(windo, font=7, text="Year of Manufacture:")
    label_year.grid(row=3, column=5)

    entry_year = tk.Entry(windo, width=30, justify="center")
    entry_year.grid(row=4, column=5)

    def save_data():
        def check_num(entry):
            try:
                int(entry)
                return False
            except:
                return True

        code = entry_code.get()
        name = entry_name.get()
        manufacturer = entry_manufacturer.get()
        year = entry_year.get()
        stock = entry_stock.get()

        cursor = database.cursor()
        exist = cursor.execute("SELECT * FROM Inventory WHERE Product_Code = ?", (code,)).fetchone()
        if exist is None:
            sql = "INSERT INTO Inventory(Product_Code, Product_Name, Manufacturer, Year, Stock) VALUES(?,?,?,?,?)"
            data = (code, name, manufacturer, year, stock)
            cursor.execute(sql, data)
            database.commit()
        if code =="":
            ok = messagebox.showerror("","Insert Code!")  
            return 
        if check_num(code) == True :
            ok = messagebox.showerror("","Insert Code!")  
            return False
        else:
            sql1 = "UPDATE Inventory SET Product_Name=?, Manufacturer=?, Year=?, Stock=? WHERE Product_Code=?"
            data1 = (name, manufacturer, year, stock, code)
            cursor.execute(sql1, data1)
            database.commit()
            return True    

       
    def save_ok():
        if save_data():
            ok = messagebox.OK("","Data saved!")

    def clear_entries():
        entry_code.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_manufacturer.delete(0, tk.END)
        entry_stock.delete(0, tk.END)
        entry_year.delete(0, tk.END)

    def save_and_clear():
        save_data()
        clear_entries()

    def show_products():
        cursor = database.cursor()
        cursor.execute("SELECT * FROM Inventory")
        data = cursor.fetchall()
        print(data)

        new_window = tk.Toplevel(windo)
        new_window.geometry("400x400")
        new_window.title("List")        
        displayed = tk.Listbox(new_window, width=40, border=3)
        displayed.grid(row=2, column=2)

        for item in data:
            displayed.insert(0, item)
        database.commit()
        cursor.close()

        def delete():
            try:
                delete_index = displayed.curselection()[0]
                delete_item = displayed.get(delete_index)
                delete_id = delete_item[0]
                displayed.delete(delete_index)
                cursor = database.cursor()
                cursor.execute("DELETE FROM Inventory WHERE id=?", (delete_id,))
                database.commit()
                cursor.close()
            except:
                pass

        def edit():
            try:
                edit_index = displayed.curselection()[0]
                edit_item = displayed.get(edit_index)
                entry_code.insert(0, edit_item[1])
                entry_name.insert(0, edit_item[2])
                entry_manufacturer.insert(0, edit_item[3])
                entry_stock.insert(0, edit_item[5])
                entry_year.insert(0, edit_item[4])
            except:
                pass
            new_window.destroy()
        def confirm_delete():
            confirm = messagebox.askyesno("Delete", "Are you sure?")
            if confirm:
                delete()

        edit_button = tk.Button(new_window, width=20, text="Edit Product", justify="center", command=edit)
        edit_button.grid(row=2, column=3)

        delete_button = tk.Button(new_window, width=20, text="Delete", justify="center", command=confirm_delete)
        delete_button.grid(row=1, column=3)

    def jump_next(x, next_field):
        next_field.focus()

    entry_code.bind("<Return>", lambda x: jump_next(x, entry_name))
    entry_name.bind("<Return>", lambda x: jump_next(x, entry_manufacturer))
    entry_manufacturer.bind("<Return>", lambda x: jump_next(x, entry_year))
    entry_year.bind("<Return>", lambda x: jump_next(x, entry_stock))

    def open_shop():
        windo.destroy()
        from Shop import shop
        shop()
        

    save_button = tk.Button(windo, width=20, text="Save", fg="red", bg="lightgreen", justify="center", command=save_and_clear)
    save_button.grid(row=5, column=3)

    show_button = tk.Button(windo, width=20, text="Show Products", fg="red", bg="lightgreen", justify="center", command=show_products)
    show_button.grid(row=7, column=3)

    clear_button = tk.Button(windo, width=20, text="Clear", fg="white", bg="red", justify="center", command=clear_entries)
    clear_button.grid(row=8, column=3)

    shop_button=tk.Button(windo,text="Back to Shop",width=20,fg="gold",bg="#70110d",command=open_shop)
    shop_button.grid(row=9, column=3)

    windo.mainloop()
if __name__ == "__main__":
 additems()
