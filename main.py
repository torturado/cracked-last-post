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
    r = requests.get(url, stream=True, headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.text, 'html.parser')
    posts = soup.find_all('table', {'class': 'tborder latestthreads_table'})
    for post in posts:
            title = post.find('span', {'class': 'post_link'}).find('a').text
            post_id = post.find('span', {'class': 'post_link'}).find('a').get('href')
            author = post.find('span', {'class': 'latest-post-uname'}).find('a').text
            link = post.find('span', {'class': 'post_link'}).find('a').get('href')
            link_author = post.find('span', {'class': 'latest-post-uname'}).find('a').get('href')  
            message = "New post: " + "<a href='https://cracked.io/{}'>{}</a>".format(link, title) + " by " + "<a href='{}'>{}</a>".format(link_author, author)

            if last_title != title:
                last_title = title

                if alert in title:
                    print("Se ha encontrado una coincidencia! " + title)

                bot.sendMessage(chat_id=chat_id,
                                text=message,
                                disable_web_page_preview=True,
                                parse_mode=telegram.ParseMode.HTML,
                )
            else:
                break
    sleep(10)
