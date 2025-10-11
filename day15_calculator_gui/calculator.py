import tkinter as tk
from gui_components import create_button

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400")

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        # Button layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, char in enumerate(row):
                create_button(btns_frame, char, row_index, col_index, self.button_click)

        clear_btn = tk.Button(btns_frame, text='C', fg='white', bg='red', height=2, width=32, command=self.clear)
        clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

    def button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
