import requests
import os

from requests import RequestException


image_dir = "[Enter default image directory here]"

def download_image(image_url, image_name):
    headers = {'Accept': 'image/*'}

    try:
        response = requests.get(image_url, timeout=5, headers=headers)
        if response.status_code != 200 and response.status_code != 201:
            #  Pages are text
            print(f"Error getting {image_url}")
            return None
        else:
            resp_content_type = response.headers['content-type']
            print(resp_content_type)
            image_path = os.path.join(image_dir, image_name)
            with open(image_path, "wb") as o_file:
                o_file.write(response.content)
                print(f"{image_path} written.")
    except RequestException as e:
        print(f'Exception received {e} - {image_url}')



if __name__ == '__main__':
    print("Starting Script")
    url = input("Enter image URL:  ")
    file_name = input("Enter the name to save the file as:  ")
    download_image(url, file_name)
    print("Ending Script")

