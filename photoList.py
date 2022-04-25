import os
import requests
import json

headers = {
    "X-MICROCMS-API-KEY": os.environ['MICROCMS_API_KEY']
}
contents_list = requests.get(os.environ['MICROCMS_URL'] + '/api/v1/photos?limit=100&orders=-date', headers=headers).json()

with open('./output/photos.json', 'w') as f:
    json.dump(contents_list, f, ensure_ascii=False, indent=4)


