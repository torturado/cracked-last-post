import requests
from bs4 import BeautifulSoup
from time import sleep
import telegram

# you must configure this parameters
# ---------------------------------
alert = ".LOLI" or "CONFIG"
# ---------------------------------


url = "https://cracked.io/index.php"

bot = telegram.Bot(token='5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI')

chat_id = '-1001597696937'

"""Add cookies for the requests.get"""
cookies = {'hc_accessibility': 'EDsP2bDIggc+3a5VW5gfhTxz4+7vgp7geQ5yTkeTYelbaJJJNwvD84VmKddjmUiUvp3E8vqF3mOkRAQlXVETI7u1TjADlL85dXo7aMjJXyv5tzQWCn4Ed06BxB0Hj2wlsXIAUVgqmO+1iN+xO8SpcVSN8ooK8KI91OaOiDD/nv0W0SjT8Hbn2KXG0cbrsATI94te50ofjKXjRtscHcEZWkL3IB0DEm5MopK3j9qX4w70mCfwEThTXWNSsscIm3/eTT8UxhWXXY8ePXmAMl5Ox9qykNsvz5WkvGsf4A0LhN5I4OUpaXaj/BclSaNEhhtf2xnIyRR/wbW05SBMqzSB9fgBIrMdl/0/YkeoBLkHn9hnQOWtww4GZonQKiJpBn0Q8bfnu0iwMjkZFUQ1aFje7WxrJQIa4IgEOVOqK+xm2mrp0vVfznjLElHqTDx/kCGecDqWdzEvfUEWOsZ4K4Fb7Gouls60hdkqpRbbSPmXUq3xzvvHlOHg2867/Ruksm6XLGThSNDbkYlz//j0Y332zzaKosMEPxQMgXAo3h9CHjlBKbWccPCiVh0IKvy6bpxNJRUc9O+6mXoSwlpx+9PsNl+2HQl3p4Vq1Mm3+vvjYv6qQWs2Q1CpppHgaJD/OVbRw2zkUio+kXjNNqx2fPTSK99zAXlvgXJOPlV5cUCRQSq4+5YG2qkLzhB7ymLHAC7LkDL6Gl6no+OY/WZn576/FUXg0NJqovrj17LaoCbNS2/a8p6/eMEzPScywzZGJL8UgVmCD+TaW5ofvHpH1c58ej4c1gkdIvpWxKTjs0k2sjkCDKVsaVp6d9GWLj/rHxv9x9rRvsJhUqLv5XuPFTS77qRXBYeGuUUzuoD2X0s9KebXUpzMkNryBK260OVvgUdZy0pXQFTEV2bVYe5JNaiWLDdp0pFIiU3t9izoceB0CGGAS/Gyp3P5Pib2uRYYL0scvCHMwzq9YKvb0dfF213pGkW00mvZr2TZSt413c6l744d5O+zWVXv++b0th5x6mNI94fc5y5GLGm7Shg7',
           'cf_clearance': '0cabX2hVmQ3eQAVNOIj9ikBLP15MuZZEVdt8iXKHplU-1657831857-0-250',
           }

"""Add headers for the requests.get"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

# The first post will always be saved in this variable, if a new post has the same title, it will be ignored
last_title = ""

while True:
    try:
        r = requests.get(url, stream=True, headers=headers, cookies=cookies)
        soup = BeautifulSoup(r.text, 'html.parser')
        if soup.find('form', class_='challenge-form interactive-form'):
            print("Verification Needed")
            while soup.find('form', class_='challenge-form interactive-form'):
                r = requests.get(url, stream=True, headers=headers, cookies=cookies)
                soup = BeautifulSoup(r.text, 'html.parser')
                print("Refreshing...")
                sleep(5)
        posts = soup.find_all('table', {'class': 'tborder latestthreads_table'})
        for post in posts:
            title = post.find('span', {'class': 'post_link'}).find('a').text
            author = post.find('span', {'class': 'latest-post-uname'}).find('a').text
            link = post.find('span', {'class': 'post_link'}).find('a').get('href')
            link_author = post.find('span', {'class': 'latest-post-uname'}).find('a').get('href')
            profile_picture = post.find('img', {'class': 'latest_post_avatars'}).get('src')
            """Go inside the post via link and look for class <a class=nav-seperator"""
            likk = "https://cracked.io/{}".format(link)
            r_inside = requests.get(likk, stream=True, headers=headers, cookies=cookies)
            soup_inside = BeautifulSoup(r_inside.text, 'html.parser')
            """Get the number of class nav-seperator"""
            number_of_cats = len(soup_inside.find_all('a', {'class': 'nav-seperator'}))
            post_inside = soup_inside.find_all('a', {'class': 'nav-seperator'})
            """Get 4 text in total from post_inside"""
            text = ""
            for i in range(number_of_cats):
                """In the last number, don't put a comma"""
                if i == number_of_cats - 1:
                    text += post_inside[i].text
                else:
                    text += post_inside[i].text + ", "
            category = text
            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

            """if src of profile_picture finishes with "default_avatar.png" or with "transparent.png", remove "https://static.cracked.io/" from start"""
            if profile_picture.endswith("default_avatar.png") or profile_picture.endswith("transparent.png"):
                profile_picture = "https://static.cracked.io/" + profile_picture.replace("https://static.cracked.io/", "")
            
            elif not profile_picture.endswith("default_avatar.png") or not profile_picture.endswith("transparent.png"):
                profile_picture = profile_picture.replace("./", "").replace("/avatars/a", "/avatars//a").split("?")[0].replace("\n", "")
                profile_picture = "https://static.cracked.io/" + profile_picture
                    
            if last_title != title:
                last_title = title

                if alert in title:
                    print("Se ha encontrado una coincidencia! " + title)

                bot.sendMessage(chat_id=chat_id,
                                text=profile_picture,
                )
            
                bot.sendMessage(chat_id=chat_id,
                                text=message,
                                disable_web_page_preview=True,
                                parse_mode=telegram.ParseMode.HTML,
                )
                
            else:
                break
        sleep(3)
    
    except requests.exceptions.ChunkedEncodingError:
        print("Error ChunkedEncodingError")
        sleep(5)
        continue
    
    except requests.exceptions.ConnectionError:
        print("Error ConnectionError")
        sleep(5)
        continue
