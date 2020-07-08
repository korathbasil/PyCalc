from tkinter import *
from tkinter import font as tkfont

window = Tk()
window.geometry("350x550")
window.title("PyCalc")
window.configure(bg = "#383838")
window.resizable(0,0)

f1 = tkfont.Font(size = 34, weight = 'bold')
f2 = tkfont.Font(size = 20, weight = 'bold')
f3 = tkfont.Font(size = 12, weight = 'bold')
f4 = tkfont.Font(size = 24, weight = 'bold')

def option_changed(*args):
    x = var.get()
    if x == "Standard":
        scffrm.forget()
        covfrm.forget()
        stdfrm.pack()
    elif x == "Scientific":
        stdfrm.forget()
        covfrm.forget()
        scffrm.pack()
    elif x == "Converter":
        stdfrm.forget()
        scffrm.forget()
        covfrm.pack()

## vriables for standard calculator ##
##''''''''''''''''''''''''''''''''''##

dispval = StringVar()
dispoper = StringVar()
value = ""
check = 0
value1 = 0
value2 = 0
ans = 0
anscheck = 0
stdm = 0
stdmemvar = StringVar()

## vriables for scientific calculator ##
##''''''''''''''''''''''''''''''''''''##

scfdispval = StringVar()
scfvalue = ""
scfmemvar = StringVar()
scfdispoper = StringVar()
scfcheck = 0
scfvalue1 = 0
scfvalue2 = 0
scfans = 0
scfanscheck = 0
scfm = 0


## functions for standard calculator ##
##'''''''''''''''''''''''''''''''''''##

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

def stdcheckmem(x):
    global stdm, value, stdmemvar, dispval
    if x == 3:
        stdm = stdm + float(value)
        stdmemvar.set("M")
    elif x ==4:
        stdm = stdm - float(value)
        stdmemvar.set("M")
    elif x == 2:
        if stdm != 0:
            value = str(stdm)
            if value[len(value)-1] == '0':
                x = len(value)
                value = value[:x - 2]
            dispval.set(value)
    elif x ==1:
        stdm = 0
        stdmemvar.set("")

## functions for scientific calculator ##
##'''''''''''''''''''''''''''''''''''''##

def add_scfdisp(x):
    global scfvalue
    scfvalue = scfvalue + x
    scfdispval.set(scfvalue)

def scfclrscr():
    global scfcheck, scfvalue1, scfvalue2, scfans, scfanscheck
    global scfvalue
    scfvalue = ""
    scfdispval.set(scfvalue)
    scfcheck = 0
    scfvalue1 = 0
    scfvalue2 = 0
    scfans = 0
    scfanscheck = 0
    scfdispoper.set("")

def scfrm_disp():
    global scfvalue
    x = len(scfvalue)
    scfvalue = scfvalue[:x-1]
    scfdispval.set(scfvalue)

def scfdo_perc():
    global scfvalue
    x = float(scfvalue)
    x = x /100
    scfvalue = str(x)
    scfdispval.set(scfvalue)

def scfcheckmem(x):
    global scfm, scfvalue, scfmemvar, scfdispval
    if x == 3:
        scfm = acfm + float(scfvalue)
        scfmemvar.set("M")
    elif x ==4:
        scfm = scfm - float(scfvalue)
        scfmemvar.set("M")
    elif x == 2:
        if scfm != 0:
            scfvalue = str(scfm)
            if scfvalue[len(scfvalue)-1] == '0':
                x = len(scfvalue)
                scfvalue = scfvalue[:x - 2]
            scfdispval.set(scfvalue)
    elif x ==1:
        scfm = 0
        scfmemvar.set("")

