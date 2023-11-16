import requests

def download_file(url, local_filename):
    with requests.get(url, stream=True) as response:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

# Example usage:
api_url = 'https://example.com/api/download'
local_filename = 'downloaded_file.mp4'

download_file(api_url, local_filename)