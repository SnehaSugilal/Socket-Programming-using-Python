##################                        EECE 7374: Fundamentals of Networks
##################                 Programming Assignment: Socket Programming with Python
##################                                                                           Sneha Sugilal

##################    Academic Integrity - I have read   and understood the course academic integrity policy.

##################    My secret flag is 5b667ea08b8c19b0a68fb8e2cd6302535c186ea3c965c260bd1f213447b3dcee

########################################################################################################################

##################                        UNDERSTANDING THE TASK                                      ##################

####  The task is to create the client-side of a network application that concerns remote evaluation
####  of simple arithmetic expressions using only one of the operators +, -, * and /.
####  The client is to connect to the sample server (sample_server.py) which gives our client math equations to solve.

####  Before that, an introductory message is to be sent from our client to the sample server, in order to
####  establish connection between our client and the server. We use the IP address and the port number to specify this.
####  We implement the TCP connection using the command SOCK_STREAM and for IPv4 F_INET.

####  Once the connection is established, the client is to send a message to the server saying "EECE7374 INTR 002475991"
####  After establishing connection, the server asks our client to evaluate a random chain of mathematical expressions.

####  If these equations are correctly evaluated by our client, then the server will return a unique, secret flag to
####  our client. The message containing this flag will signify the end of the communication session.

########################################################################################################################

##################           EXPLANATION & THOUGHT BEHIND THE HIGH LEVEL APPROACH                     ##################

#### Since the whole idea is based on socket programming, we essentially need to import sockets.
#### Then we define the server, by having a variable say "server_hostname", store the hostname.
#### To completely specify the server, we define and store the port number in a variable, say "default_server_port".
#### To create a socket on the client end, we use "client_socket" with 2 parameters, AF_INET and SOCK_STREAM.
#### AF_INET defines the IPv4 addresses set, meanwhile SOCK_STREAM is to establish connection-oriented TCP protocol.
#### Once we've the server_hostname, we use "connect" function with 2 parameters, the hostname & the server port number.
#### This will establish connection with the server which is mandatory for the client to carry the process further.
#### Next, we define a variable to send the Introductory message with our NUID "EECE7374 INTR 002475991" (Sneha's NUID)
#### Let's name this as "message_from_client". (As the name suggests, it's the message from the client to the server.)
#### In order to send this data from our client to the server, we use the "send" function.
#### We also need to use the "encode" function which encodes the message to send it in byte format from string.
#### In order to store the info received from the server, let's create another variable & call it as "message_to_client".
#### But to receive the data from the server, we use the "recv" function with parameter equal to string size it can have.
#### We define this number as the server's buffer size, and set it to 4096 as defined in the sample_server.py.
#### To use this received message from server, AKA "message_to_client" in the future, we save it in a variable.
#### Since it's in "response" to the client, let's define the variable "response" to store the server's data.
#### Note that it's in string format as we utilize the "decode" function, with parameter "UTF-8" in decode function.
#### In order to access and assess the contents of the response message, we make use of the "split" function.
#### The received data is in the format of a string, when we call the "split" function, we convert the string into a list.
#### Once the string is split, we can traverse through the contents of the response message as a list.
#### To traverse, let's define a "while" loop that holds TRUE for it to split into a list.
#### With the condition that, the received message includes "EECE7374 EXPR" equation, print the received message.
#### Identify the operands and the operator in the message sent to the client from the server, and evaluate the result.
#### Once evaluated based on the operand and its type of operation, let's print the result of the equation on screen.
#### Since it's a random process, the server may send multiple such equations till the server is satisfied & later stop.
#### This is also the result the client will send back in response represented as "EECE7374 RSLT" for the result.
#### But the other condition being, if the element of the list's first index [1] is "FAIL" or "SUCC", print that response.
#### However, this message will again need to be decoded by the server.
#### We pass this "expected solution" variable in the "message_from_client" variable to be printed as "EECE7374 RSLT".
#### Like we did previously, to send this data from our client to the sample server, we use "send" function
#### Similarly, in order to convert the data from string to byte, we use encode function.
#### After a couple of back and forth communication between our client & the server, eventually, the server sends the
#### "SUCC" or "FAIL" message, which again we decode from byte to string. Both will break our "while" loop.
#### The "FAIL" message is sent by the server to the client to say that the last expression was evaluated incorrectly.
#### The "SUCC" message is sent by the server to the client to say that the math was evaluated correctly.
#### Either of the messages breaks the loop and let's get the response printed.
#### On correct evaluation, the "SUCC" message from server indicates that the application has completed successfully.
#### And then, corresponding to the NU ID, our client receives the desired unique, secret flag that we need!
#### Further, we store the string in the "response" variable and print the desired results accordingly.
#### To conclude, we then close the client-server connection by using the "close" function.


