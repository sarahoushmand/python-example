from tkinter import *
import socket
window = Tk()
txt1 = Text(window)
txt1.pack()
from_client = ''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9090))
server.listen()
while True:
    conn, addr = server.accept()
    data = str(conn.recv(4096), 'utf8')
    if data:
        txt1.insert(INSERT, data)
    # conn.close()
    window.mainloop()


