import argparse
import pandas as pd
from requests_threads import AsyncSession
import time

parser = argparse.ArgumentParser(description='Input parser')
parser.add_argument('callback', help='The callback url.')
parser.add_argument('csv', help='Destination of csv file.')
parser.add_argument('sub_key', help='Your subscription key.')
args = parser.parse_args()
print(args)
SUBSCRIPTION_KEY = args.sub_key
CALLBACK_URL = args.callback
headers = {
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    'Content-Type': 'application/json'
}

urls = pd.read_csv(args.csv)
# urls = urls.head(5500)
print(urls.head())

# response = requests.post('https://api.getnetra.com/image-detection/process/brands',
#                          headers=headers,
#                          json=request)
session = AsyncSession(n=100)
async def _main():
	rs = []
	for line in urls.iterrows():
		img_url = line[1]['url']
		request = {
			'image_url': img_url,
    		'callback_url': CALLBACK_URL
		}
		rs.append(await session.post('https://api.getnetra.com/image-detection/process/all',
                         headers=headers,
                         json=request))
		time.sleep(0.004)
	for res in rs:
		print(res.text)
	

session.run(_main)
# print('Sent request:', response.status_code, response.text)

