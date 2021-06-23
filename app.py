import tkinter as tk
from tkinter import *

#==== Initialize ====#
window = tk.Tk()
window.geometry("1000x800")
window.title("Mini Project: A Stock Calculator")

#========= UI ==========#

# Entry Price
Entry_price_label = tk.Label(window,text="Entry Price:", font=("Times New Roman", 15))
Entry_price_label.grid(column=0, row=0)
Entry_price_entry = tk.Entry(window,text="")
Entry_price_entry.grid(column=1, row=0)

# Exit Price
Exit_price_label = tk.Label(window,text="Exit Price:", font=("Times New Roman", 15))
Exit_price_label.grid(column=1, row=1)
Entry_price_entry = tk.Entry(window,text="")
Entry_price_entry.grid(column=1, row=0)

# Profit 
profit_label = tk.Label(window,text="Profit:", font=("Times New Roman", 15))
profit_label.grid(column=1, row=2)
Entry_price_entry = tk.Entry(window,text="")
Entry_price_entry.grid(column=1, row=0)









window.mainloop()
