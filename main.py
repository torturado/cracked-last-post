import requests
from bs4 import BeautifulSoup
from time import sleep
import telegram

# you must configure this parameters
# ---------------------------------
alert = ".LOLI" or "CONFIG"
# ---------------------------------


url = "https://cracked.io/"

bot = telegram.Bot(token='5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI')

chat_id = '-1001597696937'

"""Add cookies for the requests.get"""
cookies = {'PHPSESSID': '21ue9a5qqroomap02ai2m7es39',
           'cf_clearance': 'aPOP4Mzfe7Lt13tkCc.rAO_pbZl4o2H1Z4fIv7qRQEI-1657791103-0-250',
           'csrfp_token': '6445a631fa',
           '__cf_bm': 'Cigfb.i_L1pkrvVaHIeBfpJs7rQeZaXbc9C6ctWUw2I-1657792123-0-AVIOJ/0yHx3/ZG75bQBq7E4Sspy67eRzdnmaLD5ujhUEqzPSjDiFt3qBIUIbEzs7HyrQV0PQDi2rmz6jeeOZy2hNS5m0LQWe+zDDfrV2LOtBNG14C1hrtZNyc1GfyJTH/w==',
           'sid': '34149d69d4431b8a9eeae75acac2b0b7'}

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
            message = "New post: " + "<a href='https://cracked.io/{}'>{}</a>".format(link, title) + " by " + "<a href='{}'>{}</a>".format(link_author, author) + " in categories: " + category

            if not profile_picture.startswith("https://static.cracked.io/images/default_avatar.png") or not profile_picture.startswith("https://static.cracked.to/images/transparent.png"):
                profile_picture = profile_picture.replace("avatars/", "avatars//").replace("./", "").split("?")[0].replace("\n", "")
                profile_picture = ("https://static.cracked.io/" + profile_picture)
           
            if profile_picture.startswith("https://static.cracked.io/images/default_avatar.png"):
                profile_picture = profile_picture.replace("https://static.cracked.io/", "")
                
            if profile_picture.startswith("https://static.cracked.to/images/transparent.png"):
                profile_picture = profile_picture.replace("https://static.cracked.to/", "")
            
                    
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
