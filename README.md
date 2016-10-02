# Chat_Server-with-Multi_Peer-Group_Chat-
This is a Simple Chat Server, it could be used as a Group chat over Local Lan.
It uses concept of Socket Programming using Socket Python Library.
The Message is sent to Server and Server Broadcasts it to its connected clients over wlan using Port 2300 (You may change the Port).
The client is identified using its IP4 address.
Server system require Telnet or SSH(prefered)
Client automatically detects at which server is located, and its IP4 address
Note the IP address should be within Range xxx.xxx.xxx.2 - xxx.xxx.xxx.255
Run the Main.py to start the Program
Run the Server.py to Start the on a System.

Pre-Requirements:
   *Should have library "netifaces" (install using pip)
   Other librarire's (Come's pre-installed)
    - socket
    - sys
    - os
    - platform
    - select4

My_ip detects you System ip.
Connection.py detects where the server is located and creates a connection with the server
StartChat sends and receives the message.
