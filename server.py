import asyncio

HOST = '127.0.0.1'
PORT = 8888

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Приём {message} от {addr}")

    print(f"Отправка: {message}")
    writer.write(data)
    await writer.drain()

    print("Остановка соединения")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_echo, HOST, PORT)

    addr = server.sockets[0].getsockname()
    print(f'Прослушивание порта {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())