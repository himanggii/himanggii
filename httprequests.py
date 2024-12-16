import requests

def fetch_website(url):
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Content: {response.text[:500]}")  # Print first 500 characters

if __name__ == "__main__":
    fetch_website("https://www.example.com")
