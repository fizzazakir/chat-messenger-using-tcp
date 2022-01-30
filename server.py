from time import sleep
import socket as s
from threading import *
import threading
import sys
import tkinter as tt


def send_on_port(msg):
    client.send(msg.encode())


def DisplayMessage(msg):
    portlabel['text'] = ''
    portlabel.config(text=msg)


def print_message(msg):
    messagelist.insert(tt.END, str(msg))


def VerifyPort():
    cin = int(PortNumber.get(1.0, "end-1c"))
    PortNumber.delete(1.0, tt.END)
    if cin in range(1, 65535):
        DisplayMessage("Listening on port " + str(cin) + "!!")
        t1 = threading.Thread(target=listen, args=(cin,))
        t1.start()
    else:
        print("WRONG IP ADDRESS ");


def listen(port):
    global client, addr

    socket = s.socket()
    socket.bind(("127.0.0.1", port))
    socket.listen(5)

    while True:
        client, addr = socket.accept()
        print_message("CONNECTED WITH CLIENT")

        threading.Thread(target=recv).start()


def recv():
    while True:
        msg = client.recv(1024).decode()
        print_message("Client :  " + msg)


def sendMsg():
    cin = mInput.get(1.0, "end-1c")
    mInput.delete('1.0', tt.END)
    print_message("You:" + cin)
    send_on_port(cin)


# GUI
window = tt.Tk()
window.title("CHAT BOX-SERVER")
window.geometry('400x400')
box = tt.Label(window, height=10, width=100, bg="#B0E0E6", fg="#EAECEE")
display1 = tt.Label(window, text="ENTER PORT NUMBER:")
display1.place(x=0, y=10)
PortNumber = tt.Text(window, height=1, width=30)
PortNumber.place(x=150, y=11)
ListenButton = tt.Button(window, text="START LISTENING", command=VerifyPort)
ListenButton.place(x=190, y=40)
portlabel = tt.Label(window, text="")
portlabel.place(x=150, y=70)
display2 = tt.Label(window, text="CLIENT SERVER CONVERSATION:")
display2.place(x=0, y=80)
scrollbar = tt.Scrollbar(window)
scrollbar.pack(side=tt.RIGHT, fill=tt.Y)
messagelist = tt.Listbox(window, yscrollcommand=scrollbar.set, width=60, height=10)
messagelist.place(x=6, y=100)
scrollbar.config(command=messagelist.yview)
mInput = tt.Text(window, height=3, width=35)
mInput.place(x=10, y=300)
MessageButton = tt.Button(window, text="Send", command=sendMsg, width=10)
MessageButton.place(x=300, y=320)

window.mainloop()
