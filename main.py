import requests
from bs4 import BeautifulSoup
from time import sleep
import telegram
import os
from telegram import ParseMode
import json
from multiprocessing import Process
import logging

# you must configure this parameters
# ---------------------------------
alert = "spain" or "Spain" or "SPAIN" or "FRESH" or "Fresh" or "CONFIG" or "config" # minus or mayus doesn't matter
# ---------------------------------


url = "https://cracked.io/Forum-Cracking-Configs?sortby=started&order=desc&datecut=9999&prefix=0"
url2 = "https://cracked.io/Forum-OpenBullet?sortby=started&order=desc&datecut=9999&prefix=0"
url3 = "https://cracked.io/Forum-Silverbullet?sortby=started&order=desc&datecut=9999&prefix=0"
url4 = "https://cracked.io/Forum-Accounts?sortby=started&order=desc&datecut=9999&prefix=0"
url5 = "https://cracked.io/Forum-Proxies?sortby=started&order=desc&datecut=9999&prefix=0"
url6 = "https://cracked.io/Forum-Cracking-Tools?sortby=started&order=desc&datecut=9999&prefix=0"
url7 = "https://cracked.io/Forum-Databases?sortby=started&order=desc&datecut=9999&prefix=0"
url8 = "https://wabetainfo.com/testflight/?search=instagram"


bot = telegram.Bot(token='5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI')

chat_id = '-1001597696937'

"""Add cookies for the requests.get"""
cookies = {'cf_clearance': 'v1EhUoiRRjNklJF2PC1aokCxkRBgrw_xXUyjPmkTySI-1660142318-0-250'}

