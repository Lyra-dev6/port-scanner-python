import socket

target_host = input("Enter the target website or IP: ")
target_ip = socket.gethostbyname(target_host)

print("\n" + "=" * 40)
print(f"Scanning target: {target_host} ({target_ip})")
print("=" * 40 + "\n")

for target_port in range(20, 86):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result = s.connect_ex((target_ip, target_port))
    
    if result == 0:
        print(f"[+] Port {target_port}: OPEN")
    
    s.close()

print("\nScan complete!")




