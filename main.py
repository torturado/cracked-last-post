try:
    import requests
    from bs4 import BeautifulSoup
    from time import sleep
    import telegram
    from telegram import ParseMode
    import os
except ImportError:
    os.system("pip3 install requests")
    os.system("pip3 install bs4")
    os.system("pip3 install time")
    os.system("pip3 install telegram")
    os.system("pip3 install os")

bot = telegram.Bot(token='5397486870:AAEQ1AuaEfUeof9NIhrK4dRi5UWwzPNNmJI')

chat_id = '-1001597696937'
post_id = 0

cookies = {
    '__cf_bm': "h.pMY48r0QxgdZxdjxUou9Wra4FiHc0MKGiOAG1ut7o-1657614225-0-AUM8vKJbFHt/L94On6B6t/qsNUuEWCmmPgmXVCMey0ZlcYT2xG7xgQRDQSh+RCy0EfSkQR4YcpSraa7lx44NKhvKsEcp/i7UVsNWESfxqjtl5yqNo0/PG4NFgEgSG6XJmg==",
    'cf_clearance': "mkCK71fCvuHX0oW0T70YCyvOTCN.283rLNaJL3smcPc-1657612841-0-250",
    'csrfp_token':	"03e9255aee",
    'PHPSESSID': "h93b58s6vejldek3s9k2f31s1c",
    'sid':	"7c8d1959a40c1fdb1850d52d038c6f9d",
}

headers = {
    'Host': 'cracked.io',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://cracked.io/',
    'Alt-Used': 'cracked.io',
    'Connection': 'keep-alive',
}





while True:
    old_post_id = post_id
    r = requests.get('https://cracked.io/', cookies=cookies, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    posts = soup.find_all('table', {'class': 'tborder latestthreads_table'})
    for post in posts:
        title = post.find('span', {'class': 'post_link'}).find('a').text
        post_id = post.find('span', {'class': 'post_link'}).find('a').get('href')
        if post_id == old_post_id:
            break
        author = post.find('span', {'class': 'latest-post-uname'}).find('a').text
        link = post.find('span', {'class': 'post_link'}).find('a').get('href')
        link_author = post.find('span', {'class': 'latest-post-uname'}).find('a').get('href')
        message = "New post: " + "<a href='https://cracked.io/{}'>{}</a>".format(link, title) + " by " + "<a href='{}'>{}</a>".format(link_author, author)

        bot.send_message(chat_id=chat_id,
                         text=message,
                         parse_mode=ParseMode.HTML
        )
    sleep(8)
    
    
