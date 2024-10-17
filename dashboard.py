import tkinter as tk 
from tkinter import messagebox
from pcb import open_pcb_window
from mainassembly import open_mainassembly_window
from assembly import open_assembly_window  # Assuming this imports the assembly function
from testing import open_testing_window
from generate_report import open_generate_report_dialog
from report import generate_report  # Import the function to generate the report

# Function to open the Dashboard window
def open_dashboard(root):
    dashboard_window = tk.Toplevel(root)  # Create a new top-level window
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("600x600")

    # Header for the dashboard
    dashboard_header = tk.Label(dashboard_window, text="Dashboard", font=("Arial", 24, "bold"))
    dashboard_header.pack(pady=20)

    # Add the Report button
    report_button = tk.Button(dashboard_window, text="Generate Report", command=open_generate_report_dialog)
    report_button.pack(pady=10)

    # Other existing buttons (PCB, Assembly, Testing)
    pcb_button = tk.Button(dashboard_window, text="PCB", font=("Arial", 14), width=20, command=open_pcb_window)
    pcb_button.pack(pady=10)

    mainassembly_button = tk.Button(dashboard_window, text="Main Assembly", font=("Arial", 14), width=20, command=open_mainassembly_window)
    mainassembly_button.pack(pady=10)

    assembly_button = tk.Button(dashboard_window, text="Assembly", font=("Arial", 14), width=20, command=open_assembly_window)
    assembly_button.pack(pady=10)

    testing_button = tk.Button(dashboard_window, text="Testing", font=("Arial", 14), width=20, command=open_testing_window)
    testing_button.pack(pady=10)

    # Logout Button
    logout_button = tk.Button(dashboard_window, text="Logout", font=("Arial", 12), command=lambda: logout(dashboard_window, root))
    logout_button.pack(pady=20)

# Function to handle logout
def logout(dashboard_window, root):
    dashboard_window.destroy()  # Close the dashboard window
    root.deiconify()  # Show the login window again

# Ensure that the open_dashboard function is called with the root parameter
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Dashboard")
    root.geometry("400x400")
    open_dashboard(root)
    root.mainloop()
