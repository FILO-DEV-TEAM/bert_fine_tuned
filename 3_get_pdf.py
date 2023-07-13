import requests

url = "https://ebook.mirae-n.com/@kb1327/2"
filename = "downloaded_file.pdf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers, stream=True)

if response.status_code == 200:
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)
    print(f"PDF file downloaded successfully as '{filename}'.")
else:
    print("Failed to download the PDF file.")
