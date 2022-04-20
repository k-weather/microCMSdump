import os
import requests
import json
# import markdownify

TEMPLATE_MD = '''---
sys:
    id: "{content_id}"
    updatedAt: "{updatedAt}"
    createdAt: "{createdAt}"
date: "{date}"
title: "{title}"
{banner}
categories: 
{categories}
slug: "{content_id}"
---

{body}
'''


def categories(categories) -> str:
    ret = ""
    for category in categories:
        ret += '    -   "' + category + '"\n'
    return ret

def getBanner(content) -> str:
    if 'banner' in content:
        return "banner: " + content['banner']['url']
    else:
        return ""

headers = {
    "X-MICROCMS-API-KEY": os.environ['MICROCMS_API_KEY']
}
contents_list = requests.get(os.environ['MICROCMS_URL'] + '/api/v1/blog?limit=100&orders=-date', headers=headers).json()

with open('./contents.json', 'w') as f:
    json.dump(contents_list, f, ensure_ascii=False, indent=4)

# for count in range(contents_list['totalCount']):
#     content = contents_list['contents'][count]
#     with open('./content/blog/' + content['id'] + ".md", 'w') as f:
#         f.write(TEMPLATE_MD.format(
#             content_id=content['id'],
#             updatedAt=content['updatedAt'],
#             createdAt=content['createdAt'],
#             publishedAt=content['publishedAt'],
#             date=content['date'],
#             title=content['title'],
#             categories=categories(content['category']),
#             banner=getBanner(content),
#             body=markdownify.markdownify(content['main'], heading_style="ATX")
#         ))

