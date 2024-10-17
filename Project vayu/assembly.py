import tkinter as tk
from tkinter import messagebox
from db_connection import get_db_connection  # Import the database connection function

# Function to open the Assembly window
def open_assembly_window():
    assembly_window = tk.Toplevel()
    assembly_window.title("Assembly Section")
    assembly_window.geometry("600x400")

    # Label for the input box
    input_label = tk.Label(assembly_window, text="Select Assembly Parts:", font=("Arial", 12))
    input_label.pack(pady=10)

    # Variables to store checkbox values
    sensor_left_var = tk.IntVar()
    sensor_right_var = tk.IntVar()
    kill_switch_var = tk.IntVar()
    dbt_5_var = tk.IntVar()
    motor_connection_var = tk.IntVar()
    earthing_wire_var = tk.IntVar()
    wheels_nut_bolt_var = tk.IntVar()
    solar_panel_var = tk.IntVar()

    # Checkbox for each part
    sensor_left_cb = tk.Checkbutton(assembly_window, text="Sensor Left", variable=sensor_left_var)
    sensor_left_cb.pack(anchor='w')
    sensor_right_cb = tk.Checkbutton(assembly_window, text="Sensor Right", variable=sensor_right_var)
    sensor_right_cb.pack(anchor='w')
    kill_switch_cb = tk.Checkbutton(assembly_window, text="Kill Switch", variable=kill_switch_var)
    kill_switch_cb.pack(anchor='w')
    dbt_5_cb = tk.Checkbutton(assembly_window, text="DBT 5", variable=dbt_5_var)
    dbt_5_cb.pack(anchor='w')
    motor_connection_cb = tk.Checkbutton(assembly_window, text="Motor Connection", variable=motor_connection_var)
    motor_connection_cb.pack(anchor='w')
    earthing_wire_cb = tk.Checkbutton(assembly_window, text="Earthing Wire", variable=earthing_wire_var)
    earthing_wire_cb.pack(anchor='w')
    wheels_nut_bolt_cb = tk.Checkbutton(assembly_window, text="Wheels Nut Bolt", variable=wheels_nut_bolt_var)
    wheels_nut_bolt_cb.pack(anchor='w')
    solar_panel_cb = tk.Checkbutton(assembly_window, text="Solar Panel", variable=solar_panel_var)
    solar_panel_cb.pack(anchor='w')

    # Submit button
    submit_button = tk.Button(assembly_window, text="Submit", font=("Arial", 12), 
                              command=lambda: submit_assembly(
                                  sensor_left_var.get(), sensor_right_var.get(), 
                                  kill_switch_var.get(), dbt_5_var.get(), 
                                  motor_connection_var.get(), earthing_wire_var.get(), 
                                  wheels_nut_bolt_var.get(), solar_panel_var.get()
                              ))
    submit_button.pack(pady=20)

# Function to handle Assembly input submission
def submit_assembly(sensor_left, sensor_right, kill_switch, dbt_5, motor_connection, earthing_wire, wheels_nut_bolt, solar_panel):
    # Convert checkbox values to "OK" or "NA"
    status_map = lambda val: "OK" if val == 1 else "NA"
    sensor_left_status = status_map(sensor_left)
    sensor_right_status = status_map(sensor_right)
    kill_switch_status = status_map(kill_switch)
    dbt_5_status = status_map(dbt_5)
    motor_connection_status = status_map(motor_connection)
    earthing_wire_status = status_map(earthing_wire)
    wheels_nut_bolt_status = status_map(wheels_nut_bolt)
    solar_panel_status = status_map(solar_panel)

    try:
        conn = get_db_connection()  # Get the database connection
        if conn is None:
            messagebox.showerror("Database Error", "Failed to connect to the database.")
            return

        cursor = conn.cursor()
        try:
            # Insert the data into the Assembly table
            insert_query = """
                INSERT INTO Assembly (
                    sensor_left, sensor_right, kill_switch, dbt_5, 
                    motor_connection, earthing_wire, wheels_nut_bolt, solar_panel
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                sensor_left_status, sensor_right_status, kill_switch_status, 
                dbt_5_status, motor_connection_status, earthing_wire_status, 
                wheels_nut_bolt_status, solar_panel_status
            ))

            # Commit the transaction
            conn.commit()
            messagebox.showinfo("Success", "Assembly details submitted successfully.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            cursor.close()
            conn.close()  # Always close the connection
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
