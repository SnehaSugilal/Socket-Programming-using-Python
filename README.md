# Socket-Programming using Python

Say you are given a task to implement the client-side of a network application designed according to the client-server application architecture. Note that the server is already implemented for you and running on a remote machine (hostname kopi.ece.neu.edu). Known that the server uses the port numbers in the range [5203, 5212]. 

The description of the application and its application layer protocol is provided below. 


## **Overview**

The application concerns the remote evaluation of simple arithmetical expressions using only one of the operators +, -, *, and / (no parenthesis or other operators). Examples: 3 + 5, 5 * 8, etc. After an initial greeting message used by your client to start the connection to the server, the server asks your client to evaluate a (server-chosen, unspecified) number of expressions one after the other. Each of these expressions will be sent as a separate message. For each expression message, the server expects a response message containing the result of the evaluation of the expression. If your program can correctly evaluate all the expressions, then the server will return a secret flag to the client. This flag is unique to each student and should be saved for submission (see Section Submission). The message containing the flag will signify the end of the communication session. At this point, the client can close the connection to the server, and the application terminates. 

**Behavior: Protocol Actions and Messages**

Upon starting, the client must set up a TCP connection with the server. Then, the client must send the introductory message to the server. The server will respond with an expression message. The client must evaluate the expression and send back a result message. If the result is incorrect, the server will send back a failure message and close the connection to the client (this means that your client is not correctly designed and you have to modify it and try again). Otherwise, the server will either send another expression message or, if enough expressions have been evaluated, a success message. The success carries the secret flag, which you should save and keep for submission.

## **UNDERSTANDING THE TASK:**

The task is to create the client-side of a network application that concerns remote evaluation of simple arithmetic expressions using only one of the operators +, -, *, and /.  The client is to connect to the sample server (sample_server.py) which gives our client math equations to solve. Before that, an introductory message is to be sent from our client to the sample server, to establish a connection between our client and the server. We use the IP address and the port number to specify this. We implement the TCP connection using the command **SOCK_STREAM and for IPv4 F_INET.**

Once the connection is established, the client is to send a message to the server saying "EECE7374 INTR 002475991". After establishing the connection, the server asks our client to evaluate a random chain of mathematical expressions. If these equations are correctly evaluated by our client, then the server will return a unique, secret flag to our client. The message containing this flag will signify the end of the communication session. 

### **EXPLANATION & THOUGHT BEHIND THE HIGH-LEVEL APPROACH:**

Since the whole idea is based on socket programming, we essentially need to import sockets. Then we define the server, by having a variable say "server_hostname", store the hostname. To completely specify the server, we define and store the port number in a variable, say "default_server_port". To create a socket on the client end, we use "client_socket" with 2 parameters, AF_INET and SOCK_STREAM. AF_INET defines the IPv4 addresses set, meanwhile, SOCK_STREAM establishes connection-oriented TCP protocol. Once we've got the server_hostname, we use the "connect" function with 2 parameters, the hostname & the server port number. This will establish a connection with the server which is mandatory for the client to carry the process further. Next, we define a variable to send the Introductory message with our NUID "EECE7374 INTR 002475991" (Sneha's NUID). Let's name this "message_from_client". (As the name suggests, it's the message from the client to the server.) 

To send this data from our client to the server, we use the "send" function. We also need to use the "encode" function which encodes the message to send it in byte format from the string. To store the info received from the server, let's create another variable & call it "message_to_client". But to receive the data from the server, we use the "recv" function with a parameter equal to the string size it can have. We define this number as the server's buffer size and set it to 4096 as defined in the sample_server.py. To use this received message from the server, AKA "message_to_client" in the future, we save it in a variable. Since it's in "response" to the client, let's define the variable "response" to store the server's data. '

Note that it's in string format as we utilize the "decode" function, with the parameter "UTF-8" in the decode function. To access and assess the contents of the response message, we make use of the "split" function. The received data is in the format of a string, when we call the "split" function, we convert the string into a list. Once the string is split, we can traverse through the contents of the response message as a list. To traverse, let's define a "while" loop that holds TRUE for it to split into a list.

With the condition that, the received message includes the "EECE7374 EXPR" equation, print the received message. Identify the operands and the operator in the message sent to the client from the server, and evaluate the result. Once evaluated based on the operand and its type of operation, let's print the result of the equation on screen. Since it's a random process, the server may send multiple such equations till the server is satisfied & later stops.

This is also the result the client will send back in response represented as "EECE7374 RSLT" for the result. But the other condition is if the element of the list's first index [1] is "FAIL" or "SUCC", print that response. However, this message will again need to be decoded by the server. We pass this "expected solution" variable in the "message_from_client" variable to be printed as "EECE7374 RSLT". As we did previously, to send this data from our client to the sample server, we use the "send" function. Similarly, to convert the data from string to byte, we use the encode function. After a couple of back-and-forth communication between our client & the server, eventually, the server sends the "SUCC" or "FAIL" message, which again we decode from byte to string. Both will break our "while" loop. The "FAIL" message is sent by the server to the client to say that the last expression was evaluated incorrectly. The "SUCC" message is sent by the server to the client to say that the math was evaluated correctly. Either of the messages breaks the loop and let's get the response printed.

On correct evaluation, the "SUCC" message from the server indicates that the application has been completed successfully. And then, corresponding to the NU ID, our client receives the desired unique, secret flag that we need! Further, we store the string in the "response" variable and print the desired results accordingly. To conclude, we then close the client-server connection by using the "close" function.


#### For me, the SECRET KEY RECEIVED is: EECE7374 SUCC 5b667ea08b8c19b0a68fb8e2cd6302535c186ea3c965c260bd1f213447b3dcee

The client is programmed as attached.
