import vk_api, time
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

import requests
from bs4 import BeautifulSoup

vk_session = vk_api.VkApi(token="""VK API TOKEN""")

longpoll = VkBotLongPoll(vk_session, group_id="""GROUP ID VK""")
vk = vk_session.get_api()

url = "https://www.worldometers.info/coronavirus/"
headers = {
    "User-Agent": """USER AGENT"""}


def mes():
    messages = vk.messages.getConversations(offset=0, count=20, filter="all")
    if messages["count"] >= 1:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:
                text = event.obj.text
                if text.lower() == "корона":
                    vk.messages.send(peer_id=event.obj.peer_id,
                                     message="👾Заболевших во всем мире : " + Corona[4].text +
                                             "\n💀Умерших во всем мире : " + Corona[5].text +
                                             "\n❣Выздоровшие во всем мире : " + Corona[6].text,
                                     random_id=0)
                vk.messages.markAsAnsweredConversation(peer_id=event.obj.peer_id, answered=1)
                break


while True:
    time.sleep(1)

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")

    Corona = soup.findAll("span")

    mes()
