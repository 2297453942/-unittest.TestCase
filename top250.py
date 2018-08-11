import requests
import bs4
res = requests.get("https://movie.douban.com/top250")
soup = bs4.BeautifulSoup(res.text,"html.parser")
targets = soup.find_all("div",class_="hd")
for top250 in targets:
    print(top250.a.span.text)
