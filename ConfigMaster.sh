#!/bin/bash
#### Colors Output
RESET="\033[0m"          # Normal Colour
RED="\033[0;31m"         # Error / Issues
GREEN="\033[0;32m"       # Successful       
BOLD="\033[01;01m"       # Highlight         
WHITE="\033[1;37m"       # Bold Text         
YELLOW="\033[1;33m"      # Warnings and Info 
BLINK="\033[5m"          # Blinking Effect


banner() {
  echo -e "${GREEN}${BOLD} ==========================================================================================================${RESET}"                                                                                  
  echo -e "${RED}"
  echo -e " ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗ ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ "
  echo -e "██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝ ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗"
  echo -e "██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝"
  echo -e "██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗"
  echo -e "╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║"
  echo -e " ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝"
  echo -e "${RESET}"                                                       
  echo -e "${GREEN}${BOLD} ==========================================================================================================${RESET}"        
                                                                                                                                                                
# Tool Info & Author Credits with Blinking Effect
current_date_time=$(date '+%Y-%m-%d %H:%M:%S') # Get current date and time
echo -e "${WHITE}=============================================================="
echo -e "${RED}${BOLD}               CONFIGMASTER Network Automation Tool             "
echo -e "${WHITE}=============================================================="
echo -e " "
echo -e "${WHITE}#       *********${RED}${BOLD} Author: SDK-NETWORKS${RESET}${WHITE}*********                #"
echo -e "${WHITE}#       ******${RED}${BOLD} Date: $current_date_time${RESET}${WHITE} ******                #"
echo -e "${WHITE}=============================================================="
echo -e " "
}

clear
banner
# Ask for user choice
while true; do
  
  echo -e "${WHITE}"
  
  echo "Device Configuration Options:"
  echo "1. Single Device Configuration"
  echo "2. Multiple Devices"
  echo "3. Exit from script"


  read -p "Enter your choice: " choice

  if [ "$choice" = "1" ]; then
    break
  elif [ "$choice" = "2" ]; then
    break
  elif [ "$choice" = "3" ]; then
    echo -e "${RED}${BOLD}Exiting script...${RESET}"
    exit 0
  else
    echo -e "${RED}${BOLD}Invalid choice. Please try again.${RESET}"
    sleep 3
    clear
    banner
  fi
done

# Ask for user protocol
while true; do
  
  echo -e "${WHITE}"
  echo "Configuration protocol:"
  echo "1. Telnet"
  echo "2. SSH"
  echo "3. Exit from script"
  read -p "Which Protocol You Want To Use: " protocol
  echo -e "${RESET}"

  if [ "$protocol" = "1" ]; then
    break
  elif [ "$protocol" = "2" ]; then
    break
  elif [ "$protocol" = "3" ]; then
    echo -e "${RED}${BOLD}Exiting script...${RESET}"
    exit 0
  else
    echo -e "${RED}${BOLD}Invalid protocol. Please try again.${RESET}"
    sleep 3
    clear
    banner
  fi
done

# Use if and else statements to handle different choices and protocols
if [ "$choice" = "1" ]; then
  if [ "$protocol" = "1" ]; then
    clear
    banner
    python3 Single_Telnet.py
  elif [ "$protocol" = "2" ]; then
    clear
    banner
    python3 Single_SSH.py
  fi
else
  if [ "$protocol" = "1" ]; then
    clear
    banner
    python3 Multiple_telnet.py
  elif [ "$protocol" = "2" ]; then
    clear
    banner
    python3 Multiple_SSH.py
  fi
fi