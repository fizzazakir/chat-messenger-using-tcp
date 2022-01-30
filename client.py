from time import sleep
import socket
from threading import *
import threading
import sys
import tkinter as tt

import re


def send_on_port(msg):
    client.send(msg.encode())


def DisplayMessage(msg):
    portlabel['text'] = ''
    portlabel.config(text=msg)


def print_message(msg):
    messagelist.insert(tt.END, str(msg))


def VerifyPort():
    cin = PortNumber.get(1.0, "end-1c")
    PortNumber.delete(1.0, tt.END)

    pin = int(IPNumber.get(1.0, "end-1c"))
    IPNumber.delete(1.0, tt.END)
    if pin in range(0, 65535):
        t1 = threading.Thread(target=connect, args=(cin, pin))
        t1.start()
    else:
        DisplayMessage("INVALID PORT NUMBER!!")

def connect(ip, port):
    global client
    client = socket.socket()
    client.connect((ip, port))

    threading.Thread(target=recv).start()

def recv():
    while True:
        msg = client.recv(1024).decode()
        print_message("Server :  "+msg)

def check(Ip):

    # pass the regular expression
    # and the string in search() method
    if (re.search(regex, Ip)):
        print("Valid Ip address")

    else:
        print("Invalid Ip address")
def sendMsg():
    cin = mInput.get(1.0, "end-1c")
    mInput.delete('1.0', tt.END)
    print_message("You:" + cin)
    send_on_port(cin)


# GUI
window = tt.Tk()
window.title("CHAT BOX-CLIENT")
window.geometry('400x400')
box = tt.Label(window, height=10, width=100, bg="#B0E0E6",
               fg="#EAECEE")
display1 = tt.Label(window, text="ENTER IP ADDRESS:")
display1.place(x=0, y=10)
PortNumber = tt.Text(window, height=1, width=30)
PortNumber.place(x=150, y=12)
display3 = tt.Label(window, text="ENTER PORT NUMBER:")
display3.place(x=0, y=35)
IPNumber = tt.Text(window, height=1, width=30)
IPNumber.place(x=150, y=40)
ListenButton = tt.Button(window, text="START LISTENING", command=VerifyPort)
ListenButton.place(x=150, y=65)
portlabel = tt.Label(window, text="")
portlabel.place(x=150, y=70)
display2 = tt.Label(window, text="CLIENT SERVER CONVERSATION:")
display2.place(x=0, y=90)
scrollbar = tt.Scrollbar(window)
scrollbar.pack(side=tt.RIGHT, fill=tt.Y)
messagelist = tt.Listbox(window, yscrollcommand=scrollbar.set, width=60, height=10)
messagelist.place(x=6, y=110)
scrollbar.config(command=messagelist.yview)
mInput = tt.Text(window, height=3, width=35)
mInput.place(x=10, y=310)
MessageButton = tt.Button(window, text="Send", command=sendMsg, width=10)
MessageButton.place(x=300, y=330)
window.mainloop()