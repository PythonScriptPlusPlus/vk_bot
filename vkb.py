import vk_api
from random import randint
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": get_random_id()})


# API-ключ созданный ранее
token = "38bd49d5c8c80c9a708afaf884a59eb7822efc6111171a8a76983eded89079ee837844937a49e92fb720c"

# Переменная для проверки начала программы/цикла
answer = 0
moodGood = ["прекрасно","хорошо","нормально","отлично"]
moodBad = ["ужасно","отвратительно","плохо"]

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request.lower() == "привет":
                write_msg(event.user_id, "Привет")
            elif request.lower() == "пока":
                write_msg(event.user_id, "Увидимся!")
            elif request.lower() == "как дела?":
                write_msg(event.user_id, moodGood[randint(0,3)] + ". А у тебя как?")
                answer = 1
            elif request.lower() in moodGood and answer == 1:
                write_msg(event.user_id, "Это хорошо, что хорошо")
                answer = 0
            elif request.lower() in moodBad and answer == 1:
                write_msg(event.user_id, "Это плохо! Надеюсь скоро всё наладится! ")
                answer = 0
            else:
                write_msg(event.user_id, "Я не понял твоего сообщения. Наверное слова в нём не входят в мой словарный запас")
