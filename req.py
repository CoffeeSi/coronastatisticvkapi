import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.content,"html.parser")

Corona = soup.findAll("span")