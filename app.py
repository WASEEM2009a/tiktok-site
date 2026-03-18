from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio import config
from pywebio.session import *
from pywebio.pin import *
import requests
import os
def main():
    # صورة قناة لـ شروحات شريان السرحاني
    #put_image('https://image2url.com/r2/default/images/1771666747285-094f4619-15f0-41c0-8ff8-f53b4407bff5.jpg',width='500',height='500')
    put_html(""" <ol>
        <h2> اهلا بكم <h2>
        <li> - موقع رشق تيك توك 
        <li> - رشق مشاهدات تيك توك
        <li> - رشق اعجابات تيك توك
        <li> - مبرمج الموقع شريان السرحاني
        <li> - تواصل تيلجرام - @oio_r6
        <lo> """)

    url=input(f'Url-TikTok : ',
    placeholder='رابط الريلز')
    cookies = {
        'token': '45fe84f361c3a0b47bc3c01cbbaffaf6',
        'ci_session': '932331134eaf44a133a54be17712106c6bf7a904',
        'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%221%22%7D%7D',
        'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1803382696518%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1771846701601%2C%22e%22%3A1803382702495%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2235%22%2C%22e%22%3A1803382696518%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%226%22%2C%22e%22%3A1803382696518%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%221544b336-8c65-4aac-b26f-5eef6ed9c5f6%22%2C%22e%22%3A1803382696518%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221771846696518%22%2C%22e%22%3A1803382696518%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22882315814%22%2C%22e%22%3A1771848496518%7D%7D',
    }

    headers = {
        'authority': 'leofame.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://leofame.com',
        'referer': 'https://leofame.com/ar/free-tiktok-likes',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'api': '1',
    }

    data = {
        'token': '45fe84f361c3a0b47bc3c01cbbaffaf6',
        'timezone_offset': 'Asia/Riyadh',
        'free_link': url
    }

    response = requests.post('https://leofame.com/ar/free-tiktok-likes', params=params, cookies=cookies, headers=headers, data=data).text
    if "success" in response:
        put_text(f'It was sprayed Likes ✅ ')
    else:
        put_text(f'Failure to throw Likes ❌')
        
    cookies = {
        'token': '45fe84f361c3a0b47bc3c01cbbaffaf6',
        'ci_session': '932331134eaf44a133a54be17712106c6bf7a904',
        'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%222%22%7D%7D',
        'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1803384160032%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1771848164046%2C%22e%22%3A1803384164614%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2239%22%2C%22e%22%3A1803384160032%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%226%22%2C%22e%22%3A1803384160032%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%221544b336-8c65-4aac-b26f-5eef6ed9c5f6%22%2C%22e%22%3A1803384160032%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221771848160032%22%2C%22e%22%3A1803384160032%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22882315814%22%2C%22e%22%3A1771849960032%7D%7D',
    }

    headers = {
        'authority': 'leofame.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'token=45fe84f361c3a0b47bc3c01cbbaffaf6'
        'origin': 'https://leofame.com',
        'referer': 'https://leofame.com/ar/free-tiktok-views',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'api': '1',
    }

    data = {
        'token': '45fe84f361c3a0b47bc3c01cbbaffaf6',
        'timezone_offset': 'Asia/Riyadh',
        'free_link': url,
    }

    response = requests.post('https://leofame.com/ar/free-tiktok-views', params=params, cookies=cookies, headers=headers, data=data).text
    if "success" in response:
        put_text(f'It was sprayed Views ✅ ')
    else:
        put_text(f'Failure to throw Views ❌')
    pass
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    start_server(main, port=port)