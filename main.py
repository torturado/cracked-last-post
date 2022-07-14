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
cookies = {'PHPSESSID': 'bimr9fcf952l5dmvh55pf5qlpc',
           'cf_clearance': 'IO4oAvHbHPk48k7TtAVK4jd1HTPx_Q2clDPQDjfZ0tw-1657711150-0-250',
           'csrfp_token': '33ed1ce66c',
           '__cf_bm': 'D2UO0.qDEdMXhiRyZN1KJ.mTHtCWeYPWWDx6Rbm19sA-1657712023-0-AbphBzWtNOU1Rw7bC9G0YP43Ebt51jZLl9nseW/ZO0OAYqBcygwGexsYXvLWo/wq3BWvKpgu8uIMpRIGbq6RmvbCTO26NTJpLZK8HS9qXbj5ugotljn2ytAj4LLx6cBZ4w==',
           'sid': '3e0711b721a533577b7e7476980517b9'}

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

            """if src of profile_picture finishes with "default_avatar.png" or with "transparent.png", remove "https://static.cracked.io/" from start"""
            if profile_picture.endswith("default_avatar.png") or profile_picture.endswith("transparent.png"):
                profile_picture = profile_picture.replace("https://static.cracked.io/", "")
            
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
        sleep(2)
    
    except requests.exceptions.ChunkedEncodingError:
        print("Error ChunkedEncodingError")
        sleep(3)
        continue
    
    except requests.exceptions.ConnectionError:
        print("Error ConnectionError")
        sleep(3)
        continue
