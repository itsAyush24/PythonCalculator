import tkinter
from tkinter import *
from tkinter import messagebox


val = ""
A = 0
operator = ""

def btn_1_clicked() :
    global val
    val = val + "1"
    data.set(val)

def btn_2_clicked() :
    global val
    val = val + "2"
    data.set(val)
    

def btn_3_clicked() :
    global val
    val = val + "3"
    data.set(val)

def btn_4_clicked() :
    global val
    val = val + "4"
    data.set(val)

def btn_5_clicked() :
    global val
    val = val + "5"
    data.set(val)

def btn_6_clicked() :
    global val
    val = val + "6"
    data.set(val)

def btn_7_clicked() :
    global val
    val = val + "7"
    data.set(val)

def btn_8_clicked() :
    global val
    val = val + "8"
    data.set(val)

def btn_9_clicked() :
    global val
    val = val + "9"
    data.set(val)

def btn_0_clicked() :
    global val
    val = val + "0"
    data.set(val)


def btn_plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_minus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_multiplication_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "x"
    val = val + "x"
    data.set(val)


def btn_divide_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def c_clicked() :
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def result() :
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        stored = int(val2.split("+")[1])
        c = A + stored
        data.set(c)
        val = str(c)

    elif operator == "-":
        stored = int(val2.split("-")[1])
        c = A - stored
        data.set(c)
        val = str(c)

    elif operator == "x":
        stored = int(val2.split("x")[1])
        c = A * stored
        data.set(c)
        val = str(c)

    elif operator == "/":
        stored = int(val2.split("/")[1])
        if stored == 0 :
            messagebox.showerror("Error", "Division by zero not allowed")
            A = ""
            val = ""
            data.set(val)
        else :
            c= int(A / stored)
            data.set(c)
            val = str(c)



    

root = tkinter.Tk()
root.geometry("250x400+350+50")
root.resizable(0,0)
root.title("Calculator")


data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Bahnschrift SemiLight", 20),
    textvariable = data,
    bg = "#ffffff",
    fg = "#000000"
    )
lbl.pack(expand = True, fill = "both")


btnrow1 = Frame(root, bg= "#000000")
btnrow1.pack(expand = True, fill = "both", )

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")







btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_1_clicked
    )
btn1.pack(side = LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_2_clicked
    )
btn2.pack(side = LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_3_clicked
    )
btn3.pack(side = LEFT, expand = True, fill = "both")

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked
    )
btnplus.pack(side = LEFT, expand = True, fill = "both")







btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_4_clicked
    )
btn4.pack(side = LEFT, expand = True, fill = "both")

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_5_clicked
    )
btn5.pack(side = LEFT, expand = True, fill = "both")

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_6_clicked
    )
btn6.pack(side = LEFT, expand = True, fill = "both")

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked
    )
btnminus.pack(side = LEFT, expand = True, fill = "both")






btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_7_clicked
    )
btn7.pack(side = LEFT, expand = True, fill = "both")

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_8_clicked
    )
btn8.pack(side = LEFT, expand = True, fill = "both")

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_9_clicked
    )
btn9.pack(side = LEFT, expand = True, fill = "both")

btnmultiply = Button(
    btnrow3,
    text = "x",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_multiplication_clicked
    )
btnmultiply.pack(side = LEFT, expand = True, fill = "both")




btn_cancel = Button(
    btnrow4,
    text = "C",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = c_clicked
    )
btn_cancel.pack(side = LEFT, expand = True, fill = "both")

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_0_clicked
    )
btn0.pack(side = LEFT, expand = True, fill = "both")

btn_equals = Button(
    btnrow4,
    text = "=",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = result
    )
btn_equals.pack(side = LEFT, expand = True, fill = "both")

btn_divide = Button(
    btnrow4,
    text = "/",
    font = ("Bahnschrift SemiLight", 16),
    relief = GROOVE,
    border = 0,
    command = btn_divide_clicked
    )
btn_divide.pack(side = LEFT, expand = True, fill = "both")

root.mainloop()
