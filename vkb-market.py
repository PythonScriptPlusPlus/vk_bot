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
        write_msg(event.user_id,"Приветствую в магазине 'У Бобра'! Тут можно купить рыбу и не только.")
        answer = 1
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request.lower() == "про вас":
                write_msg(event.user_id, "Тут можно купить рыбу и не только!")
            elif request.lower() == "товары":
                write_msg(event.user_id,", ".join(staff))
            elif request.lower() in staff1:
                index = staff1.index(request.lower())
                write_msg(event.user_id,request.lower()+":")
                write_msg(event.user_id,"Цена: " + cost[index])
                write_msg(event.user_id,"Описание: " + desc[index])
            else:
                write_msg(event.user_id, "Я не понял твоего сообщения. Наверное слова в нём не входят в мой словарный запас")
