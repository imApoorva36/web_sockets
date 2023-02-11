# Team Embedus(by Apoorva Agrawal and Sanjeev Holla S)
## ***Websockets implementation***

<br>
<br>

### **Skills we gained by doing this Project:** *(Its a better way of writing 'Prerequisites', as 'Learn while doing a Project' is better than 'Learn and then do a Project')*

<br>

 1. We were introduced to the world of websockets and could apply the concepts of websockets that we researched during the course of making this project
 2. We learned about various modules like asyncio, websockets, faker, logging etc that exist in python and about how vast the scope of python application in real life     is
 3. Increased our knowledge of how connections between client and server in real life would be happening
 
<br>

### ***A detailed report of the task*** :

<br>

 1. In this project we have created a server and number of clients in which two-way interactive communication between client and the server is enabled
 2. The connection between server and client is enabled by using ***websockets*** and ***async*** libraries.
 3. Once the client is connected to the server, we get random data like name, link, country etc. (in the server) using ***faker*** library and then the server sends       that data to the client.
 4. The client would receive the messages sent by the server and it will select the type of data it wants and timestamps only the selected type of messages.
 5. Then the client will wait till a particular block of data (block sizes for different clients are different) is received and then caculate the time taken to receive     that block of data and then it would Log that block into a text file using ***logging*** module of  python.
 6. Then the client would send a response back to the server ***'client <client_name> received <n> block in <t> time’***, where n has to be the sequence number of the     block that the client received and time t taken for the client to receive the entire message block. Also, the client prints that block with sequence number n is       succcessfully received.
 7. The server would receive and print all of the messages received by the various clients.
 8. The client is also having the feature of ***re-establishing the connection with the sever if server restarts for some reason*** (Here we have used error handling       via try except block)
 9. The server also has a feature of handling multiple concurrent connections such as in our code, the server is handling 8 such clients concurrently as shown in the       screenshots of the outputs and it can send and receive data efficiently to and fro all blocks with any discontinuity in data transfer with any of the clients.
 10. Also, we can see that in all our clients, the block size varies for the clients, i.e. the block size is assigned differently for different clients. Hence, we can     see that different block sizes require different time for logging, as reflected in the data files
 11. The client has the feature for selecting between different kind of data received from the server.
 
 <br>
 
 ### ***Instructions on how to run the files :***
 <br>
 To run the files of this repository, you have to first fork this repository into your git hub and then by using git clone command in your terminal window. Then first start the server by typing "python3 server.py". Then run the client code by typing out "python3 client1.py" in your terminal window and You can see the interactions happening between the server and the client.
 
 <br>
 
 ### ***Steps taken in finishing the task :***
 <br>
   Both of us collaborated via this github repository for sharing and working on the code. Sometimes we sat together and made algorithms such as that when we had to   log   data in blocks and not log individual messages and whenever we encountered a bug, we would think over how to resolve it. For all references and help, google remained   our saviour as it guided us to various documentations for various modules and showed us how we can apply and use them as per our requirrements. Finally, we compiled   all our code, produced the required output, and henceforth commited all changes to this repository.
 <br>
 
 ### ***A brief description of the modules used and why they were chosen :***
 
   In our code for server and client, we have used the asyncio, websockets, logging, time, datetime and faker modules. 
 
  While ***Asyncio and websocket*** modules were crucial to be able to establish connection and successfully run the connection between server and client, the other modules were applicable to serve various purposes. 
 
 The ***logging*** module allowed us to store the required data and consequenctly log that data in different block size of each client into it's respective data file.
 
 The  ***time*** module allowed for creating ***timestamps*** for blocks and for each individual message and through timestamps we were able to calculate the time taken by the client to receive each block.
    
The ***datetime*** module was just used to get the current date and time at which each message was received by the client from the server.
    
   The ***faker*** module was used for generating various random data such as name, country, city etc. which was sent from server to client and which was also logged in blocks in the respective client's data file.
    
 
 # ***Outputs and Screenshots of outputs of program execution :***
 
 <br>
 
