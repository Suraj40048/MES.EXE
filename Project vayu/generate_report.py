import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from datetime import datetime

# Function to open the Generate Report dialog
def open_generate_report_dialog():
    report_window = tk.Toplevel()
    report_window.title("Generate Report")
    report_window.geometry("400x300")

    # Default path (you can customize this)
    default_directory = os.path.expanduser("~")  # Sets default to the user's home directory

    # Label for directory path
    directory_label = tk.Label(report_window, text="Directory Path:")
    directory_label.pack(pady=5)

    # Entry for directory path
    directory_entry = tk.Entry(report_window, width=40)
    directory_entry.insert(0, default_directory)  # Set the default path
    directory_entry.pack(pady=5)

    # Button to browse for directory
    def browse_directory():
        selected_directory = filedialog.askdirectory(initialdir=default_directory)  # Open dialog with default directory
        if selected_directory:
            directory_entry.delete(0, tk.END)  # Clear the current entry
            directory_entry.insert(0, selected_directory)  # Insert the selected directory

    browse_button = tk.Button(report_window, text="Browse", command=browse_directory)
    browse_button.pack(pady=5)

    # Label for date
    date_label = tk.Label(report_window, text="Report Date (YYYY-MM-DD):")
    date_label.pack(pady=5)

    # Entry for report date
    date_entry = tk.Entry(report_window, width=40)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Set today's date as default
    date_entry.pack(pady=5)

    # Submit button
    submit_button = tk.Button(report_window, text="Submit", command=lambda: generate_report(directory_entry.get(), date_entry.get()))
    submit_button.pack(pady=20)

# Function to generate report (placeholder)
def generate_report(file_path, report_date):
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "Directory does not exist.")
        return
    # Here, you would implement your report generation logic
    messagebox.showinfo("Success", f"Report generated at {file_path} for date {report_date}.")

# Start the Tkinter main loop
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    open_generate_report_dialog()
    root.mainloop()
