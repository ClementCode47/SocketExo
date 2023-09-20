# echo-server.py
#import socket

#if __name__ == '__main__':
 #   HOST = "10.4.1.128"  # Standard loopback interface address (localhost)
  #  PORT = 56  # Port to listen on (non-privileged ports are > 1023)
#
 #   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  #      s.bind((HOST, PORT))
   #     s.listen()
    #    conn, addr = s.accept()
     #   with conn:
      #      print(f"Connected by {addr}")
       #     while True:
        #        data = conn.recv(1024)
         #       if not data:
          #          break
           #     conn.sendall(data)

# client.py

# importing socket module
import socket

# creating socket instance
client_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# target ip address and port
ip_address = '10.4.1.128'
port = 56

# instance requesting for connection to the specified address and port
client_object.connect((ip_address, port))

# receiving response from server
data_receive = client_object.recv(1024)

# if response is not null
if data_receive:
    # Connection is successful
    print("CLIENT CONNECTED TO SERVER")
    print(data_receive.decode('utf-8'))

    while data_receive:
        # user input
        client_input = input().encode('utf-8')

        # sending request to the server
        client_object.send(client_input)

        # receiving response from the server
        data_receive = client_object.recv(1024)
        if data_receive:
            print("{}: {}".format("SERVER", data_receive.decode('utf-8')))