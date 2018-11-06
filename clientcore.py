import socket
import os
def client():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ADDR=("127.0.0.1",8000)
    tcp_socket.connect(ADDR)
    print("server connected ")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    post='post|1.wav'
    while 1:
        flag,path=post.split('|')
        path = os.path.join(BASE_DIR,path)
        filename = os.path.basename(path)
        print('send',filename,'?(y)')
        if 'y'==input():
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
            print(res)
        else:
            break
    tcp_socket.close()

if __name__ == "__main__":
    client()