import asyncio

HOST = '127.0.0.1'
PORT = 8888

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(HOST, PORT)

    message = input("Введите сообщение для отправки серверу: ")
    print(f'Отправка данных серверу: {message}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()}')

    print('Closing the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello, World!'))