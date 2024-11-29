import socket
import time

host = '127.0.0.1'
port = 8080
try:
    while True:
        status = 1  # статус подключенности к серверу
        # проверка на подключение
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((host, port))
        except Exception as e:
            print("не получилось подключиться к серверу, пробуем еще раз")
            time.sleep(1)
            status = 0

        if status == 1:
            message = "ping"

            # отправляем пинг
            client.send(message.encode("utf-8"))
            print(message)

            # получаем сообщение от сервера

            try:
                data = client.recv(1024).decode("utf-8")
                print(data)

                # проверки
                if data is None:
                    raise socket.error("ничего не было получено от сервера")
                if data == "Wrong input string":
                    raise socket.error("неправильное сообщение было отправлено клиентов")
                if data != "pong":
                    raise socket.error("неправильное сообщение было отправлено сервером")


            except Exception as e:
                print(e)
except KeyboardInterrupt as ke:
    print("Клиент остановлен вручную.")
