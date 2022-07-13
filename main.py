import requests
from bs4 import BeautifulSoup
from time import sleep
import telegram

# you must configure this parameters
# ---------------------------------
alert = ".LOLI" or "CONFIG"
# ---------------------------------




bot = telegram.Bot(token='5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI')

chat_id = '-1001597696937'

# The first post will always be saved in this variable, if a new post has the same title, it will be ignored
last_title = ""

while True:
    r = requests.get('https://cracked.io/')
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
