import socket
import time

# Создаем сокет для работы с сетью
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))  # Привязываем сервер к хосту и порту
server.listen(5)  # Устанавливаем сервер в режим ожидания подключений (до 5 клиентов в очереди)

print("Сервер запущен и ожидает подключения...")

try:
    while True:  # Главный цикл для обработки подключений
        print("Ожидание подключения клиента...")
        try:
            # Ожидаем подключения клиента
            client, client_addr = server.accept()
            print(f"Клиент подключился: {client_addr}")

            while True:  # Цикл для работы с конкретным клиентом
                client.settimeout(5)
                try:
                    # Получаем сообщение от клиента
                    message = client.recv(1024).decode('utf-8')
                    if not message:
                        print("Клиент отключился")
                        break

                    print(f"Получено от клиента: {message}")

                    # Формируем ответ в зависимости от сообщения клиента
                    if message == "ping":
                        send = "pong"
                    else:
                        send = "Wrong input string"

                    # Отправляем ответ клиенту
                    client.send(send.encode('utf-8'))
                    print(f"Отправлено: {send}")

                except socket.timeout:
                    print("Клиент слишком долго не отправляет данные")
                    break
                except Exception as e:
                    print(f"Ошибка при обработке данных от клиента: {e}")
                    break

            client.close()  # Закрываем соединение с клиентом

        except Exception as e:
            print(f"Ошибка при ожидании подключения: {e}")

except KeyboardInterrupt:
    print("Сервер остановлен вручную")
finally:
    server.close()
    print("Сервер завершил работу")