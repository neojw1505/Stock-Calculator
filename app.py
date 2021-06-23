import tkinter as tk
from tkinter import *

#==== Initialize ====#

root = tk.Tk()
root.geometry("500x500")
root.title("Mini Project: A Stock Calculator")

#========== Calculate Profit ==========#

def calculateProfitUI():
    window = tk.Tk()
    window.geometry("500x500")

    # Entry Price
    Entry_price_label = tk.Label(window,text="Entry Price:", font=("Times New Roman", 15))
    Entry_price_label.grid(column=0, row=0)
    Entry_price_entry = tk.Entry(window,text="")
    Entry_price_entry.grid(column=1, row=0)

    # Exit Price
    Exit_price_label = tk.Label(window,text="Exit Price:", font=("Times New Roman", 15))
    Exit_price_label.grid(column=0, row=1)
    Exit_price_entry = tk.Entry(window,text="")
    Exit_price_entry.grid(column=1, row=1)

    # Stock Quantity
    Stock_label = tk.Label(window,text="Shares Qty:", font=("Times New Roman", 15))
    Stock_label.grid(column=0, row=2)
    Stock_entry = tk.Entry(window,text="")
    Stock_entry.grid(column=1, row=2)

    # Commission rate per share
    commission_rps_label = tk.Label(window,text="Commission Rate/share:", font=("Times New Roman", 15))
    commission_rps_label.grid(column=0, row=3)
    commission_rps_entry = tk.Entry(window,text="")
    commission_rps_entry.grid(column=1, row=3)

    # Total Commission Fee 
    commission_fee_label = tk.Label(window,text="Commission Fee:", font=("Times New Roman", 15))
    commission_fee_label.grid(column=0, row=4)
    commission_fee_entry = tk.Entry(window,text="",state="readonly")
    commission_fee_entry.grid(column=1, row=4)

    # Profit 
    profit_label = tk.Label(window,text="Profit:", font=("Times New Roman", 15))
    profit_label.grid(column=0, row=5)
    profit_entry = tk.Entry(window,text="",state="readonly")
    profit_entry.grid(column=1, row=5)

    def calculateCommissionFee():
        commsFee = float(commission_rps_entry.get()) * float(Stock_entry.get()) * 2
        return commsFee

    def calculateProfit():
        commission_fee_entry.configure(state='normal')
        commission_fee_entry.insert(0,calculateCommissionFee())
        commission_fee_entry.configure(state='readonly')

        profit = '{:.2f}'.format(((float(Exit_price_entry.get()) - float(Entry_price_entry.get())) * float(Stock_entry.get())) - float(commission_fee_entry.get()))
        profit_entry.configure(state='normal')
        profit_entry.insert(0,profit)
        profit_entry.configure(state='readonly')
        
    def reset():
        Entry_price_entry.delete(0, END)
        Exit_price_entry.delete(0, END)
        Stock_entry.delete(0, END)
        commission_rps_entry.delete(0, END)

        commission_fee_entry.configure(state='normal')
        commission_fee_entry.delete(0, END)
        commission_fee_entry.configure(state='readonly')
        
        profit_entry.configure(state='normal')
        profit_entry.delete(0, END)
        profit_entry.configure(state='readonly')

    def close():
        window.destroy()

    btn_calculate = tk.Button(window, text="Calculate!", command=calculateProfit) 
    btn_calculate.grid(column=1, row=6)

    btn_reset= tk.Button(window, text="Reset", command=reset) 
    btn_reset.grid(column=1, row=7)

    btn_close = tk.Button(window, text="Close", command=close) 
    btn_close.grid(column=1, row=8)

#========== Dollar Cost Averaging ==========#

def dollarCostAveragingUI():
    window = tk.Tk()
    window.geometry("500x500")

    # Current Price Per Share
    curr_price_label = tk.Label(window,text="Current Price Per Share:", font=("Times New Roman", 15))
    curr_price_label.grid(column=0, row=0)
    curr_price_entry = tk.Entry(window,text="")
    curr_price_entry.grid(column=1, row=0)

    # Current Shares Quantity
    curr_qty_label = tk.Label(window,text="Current Shares Qty:", font=("Times New Roman", 15))
    curr_qty_label.grid(column=0, row=1)
    curr_qty_entry = tk.Entry(window,text="")
    curr_qty_entry.grid(column=1, row=1)

    # Potential Avg Down Price
    avg_down_price_label = tk.Label(window,text="Average Down Share Price:", font=("Times New Roman", 15))
    avg_down_price_label.grid(column=0, row=2)
    avg_down_price_entry = tk.Entry(window,text="")
    avg_down_price_entry.grid(column=1, row=2)

    # Potential Shares Quantity
    avg_down_qty_label = tk.Label(window,text="Average Down Quantity :", font=("Times New Roman", 15))
    avg_down_qty_label.grid(column=0, row=3)
    avg_down_qty_entry = tk.Entry(window,text="")
    avg_down_qty_entry.grid(column=1, row=3)

    # New Price Per Share
    new_pps_label = tk.Label(window,text="New Price Per Share :", font=("Times New Roman", 15))
    new_pps_label.grid(column=0, row=4)
    new_pps_entry = tk.Entry(window,text="",state='readonly')
    new_pps_entry.grid(column=1, row=4)

    def calculateDCA():
        total_value_of_shares = float(curr_price_entry.get()) * float(curr_qty_entry.get()) + float(avg_down_price_entry.get()) * float(avg_down_qty_entry.get())
        total_num_of_shares = float(curr_qty_entry.get()) + float(avg_down_qty_entry.get())
        new_price_per_share = '{:.2f}'.format(total_value_of_shares / total_num_of_shares)
        new_pps_entry.configure(state='normal')
        new_pps_entry.insert(0,new_price_per_share)
        new_pps_entry.configure(state='readonly')

    def reset():
        curr_price_entry.delete(0, END)
        curr_qty_entry.delete(0, END)
        avg_down_price_entry.delete(0,END)
        avg_down_qty_entry.delete(0,END)
        new_pps_entry.configure(state='normal')
        new_pps_entry.delete(0,END)
        new_pps_entry.configure(state='readonly')


    def close():
        window.destroy()

    btn_calculate = tk.Button(window, text="Calculate!", command=calculateDCA) 
    btn_calculate.grid(column=1, row=6)

    btn_reset= tk.Button(window, text="Reset", command=reset) 
    btn_reset.grid(column=1, row=7)

    btn_close = tk.Button(window, text="Close", command=close) 
    btn_close.grid(column=1, row=8)


###==== Button Options ====###

# Calculate Profit Button #
btn_cal_profit = tk.Button(root, text="Calculate Profit", command=calculateProfitUI)
btn_cal_profit.grid(column=1, row=1)

# Dollar Cost Averaging Button #
btn_dollar_cost_avg = tk.Button(root, text="Dollar Cost Averaging", command=dollarCostAveragingUI)
btn_dollar_cost_avg.grid(column=1, row=2)

# Trade History Button #
btn_trade_history = tk.Button(root, text="Trade History", command="")
btn_trade_history.grid(column=1, row=3)

root.mainloop()
