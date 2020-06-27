from tkinter import *

window = Tk()
window.geometry("348x500")
window.title("Pycalc")
window.configure(bg = "#212222")

dispval = StringVar()
value = ""
check = 0
value1 = 0
value2 = 0
ans = 0
anscheck = 0

def clrscr():
    global value
    value = ""
    dispval.set(value)

def add_disp(x):
    global value,anscheck
    if anscheck == 1:
        value = ""
        dispval.set(value)
    value = value + x
    dispval.set(value)

def operation(x):
    global value,value1
    global check

    if x == 1:
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 1
    elif x == 2:
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 2
    elif x == 3:
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 3
    elif x == 4:
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 4

def result():
    global value, value1, value2, ans, check, anscheck
    if check == 1:
        value2 = float(value)
        ans = value1 + value2
        value = str(ans)
        dispval.set(value)
        check = 0
        anscheck = 1
    elif check == 2:
        value2 = float(value)
        ans = value1 - value2
        value = str(ans)
        dispval.set(value)
        check = 0
        anscheck = 1
    elif check == 3:
        value2 = float(value)
        ans = value1 * value2
        value = str(ans)
        dispval.set(value)
        check = 0
        anscheck = 1
    elif check == 4:
        value2 = float(value)
        ans = value1 / value2
        value = str(ans)
        dispval.set(value)
        check = 0
        anscheck = 1


display = Entry(window, textvariable = dispval, bd = 0, bg = "#151515", fg = "white")
display.place(x = 0, y = 30, width =348, height = 100)

bt7 = Button(window, text = "7", command = lambda :add_disp("7"))
bt7.place(x = 3, y = 133, width = 66, height = 66)
bt8 = Button(window, text = "8", command = lambda :add_disp("8"))
bt8.place(x = 72, y = 133, width = 66, height = 66)
bt9 = Button(window, text = "9", command = lambda :add_disp("9"))
bt9.place(x = 141, y = 133, width = 66, height = 66)
bt4 = Button(window, text = "4", command = lambda :add_disp("4"))
bt4.place(x = 3, y = 202, width = 66, height = 66)
bt5 = Button(window, text = "5", command = lambda :add_disp("5"))
bt5.place(x = 72, y = 202, width = 66, height = 66)
bt6 = Button(window, text = "6", command = lambda :add_disp("6"))
bt6.place(x = 141, y = 202, width = 66, height = 66)
bt1 = Button(window, text = "1", command = lambda :add_disp("1"))
bt1.place(x = 3, y = 271, width = 66, height = 66)
bt2 = Button(window, text = "2", command = lambda :add_disp("2"))
bt2.place(x = 72, y = 271, width = 66, height = 66)
bt3 = Button(window, text = "3", command = lambda :add_disp("3"))
bt3.place(x = 141, y = 271, width = 66, height = 66)
btDot = Button(window, text = ".", command = lambda :add_disp("."))
btDot.place(x = 3, y = 340, width = 66, height = 66)
bt0 = Button(window, text = "0", command = lambda :add_disp("0"))
bt0.place(x = 72, y = 340, width = 66, height = 66)
btPerc = Button(window, text = "%")
btPerc.place(x = 141, y = 340, width = 66, height = 66)

btDel = Button(window, text = "<-")
btDel.place(x = 210, y = 133, width = 66, height = 66)
btCLR = Button(window, text = "C", command = lambda : clrscr())
btCLR.place(x = 279, y = 133, width = 66, height = 66)
btMul = Button(window, text = "*", command = lambda : operation(3))
btMul.place(x = 210, y = 202, width = 66, height = 66)
btDiv = Button(window, text = "÷", command = lambda : operation(4))
btDiv.place(x = 279, y = 202, width = 66, height = 66)
btAdd = Button(window, text = "+", command = lambda : operation(1))
btAdd.place(x = 210, y = 271, width = 66, height = 66)
btSub = Button(window, text = "-", command = lambda : operation(2))
btSub.place(x = 279, y = 271, width = 66, height = 66)
btEq = Button(window, text = "=", command = lambda : result())
btEq.place(x = 210, y = 340, width = 135, height = 66)




window.mainloop()