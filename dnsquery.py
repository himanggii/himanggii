import socket

def resolve_vulnerable():
    while True:  # No rate limiting
        domain = input("Enter domain to resolve: ")
        try:
            ip = socket.gethostbyname(domain)
            print(f"{domain} resolves to {ip}")
        except:
            print(f"Failed to resolve {domain}")

if __name__ == "__main__":
    resolve_vulnerable()