1. This is the output of a simple connection of the server connected to just 1 client
 
    Output of Server
 ![p1c1](https://user-images.githubusercontent.com/90238207/216105354-7f5d1f7d-9b82-47d6-b2b2-bc7bd71cc860.png)
 
    Output of Client
 ![p2c1](https://user-images.githubusercontent.com/90238207/216105699-988a2036-c571-4351-9cac-e980c8a69f28.png)

2. Showing output that the server is able to manage multiple connections from the clients
 
 ![p3](https://user-images.githubusercontent.com/90238207/216108410-70215148-ddfb-44ba-b6ef-0ea8944ade3f.png)

3. Showing that server can successfully connect to all clients at the same time on restarting
 
 ![p4](https://user-images.githubusercontent.com/90238207/216108735-67e2e0d3-07b7-4681-9cbf-5a13963ecba5.png)

 4. Showing the output of any one client that it could successfully reestablish connection with the server when it was restarted
 
 ![p5](https://user-images.githubusercontent.com/90238207/216109028-7a39dbed-a5df-4dd6-b3c8-d8da467d9afb.png)

 5. Showing any one data file that the data could be successfully logged in the data file even after connection between server and client got re-established
 
 ![p6](https://user-images.githubusercontent.com/90238207/216109451-6b526764-88fe-4817-9b36-f63732063d61.png)
<br>
<br>
# ***Hardware Subtasks***
<br>
<br>
 
<br>
 
### ***Our breadboard circuit connections and implementation are as explained below and are as shown in the below picture:***
 
<br>

![Breadboard_Implementation](https://user-images.githubusercontent.com/90238207/217834680-cf0942ce-2329-49b0-971a-65942e2b464d.jpg)
 
 We have completed and executed ***milestones 1,2 and 3*** via our codes and the link to the functioning of them are as present in the drive link: https://drive.google.com/drive/folders/1-y2lRHNFNLPVLdF2iYOojacUmZ1ZpRQk
 
 All of our codes executed successfully with the output coming similar to the below one for all our codes: 
 ![image](https://user-images.githubusercontent.com/90238207/217836677-d03d8467-3272-4296-85ad-a61466780724.png)
 
 <br>
 
 ### ***Codes Explanation:***
 
 <br>
 
 In our code, the main idea was that firstly we will be using three variables, latchpin, datapin and clockpin to make connections from the nodemcuv1.0 to the 74HC595 register which is such that latchpin connects to RCLK, clockpin to SRCLK and datapin to SER of the register. Further,  We notice that to connect each row of a 4x4 led matrix with all the LED's anodes in the same line will make it difficult for us to control individual LEDs, so we connect the two rear ends and the two middle LEDs of each row to one particular row, where their anodes are connected to that row. So therefore now that we have given input and are able to access that particular row and we know which input will control which row and which LEDs, then we can now begin with using the shift function and we now use binary numbers to refer to which wire input signals we want as 1, i.e. high voltage and which as 0 , i.e. low voltage. Now, we will be using say B00000100 to refer to the third output pin in our register, i.e. QC of our register. Further, we have also added delay function, which helps us with the time delay/ time gap that the code/micro-controller has to follow. Further, we added an ESP.reset function in one of our milestones, just so that the next time the loop is excuted, the transition is smooth and the contents of the register can get refreshed without causing much problem to our order of blinking. 

 
 <br>
  
 ## ***Final Hackathon***
 
 <br>
 
 In the further sentences, we would be discussing on how we accomplished milestones 1, 2 and 3. 
 
### ***A detailed report of milestone 1*** :
 
 During this milestone, we were successfully able to get the sensor data of the MPU6050 on connecting it to the nodemcu,we received the data such as acceleration in x,y,z and angles along x,y,z and so on and we were able to display the data in the serial monitor . The video link of the code execution is in the milestone1 video file and the code is in the final_milestone_1&3 file.
 
### ***A detailed report of milestone 2*** :
 
 In this milestone, we were successfully able to establish WiFi communication between the nodemcu and the PC , and we were testing the connection by sending messages through the connection as shown in the video titled milestone 2 video and the relevant code is present in the final_milestone_2 code file. 
 
### ***A detailed report of milestone 3*** :
This milestone was similar to milestone 1, but we needed to make the data accurate, therefore we calibrated and tested the data by changing the orientation of the MPU6050(which was on the breadboard) and we therefore noticed that the data also accurately got changed. Also, the data remained fairly constant on no movement of the MPU6050, hence the conculusion of accuracy can be justified. 
 
### ***A detailed report on Milestone 4*** :

During this milestone, we know that we needed to get the data from the MPU and we had to interact with the game, we accordingly created the nodemcu as an access point so that it could create its own wifi. (This part of the code is titled as Final_WiFi_Access_Point) Also, we were able to connect other devices to this WiFi which proved that the WiFi was working properly.  But we were not able to integrate our code with the game. 
 
 



