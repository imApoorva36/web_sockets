import asyncio
import websockets
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
)

async def send_messages(websocket):
    while True:
        await websocket.send("Hey Server!")
        await asyncio.sleep(1)


async def receive_messages(websocket):
    numbering = 0
    logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
)
    while True:
        message = await websocket.recv()
        print(f"{numbering}.{logging} Received message: {message}")
        numbering += 1


async def client():
    async with websockets.connect("ws://localhost:8000") as websocket:
        # Create tasks to send and receive messages concurrently
        send_task = asyncio.create_task(send_messages(websocket))
        receive_task = asyncio.create_task(receive_messages(websocket))
        await asyncio.gather(send_task, receive_task)

asyncio.run(client())