import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

print("Сервер запущен и ожидает подключения...")

try:
    while True:
        client, client_addr = server.accept()
        client.settimeout(5)

        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("Клиент не отправил данных, разрываю соединение.")
                client.close()
                continue
            print(message)
            if message.strip() == "ping":
                send = "pong"
            else:
                send = "Wrong input string"
            client.send(send.encode('utf-8'))
            print(send)
        except socket.timeout:
            print("Таймаут: клиент слишком долго не отправляет данные.")
        except Exception as e:
            print(f"Ошибка при обработке клиента: {e}")
        finally:
            client.close()
except KeyboardInterrupt:
    print("Сервер остановлен вручную.")
finally:
    server.close()
    print("Сервер завершил работу.")
