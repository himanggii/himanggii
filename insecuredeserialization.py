import pickle

def vulnerable_deserialization():
    data = input("Enter serialized data: ")  # Input is taken as raw
    obj = pickle.loads(data.encode('utf-8'))  # Deserializes untrusted input
    print(f"Deserialized object: {obj}")

if __name__ == "__main__":
    vulnerable_deserialization()
