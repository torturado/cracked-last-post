import aiohttp
from bs4 import BeautifulSoup
import asyncio
from multiprocessing import Process
import logging
import telegram

# your configuration
alert = "config"


urls = {
    "https://cracked.io/Forum-Cracking-Configs?sortby=started&order=desc&datecut=9999&prefix=0": 3,
    "https://cracked.io/Forum-OpenBullet?sortby=started&order=desc&datecut=9999&prefix=0": 2,
    "https://cracked.io/Forum-Silverbullet?sortby=started&order=desc&datecut=9999&prefix=0": 0,
    "https://cracked.io/Forum-Accounts?sortby=started&order=desc&datecut=9999&prefix=0": 0,
    "https://cracked.io/Forum-Proxies?sortby=started&order=desc&datecut=9999&prefix=0": 0,
    "https://cracked.io/Forum-Cracking-Tools?sortby=started&order=desc&datecut=9999&prefix=0": 1,
    "https://cracked.io/Forum-Tutorials-Guides-etc?sortby=started&order=desc&datecut=9999&prefix=0": 3,
    "https://cracked.io/Forum-Upgraded-Tools?sortby=started&order=desc&datecut=9999&prefix=0": 12,
    "https://cracked.io/Forum-Exclusive-Releases?sortby=started&order=desc&datecut=9999&prefix=0": 2
}

url_last_title = {url: None for url in urls}

bot = telegram.Bot(token='5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI')

chat_id = '-1001597696937'

async def send_message(message, profile_picture):
    message_id = await bot.send_photo(chat_id=chat_id, photo=profile_picture)
    await bot.sendMessage(chat_id=chat_id, text=message, parse_mode='HTML', reply_to_message_id=message_id.message_id)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def check():
    while True:
        async with aiohttp.ClientSession() as session:
            for url, index in urls.items():
                try:
                    response_text = await fetch(session, url)
                    soup = BeautifulSoup(response_text, 'html.parser')
                    if soup.find('form', class_='challenge-form interactive-form'):
                        print("cloudflare activated sorry. Retrying in 5 seconds")
                        await asyncio.sleep(1)
                        continue
                    posts = soup.find_all('tr', {'class': 'inline_row forum2'})

                    if len(posts) > index:
                        post = posts[index]
                        title = post.find('span', {'class': ''}).find('a').find('span').text
                        author = post.find('div', {'class': 'author smalltext'}).find('a').text
                        link = post.find('span', {'class': ''}).find('a').get('href')
                        link_author = post.find('div', {'class': 'author smalltext'}).find('a').get('href')
                        profile_picture = post.find('img', {'class': 'last-post-avatar'}).get('src')
                        category = url.split('/')[3].replace("-", " ").replace("Forum", "").split('?')[0].title()
                        title = title.replace("<", "").replace(">", "")
                        message = f"⚠ Detectada Filtracion ⚠\n{{\n\t\t'site': <a href=\"https://cracked.io/{link}\">'{title}'</a>,\n\t\t'author': <a href='{link_author}'>'{author}'</a>,\n\t\t'categories': '{category}'\n}}\n\t🔹Cracked.io monitoring system🔹"

                        if profile_picture.endswith(("default_avatar.png", "transparent.png")):
                            profile_picture = profile_picture.split("?")[0].replace("\n", "")

                        if url_last_title[url] != title:
                            url_last_title[url] = title
                            await send_message(message, profile_picture)
                except Exception as e:
                    logging.error(e)
                    await asyncio.sleep(60)
                await asyncio.sleep(1)

async def main():
    await asyncio.gather(check())

if __name__ == '__main__':
    asyncio.run(main())
