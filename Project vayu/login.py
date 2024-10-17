# login.py

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv
from dashboard import open_dashboard

# Load environment variables from .env file
load_dotenv()

# MySQL connection details from environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),  # Use default to 'localhost'
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'D252V4L3t8xTC7F'),
    'database': os.getenv('DB_NAME', 'solar')
}

# Function to handle login
def login(username, password, root):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            messagebox.showinfo("Login Successful", "Welcome!")
            open_dashboard(root)  # Open the dashboard if login is successful
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Function to create the login window
def create_login_window():
    root = tk.Tk()
    root.title("Solar VAYU Login")
    root.geometry("400x400")

    # Header
    header_frame = tk.Frame(root)
    header_frame.pack(pady=10)
    header_label = tk.Label(header_frame, text="SOLAR VAYU", font=("Arial", 24, "bold"))
    header_label.pack()
    sub_header_label = tk.Label(header_frame, text="MAKING SOLAR SPOTLESS", font=("Arial", 14))
    sub_header_label.pack()

    # Login container
    login_frame = tk.Frame(root)
    login_frame.pack(pady=20)

    username_label = tk.Label(login_frame, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)

    username_entry = tk.Entry(login_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(login_frame, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)

    password_entry = tk.Entry(login_frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    # Login button
    login_button = tk.Button(login_frame, text="LOGIN", command=lambda: login(username_entry.get(), password_entry.get(), root))
    login_button.grid(row=2, columnspan=2, pady=10)

    # Cancel button
    cancel_button = tk.Button(login_frame, text="Cancel", command=root.quit)
    cancel_button.grid(row=3, columnspan=2, pady=5)

    # Footer
    footer_frame = tk.Frame(root)
    footer_frame.pack(pady=10)
    footer_label = tk.Label(footer_frame, text="© 2023 Solar VAYU. All rights reserved.")
    footer_label.pack()

    # Start the Tkinter main loop
    root.mainloop()