def scfoperation(x):
    global scfvalue, scfvalue1
    global scfcheck
    if x == 1:
        scfdispoper.set("+")
        if scfcheck ==1 or scfcheck == 2 or scfcheck == 3 or scfcheck ==4 :
            scfresult()
        else:
            scfvalue1 = float(scfvalue)
            scfvalue = ""
            scfdispval.set(scfvalue)
        scfcheck = 1
    elif x == 2:
        scfdispoper.set("-")
        if scfcheck ==1 or scfcheck == 2 or scfcheck == 3 or scfcheck ==4 :
            scfresult()
        else:
            scfvalue1 = float(scfvalue)
            scfvalue = ""
            scfdispval.set(scfvalue)
        scfcheck = 2
    elif x == 3:
        scfdispoper.set("*")
        if scfcheck ==1 or scfcheck == 2 or scfcheck == 3 or scfcheck ==4 :
            scfresult()
        else:
            scfvalue1 = float(scfvalue)
            scfvalue = ""
            scfdispval.set(scfvalue)
        scfcheck = 3
    elif x == 4:
        scfdispoper.set("÷")
        if scfcheck ==1 or scfcheck == 2 or scfcheck == 3 or scfcheck ==4 :
            scfresult()
        else:
            scfvalue1 = float(scfvalue)
            scfvalue = ""
            scfdispval.set(scfvalue)
        scfcheck = 4

def scfresult(y=0):
    global scfvalue, scfvalue1, scfvalue2, scfans, scfcheck, scfanscheck
    if scfcheck == 1:
        if scfvalue == "":
            scfvalue2 = scfvalue1
        else:
            scfvalue2 = float(scfvalue)
        scfans = scfvalue1 + scfvalue2
        scfvalue = str(scfans)
        if scfvalue[len(scfvalue)-1] == '0':
            x = len(scfvalue)
            scfvalue = scfvalue[:x - 2]
        scfvalue1 = float(scfvalue)
        scfdispval.set(scfvalue)
        if y == 1:
            scfcheck = 0
            scfdispoper.set("=")
        scfanscheck = 1
    elif scfcheck == 2:
        if scfvalue == "":
            scfvalue2 = scfvalue1
        else:
            scfvalue2 = float(scfvalue)
        scfans = scfvalue1 - scfvalue2
        scfvalue = str(scfans)
        if scfvalue[len(scfvalue)-1] == '0':
            x = len(scfvalue)
            scfvalue = scfvalue[:x - 2]
        scfvalue1 =float(scfvalue)
        scfdispval.set(scfvalue)
        if y == 1:
            scfcheck = 0
            scfdispoper.set("=")
        scfanscheck = 1
    elif scfcheck == 3:
        if scfvalue == "":
            scfvalue2 = scfvalue1
        else:
            scfvalue2 = float(scfvalue)
        scfans = scfvalue1 * scfvalue2
        scfvalue = str(scfans)
        if scfvalue[len(scfvalue)-1] == '0':
            x = len(scfvalue)
            scfvalue = scfvalue[:x - 2]
        scfvalue1 = float(scfvalue)
        scfdispval.set(scfvalue)
        if y == 1:
            scfcheck = 0
            scfdispoper.set("=")
        scfanscheck = 1
    elif scfcheck == 4:
        if scfvalue == "":
            scfvalue2 = scfvalue1
        else:
            scfvalue2 = float(scfvalue)
        scfans = scfvalue1 / scfvalue2
        scfvalue = str(scfans)
        if scfvalue[len(scfvalue)-1] == '0':
            x = len(scfvalue)
            scfvalue = scfvalue[:x - 2]
        scfvalue1 = float(scfvalue)
        scfdispval.set(scfvalue)
        if y == 1:
            scfcheck = 0
            scfdispoper.set("=")
        scfanscheck = 1


## General elements for all mode ##
##===============================##

basefrm = Frame(window, height = 40, width = 348, bg = "#383838").pack()
var = StringVar(basefrm)
var.set("Standard")
var.trace('w',option_changed)
switcher = OptionMenu(basefrm, var, "Standard", "Scientific", "Converter")
switcher.place(x = 7, y = 7)
switcher.configure(bg = "#383838", fg = "white", highlightthickness = 0, bd = 0, font = f3, width = 8)

stdfrm = Frame(window, height = 510, width = 350, bg = "#383838")
scffrm = Frame(window, height = 510, width = 350, bg = "#383838")
covfrm = Frame(window, height = 510, width = 350, bg = "#383838")

## Elements for standard calculator ##
##==================================##

