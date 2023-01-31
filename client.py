import asyncio
import websockets
import logging
import time
import socket  
from time import sleep 
import datetime 

connected = True

logging.basicConfig(
    filename="data.txt",
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
        await websocket.send("Hey Server!")
        await asyncio.sleep(1)


async def receive_messages(websocket):
    dic = {}
    numbering = 0
    blockno = 0
    '''logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    )'''
    while True:
        #clientSocket = socket.socket()  

        try:
            if numbering != 5 :
                ts = time.time()
                current_time = datetime.datetime.now()
                message = await websocket.recv()
                #print(f"{numbering}.{logging} Received message: {message}")
                #logging.info(f'{ts} : {message}')
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
                for i in dic :
                    logging.info(f"{dic[i]}")
                dic.clear()
        except :
            
            connected = False  
            websocket = websockets.connect("ws://localhost:8000")
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
        #clientSocket.close();  '''

    '''except websockets.exceptions.ConnectionClosedError :
        #connected = False
        print("Connection with server lost.. Reconnecting")
        await asyncio.sleep(10)
        client()
        while not connected:
            try :
                websockets.connect("ws://localhost:8000")
                connected = True
            except websockets.exceptions.ConnectionClosedError:
                await asyncio.sleep(10)'''
    
'''@retry(client().websocket.WebSocketConnectionClosedException, delay=2, logger=None)
def start_wss_client():

    wss_gateway_host = "ws://{0}:{1}".format(wss_gateway_host, wss_gateway_port)
    web_socket = client().websocket.WebSocketApp(wss_gateway_host,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
    web_socket.on_open = on_open
    web_socket.run_forever()

@asyncio.coroutine

def _start_loop(self, websocket, event_handler):
    while True:
        try:
            yield from asyncio.wait_for(
            self._wait_for_message(websocket, event_handler),
            timeout=self.options['timeout']
            )
        except asyncio.TimeoutError:
            yield from websocket.pong()
            log.debug("Sending heartbeat...")
            continue'''


asyncio.run(client())