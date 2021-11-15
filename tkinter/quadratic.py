# AUTHOR : gonewithharshwinds
# 
# 
from tkinter import *
root = Tk()
root.title("Quadratic Equation Calculator")
h = StringVar()
z = 0

def adding():
    x1 = 0
    a = float(R1.get())
    b = float(R2.get())
    c = float(R3.get())
    d = abs(b**2-4*a*c)
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    h.set(str(x1) + " or " + str(x2))

I = Label(root, text = " Enter the value of A, B, and C in Ax^2 + Bx + C : \t", font=('Helvetica',16))
I.grid(row = 0, column = 0, columnspan = 2)
V_A = Label(root, text = "A \t = ")
V_A.grid(row = 1, column = 0)
V_B = Label(root, text = "B \t = ")
V_B.grid(row = 2, column = 0)
V_C = Label(root, text = "C \t = ")
V_C.grid(row = 3, column = 0)
R1 = Entry(root)
R1.grid(row = 1, column = 1)
R2 = Entry(root)
R2.grid(row =2, column =1)
R3 =  Entry(root)
R3.grid(row =3, column =1)
V = Label(root, text = "X \t = ")
V.grid(row = 5, column = 0)
R4 = Entry(root, textvariable=h)
R4.grid(row = 5, column = 1)
b1 = Button(root, text =  "SOLVE", command = lambda  :adding(), font=('Helvetica',12)).grid(row = 4, column =1)
root.mainloop()