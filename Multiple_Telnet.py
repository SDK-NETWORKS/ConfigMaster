# CONNECT MULTIPLE SWITCHES...
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import telnetlib
import time
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

    # Establish a Telnet connection
    try:
        print("Configuring switch " + ip)
        tn = telnetlib.Telnet(ip)
        print(f"Connected To {ip}")   
    except Exception as e:
        print(f"Failed To Connect To {ip}: {e}")
        time.sleep(1)
        continue
    except KeyboardInterrupt:
        print("\nExiting From Script")
        exit(0)

    # Login to the switch
    for i in range(3,0,-1):
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
                print (str(i-1) + " attempts left")
        except KeyboardInterrupt:
            print("\nExiting From Script")
            exit(0)
    else:
        print("Failed to login to switch " + ip)
        continue

    # Execute commands on the switch
    for command in commands:
        tn.write(command.encode('ascii') + b"\n")

    # Exit Telnet session
    tn.write(b"end\n")
    tn.write(b"exit\n")

    # Print output
    print(tn.read_all().decode('ascii'))

# Close file
f.close()