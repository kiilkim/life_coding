#웹 스크래핑 / 노마드코더 

#파이썬 관련 일자리 찾기

#할것을 나눠서 생각한다.
# 
# 사이트로 가서
# 페이지가 몇개인지 
# 
import requests
from bs4 import BeautifulSoup

#requests 파이썬에서 요청을 만드는 기능을 모아놓은 것.
#request.org requests 2 

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")

print(indeed_result.text)
#200 은 ok

#우리가 원하는 것은 text

#html 에서 정보 추출
#페이지 숫자 beautifulsoup  _편리한 라이브러리 html 에서 정보추출하기 좋음

#html 에서 정보 추출 
#beautifulsoup 사이트 봐라

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

print(indeed_soup)


#fild_all 반환에 아주 유리


pagination = indeed_soup.find("ul", {"class":"pagination-list"})


pages = pagination.find_all('a')

spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])