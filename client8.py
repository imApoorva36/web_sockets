import asyncio
import websockets
import logging
import time  
from time import sleep 
import datetime 

connected = True

logging.basicConfig(
    filename="data8.txt",
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
    await websocket.send("Connected with client-8")


async def receive_messages(websocket):
    dic = {}
    numbering = 0
    blockno = 0
    blocksize = 3
    while True:
        try:
            if numbering != blocksize :
                ts = time.time()
                current_time = datetime.datetime.now()
                message1 = await websocket.recv()
                message2 = await websocket.recv()
                message3 = await websocket.recv()
                message4 = await websocket.recv()
                message5 = await websocket.recv()
                message6 = await websocket.recv()
                message7 = await websocket.recv()
                message = await websocket.recv()
                dic[ts] = f"{current_time} : {message}"
                numbering += 1
                
            if numbering == blocksize :
                numbering = 0
                blockno += 1
                for j in dic :
                    t = j
                    break
                tt = ts - t
                logging.info(f'\nBlock {blockno} received in time {tt} sec\n')
                print(f"Block {blockno} received from server successfully")
                await websocket.send(f"Client Client-8 received block number {blockno} in time {tt} sec")
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
                        print( "re-connection successful" )
                        connected = True
                        send_task = asyncio.create_task(send_messages(websocket))
                        receive_task = asyncio.create_task(receive_messages(websocket))
                        await asyncio.gather(send_task, receive_task)
                         
                except:  
                    sleep( 2 ) 
                    
asyncio.run(client())