"""Add headers for the requests.get"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

# The first post will always be saved in this variable, if a new post has the same title, it will be ignored
last_title1 = ""
last_title2 = ""
last_title3 = ""
last_title4 = ""
last_title5 = ""
last_title6 = ""
last_title7 = ""
last_title8 = ""


def crackedio(alert, url, url2, url3, url4, url5, url6, url7, url8, bot, chat_id, cookies, headers, last_title1, last_title2, last_title3, last_title4, last_title5, last_title6, last_title7, last_title8):
    while True:
        try:
            """Fix that sends 2 messages at the same time"""
            """Configs category"""
            r = requests.get(url, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('form', class_='challenge-form interactive-form'):
                # if in page appears an h captcha, solve it with TwoCaptcha and get the cookie 'cf_clearance'
                r = requests.get("http://2captcha.com/in.php?key=b8ac57e2fd7c9f802d5a491b2edc1e15&method=hcaptcha&sitekey=45fbc4de-366c-40ef-9274-9f3feca1cd6c&pageurl=https://cracked.io/", stream=True)
                sleep(25)
                soup = BeautifulSoup(r.text, 'html.parser')
                # get the captcha id
                captcha_id = soup.find('div', class_='id').text
                print(captcha_id)
                # do a post request to 'url' with the captcha id
                r = requests.post(url, data={'g-recaptcha-response': captcha_id}, stream=True, headers=headers, cookies=cookies)
                print(r.text)
            posts = soup.find_all('tr', {'class': 'inline_row forum2'})
            for post in posts:
                """Get only the 4th post, the first 3 are pinned posts, always the same"""
                if posts.index(post) == 3:
                    title = post.find('span', {'class': ''}).find('a').find('span').text
                    author = post.find('div', {'class': 'author smalltext'}).find('a').text
                    link = post.find('span', {'class': ''}).find('a').get('href')
                    link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                    profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                    text = "Configs category"
                    category = text
                    if "<" or ">" in title:
                        title = title.replace("<", "")
                        title = title.replace(">", "")
                    message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                    
                    if not profile_picture.endswith("default_avatar.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                    
                    elif not profile_picture.endswith("transparent.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                
                
                        
                    if last_title1 != title:
                        last_title1 = title
                    
                        if alert in title:
                            print("Se ha encontrado una coincidencia! " + title)
                            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n\t\t 'Alert in title': '@kifera2'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        
                        message_id = bot.sendMessage(chat_id=chat_id,
                                        text=profile_picture,
                        ).message_id

                        bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=telegram.ParseMode.HTML,
                                        reply_to_message_id=message_id,
                        )
                        
                    else:
                        break
            sleep(3)

            """Do the same requests for all the urls"""
            r = requests.get(url2, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('form', class_='challenge-form interactive-form'):
                print("Verification Needed")
                while soup.find('form', class_='challenge-form interactive-form'):
                    r = requests.get(url2, stream=True, headers=headers, cookies=cookies)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    print("Refreshing...")
                    sleep(5)
            posts = soup.find_all('tr', {'class': 'inline_row forum2'})
            for post in posts:
                if posts.index(post) == 2:
                    title = post.find('span', {'class': ''}).find('a').find('span').text
                    author = post.find('div', {'class': 'author smalltext'}).find('a').text
                    link = post.find('span', {'class': ''}).find('a').get('href')
                    link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                    profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                    text = "Openbullet categories"
                    category = text
                    if "<" or ">" in title:
                        title = title.replace("<", "")
                        title = title.replace(">", "")
                    message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                    
                    if not profile_picture.endswith("default_avatar.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                    
                    elif not profile_picture.endswith("transparent.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                
                
                        
                    if last_title2 != title:
                        last_title2 = title
                        
                        if alert in title:
                            print("Se ha encontrado una coincidencia! " + title)
                            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n\t\t 'Alert in title': '@kifera2'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        message_id = bot.sendMessage(chat_id=chat_id,
                                        text=profile_picture,
                        ).message_id
                        
                        """If the title has a word from alert, add the alert to the message"""

                        bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=telegram.ParseMode.HTML,
                                        reply_to_message_id=message_id,
                        )
                        
                    else:
                        break
            
            sleep(3)

            r = requests.get(url3, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('form', class_='challenge-form interactive-form'):
                print("Verification Needed")
                while soup.find('form', class_='challenge-form interactive-form'):
                    r = requests.get(url3, stream=True, headers=headers, cookies=cookies)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    print("Refreshing...")
                    sleep(5)
            posts = soup.find_all('tr', {'class': 'inline_row forum2'})
            for post in posts:
                if posts.index(post) == 0:
                    title = post.find('span', {'class': ''}).find('a').find('span').text
                    author = post.find('div', {'class': 'author smalltext'}).find('a').text
                    link = post.find('span', {'class': ''}).find('a').get('href')
                    link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                    profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                    text = "Silverbullet categories"
                    category = text
                    if "<" or ">" in title:
                        title = title.replace("<", "")
                        title = title.replace(">", "")
                    message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                    
                    if not profile_picture.endswith("default_avatar.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                    
                    elif not profile_picture.endswith("transparent.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                
                
                        
                    if last_title3 != title:
                        last_title3 = title

                        if alert in title:
                            print("Se ha encontrado una coincidencia! " + title)
                            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n\t\t 'Alert in title': '@kifera2'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        message_id = bot.sendMessage(chat_id=chat_id,
                                        text=profile_picture,
                        ).message_id
                        
                        bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=telegram.ParseMode.HTML,
                                        reply_to_message_id=message_id,
                        )
                        
                    else:
                        break

            sleep(3)

            r = requests.get(url4, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('form', class_='challenge-form interactive-form'):
                print("Verification Needed")
                while soup.find('form', class_='challenge-form interactive-form'):
                    r = requests.get(url4, stream=True, headers=headers, cookies=cookies)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    print("Refreshing...")
                    sleep(5)
            posts = soup.find_all('tr', {'class': 'inline_row forum2'})
            for post in posts:
                if posts.index(post) == 0:
                    title = post.find('span', {'class': ''}).find('a').find('span').text
                    author = post.find('div', {'class': 'author smalltext'}).find('a').text
                    link = post.find('span', {'class': ''}).find('a').get('href')
                    link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                    profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                    text = "Accounts categories"
                    category = text
                    if "<" or ">" in title:
                        title = title.replace("<", "")
                        title = title.replace(">", "")
                    message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                    
                    if not profile_picture.endswith("default_avatar.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                    
                    elif not profile_picture.endswith("transparent.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                
                
                        
                    if last_title4 != title:
                        last_title4 = title

                        if alert in title:
                            print("Se ha encontrado una coincidencia! " + title)
                            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n\t\t 'Alert in title': '@kifera2'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        message_id = bot.sendMessage(chat_id=chat_id,
                                        text=profile_picture,
                        ).message_id
                        
                        bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=telegram.ParseMode.HTML,
                                        reply_to_message_id=message_id,
                        )
                        
                    else:
                        break

            sleep(3)
            r = requests.get(url5, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('form', class_='challenge-form interactive-form'):
                print("Verification Needed")
                while soup.find('form', class_='challenge-form interactive-form'):
                    r = requests.get(url5, stream=True, headers=headers, cookies=cookies)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    print("Refreshing...")
                    sleep(5)
            posts = soup.find_all('tr', {'class': 'inline_row forum2'})
            for post in posts:
                if posts.index(post) == 0:
                    title = post.find('span', {'class': ''}).find('a').find('span').text
                    author = post.find('div', {'class': 'author smalltext'}).find('a').text
                    link = post.find('span', {'class': ''}).find('a').get('href')
                    link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                    profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                    text = "Proxies categories"
                    category = text
                    if "<" or ">" in title:
                        title = title.replace("<", "")
                        title = title.replace(">", "")
                    message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                    
                    if not profile_picture.endswith("default_avatar.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                    
                    elif not profile_picture.endswith("transparent.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                
                
                        
                    if last_title5 != title:
                        last_title5 = title

                        if alert in title:
                            print("Se ha encontrado una coincidencia! " + title)
                            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n\t\t 'Alert in title': '@kifera2'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        message_id = bot.sendMessage(chat_id=chat_id,
                                        text=profile_picture,
                        ).message_id
                        
                        bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=ParseMode.HTML,
                                        reply_to_message_id=message_id,
                        )
                        
                    else:
                        break
            
            sleep(3)
            r = requests.get(url6, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('form', class_='challenge-form interactive-form'):
                print("Verification Needed")
                while soup.find('form', class_='challenge-form interactive-form'):
                    r = requests.get(url6, stream=True, headers=headers, cookies=cookies)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    print("Refreshing...")
                    sleep(5)
            posts = soup.find_all('tr', {'class': 'inline_row forum2'})
            for post in posts:
                if posts.index(post) == 1:
                    title = post.find('span', {'class': ''}).find('a').find('span').text
                    author = post.find('div', {'class': 'author smalltext'}).find('a').text
                    link = post.find('span', {'class': ''}).find('a').get('href')
                    link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                    profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                    text = "Cracking tools categories"
                    category = text
                    if "<" or ">" in title:
                        title = title.replace("<", "")
                        title = title.replace(">", "")
                    message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                    
                    if not profile_picture.endswith("default_avatar.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                    
                    elif not profile_picture.endswith("transparent.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                
                
                        
                    if last_title6 != title:
                        last_title6 = title

                        if alert in title:
                            print("Se ha encontrado una coincidencia! " + title)
                            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n\t\t 'Alert in title': '@kifera2'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        message_id = bot.sendMessage(chat_id=chat_id,
                                        text=profile_picture,
                        ).message_id
                        
                        bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=telegram.ParseMode.HTML,
                                        reply_to_message_id=message_id,
                        )
                        
                    else:
                        break                        

            sleep(3)

            r = requests.get(url7, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            if soup.find('form', class_='challenge-form interactive-form'):
                print("Verification Needed")
                while soup.find('form', class_='challenge-form interactive-form'):
                    r = requests.get(url7, stream=True, headers=headers, cookies=cookies)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    print("Refreshing...")
                    sleep(5)
            posts = soup.find_all('tr', {'class': 'inline_row forum2'})
            for post in posts:
                if posts.index(post) == 0:
                    title = post.find('span', {'class': ''}).find('a').find('span').text
                    author = post.find('div', {'class': 'author smalltext'}).find('a').text
                    link = post.find('span', {'class': ''}).find('a').get('href')
                    link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                    profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                    text = "Databases categories"
                    category = text
                    if "<" or ">" in title:
                        title = title.replace("<", "")
                        title = title.replace(">", "")
                    message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                    
                    if not profile_picture.endswith("default_avatar.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                    
                    elif not profile_picture.endswith("transparent.png"):
                        profile_picture = profile_picture.split("?")[0].replace("\n", "")
                
                
                        
                    if last_title7 != title:
                        last_title7 = title

                        if alert in title:
                            print("Se ha encontrado una coincidencia! " + title)
                            message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n\t\t 'Alert in title': '@kifera2'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        message_id = bot.sendMessage(chat_id=chat_id,
                                        text=profile_picture,
                        ).message_id
                        
                        bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=telegram.ParseMode.HTML,
                                        reply_to_message_id=message_id,
                        )
                        
                    else:
                        break                        

            sleep(3)

            r = requests.get(url8, stream=True, headers=headers, cookies=cookies)
            soup = BeautifulSoup(r.text, 'html.parser')
            slot = soup.find('span', {'id': 'corners1'}).text
            if slot == "SLOT AVAILABLE":
                message = f"Instagram beta disponible!!"
                bot.sendMessage(chat_id=chat_id,
                                        text=message,
                                        disable_web_page_preview=True,
                                        parse_mode=telegram.ParseMode.HTML,
                        )

            sleep(3)

        except requests.exceptions.ChunkedEncodingError:
            print("Error ChunkedEncodingError")
            sleep(5)
            continue
        
        
        except telegram.error.RetryAfter:
            print("Error RetryAfter")
            sleep(5)
            continue
        except telegram.error.TimedOut:
            print("Error TimedOut")
            sleep(5)
            continue
        except telegram.error.Conflict:
            print("Error Conflict")
            sleep(5)
            continue




update_id = ""

def main():
        global update_id
        # Telegram Bot Authorization Token
        bot_token = '5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI'
        # get the first pending update_id, this is so we can skip over it in case
        # we get an "Unauthorized" error.
        try:
            update_id = bot.getUpdates()[0].update_id
        except IndexError:
            update_id = None

        def handle_message(message):
                        print('Got message: {}'.format(message.text))
                        # Sends the response back to the channel
                        url = "https://api.safone.tech/ipinfo?ip={}".format(message.text)
                        resp = requests.get(url, headers=headers)
                        data = json.loads(resp.text)
                        print(data)
                        bot.sendMessage(chat_id=chat_id, text=data)

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        """Activate this only when message sent to the chat"""
        # bot.message_loop(handle_message)
        # print('Listening ...')
        # Keep the program running.
        # For a while() loop, the program will sleep for 5 seconds and then check if there are any new messages.
        # If there are, it will call the handle_message function.
        while True:
            sleep(5)
            updates = bot.getUpdates(offset=update_id, timeout=10)
            if updates:
                for update in updates:
                    if update.message:
                        # look if the message is from the bot
                        if update.message.from_user.username == 'delocosmaninbot':
                            # look in the message for the word "."
                            if '.' in update.message.text:
                                handle_message(update.message)
                        else:
                            print("No ip address")
                        update_id = update.update_id + 1

    
if __name__ == '__main__':
    Process(target=main).start()
    Process(target=crackedio(alert, url, url2, url3, url4, url5, url6, url7, bot, chat_id, cookies, headers, last_title1, last_title2, last_title3, last_title4, last_title5, last_title6, last_title7)).start()
