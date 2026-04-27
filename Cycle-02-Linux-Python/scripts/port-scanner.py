import socket
import time

target = input("Enter target IP: ")

start = time.time()

print(f"Scanning {target}...")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
    except:
        pass

    s.close()

end = time.time()
print(f"Scan completed in {end - start:.2f} seconds")
