import asyncio
import websockets
import logging
import time  
from time import sleep 
import datetime 

connected = True

logging.basicConfig(
    filename="data1.txt",
    filemode='w',
    format="%(message)s",
    level=logging.INFO,
)

async def client():
    async with websockets.connect("ws://localhost:8000") as websocket:
        # Create tasks to send and receive messages concurrently
        send_task = asyncio.create_task(send_messages(websocket))
        receive_task = asyncio.create_task(receive_messages(websocket))
        await asyncio.gather(send_task, receive_task)


async def send_messages(websocket):
    while True:
        await asyncio.sleep(1)


async def receive_messages(websocket):
    dic = {}
    numbering = 0
    blockno = 0
    while True:
        try:
            if numbering != 5 :
                ts = time.time()
                current_time = datetime.datetime.now()
                message = await websocket.recv()
                dic[ts] = f"{current_time} : {message}"
                numbering += 1
                
            if numbering == 5 :
                numbering = 0
                blockno += 1
                for j in dic :
                    t = j
                    break
                tt = ts - t
                logging.info(f'\n{tt} : Block {blockno} received\n')
                await websocket.send(f"Client Client-3 received block number {blockno} in time {tt}")
                for i in dic :
                    logging.info(f"{dic[i]}")
                dic.clear()
        except :
            connected = False  
            print( "connection lost... reconnecting" )  
            while not connected:  
                # attempt to reconnect, otherwise sleep for 2 seconds  
                try:  
                    async with websockets.connect("ws://localhost:8000") as websocket:
                        # Create tasks to send and receive messages concurrently
                        send_task = asyncio.create_task(send_messages(websocket))
                        receive_task = asyncio.create_task(receive_messages(websocket))
                        await asyncio.gather(send_task, receive_task)
                        print( "re-connection successful" ) 
                        connected = True
 
                except:  
                    sleep( 2 ) 
                    print("sleeping")

asyncio.run(client())