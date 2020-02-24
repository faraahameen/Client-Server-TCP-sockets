
import sys
import socket

ip = 'localhost'
port = 9005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

flag = True
print ('GET file-name host-name (port-number)')
print ('POST file-name host-name (port-number)')
while flag == True:
    request = input('Please enter your request :  ')
    array_data = request.split()
    clientrequest = array_data[0]
    
    if clientrequest == 'GET' or clientrequest == 'get':
        sock.send(request.encode())
        with open('requested_file', 'wb') as files:
            print ('\n  File Opened')
            print('HTTP/1.0 200 OK \r \n')
           
            while True:
                data = sock.recv(1024).decode()
                if not data:
                    files.close()
                    break
                # write data to a file
                print ('\n  Data :', (data) )
                getdata=data.encode()
                files.write(getdata).decode()
        files.close()     
           
        flag = False
    elif clientrequest == 'POST' or clientrequest == 'post':
        sock.send(request.encode())
        filename = array_data[1]
        files = open(filename,'rb')
        while True:
            l = files.read(1024)
            while (l):
                sock.send(l)
                l = files.read(1024)
            if not l:
                files.close()
                sock.close()
                break
        files.close()    
        print('\n File successfuly posted!.\n')
        
    

   
sock.close()
print ('  Connection terminated')
eval(input())