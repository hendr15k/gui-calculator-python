import tkinter
from tkinter import *
from math import *
from random import *
import time
gui = Tk()
gui.title("Taschenrechner")
msg = Message
var = DoubleVar()

def evaluate(event):
    res.configure(text="Ergebnis: " + str(eval(evil.get())))
def op():
    print (evil.get())
v = StringVar()
evil = Entry(gui, textvariable=v)
evil.bind("<Return>", evaluate)
evil.pack()
res = Label(gui)
res.pack()
def ein():
    opt = Tk()
    opt.title("Einstellungen")
    def cle():
        print("\n" * 100)
    clear = Button(opt, text="Speicher leeren", command=cle)
    clear.pack()
def one():
    v.set(v.get()+"1")
    s = v.get()
def two():
    v.set(v.get() + "2")
    s = v.get()
def drei():
    v.set(v.get() + "3")
    s = v.get()
def vier():
    v.set(v.get() + "4")
    s = v.get()
def funf():
    v.set(v.get() + "5")
    s = v.get()
def sechs():
    v.set(v.get() + "6")
    s = v.get()
def sieben():
    v.set(v.get() + "7")
    s = v.get()
def acht():
    v.set(v.get() + "8")
    s = v.get()
def neun():
    v.set(v.get() + "9")
    s = v.get()
def nul():
    v.set(v.get() + "0")
    s = v.get()
def ce():
    v.set("")
    s = v.get()
def p():
    v.set(v.get() + "+")
    s = v.get()
def g():
    v.set(v.get() + "/")
    s = v.get()
def mal():
    v.set(v.get() + "*")
    s = v.get()
def min():
    v.set(v.get() + "-")
    s = v.get()
def ran():
    v.set("random()")
    s = v.get
def wur():
    v.set("randint")
    s = v.get
def ok():
    res.configure(text="Ergebnis: " + str(eval(evil.get())))
def pi():
    v.set(v.get() + "3.14159265359")
    s = v.get()
def wurzel():
    v.set("sqrt")
    s = v.get
def c():
    v.set(v.get() + "(")
def c2():
    v.set(v.get() + ")")
def co():
    v.set(v.get() + ",")
def cr():
    v.set(v.get()[:-1])
#c = Checkbutton(gui, text="Tastensperre")
#c.pack()
ein = Button (gui, text="Einstellungen", command=ein)
ein.pack(side=BOTTOM)
ran = Button (gui, text="random", command=ran)
ran.pack(side=BOTTOM)
wur = Button (gui, text="Würfel", command=wur)
wur.pack(side=BOTTOM)
speichern = Button (gui, text="Speichern", command=op)
speichern.pack()
b1 = Button (gui, text="1", width=4,height=2, command=one)
b1.pack(side=LEFT)
b2 = Button (gui, text="2", width=4,height=2, command=two)
b2.pack(side=LEFT)
b3 = Button (gui, text="3", width=4,height=2, command=drei)
b3.pack(side=LEFT)
b4 = Button (gui, text="4", width=4,height=2, command=vier)
b4.pack(side=LEFT)
b5 = Button (gui, text="5", width=4,height=2, command= funf)
b5.pack(side=LEFT)
b6 = Button (gui, text="6", width=4,height=2, command=sechs)
b6.pack(side=LEFT)
b7 = Button (gui, text="7", width=4,height=2, command=sieben)
b7.pack(side=LEFT)
b8 = Button (gui, text="8", width=4,height=2, command=acht)
b8.pack(side=LEFT)
b9 = Button (gui, text="9", width=4,height=2, command=neun)
b9.pack(side=LEFT)
b0 = Button (gui, text="0", width=4,height=2, command=nul)
b0.pack(side=LEFT)
pi = Button (gui, text="pi", command=pi)
pi.pack(side=LEFT)
cla = Button (gui, text="(", command=c)
cla.pack(side=LEFT)
cla2 = Button (gui, text=")", command=c2)
cla2.pack(side=LEFT)
co = Button(gui, text=",", command=co)
co.pack(side=BOTTOM)
e = Button (gui, text="=", command=ok)
e.pack(side=BOTTOM)
p = Button (gui, text="+", command=p)
p.pack(side=BOTTOM)
min = Button (gui,text="-", command=min)
min.pack(side=BOTTOM)
mal = Button (gui, text="*", command=mal)
mal.pack(side=BOTTOM)
g = Button (gui, text="/", command=g)
g.pack(side=BOTTOM)
wurzel = Button(gui, text="√", command=wurzel)
wurzel.pack(side=BOTTOM)
cr = Button (gui, text="C", command=cr)
cr.pack(side=BOTTOM)
ce = Button (gui, text="CE", command=ce)
ce.pack(side=BOTTOM)
def exi():
    print(exit())
ex = Button (gui, text="X", command=exi)
ex.pack(side=BOTTOM)


gui.mainloop()