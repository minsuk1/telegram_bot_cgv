import time
import requests
import telegram
import random
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Pool


def send(val):
    bot.send_message(chat_id = 5219383547, text = '닥터스트레인지 예매해야해!!!', timeout = 30)


# theatercode
# 0013 : 용산
# 0107 : 청담
# 0112 : 여의도
bot = telegram.Bot(token = '5315643529:AAFpBj0jUQVob1IH_wqe7gw5MiGy4EZos78')
# 용산
url_yong = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220420'

# 청담
url_c = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220420'

# 여의도
url_y = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220420'

urls = [url_yong, url_c, url_y]

def minsuk_RPA():
    urls = [url_yong, url_c, url_y]
    for url in urls:
        html = requests.get(url, timeout = 5)
        time.sleep(random.uniform(1,4))
        soup = BeautifulSoup(html.text, 'html.parser')

        # 영화 제목만 추출해서 리스트에 넣기, 용산/여의도/청담 다 찾아서 넣기
        final_movieNames = []
        origin_movieNames = soup.select('div[class="info-movie"]')
        for name in origin_movieNames:
            tmp = name.find("strong").text
            result = tmp.strip()
            result = result.replace("\n", "")
            final_movieNames.append(result)

        # 리스트 안에 영화 제목 돌면서 "스트레인지" 포함된 영화 추출해서 Bot에 보내기
        Hope_Movie = '동물'
        for movie in final_movieNames:
            if Hope_Movie in movie:
                # 멀티 프로세싱 적용
                #pool = Pool(2)
                #pool.map(send, range(0, 5000))
                bot.sendMessage(chat_id = 5219383547, text = movie +' 예매해야해!!!')
                sched.pause()

# if __name__ == "__main__":
#     minsuk_RPA(urls)

if __name__ == '__main__':
    sched = BlockingScheduler(timezone='Asia/Seoul')
    sched.add_job(minsuk_RPA, 'interval', seconds=50)
    sched.start()


# pip install requests
# pip install python-telegram-bot
# pip install BeautifulSoup4
# pip install apscheduler