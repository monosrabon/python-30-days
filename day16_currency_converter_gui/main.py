import customtkinter as ctk
from tkinter import messagebox
from api_handler import get_exchange_rate

import customtkinter as ctk
from tkinter import messagebox
from api_handler import get_exchange_rate

# Initialize custom theme
ctk.set_appearance_mode("light")  # "dark" or "light"
ctk.set_default_color_theme("blue")

# App Window
app = ctk.CTk()
app.title("💱 Modern Currency Converter")
app.geometry("420x400")
app.resizable(False, False)

# Heading
title_label = ctk.CTkLabel(app, text="💱 Currency Converter", font=ctk.CTkFont(size=22, weight="bold"))
title_label.pack(pady=20)

# Frame for inputs
frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=20, fill="both", expand=True)

# Amount input
ctk.CTkLabel(frame, text="Amount:", font=ctk.CTkFont(size=14)).grid(row=0, column=0, padx=10, pady=10)
amount_entry = ctk.CTkEntry(frame, placeholder_text="Enter amount")
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# Currency options
currencies = ["USD", "EUR", "BDT", "INR", "GBP", "CAD", "JPY", "AUD"]

ctk.CTkLabel(frame, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
from_currency = ctk.CTkComboBox(frame, values=currencies)
from_currency.set("USD")
from_currency.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkLabel(frame, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
to_currency = ctk.CTkComboBox(frame, values=currencies)
to_currency.set("BDT")
to_currency.grid(row=2, column=1, padx=10, pady=10)

# Output Label
result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=16))
result_label.pack(pady=20)

# Convert Function
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        rate = get_exchange_rate(from_curr, to_curr)
        result = round(amount * rate, 2)

        result_label.configure(text=f"{amount} {from_curr} = {result} {to_curr}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Convert Button
convert_btn = ctk.CTkButton(app, text="Convert", command=convert_currency, width=200, height=40, corner_radius=10)
convert_btn.pack(pady=15)

# Run App
app.mainloop()
