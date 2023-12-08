import pyktok as pyk

# pyk.save_tiktok(
#    'https://www.tiktok.com/@thehumoraddict1/video/7292917378738867499?is_from_webapp=1&sender_device=pc&web_id=7275459214855194143',
#    True,
#    'video.csv',
#    'firefox')

def download_tiktok(link, dataName, browser):
   pyk.save_tiktok(link,True,dataName,browser)

