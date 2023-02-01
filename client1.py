import asyncio
import websockets
import logging
import time  
from time import sleep 
import datetime 

connected = True
#Changing the configuration of logging
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
    await websocket.send("Connected with client-1")
    

async def receive_messages(websocket):
    # Creating an empty dictionary to store the value of data of each block temporarily.
    dic = {}
    numbering = 0
    blockno = 0
    blocksize = 5 # Setting the block size as 5
    while True:
        # Using Error handling
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
                # Logging the messages to the text file
                logging.info(f'\n Block {blockno} received in time {tt} sec\n')
                await websocket.send(f"Client Client-1 received block number {blockno} in time {tt} sec")
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
                         
                except :  
                    sleep( 2 ) 
                    
asyncio.run(client())