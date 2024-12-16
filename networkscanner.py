import socket

def scan_vulnerable():
    ip = input("Enter IP to scan: ")  # No input validation
    port = int(input("Enter port to scan: "))
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip, port))
            print(f"Port {port} is open on {ip}")
    except:
        pass

if __name__ == "__main__":
    scan_vulnerable()
