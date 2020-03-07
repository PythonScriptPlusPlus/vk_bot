import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id

start = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons':'1'}),
            'label': 'Начать',
        },
        'color':'positive'
    }]]
}

keyboard1 = {
  "one_time": True,
  "buttons": [
    [
      {
        "action": {
          "type": "text",
          "label": "3.1415"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "3.1315"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "3"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "9.8"
        },
        "color": "positive"
      }
    ]]
}

keyboard2 = {
  "one_time": True,
  "buttons": [
    [
      {
        "action": {
          "type": "text",
          "label": "9.867"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "3.1315"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "1.618"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "1.5"
        },
        "color": "positive"
      }
    ]]
}

keyboard3 = {
  "one_time": True,
  "buttons": [
    [
      {
        "action": {
          "type": "text",
          "label": "9.86"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "9.8672"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "10"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "9"
        },
        "color": "positive"
      }
    ]]
}

'''
keyboard1 = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'товары',
        },
        'color': 'positive'
    }
    ]]
}
keyboard2 = {
  "one_time": True,
  "buttons": [
    [
      {
        "action": {
          "type": "text",
          "label": "Профиль"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Магазин"
        },
        "color": "positive"
      }
    ],
    [
      {
        "action": {
          "type": "text",
          "label": "Склад"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Фарм"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Помощь"
        },
        "color": "positive"
      }
    ]
  ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
'''

def write_msg(user_id, msg, keyboard=False):
    if keyboard == False:
        vk.method('messages.send', {'user_id': user_id, 'message': msg, "random_id":get_random_id()})
    else:
        vk.method('messages.send', {'user_id': user_id, 'message': msg, 'keyboard': str(json.dumps(keyboard)), "random_id":get_random_id()})



# API-ключ созданный ранее
token = "3fd3dac19c9154b58352d0efb3d1479d782b3d02e02ab9d16be64668a3638b5be07a337c7eff7241d2af2"
# Переменная для проверки начала программы/цикла
answer = 0
question = 0
a = 0
right = 0

staff = ["Треска","Фуга","Дельфин","Кит","Дарадо","Нарвал","Единорог","Касатка"]
staff1 = ["треска","фуга","дельфин","кит","дарадо","нарвал","единорог","касатка"]
cost = ["200руб","1000руб","10000руб","1000000руб","350руб","35000руб","9999999990руб","800000руб"]
desc = ["Вкусная рыба","Поосторожней с её проготовлением","Не знаю зачем, но ты его можешь купить",
        "ЭТО ЖЕ КИТ!!!","Вкусная, но редкая рыба","Можешь продать рог", "Оно того стоит","Осторожней! Она может съесть!"]
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():
    if answer == 0:
        write_msg(event.user_id,"Ты сейчас пройдёшь тест на знание забавных математических фактов. Нажми кнопку 'Начать', и ты начнёшь проходить тест.", start)
        answer = 1
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request.lower() == "начать" and question == 0:
                write_msg(event.user_id, "Вопрос №1. Чему равно число Пи?",keyboard1)
                question = 1
            elif request.lower() == "3.1415" and question == 1:
                right += 1
                a += 1
            else:
                a +=1

            if question == 1 and a == 1:
                write_msg(event.user_id,"Вопрос №2. Чему равно число Фи?",keyboard2)
                question = 2
            elif request.lower() == "1.618" and question == 2:
                right += 1
                a += 1
            else:
                a += 1

            if question == 2 and a == 2:
                write_msg(event.user_id, "Вопрос №3. Чему равно число Джи?", keyboard3)
                question = 3
            elif request.lower() == "9.86" and question == 3:
                right += 1
                a += 1
            else:
                a += 1

            if a == 3:
                if right == 3:
                    write_msg(event.user_id, "Молодец! ты прошёл весь тест правильно!")
                if right == 2 or right == 1:
                    write_msg(event.user_id, "Ты прошёл весь тест! Правильных ответов " + right + "/3")
                if right == 0:
                    write_msg(event.user_id,"Всё не правильно! Учи лучше!")