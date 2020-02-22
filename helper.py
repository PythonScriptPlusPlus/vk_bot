import vk_api
from random import randint
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": get_random_id()})


# API-ключ созданный ранее
token = "3fd3dac19c9154b58352d0efb3d1479d782b3d02e02ab9d16be64668a3638b5be07a337c7eff7241d****"

# Переменная для проверки начала программы/цикла
answer = 0
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if answer == 0:
        write_msg(event.user_id,"Я помогу с программированием")
        answer = 1
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request.lower() in "print()":
                write_msg(event.user_id, "Выводит то что ты напишешь в скобках\n https://www.internet-technologies.ru/articles/funkcii-print-v-python.html")
            elif request.lower() in "переменная":
                write_msg(event.user_id, "Конейнер для информации\nhttps://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)")
            elif request.lower() == "цикл":
                write_msg(event.user_id,"Конструкция для многократного исполнения набора инструкций\nhttps://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D0%BA%D0%BB_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)")
            elif request.lower() == "for":
                write_msg(event.user_id, "For предназначен для перебора элементов структур данных и некоторых других объектов\nhttps://younglinux.info/python/for.php")
            elif request.lower() == "while":
                write_msg(event.user_id,"Цикл, который работает до тех пор, пока условие истино\nhttps://pythontutor.ru/lessons/while/")
            elif request.lower() in "integer":
                write_msg(event.user_id,"Тип данных/переменных, который хранит числа\nhttps://pythoner.name/int-function")
            elif request.lower() in "string":
                write_msg(event.user_id,"Тип данных/переменных, который хранит текст\nhttps://o7planning.org/ru/11423/python-string-tutorial")
            elif request.lower() == "python":
                write_msg(event.user_id,"Высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода\n https://ru.wikipedia.org/wiki/Python")
            else:
                write_msg(event.user_id, "Я такого не знаю, либо ты написал что-то не правильно")