oper = Label(stdfrm, textvariable = dispoper, bg = "#383838", fg = '#C8C8C8', font = f2)
oper.place(x = 320, y = 10)
display = Label(stdfrm, textvariable = dispval, bd = 0, bg = "#383838", anchor = 'e', fg = "white", justify = RIGHT, font = f1)
display.place(x = 3, y = 75, width =340, height = 50)
stdmemdisp = Label(stdfrm, textvariable = stdmemvar, bg = "#383838", fg = '#C8C8C8', font = f2 )
stdmemdisp.place(x = 10, y = 10, height = 30, width = 30)

stdbtMC = Button(stdfrm, text = "MC", bg = '#383838', fg = 'white', bd = 0, highlightbackground = "#383838", activebackground = '#383838', font = f3, command = lambda : stdcheckmem(1))
stdbtMC.place(x = 39, y = 165, height = 63, width = 63)
stdbtMRC = Button(stdfrm, text = "MRC", bg = '#383838', fg = 'white', bd = 0, highlightbackground = "#383838", activebackground = '#383838', font = f3, command = lambda : stdcheckmem(2))
stdbtMRC.place(x = 108, y = 165, height = 63, width = 63)
stdbtMadd = Button(stdfrm, text = "M+", bg = '#383838', fg = 'white',bd = 0, highlightbackground = "#383838", activebackground = '#383838', font = f3, command = lambda : stdcheckmem(3))
stdbtMadd.place(x = 177, y = 165, height = 63, width = 63)
stdbtMsub = Button(stdfrm, text = "M-", bg = '#383838', fg = 'white', bd = 0, highlightbackground = "#383838", activebackground = '#383838', font = f3, command = lambda : stdcheckmem(4))
stdbtMsub.place(x = 246, y = 165, height = 63, width = 63)


bt7 = Button(stdfrm, text = "7", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("7"))
bt7.place(x = 3, y = 231, width = 66, height = 66)
bt8 = Button(stdfrm, text = "8", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("8"))
bt8.place(x = 72, y = 231, width = 66, height = 66)
bt9 = Button(stdfrm, text = "9", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("9"))
bt9.place(x = 141, y = 231, width = 66, height = 66)
bt4 = Button(stdfrm, text = "4", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("4"))
bt4.place(x = 3, y = 300, width = 66, height = 66)
bt5 = Button(stdfrm, text = "5", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("5"))
bt5.place(x = 72, y = 300, width = 66, height = 66)
bt6 = Button(stdfrm, text = "6", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("6"))
bt6.place(x = 141, y = 300, width = 66, height = 66)
bt1 = Button(stdfrm, text = "1", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("1"))
bt1.place(x = 3, y = 369, width = 66, height = 66)
bt2 = Button(stdfrm, text = "2", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("2"))
bt2.place(x = 72, y = 369, width = 66, height = 66)
bt3 = Button(stdfrm, text = "3", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : add_disp("3"))
bt3.place(x = 141, y = 369, width = 66, height = 66)
btDot = Button(stdfrm, text = ".", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda :add_disp("."))
btDot.place(x = 3, y = 438, width = 66, height = 66)
bt0 = Button(stdfrm, text = "0", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda :add_disp("0"))
bt0.place(x = 72, y = 438, width = 66, height = 66)
btPerc = Button(stdfrm, text = "%", font = f2, bg = 'black', fg = 'white', bd = 0, highlightbackground = 'black', activebackground = '#787878', command = lambda : do_perc())
btPerc.place(x = 141, y = 438, width = 66, height = 66)

