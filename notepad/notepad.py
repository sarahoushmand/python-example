from tkinter import *
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import filedialog
import Io


def openCommand():
    global txt
    txt.delete('1.0', 'end-1c')
    file = filedialog.askopenfile(filetypes=[('Text Document', '*.txt')])
    data = Io.Open(file)
    txt.insert(INSERT, data)


def SaveCommand():
    global txt
    data=txt.get('1.0', 'end-1c')
    file = filedialog.asksaveasfile(filetypes=[('Text Document', '*.txt')] ,mode='w', defaultextension=".txt")
    print(file)
    Io.Save(file, data)
    txt.delete('1.0', 'end-1c')


def exitCommand():
    global window
    window.destroy()


window = Tk()
window.title("My NotePad")
window.geometry('450x320')

txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.place(x=50, y=20)


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Open', command=openCommand)
new_item.add_command(label='Save', command=SaveCommand)
new_item.add_command(label='Exit', command=exitCommand)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)


OpenBtn = Button(window, text="Open File", command=openCommand)
OpenBtn.place(x=70, y=220, width=150, height=35)

SaveBtn = Button(window, text="Save File", command=SaveCommand)
SaveBtn.place(x=220, y=220, width=150, height=35)

window.mainloop()
