import os
import requests

query = "database"
count = 10
access_key = 'd6afZXNOjmMWW0OrZr4D75bKEABI5X6YCKld5j0yTQs'

if not os.path.exists("images"):
    os.makedirs("images")

def download_images():
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={access_key}&per_page={count}"
    response = requests.get(url)
    
    if response.status_code == 200:
        images = response.json().get('results', [])
        for i, img in enumerate(images):
            img_url = img['urls']['regular']
            img_data = requests.get(img_url).content
            with open(f"images/image_{i+1}.jpg", 'wb') as handler:
                handler.write(img_data)
            print(f"Image {i+1} downloaded.")
    else:
        print("Error fetching images:", response.status_code)

download_images()
