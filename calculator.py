import tkinter as tk

def calculator():
    calc = tk.Tk()
    calc.geometry("300x377")
    calc.title("CALCULATOR")
    calc.resizable(True, True)

    entry = tk.Entry(calc, font=("Calibri", 20), width=30, justify="center")
    entry.grid(columnspan=4, sticky="NSEW")

    def write(value):
        entry.insert(tk.END, value)
    
    def clear():
        entry.delete(0, tk.END)

    def calculate():
        expression = entry.get()
        try:
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
         
    calc.grid_columnconfigure(0, weight=1)  
    calc.grid_columnconfigure(1, weight=1)  
    calc.grid_columnconfigure(2, weight=1)  
    calc.grid_columnconfigure(3, weight=1)  
    calc.grid_columnconfigure(4, weight=1)

    button1 = tk.Button(calc, text="1", background="lightgreen", height=4, width=7, command=lambda: write("1"))
    button1.grid(row=1, column=0, sticky="NSEW")

    button2 = tk.Button(calc, text="2", background="lightgreen", height=4, width=7, command=lambda: write("2"))
    button2.grid(row=1, column=1, sticky="NSEW")

    button3 = tk.Button(calc, text="3", background="lightgreen", height=4, width=7, command=lambda: write("3"))
    button3.grid(row=1, column=2, sticky="NSEW")

    button4 = tk.Button(calc, text="4", background="lightgreen", height=4, width=7, command=lambda: write("4"))
    button4.grid(row=2, column=0, sticky="NSEW")

    button5 = tk.Button(calc, text="5", background="lightgreen", height=4, width=7, command=lambda: write("5"))
    button5.grid(row=2, column=1, sticky="NSEW")

    button6 = tk.Button(calc, text="6", background="lightgreen", height=4, width=7, command=lambda: write("6"))
    button6.grid(row=2, column=2, sticky="NSEW")

    button7 = tk.Button(calc, text="7", background="lightgreen", height=4, width=7, command=lambda: write("7"))
    button7.grid(row=3, column=0, sticky="NSEW")

    button8 = tk.Button(calc, text="8", background="lightgreen", height=4, width=7, command=lambda: write("8"))
    button8.grid(row=3, column=1, sticky="NSEW")

    button9 = tk.Button(calc, text="9", background="lightgreen", height=4, width=7, command=lambda: write("9"))
    button9.grid(row=3, column=2, sticky="NSEW")

    button_dot = tk.Button(calc, text=".", background="lightgreen", height=4, width=7, command=lambda: write("."))
    button_dot.grid(row=4, column=0, sticky="NSEW")

    button0 = tk.Button(calc, text="0", background="lightgreen", height=4, width=7, command=lambda: write("0"))
    button0.grid(row=4, column=1, sticky="NSEW")

    button_equals = tk.Button(calc, text="=", height=4, width=7, bg="pink", command=calculate)
    button_equals.grid(row=4, column=2, sticky="NSEW")

    button_plus = tk.Button(calc, text="+", height=4, width=7, bg="lightblue", command=lambda: write("+"))
    button_plus.grid(row=1, column=3, sticky="NSEW")

    button_minus = tk.Button(calc, text="-", height=4, width=7, bg="lightblue", command=lambda: write("-"))
    button_minus.grid(row=2, column=3, sticky="NSEW")

    button_divide = tk.Button(calc, text="/", height=4, width=7, bg="lightblue", command=lambda: write("/"))
    button_divide.grid(row=3, column=3, sticky="NSEW")

    button_multiply = tk.Button(calc, text="*", height=4, width=7, bg="lightblue", command=lambda: write("*"))
    button_multiply.grid(row=4, column=3, sticky="NSEW")

    button_clear = tk.Button(calc, text="C", height=3, width=10, bg="yellow3", command=clear)
    button_clear.grid(row=5, columnspan=4, sticky="NSEW")

    calc.mainloop()
 if __name__ == "__main__":   
 calculator()
