import pyktok as pyk
import os
import os.path 
import shutil
import requests
import urllib.request
from pytube import YouTube

def download_file(link, metadata_name, browser):
	pyk.save_tiktok(link, True, metadata_name, browser) 

	video_name = link.split('/')
	for i in range(len(video_name)):
		if (video_name[i] == 'video') or (video_name[i] == 'vm.tiktok.com'):
			if '?' in video_name[i]:
				file_name_list = video_name[i].split('?')
				file_name = f'{file_name_list[0]}.mp4'
			else: 
				file_name = f'{video_name[i+1]}.mp4'

			if check_file(file_name) == True: 
				directory(file_name, metadata_name)
				break 

def check_file(file_dir):
  return os.path.isfile(file_dir)

def directory(video_name_dir):
	current_dir = os.path.dirname(os.path.realpath(__file__))
	video_title_dir = current_dir.split("\\")
	video_title_dir.pop()

	# get future video directory
	temp_videos_dir = '\\'.join(video_title_dir)
	videos_dir = f'{temp_videos_dir}\\video_to_text\\video\\{video_name_dir}'

	# get current video directory
	video_title_dir = '\\'.join(video_title_dir)
	temp_video = f'{video_title_dir}\\{video_name_dir}'

	if check_file(temp_video):
		shutil.move(temp_video, videos_dir)

def download_from_youtube(links):
	current_dir = os.path.dirname(os.path.realpath(__file__))
	videos_dir = f'{current_dir}\\video'
	YouTube(links).streams.filter(subtype='webm').first().download()
	print('done')

def get_tiktok_video(url_video):
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url":url_video}
	headers = {
		"X-RapidAPI-Key": "0f96a654b5msh32c9adbc696a5d5p1488dfjsn768e9fc6aaa6",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	response_data = response.json()
	video_url = response_data['video'][0]

	urllib.request.urlretrieve(video_url, "temp.mp4")
	directory('temp.mp4')

url_video = 'https://www.tiktok.com/@nick.digiovanni/video/7307311219571019039?is_from_webapp=1&sender_device=pc'
get_tiktok_video(url_video)