import hashlib

def store_password():
    password = input("Enter your password: ")
    hash = hashlib.md5(password.encode()).hexdigest()  # Insecure hashing algorithm
    print(f"Password hash: {hash}")

if __name__ == "__main__":
    store_password()
