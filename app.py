from pywebio import start_server
from pywebio.input import input
from pywebio.output import *
from pywebio.session import run_js
import requests
import os
import time
# ---------------- TikTok ----------------
def send_tiktok(link, endpoint):
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
        'free_link': link
    }
    r = requests.post(
        f'https://leofame.com/ar/{endpoint}',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data
    ).text
    return "success" in r
# ---------------- Telegram ----------------
def send_telegram(link):
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/json',
        'origin': 'https://tgpanel.org',
        'referer': 'https://tgpanel.org/free-telegram-reaction',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10)',
        'daVTOOL': 'Jafr',
        'x-panel-origin': 'https://tgpanel.org',
        'x-panel-referer': 'https://tgpanel.org/free-telegram-reaction',
    }
    json_data = {
        'link': link,
        'quantity': '50',
        'provider_service_id': '10949',
        'username': 'guest',}
    r = requests.post(
        'https://test.socialfruit.co/api/gateway',
        headers=headers,
        json=json_data
    )
    return "success" in r.text
# ---------------- insta ----------------
def send_insta(user):
    cookies = {
        'token': '51499f30237c3512620af85dbd489e7c',
    'general_sessions': '3kseh8l1q5umn1v66qbgtb0ta7dcv2ub',
    'utm_source': 'none',
    'utm_medium': 'none',
    'utm_campaign': 'none',
    'utm_term': 'none',
    'utm_content': 'none',
    '_omappvp': '87uf3AzLN5CEJlXkM7l3Htw7tdYzuVbMB65viZnmyeVtPIvesQvm8U3AouJ16tB3FNfw4wzZXoePRvtuBi2S9zTGZE7gP9Ld',
    '_omappvs': '1773948245564',
    '_fbp': 'fb.1.1773948245937.837870156443809936',
    'cf_clearance': 'Z_zJLn07eZ07i82iz.0BPlIgY2AwJeXQnPxMkm7K_js-1773948246-1.2.1.1-ovgR_ekJSpBZIrYaEh9fVtYpTdHC1NCWtN44Co1.pJX.p9dXLxQmm_pDpyw.icFHHEljuEI6zxzrolfynKeb.5xVnDPhB_rH1L9tItNzPmAjYSE7eoDKx5Ym5WeH34VJb64jnzuiSPauArKQPELUNJ19a9iElzfHnyiUMcGpeCbvDLItWC4gXZxoVkFAGeJ3t1qh1xO_6j3KLwR_42YFNgH69gPQw03ebFP7TgTnjuw',
    '_uetsid': '320e33f023c911f1998a4772b5419230',
    '_uetvid': '320e5e7023c911f18e40bbc412f27763',
    '_ga_BDPYFFQXV6': 'GS2.1.s1773948246$o1$g0$t1773948246$j60$l0$h0',
    '_ga': 'GA1.1.1569531429.1773948247',
    '_clck': '1q3hoe5%5E2%5Eg4h%5E0%5E2269',
    '_clsk': 'kvtocn%5E1773948248234%5E1%5E1%5Ey.clarity.ms%2Fcollect',
    '_gcl_au': '1.1.1037702829.1773948246.5128743.1773948250.1773948250',
    '_ga_73SRTEBYMR': 'GS2.1.s1773948246$o1$g0$t1773948250$j56$l0$h0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary6lrcZZBGQKuxBOt2',
        'origin': 'https://goread.io',
        'priority': 'u=1, i',
        'referer': 'https://goread.io/free-instagram-followers',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
    }

    files = {
        'token': (None, '51499f30237c3512620af85dbd489e7c'),
        'username': (None, user),
    }

    r = requests.post(
        'https://goread.io/package/loadProfile',
        cookies=cookies,
        headers=headers,
        files=files
    )

    return "success" in r.text
# ----------------insta2--------------
def send_insta2(user):
    cookies = {
        'wffn_traffic_source': 'https://chatgpt.com/',
        'wffn_timezone': 'Asia/Amman',
    }

    headers = {
        'accept': '*/*',
        'origin': 'https://growmyprofile.com',
        'referer': 'https://growmyprofile.com/free-instagram-followers/',
        'user-agent': 'Mozilla/5.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    files = {
        'post_id': (None, '610311'),
        'form_id': (None, '8baf789'),
        'form_fields[message]': (None, user),  # اليوزر
        'form_fields[email]': (None, 'test@gmail.com'),
        'form_fields[business]': (None, 'Music'),
        'action': (None, 'elementor_pro_forms_send_form'),
    }

    r = requests.post(
        'https://growmyprofile.com/wp-admin/admin-ajax.php',
        cookies=cookies,
        headers=headers,
        files=files
    )

    return "success" in r.text.lower()
# ---------------- UI ----------------
def main():
    clear()
    put_html("""
    <h2>اهلا بك 👋</h2>
    <ul>
        <li>🎵 رشق تيك توك</li>
        <li>📢 رشق تيليجرام</li>
        <li>📸 رشق انستغرام</li>
        <li>👨‍💻 المبرمج: شريان</li>
    </ul>
    """)

    put_buttons(
        [
            {'label': '🎵 TikTok', 'value': 'tiktok'},
            {'label': '📢 Telegram', 'value': 'telegram'},
            {'label': '📸 Insta #1', 'value': 'insta'},
            {'label': '🔥 Insta #2', 'value': 'insta2'},
            {'label': '📲 انضم لقناتي', 'value': 'join'}
        ],
        onclick=handle_choice
    )


# ---------------- Actions ----------------
def handle_choice(choice):
    clear()

    if choice == "join":
        run_js("window.open('https://t.me/oio_r6')")
        main()
        return

    link = input("🔗 ضع الرابط او اليوزر")

    with put_loading():
        time.sleep(1)

        # -------- TikTok --------
        if choice == "tiktok":
            put_text("⏳ جاري تنفيذ TikTok...")

            if send_tiktok(link, "free-tiktok-likes"):
                put_success("نجاح لايكات ✅")
            else:
                put_error("فشل لايكات ❌")

            time.sleep(2)

            if send_tiktok(link, "free-tiktok-views"):
                put_success("نجاح مشاهدات ✅")
            else:
                put_error("فشل مشاهدات ❌")

        # -------- Telegram --------
        elif choice == "telegram":
            put_text("⏳ جاري تنفيذ Telegram...")

            if send_telegram(link):
                put_success("تم بنجاح ✅")
            else:
                put_error("فشل ❌")

        # -------- Insta #1 --------
        elif choice == "insta":
            put_text("⏳ جاري تنفيذ Insta #1...")

            if send_insta(link):
                put_success("تم بنجاح ✅")
            else:
                put_error("فشل ❌")

        # -------- Insta #2 --------
        elif choice == "insta2":
            put_text("⏳ جاري تنفيذ Insta #2...")

            if send_insta2(link):
                put_success("تم بنجاح ✅")
            else:
                put_error("فشل ❌")

    put_buttons(['🔙 رجوع'], onclick=lambda _: main())
# ---------------- Run ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    start_server(main, port=port)