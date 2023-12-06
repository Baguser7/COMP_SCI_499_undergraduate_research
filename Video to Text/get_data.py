import requests

url = "https://tiktok-download-video1.p.rapidapi.com/getVideo"

querystring = {"url":"https://www.tiktok.com/@huynhbrian/video/6928840070904564998?is_from_webapp=1&sender_device=pc","hd":"1"}

headers = {
	"X-RapidAPI-Key": "a597122887mshc8d0bd01f969791p1e0669jsn80740e9e20d2",
	"X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())