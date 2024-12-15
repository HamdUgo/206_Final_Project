# use "pip install TikTokApi
# python -m playwright install" in the terminal to get unofficial tiktok API
from TikTokApi import TikTokApi
try:
    api = TikTokApi.get_instance()
except:
    print('error occured')


