"""GUI Calculator
    This program is GUI based. We are using tkinter library-
    for making calculator interface and lambda function.
    lambda is anonymous function and can take any number of arguments,
    but can only have one expression.
"""
import tkinter as tk
calculation = ""

# Function to evalute the expressopm in the entry field
def evalute_cal():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
    except:
        clear_display()
        text_result.insert(1.0, "Error")


# Add the buttons to the windows
def add_to_cal(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


# Function to clear the display
def clear_display():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")


# Create a application window size
root = tk.Tk()
root.geometry("300x275")
root.title("GUI Calculator")
root.iconbitmap("calculator5.ico")
root.resizable(False, False)

# Create an entry filed
text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan=5)

# Create buttons for the calculator
btn_1 = tk.Button(root, text="1",command=lambda: add_to_cal(1), width=5,font=("Arial",14))
btn_1.grid(row=2, column =1)
btn_2 = tk.Button(root, text="2",command=lambda: add_to_cal(2), width=5,font=("Arial",14))
btn_2.grid(row=2, column =2)
btn_3 = tk.Button(root, text="3",command=lambda: add_to_cal(3), width=5,font=("Arial",14))
btn_3.grid(row=2, column =3)
btn_4 = tk.Button(root, text="4",command=lambda: add_to_cal(4), width=5,font=("Arial",14))
btn_4.grid(row=3, column =1)
btn_5 = tk.Button(root, text="5",command=lambda: add_to_cal(5), width=5,font=("Arial",14))
btn_5.grid(row=3, column =2)
btn_6 = tk.Button(root, text="6",command=lambda: add_to_cal(6), width=5,font=("Arial",14))
btn_6.grid(row=3, column =3)
btn_7 = tk.Button(root, text="7",command=lambda: add_to_cal(7), width=5,font=("Arial",14))
btn_7.grid(row=4, column =1)
btn_8 = tk.Button(root, text="8",command=lambda: add_to_cal(8), width=5,font=("Arial",14))
btn_8.grid(row=4, column =2)
btn_9 = tk.Button(root, text="9",command=lambda: add_to_cal(9), width=5,font=("Arial",14))
btn_9.grid(row=4, column =3)
btn_0 = tk.Button(root, text="0",command=lambda: add_to_cal(0), width=5,font=("Arial",14))
btn_0.grid(row=5, column =2)
btn_dec = tk.Button(root, text=".",command=lambda: add_to_cal('.'), width=5,font=("Arial",14))
btn_dec.grid(row=5, column =1)
btn_per = tk.Button(root, text="%",command=lambda: add_to_cal('%'), width=5,font=("Arial",14))
btn_per.grid(row=5, column =3)
btn_plu = tk.Button(root, text="+",command=lambda: add_to_cal('+'), width=5,font=("Arial",14))
btn_plu.grid(row=2, column =4)
btn_min = tk.Button(root, text="-",command=lambda: add_to_cal('-'), width=5,font=("Arial",14))
btn_min.grid(row=3, column =4)
btn_mul = tk.Button(root, text="x",command=lambda: add_to_cal('*'), width=5,font=("Arial",14))
btn_mul.grid(row=4, column =4)
btn_div = tk.Button(root, text="/",command=lambda: add_to_cal('/'), width=5,font=("Arial",14))
btn_div.grid(row=5, column =4)
btn_clear = tk.Button(root, text="C",command=clear_display, width=11,font=("Arial",14))
btn_clear.grid(row=6, column =1, columnspan=2)
btn_eql = tk.Button(root, text="=",command=evalute_cal, width=11,font=("Arial",14))
btn_eql.grid(row=6, column =3 ,columnspan=2)

root.mainloop()