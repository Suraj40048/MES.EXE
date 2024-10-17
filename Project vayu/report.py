import tkinter as tk
from tkinter import filedialog, messagebox
import datetime
import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MySQL connection details from environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),  # Use default to 'localhost'
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'D252V4L3t8xTC7F'),
    'database': os.getenv('DB_NAME', 'solar')
}

# Function to generate the report
def generate_report(file_path, report_date):
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        query = "SELECT * FROM your_table_name"  # Replace 'your_table_name' with the actual table name
        df = pd.read_sql(query, conn)  # Load data into a DataFrame

        # Save the DataFrame to an Excel file
        df.to_excel(file_path, index=False, engine='openpyxl')  # Save to Excel
        messagebox.showinfo("Success", f"Report generated successfully: {file_path}")
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")
    finally:
        if conn:
            conn.close()  # Close the database connection

# Function to open the file dialog and generate the report
def open_generate_report_dialog():
    # Prompt user to select file path for saving the report
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if not file_path:
        return  # If no file is selected, return

    # Get current date for report
    report_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Call generate_report with the correct arguments
    generate_report(file_path, report_date)

# Function to create the report generation window
def create_report_window():
    root = tk.Tk()
    root.title("Report Generator")
    root.geometry("300x200")

    # Button to generate the report
    generate_button = tk.Button(root, text="Generate Report", command=open_generate_report_dialog)
    generate_button.pack(pady=20)

    # Start the Tkinter main loop
    root.mainloop()

# Entry point for the application
if __name__ == "__main__":
    create_report_window()
