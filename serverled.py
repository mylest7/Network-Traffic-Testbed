import os 
import RPi.GPIO as GPIO 
import time 
import socket 

time.sleep(2) 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(18, GPIO.OUT) 
GPIO.output(18, GPIO.HIGH)
time.sleep(15)             #This delay is so the Raspberry Pi's have enough time to establish an IP Address before running the server 

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(23, GPIO.OUT) 
GPIO.output(23, GPIO.HIGH)
time.sleep(2) 
serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

serv.bind(('localhost', 8080)) #localhost can be replaced by the IP address of the device running as the server 
serv.listen(5) 

while True: 
    conn, adds = serv.accept() 
    from_client='' 

    while True: 
	data = conn.recv(4096) 
	if not data: break 
	from_client += data 
	print from_client
	
	conn.send("I am SERVER\n") 
	GPIO.output(18, GPIO.LOW) 
	GPIO.output(23, GPIO.LOW) 
    conn.close() 

GPIO.cleanup() 