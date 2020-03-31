client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

ip = raw_input(“Server IP Address: “)

client.connect((str(ip), 8080))
client.send(“I am CLIENT\n”) 

from_server  = client.recv(4096) 

client.close() 
print from_server 
