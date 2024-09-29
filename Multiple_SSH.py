#configur single device via file
import paramiko
import time
import threading
import re

# Get IP file from user
while True:
    try:
        ip_file = input("Enter the path to the file containing IP addresses of switches:")
        # Open file containing IP addresses of switches
        f = open(ip_file, 'r')
        break
    except FileNotFoundError:
        print("Error: The file " + ip_file + " does not exist.")
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)
        
while True:
    try:
        # Get file path from user
        file_path = input("Enter the path to the config file: ")
        # Read commands from config file
        with open(file_path, 'r') as config_f:
            commands = [line.strip() for line in config_f.readlines()]
        break
    except FileNotFoundError:
        print("Error: The file " + file_path + " does not exist.")
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)

# Loop through each IP address in the file
for ip in f:
    ip = ip.strip()  # Remove leading and trailing whitespaces

    # Validate IP address
    if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        print(ip + " Invalid IP Address. Skipping...")
        continue
    
    print("Configuring switch " + ip)
    # Get username from user
    USERNAME = input("Enter the username: ")

    # Get password from user
    PASSWORD = input("Enter the password: ")

    print("Wait Few Seconds To Connect With Device")

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=USERNAME, password=PASSWORD, timeout=10)
        print(f"Connected To {ip}")
    except Exception as e:
        print(f"Error: Unable to connect to {ip} on port 22.")
        continue
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)

    # Open an interactive shell session
    channel = ssh.invoke_shell()

    def print_output(channel):
        while True:
            data = channel.recv(1024)
            if not data:
                break
            print(data.decode(), end='')

    # Start a new thread to print the output
    output_thread = threading.Thread(target=print_output, args=(channel,))
    output_thread.daemon = True
    output_thread.start()

    # Execute configuration commands
    for command in commands:
        channel.send(command + "\n")
        time.sleep(1)  # wait for 1 second before sending the next command

    # Close the SSH connection
    ssh.close()
    print("\nConnection Closed.")

# Close file
f.close()
