import requests

def fetch_website_vulnerable(url):
    response = requests.get(url, verify=False)  # SSL verification disabled
    print(f"Content: {response.text[:500]}")

if __name__ == "__main__":
    fetch_website_vulnerable("https://example.com")
