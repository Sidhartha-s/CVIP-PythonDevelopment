import tkinter as tk

def onclick(value):
    current_value = disp.get()
    disp.delete(0, tk.END)
    disp.insert(tk.END, current_value + value)

def clear_display():
    disp.delete(0, tk.END)

def calculate_result():
    try:
        expression = disp.get()
        result = eval(expression)
        disp.delete(0, tk.END)
        disp.insert(tk.END, str(result))
    except Exception as e:
        disp.delete(0, tk.END)
        disp.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")
window.configure(bg="#333333")

disp = tk.Entry(window, width=16, font=('Arial', 20), bd=5, bg="#333333", fg="#FFFFFF")
disp.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for i in buttons:
    if i != '=' and i != 'C':
        if i.isdigit():
            bg_color = "#666666"
        else:
            bg_color = "#4d90fe"
        tk.Button(window, text=i, width=4, height=2, bg=bg_color, fg="#FFFFFF", bd=0,
                  command=lambda value=i: onclick(value)).grid(row=row, column=col, padx=2, pady=2)
    elif i == 'C':
        tk.Button(window, text=i, width=4, height=2, bg="#ff6666", fg="#FFFFFF", bd=0,
                  command=clear_display).grid(row=row, column=col, padx=2, pady=2)
    else:
        tk.Button(window, text=i, width=4, height=2, bg="#666666", fg="#FFFFFF", bd=0,
                  command=calculate_result).grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.resizable(False, False)

window.mainloop()
