<h1 align="center">
  <img src="static/ConfigMaster.png" alt="ConfigMaster">
  <br>
</h1>

🚀 Just wrapped up a Network Automation script! 💻 This Python & BASH based tool allows seamless interaction with Devices, making it easy to connect, authenticate, and execute commands directly from the terminal. 🔄

# Features

**1.Telnet and SSH Connection Handling:** 
- Establishes secure connections to network devices using either Telnet or SSH protocols.
- Automatically detects and validates IP addresses before initiating connections, ensuring error-free configurations.
- Supports both legacy devices that require Telnet and modern devices using SSH for secure access.
 
**2.User Authentication:** 
- Prompts for username and password credentials with hidden input for the password using the getpass module.
- Manages authentication securely and confirms successful login based on the device’s prompt for both Telnet and SSH sessions.

**3.Batch Command Execution:**
- Supports executing a series of configuration commands on multiple devices by reading from a predefined configuration file.
- Provides real-time feedback for each command executed on the network devices, ensuring immediate results and monitoring.

**4.Error Handling and User-Friendly Interface:** 
- The script includes robust error handling for failed connections, invalid credentials, and unexpected errors.
- Provides clear prompts and error messages, improving user experience.

**5.Graceful Exit:** 
- Supports user interruptions with **Ctrl+C**, allowing users to exit loops and close the Telnet session cleanly.
- Automatically closes both Telnet and SSH connections when the session is completed, avoiding hanging connections.

**6.Timeout Mechanism:** 
- Implements a timeout mechanism during command execution to prevent the tool from freezing when devices become unresponsive.

**CONFIGMASTER** is designed for ease of use and compatibility with a wide range of network devices. It provides network administrators with a flexible, secure, and efficient way to automate configurations using both Telnet and SSH protocols. Whether you’re configuring a single switch or an entire fleet, ConfigMaster simplifies the process while providing real-time feedback and error-handling.

# Available On :

- 𝙇𝙄𝙉𝙐𝙓

- 𝙏𝙀𝙍𝙈𝙐𝙓

- 𝙒𝙄𝙉𝘿𝙊𝙒𝙎

# ConfigMaster Installation
```
git clone https://github.com/SDK-NETWORKS/ConfigMaster
cd ConfigMaster
chmod +x ConfigMaster.sh
```
# Running ConfigMaster

This will Run **ConfigMaster** Tool.

```
bash ConfigMaster.sh 
```
**CONNECTOR IS MADE WITH 🖤 BY SDK-NETWORKS.**
