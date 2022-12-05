from tkinter import *

'''EVENT HANDLING STARTS HERE-------------------------------------'''


def one():
    e1.insert(END, "1")


def two():
    e1.insert(END, "2")


def three():
    e1.insert(END, "3")


def four():
    e1.insert(END, "4")


def five():
    e1.insert(END, "5")


def six():
    e1.insert(END, "6")


def seven():
    e1.insert(END, "7")



def eight():
    e1.insert(END, "8")


def dot():
    e1.insert(END, ".")


def nine():
    e1.insert(END, "9")


def addit():
    e1.insert(END, "+")

def subt():
    e1.insert(END, "-")


def div():
    e1.insert(END, "/")


def per():
    e1.insert(END, "//")


def equals():
    a = e1.get()
    e1.delete(0, len(a))
    e1.insert(len(a), eval(a))


def zero():
    e1.insert(END, "0")


def mult():
    e1.insert(END, "*")


def all_clr():
    b = e1.get()
    e1.delete(0, len(b))


def one_clr():
    c = e1.get()
    e1.delete(len(c)-1)


root = Tk()
root.title("CALCULATOR")
root.geometry("295x340")
root.config(bg="blACK", border=4)
f1 = "Times", "18"
e1 = Entry(root, borderwidth=1, width=22, border=4, font=f1,justify="right")
e1.place(x=10, y=20)

''' FIRST COLUMN --------------------------------------------------'''

ac = Button(root, text="AC", background="red", font=f1, command=all_clr) #AC Button
ac.place(x=20, y=80, height=40, width=50)

b0 = Button(root, text="0", background="lightgrey", font=f1, command=zero) #0 Button
b0.place(x=20, y=280, height=40, width=50)

b1 = Button(root, text="1", background="lightgrey", font=f1, command=one) #1 Button
b1.place(x=20, y=230, height=40, width=50)

b4 = Button(root, text="4", background="lightgrey", font=f1, command=four) #4 Button
b4.place(x=20, y=180, height=40, width=50)

b7 = Button(root, text="7", background="lightgrey", font=f1, command=seven) #7 Button
b7.place(x=20, y=130, height=40, width=50)

''' SECOND COLUMN-----------------------------------------------------'''

bd = Button(root, text=".", background="lightgrey", font=f1, command=dot) #dot Button
bd.place(x=90, y=280, height=40, width=50)

b2 = Button(root, text="2", background="light grey", font=f1, command=two) #2 Button
b2.place(x=90, y=230, height=40, width=50)

b5 = Button(root, text="5", background="lightgrey", font=f1, command=five) #5 Button
b5.place(x=90, y=180, height=40, width=50)

b8 = Button(root, text="8", background="lightgrey", font=f1, command=eight) #8 Button
b8.place(x=90, y=130, height=40, width=50)

de = Button(root, text="DEL", background="red", font="Times, 15", command=one_clr) #DELETE Button (delete one operand)
de.place(x=90, y=80, height=40, width=50)

'''THIRD COLUMN------------------------------------------------------'''

eq = Button(root, text="=", background="grey", font=f1, command=equals) #= Button
eq.place(x=160, y=280, height=40, width=50)

b3 = Button(root, text="3", background="lightgrey", font=f1, command=three) #3 Button
b3.place(x=160, y=230, height=40, width=50)

b6 = Button(root, text="6", background="lightgrey", font=f1, command=six) #6 Button
b6.place(x=160, y=180, height=40, width=50)

b9 = Button(root, text="9", background="lightgrey", font=f1, command=nine) #9 Button
b9.place(x=160, y=130, height=40, width=50)


'''LAST COLUMN -------------------------------------------------------'''


ad = Button(root, text="+", background="grey", font=f1, command=addit) #= Button
ad.place(x=230, y=230, height=90, width=50)

m = Button(root, text="-", background="grey", font=f1, command=subt) #3 Button
m.place(x=230, y=180, height=40, width=50)

mul = Button(root, text="x", background="grey", font=f1, command=mult) #6 Button
mul.place(x=230, y=130, height=40, width=50)

div = Button(root, text="/", background="grey", font=f1, command=div) #9 Button
div.place(x=230, y=80, height=40, width=50)

per = Button(root, text="%", background="grey", font=f1, command=per) #% Button
per.place(x=160, y=80, height=40, width=50)


root.mainloop()

