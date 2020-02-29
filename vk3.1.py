import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id

keyboardAbout = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'про вас',
        },
        'color': 'positive'
    }
    ],
    [{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'расположение магазинов',
        },
        'color': 'positive'
    }
    ]
    ]
}

keyboard = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'про вас',
        },
        'color': 'positive'
    }
    ]]
}
keyboardAdr = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Расположение магазинов',
        },
        'color': 'positive'
    }
    ]]
}
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
          "label": "Треска"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Фуга"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Дельфин"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Кит"
        },
        "color": "positive"
      }
    ],
    [
      {
        "action": {
          "type": "text",
          "label": "Дарадо"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Нарвал"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Единорог"
        },
        "color": "positive"
      },
      {
        "action": {
          "type": "text",
          "label": "Касатка"
        },
        "color": "positive"
      }
    ]
  ]
}
keyboard3 = {
    'one_time': True,
    'buttons': [[{
        'action': {
            'type': 'text',
            'payload': json.dumps({'buttons': '1'}),
            'label': 'Заказать',
        },
        'color': 'positive'
    }
    ]]
}
'''
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
        write_msg(event.user_id,"Приветствую в магазине 'У Бобра'! Тут можно купить рыбу и не только.", keyboardAbout)
        answer = 1
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request.lower() == "про вас":
                write_msg(event.user_id, "Тут можно купить рыбу и не только!",keyboard1)
            elif request.lower() == "товары":
                write_msg(event.user_id,", ".join(staff), keyboard2)
            elif request.lower() in staff1:
                index = staff1.index(request.lower())
                write_msg(event.user_id,request.lower()+":")
                write_msg(event.user_id,"Цена: " + cost[index])
                write_msg(event.user_id,"Описание: " + desc[index], keyboard3)
            elif request.lower() == "заказать":
                write_msg(event.user_id,"Товар прибудет в наши магазины через 2 дня",keyboardAdr)
            elif request.lower() == "расположение магазинов":
                write_msg(event.user_id,"Москва, ул. Радио, 25\nМосква, Переведеновский переулок, 34",keyboardAbout)
            else:
                write_msg(event.user_id, "Я не понял твоего сообщения. Наверное слова в нём не входят в мой словарный запас",keyboard1)