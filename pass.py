import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1.")
            return
        
        characters = string.ascii_lowercase
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if digits_var.get():
            characters += string.digits
        if special_chars_var.get():
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        
        messagebox.showinfo("Generated Password", f"Your Password: {password}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x600")  
root.resizable(False, False)
root.configure(bg="#2c3e50")

font_large = ("Helvetica", 18, "bold")
font_medium = ("Helvetica", 14)
font_small = ("Helvetica", 12)

input_frame = tk.Frame(root, bg="#34495e", pady=20, padx=20)
input_frame.pack(pady=20, padx=20, fill="x")

tk.Label(input_frame, text="Password Generator", font=font_large, bg="#34495e", fg="#ecf0f1").pack(pady=10)

length_label = tk.Label(input_frame, text="Enter the desired length of the password:", font=font_medium, bg="#34495e", fg="#ecf0f1")
length_label.pack(anchor="w", pady=10)

length_entry = tk.Entry(input_frame, font=font_medium, bd=2, relief="solid")
length_entry.pack(fill="x", pady=10)

options_frame = tk.Frame(root, bg="#34495e", pady=20, padx=20)
options_frame.pack(pady=20, padx=20, fill="x")

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(options_frame, text="Include uppercase letters", variable=uppercase_var, font=font_small, bg="#34495e", fg="#ecf0f1", selectcolor="#1abc9c").pack(anchor="w", pady=5)

digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(options_frame, text="Include digits", variable=digits_var, font=font_small, bg="#34495e", fg="#ecf0f1", selectcolor="#1abc9c").pack(anchor="w", pady=5)

special_chars_var = tk.BooleanVar(value=True)
tk.Checkbutton(options_frame, text="Include special characters", variable=special_chars_var, font=font_small, bg="#34495e", fg="#ecf0f1", selectcolor="#1abc9c").pack(anchor="w", pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=font_medium, bg="#e74c3c", fg="white", padx=20, pady=10, relief="raised", borderwidth=1, highlightthickness=0)
generate_button.pack(pady=20)

result_frame = tk.Frame(root, bg="#34495e", pady=20, padx=20)
result_frame.pack(pady=20, padx=20, fill="x")

tk.Label(result_frame, text="Generated Password:", font=font_medium, bg="#34495e", fg="#ecf0f1").pack(anchor="w", pady=10)

password_entry = tk.Entry(result_frame, font=font_medium, state='readonly', readonlybackground="#ecf0f1", fg="#2c3e50", bd=2, relief="solid")
password_entry.pack(fill="x", pady=10)

root.mainloop()
