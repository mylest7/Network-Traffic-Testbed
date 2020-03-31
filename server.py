serv = socket.socket(socket.AF_INET, sock.SOCK_STREAM) 

ip=raw_input() #The IP address of the device you are using that you want to act as a server
serv.bind((str(ip), 8080)) 
serv.listen(5) 

while True: 
    conn, addr = serv.accept() 
    from_client = '' 
    
    while True: 
        data = conn.recv(4096) 
        if not data: break 
        from_client += data 
        print from_client
        
        conn.send("I am SERVER\n") 
        
    conn.close() 