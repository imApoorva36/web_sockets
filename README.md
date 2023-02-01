# Team Embedus(by Apoorva Agrawal and Sanjeev Holla S)


'Using web sockets to make communication between client and server'


 ##***A detailed report of the task*** :
 1. In this project we have created a server and number of clients in which two-way interactive communication between         client and the server is enabled
 
 
 
 Instructions on how to run the files :
 
 
 
 Steps taken in finishing the task :
 
   Both of us collaborated via this github repository for sharing and working on the code. Sometimes we sat together and made algorithms such as that when we had to   log   data in blocks and not log individual messages and whenever we encountered a bug, we would think over how to resolve it. For all references and help, google remained   our saviour as it guided us to various documentations for various modules and showed us how we can apply and use them as per our requirrements. Finally, we compiled   all our code, produced the required output, and henceforth commited all changes to this repository.
 
 
 A brief description of the modules used and why they were chosen :
 
   In our code for server and client, we have used the asyncio, websockets, logging, time, datetime and faker modules. While Asyncio and websocket modules were crucial to be able to establish connection and successfully run the connection between server and client, the other modules were applicable to serve various purposes. The logging module allowed us to store the required data and consequenctly log that data in different block size of each client into it's respective data file. The  time module allowed for creating timestamps for blocks and for each individual message and through timestamps we were able to calculate the time taken by the client to receive each block.
    
The datetime module was just used to get the current date and time at which each message was received by the client from the server.
    
    
   The faker module was used for generating various random data such as name, country, city etc. which was sent from server to client and which was also logged in blocks in the respective client's data file.
    
 
 Screenshots of outputs of program execution :




