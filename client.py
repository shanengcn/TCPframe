from tkinter import *
import socket 
import os
import sys
import struct

class Application(Frame):

    def createWidgets(self):
        ip='218.192.170.69'
        textreceive='no connect'
        wavpath=R'D:\TCPtrans\1.wav'
        videopath=R'D:\TCPtrans\1.mp4'
        texts=R'abc'
        textreceive=R'abcd'

        self.IP=Entry(self,textvariable=ip)
        self.IP.insert(0,ip)
        self.IP.grid(row=0,column=0,padx=10,pady=10)

        self.CONNECT = Button(self,text='connect')
        self.CONNECT.grid(row=0,column=1,padx=10,pady=10)

        self.CONNECTED=Label(self,text='no connect')
        self.CONNECTED.grid(row=0,column=3,padx=10,pady=10)

        self.WAVPATH=Entry(self,textvariable=wavpath)
        self.WAVPATH.grid(row=1,column=0,padx=10,pady=10)

        self.AUDIORECORD=Button(self,text='audiorecord')
        self.AUDIORECORD.grid(row=1,column=1,padx=10,pady=10)

        self.AUDIORECORDSTOP=Button(self,text='stop&save')
        self.AUDIORECORDSTOP.grid(row=1,column=2,padx=10,pady=10)

        self.AUDIOSEND=Button(self,text='send')
        self.AUDIOSEND.grid(row=1,column=3,padx=10,pady=10)

        self.VIDEOPATH=Entry(self,textvariable=videopath)
        self.VIDEOPATH.grid(row=2,column=0,padx=10,pady=10)

        self.VIDEORECORD=Button(self,text='videorecord')
        self.VIDEORECORD.grid(row=2,column=1,padx=10,pady=10)

        self.VIDEORECORDSTOP=Button(self,text='stop&save')
        self.VIDEORECORDSTOP.grid(row=2,column=2,padx=10,pady=10)

        self.VIDEOSEND=Button(self,text='send')
        self.VIDEOSEND.grid(row=2,column=3,padx=10,pady=10)

        self.TEXTS=Entry(self,textvariable=texts)
        self.TEXTS.grid(row=3,column=0, padx=10,pady=10)


        self.TEXTSEND=Button(self,text='send')
        self.TEXTSEND.grid(row=3,column=3,padx=10,pady=10)


        self.TEXTRECEIVE=Label(self)
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
root.resizable(0,0)
app = Application(master=root)
app.mainloop()
root.destroy()