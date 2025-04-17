import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="groove", justify='right')
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

def button_click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Помилка", "Ділення на нуль!")
        clear()
    except Exception:
        messagebox.showerror("Помилка", "Некоректний вираз!")
        clear()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = calculate if btn == '=' else (clear if btn == 'C' else lambda b=btn: button_click(b))
        tk.Button(frame, text=btn, font=("Arial", 18), command=action).pack(side="left", expand=True, fill="both")

tk.Button(root, text='C', font=("Arial", 18), command=clear, bg='red', fg='white').pack(fill="both", padx=10, pady=(0,10))

root.mainloop()
