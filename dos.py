def vulnerable_dos():
    size = int(input("Enter the size of list to create: "))  # No input limits
    large_list = [0] * size  # Can allocate massive memory
    print("List created")

if __name__ == "__main__":
    vulnerable_dos()
