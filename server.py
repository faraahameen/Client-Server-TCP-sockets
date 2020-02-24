import socket
from threading import Thread
from socketserver import ThreadingMixIn

ip = 'localhost'
port = 9005



class ClientGETResponse(Thread):

    def __init__(self, ip, port, sock, filename):
        self.ip = ip
        self.port = port
        self.sock = sock
        self.filename = filename
        Thread.__init__(self)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((ip, port))
threads = []


def run(self):
        try:
            files = open(self.filename, 'rb')
            while True:
                # read received file from the client.
                l = files.read()
                while (l):

                    self.sock.send(l)
                    l = files.read()
                if not l:
                    files.close()
                    self.sock.close()
                    break
        except IOError:
            print ('\n  HTTP/1.0 404 Not Found \r \n' )
            self.sock.close()


class ClientPOSTResponse(Thread):

    def __init__(self, ip, port, sock):
    
        self.ip = ip
        self.port = port
        self.sock = sock
        Thread.__init__(self)

    def run(self):
        with open('file_to_be_posted', 'wb') as files:
            print('File Opened ')
            while True:
                data = self.sock.recv(1024).decode()
                if not data:
                    files.close()
                    break
                # write data to a file
                print('Data :', (data))
                postdata=data.encode()
                files.write(postdata).decode()
        files.close()
        self.sock.close()


while True:
    print("\n  Listening to port ....")
    sock.listen(1)
    (conn, (ip, port)) = sock.accept()
    print('\n New Connection From ', (ip, port))
    # recieving the request from the client
    data = conn.recv(1024).decode()
    data = data.split()
    Request_handle = '\n  Request : '
    if len(data) == 4:
        requestType = data[0]
        filename = data[1]
        hostname = data[2]
        portno = data[3]
        print(Request_handle, requestType, filename, hostname, portno)

    elif len(data) == 3:
        requestType = data[0]
        filename = data[1]
        hostname = data[2]
        print(Request_handle, requestType, filename, hostname)
     
     
    if requestType == 'GET' or requestType == 'get':
        # opens a thread for the get method as It gets the file of this
        # filename.
        newthread = ClientGETResponse(ip, port, conn, filename)
        newthread.start()
        threads.append(newthread)
    elif requestType == 'POST' or requestType == 'post':
        # opens a thread for the post method as It receives the file
        # from the client.
        newthread = ClientPOSTResponse(ip, port, conn)
        newthread.start()
        threads.append(newthread)
for t in threads:
    t.join()

eval(input())
