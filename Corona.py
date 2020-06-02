import vk_api, time
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

import requests
from bs4 import BeautifulSoup

vk_session = vk_api.VkApi(token="ac77486334a745bd6034a4b6a8b5a35cf9a1a0c8cf92ba403821479ec46e525df5e65cf6d2f4401f8a36c")

longpoll = VkBotLongPoll(vk_session, group_id=193573819)
vk = vk_session.get_api()

url = "https://www.worldometers.info/coronavirus/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

def mes():
    messages = vk.messages.getConversations(offset = 0, count = 20, filter="all")
    if messages["count"] >= 1:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:
                text = event.obj.text
                if text.lower() == "корона":
                    vk.messages.send(peer_id=event.obj.peer_id,
                                     message="Время " + tt +
                                             "\n👾Заболевших во всем мире : " + Corona[4].text +
                                             "\n💀Умерших во всем мире : " + Corona[5].text +
                                             "\n❣Выздоровшие во всем мире : " + Corona[6].text,
                                     random_id=0)
                vk.messages.markAsAnsweredConversation(peer_id=event.obj.peer_id,answered=1)
                break

while True:
    time.sleep(1)
    tt = time.strftime("%H:%M:%S")
    if tt == "06:00:30":
        vk.messages.send(user_id=316517171,
                         message=tt+
                         "\n👾Заболевших во всем мире : " + Corona[4].text+
                         "\n💀Умерших во всем мире : " + Corona[5].text+
                         "\n❣Выздоровшие во всем мире : " + Corona[6].text,
                         random_id=0)

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")

    Corona = soup.findAll("span")
    print(Corona[4].text)

    mes()


