import tkinter as tk
from tkinter import messagebox
import mysql.connector  # Import the MySQL connector
from db_connection import get_db_connection  # Import the database connection function

# Function to open the Assembly window
def open_mainassembly_window():
    mainassembly_window = tk.Toplevel()  # Create a new window for mainassembly
    mainassembly_window.title("Main Assembly Section")
    mainassembly_window.geometry("600x400")

    # Label for the input boxes
    input_label = tk.Label(mainassembly_window, text="Enter Assembly Details:", font=("Arial", 12))
    input_label.pack(pady=10)

    # Input box for Motor
    motor_label = tk.Label(mainassembly_window, text="Motor:", font=("Arial", 10))
    motor_label.pack(pady=5)
    motor_input = tk.Entry(mainassembly_window, font=("Arial", 12), width=30)
    motor_input.pack(pady=5)

    # Input box for Battery
    battery_label = tk.Label(mainassembly_window, text="Battery:", font=("Arial", 10))
    battery_label.pack(pady=5)
    battery_input = tk.Entry(mainassembly_window, font=("Arial", 12), width=30)
    battery_input.pack(pady=5)

    # Input box for Gear Box
    gearbox_label = tk.Label(mainassembly_window, text="Gear Box:", font=("Arial", 10))
    gearbox_label.pack(pady=5)
    gearbox_input = tk.Entry(mainassembly_window, font=("Arial", 12), width=30)
    gearbox_input.pack(pady=5)

    # Submit button
    submit_button = tk.Button(mainassembly_window, text="Submit", font=("Arial", 12), 
                              command=lambda: submit_mainassembly(motor_input.get(), battery_input.get(), gearbox_input.get()))
    submit_button.pack(pady=20)

# Function to handle mainassembly input submission
def submit_mainassembly(motor, battery, gearbox):
    if motor.strip() and battery.strip() and gearbox.strip():  # Check if all inputs are not empty
        try:
            # Get the database connection
            conn = get_db_connection()  # Assuming get_db_connection returns a valid connection
            cursor = conn.cursor()

            # Prepare the INSERT statement
            insert_query = "INSERT INTO mainassembly (motor, battery, gear_box) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (motor, battery, gearbox))

            # Commit the transaction
            conn.commit()
            messagebox.showinfo("Success", "Assembly details submitted successfully.")

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            # Ensure the cursor and connection are closed
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    else:
        messagebox.showerror("Error", "Please fill in all details.")

# This function can be called to open the Assembly window in the main application.
