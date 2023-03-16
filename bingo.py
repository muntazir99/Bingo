import random
from tkinter import *
x=0
root = Tk()
root.configure(background="green")
root.title("Bingo!!!")
root.geometry("270x150")
data = list(range(1, 26))
random.shuffle(data)
print(data)

#function for color changing
def cc():
    redbutton.configure(bg="green", fg="red")


for i in range(1,6):
    frame = Frame(root)
    frame.pack()
    #frame.configure(background='green')
    bottomframe = Frame(root)
    #bottomframe.configure(background='green')
    bottomframe.pack( side = BOTTOM )
    for j in range(1,6):
        txt = "{:^2}"
        l=txt.format(data[x])
        x=x+1
        redbutton = Button(frame, text = l, fg ='green',command= cc)
        redbutton.pack( side = LEFT)
root.mainloop()

#Test 










