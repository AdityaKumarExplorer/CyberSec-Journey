import os          # Provides functions to interact with the operating system.
import platform    # Gives detailed information about the system hardware and OS.
import socket      # Handles network communication and connections.
import shutil      # Provides high-level file and disk operations.
import subprocess  # Allows Python to run system commands in the terminal.

print("=== System Information Gatherer ===\n")

# OS Information
print("[+] OS Information:")
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}\n")

# Current User
print("[+] Current User:")
print(os.getlogin(), "\n")

# IP Address
print("[+] Network Information:")
try:
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
except:
    print("Could not retrieve IP address")
print()

# Running Processes Count
print("[+] Running Processes:")
try:
    process_count = len(os.listdir('/proc'))
    print(f"Approx Process Count: {process_count}")
except:
    print("Process info not available")
print()

# Disk Usage
print("[+] Disk Usage:")
total, used, free = shutil.disk_usage("/")
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB\n")

# Network Interfaces
print("[+] Network Interfaces:")
try:
    interfaces = os.listdir('/sys/class/net')
    for interface in interfaces:
        print(interface)
except:
    print("Could not list interfaces")

print("\n=== Scan Complete ===")
