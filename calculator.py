import tkinter as tk

root = tk.Tk()
root.title("DT Intern Calculator")

displayScreen = tk.Entry(root, width=22, borderwidth=5, bg="white", fg="black", font=("Helvetica", 20,"bold"), foreground= "white", background="black", justify='right')
displayScreen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = displayScreen.get()
    displayScreen.delete(0, tk.END)
    displayScreen.insert(0, current + str(number))

def button_clear():
    displayScreen.delete(0, tk.END)

def button_equal():
    try:
        result = eval(displayScreen.get())
        displayScreen.delete(0, tk.END)
        displayScreen.insert(0, result)
    except:
        displayScreen.delete(0, tk.END)
        displayScreen.insert(0, "Error")


button_font = ("Helvetica", 25)

#buttons
button_2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2), bg="black", fg="white", font=button_font)
button_1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1), bg="black", fg="white", font=button_font)
button_3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3), bg="black", fg="white", font=button_font)
button_4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4), bg="black", fg="white", font=button_font)
button_5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5), bg="black", fg="white", font=button_font)
button_6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6), bg="black", fg="white", font=button_font)
button_7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7), bg="black", fg="white", font=button_font)
button_8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8), bg="black", fg="white", font=button_font)
button_9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9), bg="black", fg="white", font=button_font)
button_0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0), bg="black", fg="white", font=button_font)

button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_click("+"), bg="black", fg="white", font=button_font)
button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_click("-"), bg="black", fg="white", font=button_font)
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click("*"), bg="black", fg="white", font=button_font)
button_divide = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_click("/"), bg="black", fg="white", font=button_font)

button_equal = tk.Button(root, text="=", padx=20, pady=20, command=button_equal, bg="black", fg="white", font=button_font)
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear, bg="black", fg="white", font=button_font)

# button placement

button_1.grid(row=1, column=0, padx=5, pady=5)
button_2.grid(row=1, column=1, padx=5, pady=5)
button_3.grid(row=1, column=2, padx=5, pady=5)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_7.grid(row=3, column=0, padx=5, pady=5)
button_8.grid(row=3, column=1, padx=5, pady=5)
button_9.grid(row=3, column=2, padx=5, pady=5)
button_0.grid(row=4, column=1, padx=5, pady=5)

button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)

button_equal.grid(row=4, column=2, padx=5, pady=5)
button_clear.grid(row=4, column=0, padx=5, pady=5)

# Run loop
root.mainloop()