btDel = Button(stdfrm, text = "C", font = f2, bg = '#202020', fg = 'white', bd = 0, highlightbackground = '#202020', activebackground = '#A9A9A9', command = lambda : rm_disp())
btDel.place(x = 210, y = 231, width = 66, height = 66)
btCLR = Button(stdfrm, text = "AC", font = f2, bg = '#9e0e0e', fg = 'white', bd = 0, highlightbackground = '#9e0e0e', activebackground = '#cc3737', command = lambda : clrscr())
btCLR.place(x = 279, y = 231, width = 66, height = 66)
btMul = Button(stdfrm, text = "*", font = f2, bg = '#202020', fg = 'white', bd = 0, highlightbackground = '#202020', activebackground = '#A9A9A9', command = lambda : operation(3))
btMul.place(x = 210, y = 300, width = 66, height = 66)
btDiv = Button(stdfrm, text = "÷", font = f2, bg = '#202020', fg = 'white', bd = 0, highlightbackground = '#202020', activebackground = '#A9A9A9', command = lambda : operation(4))
btDiv.place(x = 279, y = 300, width = 66, height = 66)
btAdd = Button(stdfrm, text = "+", font = f2, bg = '#202020', fg = 'white', bd = 0, highlightbackground = '#202020', activebackground = '#A9A9A9', command = lambda : operation(1))
btAdd.place(x = 210, y = 369, width = 66, height = 66)
btSub = Button(stdfrm, text = "-", font = f2, bg = '#202020', fg = 'white', bd = 0, highlightbackground = '#202020', activebackground = '#A9A9A9', command = lambda : operation(2))
btSub.place(x = 279, y = 369, width = 66, height = 66)
btEq = Button(stdfrm, text = "=", font = f2, bg = '#db440d', fg = 'white', bd = 0, highlightbackground = '#db440d', activebackground = '#eb6d3f', command = lambda : result(1))
btEq.place(x = 210, y = 438, width = 135, height = 66)

## Elements for Scientic calculator ##
##==================================##

scfoper = Label(scffrm, textvariable = scfdispoper, bg = "#383838", fg = '#C8C8C8', font = f4)
scfoper.place(x = 320, y = 10)

scfdisplay = Label(scffrm, textvariable = scfdispval, bg = "black", fg = 'white', anchor = 'e', justify = RIGHT, font = f3)
scfdisplay.place(x = 5, y = 0, height = 100, width = 340)

