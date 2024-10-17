import tkinter as tk
from tkinter import messagebox
import mysql.connector
from db_connection import get_db_connection  # Import the database connection function

# Function to open the Testing window
def open_testing_window():
    testing_window = tk.Toplevel()
    testing_window.title("Testing Section")
    testing_window.geometry("400x400")

    # Label for the input boxes
    input_label = tk.Label(testing_window, text="Enter Testing Details:", font=("Arial", 12))
    input_label.pack(pady=10)

    # Input box for PCB
    pcb_label = tk.Label(testing_window, text="PCB:", font=("Arial", 10))
    pcb_label.pack(pady=5)
    pcb_input = tk.Entry(testing_window, font=("Arial", 12), width=30)
    pcb_input.pack(pady=5)

    # Input box for Testing Status
    status_label = tk.Label(testing_window, text="Testing Status:", font=("Arial", 10))
    status_label.pack(pady=5)
    status_input = tk.Entry(testing_window, font=("Arial", 12), width=30)
    status_input.pack(pady=5)

    # Submit button
    submit_button = tk.Button(testing_window, text="Submit", font=("Arial", 12), 
                              command=lambda: submit_testing(pcb_input.get(), status_input.get()))
    submit_button.pack(pady=20)

# Function to handle Testing input submission
def submit_testing(pcb_code, testing_status):
    # Prompt user to input a test name for better data management
    test_name = "Default Test Name"  # You can prompt the user for this value, or set a default

    if pcb_code.strip() and len(testing_status) == 4:  # Validate inputs
        conn = get_db_connection()  # Get the database connection
        if conn:  # If connection is successful
            cursor = conn.cursor()
            try:
                # Check if PCB exists in the PCB table
                cursor.execute("SELECT id FROM PCB WHERE pcb_code = %s", (pcb_code,))
                pcb_result = cursor.fetchone()

                if pcb_result:  # PCB exists
                    pcb_id = pcb_result[0]
                    # Insert the data into Testing table
                    insert_query = "INSERT INTO Testing (test_name, pcb_id, test_result) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (test_name, pcb_id, testing_status))

                    # Commit the transaction
                    conn.commit()
                    messagebox.showinfo("Success", "Testing details submitted successfully.")
                else:
                    messagebox.showerror("Invalid PCB", "PCB does not match any entry in the PCB table.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                cursor.close()
                conn.close()  # Always close the connection
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database.")
    else:
        messagebox.showerror("Error", "Testing Status must be exactly 4 letters.")
