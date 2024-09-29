#configur single device via file
import paramiko
import time
import threading
import re

while True:
    try:
        # Get device IP from user
        DEVICE_IP = input("Enter the device IP address: ")

        # Validate IP address using regular expression
        if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", DEVICE_IP):
            print("Invalid IP Address. Please Enter a Valid IP Address.")
            time.sleep(1)
            continue

        # Get username from user
        USERNAME = input("Enter the username: ")

        # Get password from user
        PASSWORD = input("Enter the password: ")

        break
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)

print("Wait Few Seconds To Connect With Device")

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(DEVICE_IP, username=USERNAME, password=PASSWORD, timeout=10)
    print(f"Connected To {DEVICE_IP}")
except Exception as e:
    print(f"Error: Unable to connect to {DEVICE_IP} on port 22.")
    exit(0)
except KeyboardInterrupt:
    print("\nExiting From Script")
    exit(0)


while True:
    try:
        # Get file path from user
        file_path = input("Enter the path to the config file: ")

        # Read commands from config file
        with open(file_path, 'r') as f:
            commands = [line.strip() for line in f.readlines()]        
        break
    except FileNotFoundError:
        print("Error: The file " + file_path + " does not exist.")
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