scfbtsin = Button(scffrm, text = "sin", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtsin.place(x = 5, y = 105, height = 55, width = 55)
scfbtcos = Button(scffrm, text = "cos", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtcos.place(x = 5, y = 162, height = 55, width = 55)
scfbttan = Button(scffrm, text = "tan", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbttan.place(x = 5, y = 219, height = 55, width = 55)
scfbtcsc = Button(scffrm, text = "csc", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtcsc.place(x = 62, y = 105, height = 55, width = 55)
scfbtsec = Button(scffrm, text = "sec", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtsec.place(x = 62, y = 162, height = 55, width = 55)
scfbtcot = Button(scffrm, text = "cot", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtcot.place(x = 62, y = 219, height = 55, width = 55)

scfMC = Button(scffrm, text = "MC", bd = 0, bg = '#777777', fg = 'white', highlightbackground = '#777777')
scfMC.place(x = 119, y = 162, height = 55, width = 55)
scfDel = Button(scffrm, text = "DEL", bd = 0, bg = '#777777', fg = 'white', highlightbackground = '#777777', command = lambda : scfrm_disp())
scfDel.place(x = 233, y = 105, height = 55, width = 55)
scfClr = Button(scffrm, text = "AC", bg = '#9e0e0e', fg = 'white', highlightbackground = '#9e0e0e', bd = 0, font = f2, command = lambda : scfclrscr())
scfClr.place(x = 290, y = 105, height = 55, width = 55)
scfMRC = Button(scffrm, text = "MRC", bd = 0, bg = '#777777', fg = 'white', highlightbackground = '#777777')
scfMRC.place(x = 176, y = 162, height = 55, width = 55)
scfMadd = Button(scffrm, text = "M+", bd = 0, bg = '#777777', fg = 'white', highlightbackground = '#777777')
scfMadd.place(x = 233, y = 162, height = 55, width = 55)
scfMsub = Button(scffrm, text = "M-", bd = 0, bg = '#777777', fg = 'white', highlightbackground = '#777777')
scfMsub.place(x = 290, y = 162, height = 55, width = 55)
scfbtlb = Button(scffrm, text = "(", bd = 0, bg = '#777777', fg = 'white', highlightbackground = '#777777')
scfbtlb.place(x = 119, y = 105, height = 55, width = 55)
scfbtrb = Button(scffrm, text = ")", bd = 0, bg = '#777777', fg = 'white', highlightbackground = '#777777')
scfbtrb.place(x = 176, y = 105, height = 55, width = 55)

scfbt7 = Button(scffrm, text = "7", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("7"))
scfbt7.place(x = 5, y = 276, height = 55, width = 55)
scfbt8 = Button(scffrm, text = "8", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("8"))
scfbt8.place(x = 62, y = 276, height = 55, width = 55)
scfbt9 = Button(scffrm, text = "9", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("9"))
scfbt9.place(x = 119, y = 276, height = 55, width = 55)
scfbt4 = Button(scffrm, text = "4", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("4"))
scfbt4.place(x = 5, y = 333, height = 55, width = 55)
scfbt5 = Button(scffrm, text = "5", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("5"))
scfbt5.place(x = 62, y = 333, height = 55, width = 55)
scfbt6 = Button(scffrm, text = "6", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("6"))
scfbt6.place(x = 119, y = 333, height = 55, width = 55)
scfbt1 = Button(scffrm, text = "1", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("1"))
scfbt1.place(x = 5, y = 390, height = 55, width = 55)
scfbt2 = Button(scffrm, text = "2", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("2"))
scfbt2.place(x = 62, y = 390, height = 55, width = 55)
scfbt3 = Button(scffrm, text = "3", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("3"))
scfbt3.place(x = 119, y = 390, height = 55, width = 55)
scfbt0 = Button(scffrm, text = "0", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("0"))
scfbt0.place(x = 5, y = 447, height = 55, width = 55)
scfbt00 = Button(scffrm, text = "00", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("00"))
scfbt00.place(x = 62, y = 447, height = 55, width = 55)
scfbtDot = Button(scffrm, text = ".", bg = "black", fg = "white", bd = 0, highlightbackground = 'black', font = f2, activebackground = '#787878', command = lambda :add_scfdisp("."))
scfbtDot.place(x = 119, y = 447, height = 55, width = 55)


scfbtrot = Button(scffrm, text = "√x", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtrot.place(x = 119, y = 219, height = 55, width = 55)
scfbtxy = Button(scffrm, text = "xy", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtxy.place(x = 176, y = 219, height = 55, width = 55)
scfbt10x = Button(scffrm, text = "10X", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbt10x.place(x = 233, y = 219, height = 55, width = 55)
scfbtPi = Button(scffrm, text = "Pi", bd = 0, bg = '#555555', fg = 'white', highlightbackground = '#555555')
scfbtPi.place(x = 290, y = 219, height = 55, width = 55)

scfbtx3 = Button(scffrm, text = "x³", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020')
scfbtx3.place(x = 176, y = 276, height = 55, width = 55)
scfbt1x = Button(scffrm, text = "¹⁄x", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020')
scfbt1x.place(x = 233, y = 276, height = 55, width = 55)
scfbtNF = Button(scffrm, text = "x !", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020')
scfbtNF.place(x = 290, y = 276, height = 55, width = 55)
scfbtx2 = Button(scffrm, text = "x²", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020')
scfbtx2.place(x = 176, y = 333, height = 55, width = 55)
scfbtPerc = Button(scffrm, text = "%", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020', command = lambda : scfdo_perc())
scfbtPerc.place(x = 176, y = 390, height = 55, width = 55)
scfbtSign = Button(scffrm, text = "+/-", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020')
scfbtSign.place(x = 176, y = 447, height = 55, width = 55)

scfbtMul = Button(scffrm, text = "*", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020', font = f2, command = lambda : scfoperation(3))
scfbtMul.place(x = 233, y = 333, height = 55, width = 55)
scfbtDiv = Button(scffrm, text = "/", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020', font = f2, command = lambda : scfoperation(4))
scfbtDiv.place(x = 290, y = 333, height = 55, width = 55)
scfbtAdd = Button(scffrm, text = "+", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020', font = f2, command = lambda : scfoperation(1))
scfbtAdd.place(x = 233, y = 390, height = 55, width = 55)
scfbtSub = Button(scffrm, text = "-", bd = 0, bg = '#202020', fg = 'white', highlightbackground = '#202020', font = f2, command = lambda : scfoperation(2))
scfbtSub.place(x = 290, y = 390, height = 55, width = 55)
scfbtEq = Button(scffrm, text = "=", bg = '#db440d', fg = 'white', highlightbackground = '#db440d', bd = 0, font = f2, command = lambda : scfresult(1))
scfbtEq.place(x = 233, y = 447, height = 55, width = 112)


option_changed()
window.mainloop()

