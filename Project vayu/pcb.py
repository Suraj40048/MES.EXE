import tkinter as tk
from tkinter import messagebox
import mysql.connector
from db_connection import get_db_connection  # Import the database connection function
import re  # Import regex library for validation

# Function to open the PCB window
def open_pcb_window():
    pcb_window = tk.Toplevel()
    pcb_window.title("PCB Section")
    pcb_window.geometry("400x400")

    # Label for the input box
    input_label = tk.Label(pcb_window, text="Enter PCB Details (Format: A12345):", font=("Arial", 12))
    input_label.pack(pady=10)

    # Input box for PCB code
    pcb_label = tk.Label(pcb_window, text="PCB Code:", font=("Arial", 10))
    pcb_label.pack(pady=5)
    pcb_input = tk.Entry(pcb_window, font=("Arial", 12), width=30)
    pcb_input.pack(pady=5)

    # Submit button
    submit_button = tk.Button(pcb_window, text="Submit", font=("Arial", 12), 
                              command=lambda: submit_pcb(pcb_input.get()))
    submit_button.pack(pady=20)

# Function to handle PCB input submission
def submit_pcb(pcb_code):
    # Validate input: Format should be one letter followed by five numbers (e.g., A12345)
    if re.match(r'^[A-Za-z]{1}\d{5}$', pcb_code):  # Regex pattern for 1 letter + 5 numbers
        letter = pcb_code[0]  # Extract the letter
        numbers = pcb_code[1:]  # Extract the numbers

        try:
            conn = get_db_connection()  # Get the database connection
            if conn is None:
                messagebox.showerror("Database Error", "Failed to connect to the database.")
                return

            cursor = conn.cursor()
            try:
                # Check if the numbers already exist
                select_query = "SELECT * FROM PCB WHERE numbers = %s"
                cursor.execute(select_query, (numbers,))
                result = cursor.fetchone()

                if result:
                    messagebox.showerror("Duplicate Entry", f"The number '{numbers}' already exists in the database.")
                    print(f"Debug: Duplicate entry found for numbers: {numbers}")
                else:
                    # Insert the data into the PCB table
                    insert_query = "INSERT INTO PCB (letter, numbers) VALUES (%s, %s)"
                    cursor.execute(insert_query, (letter, numbers))

                    # Commit the transaction
                    conn.commit()
                    messagebox.showinfo("Success", "PCB details submitted successfully.")
                    print("Debug: Data inserted successfully")
            except mysql.connector.Error as e:
                # Output detailed error message for debugging
                print(f"Debug: Database error occurred: {e}")
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                cursor.close()
                conn.close()  # Always close the connection
        except Exception as e:
            # Handle unexpected errors
            print(f"Debug: An unexpected error occurred: {e}")
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    else:
        messagebox.showerror("Error", "PCB Code must be one letter followed by five numbers (e.g., A12345).")

# Example usage to open the window (Uncomment the following lines to test the code)
# root = tk.Tk()
# open_pcb_window()
# root.mainloop()
