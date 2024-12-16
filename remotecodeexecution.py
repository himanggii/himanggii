import os

def vulnerable_rce():
    command = input("Enter a command to execute: ")  # No input validation
    os.system(command)  # Executes arbitrary commands

if __name__ == "__main__":
    vulnerable_rce()
