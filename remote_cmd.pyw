import socket
import subprocess
import tkinter as tk

def scan_port(target_ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout to 1 second
        sock.settimeout(1)
        # Attempt to connect to the target IP and port
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error occurred while scanning port {port}: {e}")

def execute_command(command):
    try:
        # Execute the command using subprocess
        result = subprocess.check_output(command, shell=True)
        print(result.decode())
    except Exception as e:
        print(f"Error occurred while executing command: {e}")

def scan_ports():
    target_ip = ip_entry.get()
    ports = [21, 22, 80, 443, 3389]  # Example ports, you can modify this list
    output_text.delete(1.0, tk.END)
    for port in ports:
        output_text.insert(tk.END, f"Scanning port {port}...\n")
        scan_port(target_ip, port)

def execute_command_gui():
    command = command_entry.get()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Executing command: {command}\n")
    execute_command(command)

# Create main window
window = tk.Tk()
window.title("Penetration Tool")
window.configure(bg="black")

# Target IP Entry
ip_label = tk.Label(window, text="Target IP:", fg="white", bg="black")
ip_label.grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(window)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

# Command Entry
command_label = tk.Label(window, text="Command:", fg="white", bg="black")
command_label.grid(row=1, column=0, padx=10, pady=10)
command_entry = tk.Entry(window)
command_entry.grid(row=1, column=1, padx=10, pady=10)

# Scan Ports Button
scan_ports_button = tk.Button(window, text="Scan Ports", command=scan_ports, fg="black", bg="white")
scan_ports_button.grid(row=2, column=0, padx=10, pady=10)

# Execute Command Button
execute_command_button = tk.Button(window, text="Execute Command", command=execute_command_gui, fg="black", bg="white")
execute_command_button.grid(row=2, column=1, padx=10, pady=10)

# Output Text
output_text = tk.Text(window, height=10, width=50, fg="white", bg="black")
output_text.grid(row=3, columnspan=2, padx=10, pady=10)

window.mainloop()
