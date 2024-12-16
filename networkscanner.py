import socket
import ipaddress

def scan_network(network, port):
    for ip in ipaddress.IPv4Network(network, strict=False):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((str(ip), port))
                print(f"Port {port} is open on {ip}")
        except:
            pass

if __name__ == "__main__":
    scan_network("192.168.1.0/24", 80)  # Scan port 80 on 192.168.1.x
