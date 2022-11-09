from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from pathlib import Path

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
people  = {'1': ['아이린', '수지', '아이유', '송혜교'],
          '2': ['솔라', '문별', '휘인', '화사', '장나라'],
          '3': ['개그우먼 김민경', '이영자', '이국주'],
          '4': ['개그우먼 김현정', '장도현', '오나미', '김숙'],
          '5': ['박나래', '안영미', '조정린','하리수','박경림']}
Path("./img").mkdir(parents=True, exist_ok=True)
for k, v in people.items():
    Path("./img/" + k).mkdir(parents=True, exist_ok=True)
    for person in v:
        url = baseUrl + quote_plus(person)
        html = urlopen(url)
        soup = bs(html, "html.parser")
        img = soup.find_all(class_='_img', limit=50)
        Path("./img/" + k + '/' + person).mkdir(parents=True, exist_ok=True)
        n = 1
        for i in img:
            imgUrl = i['data-source']
            with urlopen(imgUrl) as f:
                with open('./img/' + k + '/' + person + '/' + person + ' ' + str(n)+'.jpg','wb') as h: # w - write b - binary
                    img = f.read()
                    h.write(img)
            n += 1
print('다운로드 완료')
