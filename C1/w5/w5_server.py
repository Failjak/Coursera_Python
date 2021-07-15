import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 10001))
sock.listen()



response = b'ok\npalm.cpu 10.5 200.01\neardrum.cpu 15.3 151.864259\npalm.cpu 45 123\npalm.data 123.2 12\n\n'
# response = b'ok\n\n'
while True:
    conn, addr = sock.accept()
    print("Соединение установлено: ", addr)
    with conn:
        data = conn.recv(1024)
        if not data:
            break
        request = data.decode("utf-8")
        print("Получ запрос: ", request)
        print("Отправ ответ:", response)
        conn.send(response)

sock.close()


# client = Client('127.0.0.1', 10001)
# client.put("palm.cpu", 0.5, timestamp=1150864247)
