import pyktok as pyk
import os
import os.path 
import shutil

# example lists
# https://www.tiktok.com/@matt_rife/video/7302575653935779114?is_from_webapp=1&sender_device=pc
# https://vm.tiktok.com/ZT85rvWHM/

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

def directory(video_name, metadata_name):
	current_dir = os.path.dirname(os.path.realpath(__file__))
	videos_dir = f'{current_dir}\\video'
	metadata_dir = f'{current_dir}\\metadata'
	video_title_dir = f'{current_dir}\\{video_name}' 
	metadata_name_dir = f'{current_dir}\\{metadata_dir}'
	shutil.move(video_title_dir, videos_dir)
	shutil.move(metadata_name_dir, metadata_dir)


