# written by: https://github.com/Rahul-NITD
import tkinter as tk

def on_button_click(event):
    current_text = result_var.get()
    button_text = event.widget.cget("text")
    
    if button_text == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif button_text == "C":
        result_var.set("")
    else:
        result_var.set(current_text + button_text)

root = tk.Tk()
root.title("CodeClause Calculator - Rahul Goel")

result_var = tk.StringVar()
result_var.set("")

result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 20), anchor="e", padx=20, pady=10)
result_label.pack(fill=tk.BOTH)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0),
]

for (text, row, col) in buttons:
    button = tk.Button(button_frame, text=text, font=("Helvetica", 16), padx=20, pady=20)
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", on_button_click)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
button_frame.columnconfigure(list(range(4)), weight=1)
button_frame.rowconfigure(list(range(6)), weight=1)

root.mainloop()
