import tkinter as tk

def create_button(frame, text, row, col, command):
    button = tk.Button(frame, text=text, fg='black', bg='lightgray',
                       height=2, width=8, font=('Arial', 14),
                       command=lambda: command(text))
    button.grid(row=row, column=col, padx=5, pady=5)
    return button
