import socket
import os


def sendfile(tcp_socket,path):
    try:
        filename = os.path.basename(path)
        filesize = os.stat(path).st_size
        fileinfo = 'post|%s|%s'%(filename,filesize)
        tcp_socket.sendall(bytes(fileinfo,'utf8'))
        f = open(path,'rb')
        sentsize = 0
        while  sentsize != filesize:
            data = f.read(4096)
            tcp_socket.sendall(data)
            sentsize += len(data)
        f.close()
        print("file has been sent successfully")
        #接收识别返回结果
        #
        res=tcp_socket.recv(1024)
        return str(res,'utf8')
    except:
        print('send data failure')

def sendstring(tcp_socket,s):
    try: 
        tcp_socket.sendall(bytes(s,'utf8'))
        print('send string successfully')
        res=tcp_socket.recv(4096)
        return str(res,'utf8')
    except:
        print('send string failure')
