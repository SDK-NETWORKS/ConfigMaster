# configure devises from a file
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import telnetlib
import time
import re

# Establish a Telnet connection
while True:
    try:
        # Define your switch details and credentials
        SWITCH_IP = input("Enter The IP Address Of The Devices: ")

        # Validate IP address
        if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", SWITCH_IP):
            print("Invalid IP Address. Please Enter a Valid IP Address.")
            time.sleep(1)
            continue

        tn = telnetlib.Telnet(SWITCH_IP)
        print(f"Connected To {SWITCH_IP}")
        break
    except Exception as e:
        print(f"Failed To Connect To {SWITCH_IP}: {e}")
        time.sleep(1)
        continue
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)

# Login to the switch
while True:
    try:
        USERNAME = input("Enter Your Username: ")
        PASSWORD = input("Enter Your Password: ")

        tn.read_until(b"Username: ")
        tn.write(USERNAME.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(PASSWORD.encode('ascii') + b"\n")

        # Check if login was successful
        output = tn.read_until(b">", 1).decode('ascii')
        if ">" in output:
            print("Login Successful!")
            break
        elif "#" in output:
            print("Login Successful!")
            break
        elif "<" in output:
            print("Login Successful!")
            break
        else:
            print("Invalid Username Or Password. Try Again!")
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
    
# Execute commands on the switch
for command in commands:
    tn.write(command.encode('ascii') + b"\n")


# Exit Telnet session
tn.write(b"end\n")
tn.write(b"exit\n")

# Print output
print(tn.read_all().decode('ascii'))