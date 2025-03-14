import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# Configurar ventana principal
root = tk.Tk()
root.title("Calculadora")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Botones de la calculadora
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, font=("Arial", 18), width=5, height=2, 
              command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()