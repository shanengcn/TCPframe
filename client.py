from tkinter import *
import socket 
import os
import sys
import struct
from senddata import sendfile
from senddata import sendstring


class Application(Frame):
    ip=''
    tcp_socket=''
    connstat=''
    wavpath=''
    videopath=''
    texts=''
    result=''

    def tcpconnect(self):
        ip_s=str(Application.ip.get())
        Application.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR=(ip_s,8000)
        try:
            Application.tcp_socket.connect(ADDR)
            print("server connected ")
            Application.connstat.set('connected')
        except:
            Application.connstat.set('connect failure')

    def sendaudio(self):
        wp=Application.wavpath.get()
        if os.path.exists(wp):
            res=sendfile(Application.tcp_socket,wp)
            Application.result.set(res)
        else:
            Application.result.set(wp+' not exist')
    def sendvideo(self):
        ap=Application.videopath.get()
        if os.path.exists(ap):
            res=sendfile(Application.tcp_socket,ap)
            Application.result.set(res)
        else:
            Application.result.set(ap+' not exist')
    def sendtext(self):
        s=Application.texts.get()
        if s:
            res=sendstring(Application.tcp_socket,s)
            Application.result.set(res)
        else:
            Application.result.set('string not exist')

    def createWidgets(self):
        #ip input
        Application.ip=StringVar(value='127.0.0.1')
        self.IP=Entry(self,textvariable=Application.ip)
        self.IP.grid(row=0,column=0,padx=10,pady=10)
        #tcp connect
        self.CONNECT = Button(self,text='connect',command=self.tcpconnect)
        self.CONNECT.grid(row=0,column=1,padx=10,pady=10)
        #is connect
        Application.connstat=StringVar(value='no connect')
        self.CONNECTED=Label(self,textvariable=Application.connstat)
        self.CONNECTED.grid(row=0,column=3,padx=10,pady=10)
        #wav path
        Application.wavpath=StringVar(value=R'D:\TCPframe\1.wav')
        self.WAVPATH=Entry(self,textvariable=Application.wavpath)
        self.WAVPATH.grid(row=1,column=0,padx=10,pady=10)

        self.AUDIORECORD=Button(self,text='audiorecord')
        self.AUDIORECORD.grid(row=1,column=1,padx=10,pady=10)

        self.AUDIORECORDSTOP=Button(self,text='stop&save')
        self.AUDIORECORDSTOP.grid(row=1,column=2,padx=10,pady=10)

        self.AUDIOSEND=Button(self,text='send',command=self.sendaudio)
        self.AUDIOSEND.grid(row=1,column=3,padx=10,pady=10)
        #video path
        Application.videopath=StringVar(value=R'D:\TCPframe\1.mp4')
        self.VIDEOPATH=Entry(self,textvariable=Application.videopath)
        self.VIDEOPATH.grid(row=2,column=0,padx=10,pady=10)

        self.VIDEORECORD=Button(self,text='videorecord')
        self.VIDEORECORD.grid(row=2,column=1,padx=10,pady=10)

        self.VIDEORECORDSTOP=Button(self,text='stop&save')
        self.VIDEORECORDSTOP.grid(row=2,column=2,padx=10,pady=10)

        self.VIDEOSEND=Button(self,text='send',command=self.sendvideo)
        self.VIDEOSEND.grid(row=2,column=3,padx=10,pady=10)
        #send text/string
        Application.texts=StringVar(value=R'string for send')
        self.TEXTS=Entry(self,textvariable=Application.texts)
        self.TEXTS.grid(row=3,column=0, padx=10,pady=10)

        self.TEXTSEND=Button(self,text='send',command=self.sendtext)
        self.TEXTSEND.grid(row=3,column=3,padx=10,pady=10)

        Application.result=StringVar(value='No Result')
        self.TEXTRECEIVE=Label(self,textvariable=Application.result)
        self.TEXTRECEIVE.grid(row=4,column=0,padx=10,pady=10)

        self.QUIT = Button(self,text='exit')
        self.QUIT.grid(row=4,column=3,padx=10,pady=10)
        self.QUIT["command"] =  self.quit


    def __init__(self, master=None):
        Frame.__init__(self, master,height=400,width=600)
        self.pack()
        self.createWidgets()

        
root = Tk()
root.title('tcp client')
root.geometry('640x320')
root.resizable(0,0)
app = Application(master=root)
app.mainloop()
root.destroy()