from tkinter import *
from tkinter import font as tkfont

window = Tk()
window.geometry("348x389")
window.title("Pycalc")
window.configure(bg = "#383838")

f1 = tkfont.Font(size = 34, weight = 'bold')
f2 = tkfont.Font(size = 20, weight = 'bold')
f3 = tkfont.Font(size = 12, weight = 'bold')
f4 = tkfont.Font(size = 24, weight = 'bold')

dispval = StringVar()
dispoper = StringVar()
value = ""
check = 0
value1 = 0
value2 = 0
ans = 0
anscheck = 0

def clrscr():
    global check, value1, value2, ans, anscheck
    global value
    value = ""
    dispval.set(value)
    check = 0
    value1 = 0
    value2 = 0
    ans = 0
    anscheck = 0
    dispoper.set("")

def rm_disp():
    global value
    x = len(value)
    value = value[:x-1]
    dispval.set(value)

def do_perc():
    global value
    x = float(value)
    x = x /100
    value = str(x)
    dispval.set(value)

def add_disp(x):
    global value,anscheck
    if anscheck == 1:
        value = ""
        dispval.set(value)
        dispoper.set("")
        anscheck=0
    value = value + x
    dispval.set(value)

def operation(x):
    global value,value1
    global check
    if x == 1:
        dispoper.set("+")
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 1
    elif x == 2:
        dispoper.set("-")
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 2
    elif x == 3:
        dispoper.set("*")
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 3
    elif x == 4:
        dispoper.set("÷")
        if check ==1 or check == 2 or check == 3 or check ==4 :
            result()
        else:
            value1 = float(value)
            value = ""
            dispval.set(value)
        check = 4

def result(y=0):
    global value, value1, value2, ans, check, anscheck
    if check == 1:
        if value == "":
            value2 = value1
        else:
            value2 = float(value)
        ans = value1 + value2
        value = str(ans)
        if value[len(value)-1] == '0':
            x = len(value)
            value = value[:x - 2]
        value1 = float(value)
        dispval.set(value)
        if y == 1:
            check = 0
            dispoper.set("=")
        anscheck = 1
    elif check == 2:
        if value == "":
            value2 = value1
        else:
            value2 = float(value)
        ans = value1 - value2
        value = str(ans)
        if value[len(value)-1] == '0':
            x = len(value)
            value = value[:x - 2]
        value1 =float(value)
        dispval.set(value)
        if y == 1:
            check = 0
            dispoper.set("=")
        anscheck = 1
    elif check == 3:
        if value == "":
            value2 = value1
        else:
            value2 = float(value)
        ans = value1 * value2
        value = str(ans)
        if value[len(value)-1] == '0':
            x = len(value)
            value = value[:x - 2]
        value1 = float(value)
        dispval.set(value)
        if y == 1:
            check = 0
            dispoper.set("=")
        anscheck = 1
    elif check == 4:
        if value == "":
            value2 = value1
        else:
            value2 = float(value)
        ans = value1 / value2
        value = str(ans)
        if value[len(value)-1] == '0':
            x = len(value)
            value = value[:x - 2]
        value1 = float(value)
        dispval.set(value)
        if y == 1:
            check = 0
            dispoper.set("=")
        anscheck = 1

title = Label(window, text = "Calculator", bg = '#383838', fg = '#C8C8C8', font = f3)
title.place(x = 7, y = 7)
oper = Label(window, textvariable = dispoper, bg = '#383838', fg = '#C8C8C8', font = f2)
oper.place(x = 320, y = 10)
display = Label(window, textvariable = dispval, bd = 0, bg = "#383838", anchor = 'e', fg = "white", justify = RIGHT, font = f1)
display.place(x = 3, y = 35, width =340, height = 50)

bt7 = Button(window, text = "7", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("7"))
bt7.place(x = 3, y = 113, width = 66, height = 66)
bt8 = Button(window, text = "8", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("8"))
bt8.place(x = 72, y = 113, width = 66, height = 66)
bt9 = Button(window, text = "9", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("9"))
bt9.place(x = 141, y = 113, width = 66, height = 66)
bt4 = Button(window, text = "4", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("4"))
bt4.place(x = 3, y = 182, width = 66, height = 66)
bt5 = Button(window, text = "5", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("5"))
bt5.place(x = 72, y = 182, width = 66, height = 66)
bt6 = Button(window, text = "6", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("6"))
bt6.place(x = 141, y = 182, width = 66, height = 66)
bt1 = Button(window, text = "1", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("1"))
bt1.place(x = 3, y = 251, width = 66, height = 66)
bt2 = Button(window, text = "2", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("2"))
bt2.place(x = 72, y = 251, width = 66, height = 66)
bt3 = Button(window, text = "3", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("3"))
bt3.place(x = 141, y = 251, width = 66, height = 66)
btDot = Button(window, text = ".", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("."))
btDot.place(x = 3, y = 320, width = 66, height = 66)
bt0 = Button(window, text = "0", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda :add_disp("0"))
bt0.place(x = 72, y = 320, width = 66, height = 66)
btPerc = Button(window, text = "%", font = f2, bg = 'black', fg = 'white', bd = 0, activebackground = '#787878', command = lambda : do_perc())
btPerc.place(x = 141, y = 320, width = 66, height = 66)

btDel = Button(window, text = "C", font = f2, bg = '#202020', fg = 'white', bd = 0, activebackground = '#A9A9A9', command = lambda : rm_disp())
btDel.place(x = 210, y = 113, width = 66, height = 66)
btCLR = Button(window, text = "AC", font = f2, bg = '#9e0e0e', fg = 'white', bd = 0, activebackground = '#cc3737', command = lambda : clrscr())
btCLR.place(x = 279, y = 113, width = 66, height = 66)
btMul = Button(window, text = "*", font = f2, bg = '#202020', fg = 'white', bd = 0, activebackground = '#A9A9A9', command = lambda : operation(3))
btMul.place(x = 210, y = 182, width = 66, height = 66)
btDiv = Button(window, text = "÷", font = f2, bg = '#202020', fg = 'white', bd = 0, activebackground = '#A9A9A9', command = lambda : operation(4))
btDiv.place(x = 279, y = 182, width = 66, height = 66)
btAdd = Button(window, text = "+", font = f2, bg = '#202020', fg = 'white', bd = 0, activebackground = '#A9A9A9', command = lambda : operation(1))
btAdd.place(x = 210, y = 251, width = 66, height = 66)
btSub = Button(window, text = "-", font = f2, bg = '#202020', fg = 'white', bd = 0, activebackground = '#A9A9A9', command = lambda : operation(2))
btSub.place(x = 279, y = 251, width = 66, height = 66)
btEq = Button(window, text = "=", font = f2, bg = '#db440d', fg = 'white', bd = 0, activebackground = '#eb6d3f', command = lambda : result(1))
btEq.place(x = 210, y = 320, width = 135, height = 66)




window.mainloop()