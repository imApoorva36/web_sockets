import asyncio
import websockets
import logging
import time  
from time import sleep 
import datetime 

connected = True

logging.basicConfig(
    filename="data3.txt",
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
    await websocket.send("Connected with client-3")


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
                await websocket.send(f"Client Client-3 received block number {blockno} in time {tt} sec")
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