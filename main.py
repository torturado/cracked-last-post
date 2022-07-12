
import requests
from bs4 import BeautifulSoup
from time import sleep
import telegram
from telegram import ParseMode

bot = telegram.Bot(token='5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI')

chat_id = '-1001597696937'

while True:
    r = requests.get('https://cracked.io/')
    soup = BeautifulSoup(r.text, 'html.parser')
    posts = soup.find_all('table', {'class': 'tborder latestthreads_table'})
    for post in posts:
        title = post.find('span', {'class': 'post_link'}).find('a').text
        author = post.find('span', {'class': 'latest-post-uname'}).find('a').text
        link = post.find('span', {'class': 'post_link'}).find('a').get('href')
        link_author = post.find('span', {'class': 'latest-post-uname'}).find('a').get('href')
        message = "New post: " + "<a href='https://cracked.io/{}'>{}</a>".format(link, title) + " by " + "<a href='{}'>{}</a>".format(link_author, author)
        #caption = "<a href='{}'>{}</a>".format(link, title)

        bot.send_message(chat_id=chat_id,
                         text=message,
                         parse_mode='HTML'
        )
        sleep(8)
    
    