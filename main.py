import websocket
import json
import pyautogui as ag
from time import sleep

client_secret = '00cVc7q7yYAtU9W3p9RlG9ANwVvQLkvJ' \
         'LRsDX0VSmFyvz1hFIPRXzFdIOVes3KAO' \
         'aAtlCSUbwgqn3LzY8aeSugrEdIPy5jsz' \
         'r13Yu0R8cXJo2ALf4FfRSFLLd4eBF4Hh'
client_id = 'thTgkhDou9rdVFsV6mk51LqN0nYDDTYXpR8YYAsA'

ws = websocket.WebSocket()
ws.connect("wss://localhost:6868/")

d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "requestAccess",
    "params": {
        "clientId": client_id,
        "clientSecret": client_secret  # Request Access
    }
}
ws.send(json.dumps(d))


d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "authorize",
    "params": {
        "clientId": client_id,
        "clientSecret": client_secret
    }
}
ws.send(json.dumps(d))  # Авторизация

d = json.loads(ws.recv())
cortex_token = d["result"]["cortexToken"]  # Получение CortexToken

ws.send('{ "id": 1,"jsonrpc": "2.0","method": "queryHeadsets"}')  # Список интерфейсов
d = json.loads(ws.recv())
interface = d["result"][0]["id"]  # Получение ID интерфейса. В программе можно будет сделать выбор из нескольких

d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "controlDevice",
    "params":
    {
        "command": "connect",   "headset": interface
    }}
ws.send(json.dumps(d))  # Подключение к интерфейсу
ws.recv()

d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "createSession",
    "params": {
        "cortexToken": cortex_token,
        "headset": interface,
        "status": "open"
    }
}
ws.send(json.dumps(d))  # новая сессия
d = json.loads(ws.recv())
session_ID = d["result"]["id"]  # ID сессии

d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "cortexToken": cortex_token,
        "session": session_ID,
        "streams": ["com", "sys"]
    }
}
ws.send(json.dumps(d))  # Подписка на канал с командами и sys
ws.recv()



d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "queryProfile",
    "params": {
        "cortexToken": cortex_token
    }
}
ws.send(json.dumps(d))  # Список профилей
print(ws.recv())

d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "setupProfile",
    "params": {
        "cortexToken": cortex_token,
        "headset": interface,
        "profile": "Travvys Mouse",
        "status": "load"
    }
}
ws.send(json.dumps(d))  # загрузка профиля travvys mouse
print(ws.recv())
d = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "getDetectionInfo",
    "params": {
        "detection": "mentalCommand"
    }
}
ws.send(json.dumps(d))  # включаем поток данных
ws.recv()


def move(comand):
    t = 10
    x = ag.position()[0]
    y = ag.position()[1]
    if comand == 'drop':
        ag.moveTo(x, y + t)
    if comand == 'lift':
        ag.moveTo(x, y - t)
    if comand == 'right':
        ag.moveTo(x + t, y)
    if comand == 'left':
        ag.moveTo(x - t, y)


while 1 == 1:
    d = json.loads(ws.recv())
    print(d)
    c = d["com"][0]
    print(c)
    move(c)

