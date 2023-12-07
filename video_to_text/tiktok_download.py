import pyktok as pyk

# pyk.specify_browser('firefox')
# pyk.save_tiktok('https://vm.tiktok.com/ZT85hNPpn/',
# 	        True,
#                 'video_data.csv')

def download_tiktok(link, dataName, browser):
  return pyk.save_tiktok(link,True,dataName,browser)

