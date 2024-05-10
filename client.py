import asyncio

HOST = '127.0.0.1'
PORT = 8888

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(HOST, PORT)

    print(f'Отправка данных серверу: {message}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Получено: {data.decode()}')

    print('Остновка соединения')
    writer.close()
    await writer.wait_closed()

message = input("Введите сообщение для отправки серверу: ")
asyncio.run(tcp_echo_client(message))