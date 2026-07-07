"""普通方式 """
import requests

def download_image(url):
    print(f"Downloading {url}")
    response = requests.get(url)
    print(f"Finished downloading {url}")
    file_name = url.split("/")[-1] # Extracting the file name from the URL
    with open(file_name, "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net",
    ]
    for url in urls:
        download_image(url)