#### For me, the SECRET KEY RECEIVED is : EECE7374 SUCC 5b667ea08b8c19b0a68fb8e2cd6302535c186ea3c965c260bd1f213447b3dcee

#### The client is programmed as shown below.

########################################################################################################################

### First things first, we import the "socket" library.
import socket                                                 ###  We do this to get the functions for creating and managing network sockets.

### Let's start by defining the server hostname (with IP address and Port number)
server_hostname = '10.110.102.231'                            ### Here, I'm using the localhost IPv4 Address of my laptop (connected to NUwave at NEU Curry Center) obtained from ipconfig command on cmd.
default_server_port = 5211                                    ### Assigning Default port to communicate with port number of the server to establish connection.

### Let's now create a socket for our client side
client_Socket = socket.socket(socket.AF_INET,                  ### Here, we use "AF_INET" to connect with the IPv4 address.
                              socket.SOCK_STREAM)              ### And we use SOCK_STREAM to make the TCP connection.

### Next we got to connect to the server, that we defined above
client_Socket.connect((server_hostname, default_server_port))  ### By defining the host name & specified port number, we intend to establish the TCP connection with the server.

### The Introductry Message
message_from_client = "EECE7374 INTR 002475991"                ### This is the very 1st ping from our client to the sample server. "002475991" is my NUID, Sneha Sugilal's.
                                                               ###  We define and store it in a variable, so that we can send it to the server in the introduction.

### To send the above message, we encode the data into bytes
client_Socket.send(message_from_client.encode())               ### This will send the message to the server (specified by the IP address & proper port number).

### Once our client sends the opening message, the server will respond with an expression message.
### Our client-side socket receives this data from the server and stores it into a variable.

message_to_client = client_Socket.recv(4096)                   ### We define the string received to be a maximum of 4096 chars, as the sample server has its buffersize defined to be 4096.
response = message_to_client.decode("utf-8")                   ### We save this data from the server into a variable, say "response"
                                                               ### UTF-8 is a standard method of Unicode strings that represent characters, used by default.

### Now, to evaluate this mathematical expression received in response by the client from the server.
### Let's define a "while" loop:

while True:
    contents_of_response = response.split()                                               ### We use the "split" function to traverse throught the contents of the string and save into a list.
    if contents_of_response[0] == "EECE7374" and contents_of_response[1] == "EXPR":       ### Here, we need to check if the [0] & [1] indexed part are "EECE7374" & "EXPR" respectively (because that's how the format is defined).
        print(response)                                                                   ### Let's print the expression so that we can see what expressions the server wants the client to evaluate.
        a = int(contents_of_response[2])                                                  ### The [2] indexed item in the list, if is an integer, let's save that in the variable "a", as the 1st operator.
        operand = contents_of_response[3]                                                 ### The [3] indexed item will be an operand, we store this into the "operand" variable.
        b = int(contents_of_response[4])                                                  ### Similar to line #115, the [4] indexed item will be stored in variable "b", as the 2nd operator.
        if operand == '+':                                                                ### Let's define the case for each of the 4 basic operands
            expected_solution = a + b                                                     ### For Addition of "a" & "b"
        elif operand == '-':
            expected_solution = a - b                                                     ### For Subtraction of "a" & "b"
        elif operand == '*':
            expected_solution = a * b                                                     ### For Multiplication of "a" & "b"
        elif operand == '/':
            expected_solution = a / b                                                     ### For Division of "a" & "b"

        message_from_client = "EECE7374 RSLT " + str(expected_solution)                   ### After evaluating, let's set the message that's to be sent in the required format.

        print(message_from_client)                                                        ### Also, printing the same here.
        client_Socket.send(message_from_client.encode())                                  ### We need to send this message back to the server.

        message_to_client = client_Socket.recv(4096)                                      ### Further, we receive data from the server. We define the buffer value as 4096, for the reason mentioned above.
        response = message_to_client.decode("utf-8")                                      ### Like we did previously, we store and decode this response to get the string.


    elif contents_of_response[0] == "EECE7374" and contents_of_response[1] == "SUCC":     ### To identify the SUCCESS message, with [0] & [1] indexed as "EECE7374" & "SUCC", and come out of the loop.
        print(response)                                                                   ### Yay, let's get the SECRET KEY printed!
        break                                                                             ### Once we do, we break out of the loop.

### After the communication, we need to close the client-server socket connection.
client_Socket.close()                                                                     ### This function closes the Socket. And hence, terminates the connection between our client and the sample server.
