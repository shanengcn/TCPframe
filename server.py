import socket
import os
def server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ADDR=("127.0.0.1",8000)
    tcp_socket.bind(ADDR)
    tcp_socket.listen(128)
    print("waiting...")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    while 1:
        conn,addr = tcp_socket.accept()
        print ("client connetcted —> ",addr)
        while 1:
            try:
                fileinfo=conn.recv(4096)
                s=str(fileinfo,'utf8')
                if s[0:4]=='post':
                    flag,filename,filesize=str(fileinfo,'utf8').split('|')
                    path = os.path.join(BASE_DIR,'server_receive',filename)
                    filesize=int(filesize)
                    f=open(path,'wb')
                    sentsize=0
                    while sentsize!=filesize:
                        data=conn.recv(4096)
                        f.write(data)
                        sentsize+=len(data)
                    print('file received: ',filename)
                    #此处加入对语音识别/关键词识别
                    #
                    #得到识别结果传给res
                    res='server get!'
                    conn.sendall(bytes(res,'utf8'))
                else:
                    print('string received: ',s)
                    #此处加入对data的处理
                    #
                    #得到识别结果
                    res='string get!'
                    conn.sendall(bytes(res,'utf8'))
            except:
                break
        break
    tcp_socket.close()

if __name__ == "__main__":
    server()