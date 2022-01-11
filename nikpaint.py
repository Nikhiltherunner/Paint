from tkinter import *

def paint(event):
    canva.create_rectangle(event.x+50,event.y+50,event.x,event.y,outline='red')


root = Tk()
root.geometry("500x300")
root.title("Paint Application Developed By Nettechians ")

canva = Canvas(root,bg="light yellow")
canva.pack()

canva.bind("<Motion>",paint)


root.mainloop()
