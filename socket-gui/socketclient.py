from tkinter import *
import socket


window = Tk()
window.geometry('1000x800')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9090))


def send():
    client.send(bytes('client:'+en.get(), 'utf8'))
    txt.insert(INSERT, 'client:' + en.get() + '\n')
    # client.close()


Btn = Button(window, text="send", command=send)
Btn.place(x=300, y=550, width=150, height=35)

en = Entry(window, width=10)
en.place(x=450, y=550, width=150, height=35)


txt = Text(window)

txt.grid(column=0, row=0)

window.mainloop()

