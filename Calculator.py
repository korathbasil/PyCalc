from tkinter import *
from tkinter import font as tkfont
from math import sin, cos, tan, sinh, cosh, tanh, sqrt, radians
import json
import webbrowser

window = Tk()
window.geometry("350x550")
window.title("PyCalc")
icon_img = PhotoImage(file = "./app_icon.png")
window.iconphoto(False, icon_img)
window.configure(bg = "#383838")
window.resizable(0,0)

back_arrow_black = PhotoImage(file = "./back_arrow_black.png")
back_arrow_white = PhotoImage(file = "./back_arrow_white.png")
dark_theme_img = PhotoImage(file = "./dark_theme.png")
light_theme_img = PhotoImage(file = "./light_theme.png")
github_dark_img = PhotoImage(file = "./github_dark.png")
github_light_img = PhotoImage(file = "./github_light.png")

set_file = open("settings.json",)
color_theme_data = json.load(set_file)
color_theme = color_theme_data["theme"]
set_file.close()
last_frame = ""

f1 = tkfont.Font(size = 34, weight = 'bold')
f2 = tkfont.Font(size = 20, weight = 'bold')
f3 = tkfont.Font(size = 12, weight = 'bold')
f4 = tkfont.Font(size = 24, weight = 'bold')
f5 = tkfont.Font(size = 14, weight = 'bold')

arrow_color =  back_arrow_white, back_arrow_black 
github_image = github_light_img, github_dark_img
color_text = ['white', 'black']
color_bg = ['#383838', '#FFFFFF']
color_header_bg = ['#202020','#f3e2c6']
color_btlevel1 = ['#9e0e0e', '#ff1f22']
color_btlevel2 = ['#db440d', '#ff501f']
color_btlevel3 = ['black', '#efc5b5']
color_btlevel4 = ['#202020', '#f3e2c6']
color_btlevel5 = ['#555555', '#f0ead2']
color_btlevel6 = ['#777777', '#efe7df']

def option_changed(*args):
    global last_frame
    x = var.get()
    if x == "Standard":
        last_frame = x
        topfrm.pack()
        scffrm.forget()
        setfrm.forget()
        stdfrm.pack()
    elif x == "Scientific":
        last_frame = x
        topfrm.pack()
        stdfrm.forget()
        setfrm.forget()
        scffrm.pack()
    elif x == "Settings":
        topfrm.forget()
        stdfrm.forget()
        scffrm.forget()
        setfrm.pack()
        set_top_frame.pack()
        set_bottom_frame.pack()

def color_changed() :
    global color_theme, theme_variable
    color_theme = theme_variable.get()

    # Writing theme settings to settings.json

    color_theme_data["theme"] = color_theme
    set_file = open("settings.json",'w')
    json.dump(color_theme_data, set_file, indent = "")
    set_file.close()

    set_back_button.configure(highlightbackground = color_header_bg[color_theme], activebackground = color_header_bg[color_theme],bg = color_header_bg[color_theme],image = arrow_color[color_theme])
    topfrm.configure(bg = color_header_bg[color_theme])
    set_top_frame.configure(bg = color_btlevel4[color_theme])
    light_theme.configure(bg = color_bg[color_theme])
    light_theme_button.configure(bg = color_bg[color_theme], fg = color_text[color_theme])
    dark_theme.configure(bg = color_bg[color_theme])
    dark_theme_button.configure(bg = color_bg[color_theme], fg = color_text[color_theme])
    set_header.configure(bg = color_header_bg[color_theme], fg = color_text[color_theme])
    switcher.configure(bg = color_header_bg[color_theme], activebackground = color_header_bg[color_theme])
    theme.configure(fg = color_text[color_theme])
    apply_button.configure(fg = color_text[color_theme], bg = color_header_bg[color_theme], activebackground = color_header_bg[color_theme], highlightbackground = color_header_bg[color_theme], activeforeground = color_text[color_theme])
    
    x = 0
    while x < 7 :
        color_main2[x].configure(activebackground  = color_bg[color_theme])
        x = x + 1
    x = 0
    while x < 16 :
        color_main[x].configure(bg = color_bg[color_theme], highlightbackground = color_bg[color_theme])
        x = x+1
    x = 0
    while x < 2 :
        color_level1[x].configure(bg = color_btlevel1[color_theme], highlightbackground = color_btlevel1[color_theme], activebackground = color_btlevel1[color_theme])
        x = x + 1
    x = 0
    while x < 2 :
        color_level2[x].configure(bg = color_btlevel2[color_theme], highlightbackground = color_btlevel2[color_theme], activebackground = color_btlevel2[color_theme])
        x = x + 1
    x = 0
    while x < 24 :
        color_level3[x].configure(bg = color_btlevel3[color_theme], highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme])
        x = x + 1
    x = 0
    while x < 15 :
        color_level4[x].configure(bg = color_btlevel4[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme])
        x = x + 1
    x = 0
    while x < 11 :
        color_level5[x].configure(bg = color_btlevel5[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme])
        x = x + 1
    x = 0
    while x < 7 :
        color_level6[x].configure(bg = color_btlevel6[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme])
        x = x + 1
    x = 0
    while x < 71 :
        color_text_group[x].configure(fg = color_text[color_theme], activeforeground = color_text[color_theme])
        x = x + 1


# Variables for standard calculator 


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
scftempdispval = StringVar()
scftrigcheck = 0
Pi = 3.14
scfpowercheck = 0
scfevalue1 = 0
scfvalu2 = 0
scfans = 0
scfanscheck = 0
scfm = 0
scfeval = ""

# Variables for settings page

theme_variable = IntVar()
theme_variable.set(1)

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
    global scfvalue, scfeval, scftrigcheck, scfanscheck
    if scfanscheck == 1 :
        scfvalue = ""
        scfdispval.set(scfvalue)
        scftrigcheck = 0
        scfeval = ""
        scfanscheck = 0
    if x == "+":
        scf_last_add = len(scfeval)
    scfvalue = scfvalue + x
    scfeval = scfeval + x
    scfdispval.set(scfvalue)

def scfclrscr():
    global scftrigcheck, scfvalue, scfeval
    scfvalue = ""
    scfdispval.set(scfvalue)
    scftrigcheck = 0
    scfeval = ""
    scftempdispval.set("")

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

def scfdo_trig(x) :
    global scfvalue, scfeval, scftrigcheck
    if x == 1 :
        scfvalue = scfvalue + "sin("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "sin(radians("
        scftrigcheck = 1
    elif x == 2 :
        scfvalue = scfvalue + "cos("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "cos(radians("
        scftrigcheck = 1
    elif x == 3 :
        scfvalue = scfvalue + "tan("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "tan(radians("
        scftrigcheck = 1
    elif x == 4 :
        scfvalue = scfvalue + "csc("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "csc(radians("
        scftrigcheck = 1
    elif x == 5 :
        scfvalue = scfvalue + "sec("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "sec(radians("
        scftrigcheck = 1
    elif x == 6 :
        scfvalue = scfvalue + "cot("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "cot(radians("
        scftrigcheck = 1

def scfdo_power(x) :
    global scfvalue, scfeval, scfpowercheck
    if x == 1:
        scfvalue = scfvalue + "√("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "sqrt("
    if x == 2:
        scfvalue = scfvalue + "^"
        scfdispval.set(scfvalue)
        scfeval = scfeval + "**"
    if x == 3:
        scfvalue = scfvalue + "^10"
        scfdispval.set(scfvalue)
        scfeval = scfeval + "**10"
    if x == 4:
        scfvalue = scfvalue + "^3"
        scfdispval.set(scfvalue)
        scfeval = scfeval + "**3"
    if x == 5:
        scfvalue = scfvalue + "^2"
        scfdispval.set(scfvalue)
        scfeval = scfeval + "**2"

def scfdo_extrafn(x) :
    global Pi, scfvalue, scfeval
    if x == 1 :
        scfvalue = scfvalue + "π"
        scfdispval.set(scfvalue)
        scfeval = scfeval + "3.14"
    if x == 2 :
        scfvalue = scfvalue + "1/("
        scfdispval.set(scfvalue)
        scfeval = scfeval + "1/("
    if x == 3 :
        scfvalue = scfvalue + "!"
        scfdispval.set(scfvalue)
        scfeval = scfeval + "!"
    if x == 4 :
        scfvalue = scfvalue + "π"
        scfdispval.set(scfvalue)
        scfeval = scfeval + "3.14"

def scfdo_oper(x) :
    global scfvalue, scfeval, scftrigcheck
    if scftrigcheck == 1 :
        scfeval = scfeval + ")"
        scftrigcheck = 0
    scfvalue = scfvalue + x
    scfeval = scfeval + x
    scfdispval.set(scfvalue)
    


def scfcheckmem(x):
    global scfm, scfvalue, scfmemvar, scfdispval
    tempmem = ""
    if x == 3:
        scfm = scfm + eval(scfeval)
        scfmemvar.set("M")
    elif x ==4:
        scfm = scfm - eval(scfeval)
        scfmemvar.set("M")
    elif x == 2:
        tempmem = str(scfm)
        if tempmem != "" :
            if  tempmem[len(tempmem)-1] == '0' :
                tempmem = tempmem[:len(tempmem)-2]
        scfdispval.set(tempmem)
    elif x ==1:
        scfm = 0
        tempmem = ""
        scfmemvar.set("")

def scfresult() :
    global scfvalue, scfeval, scftrigcheck, scfanscheck
    if scftrigcheck == 1:
        scfeval = scfeval + ")"
    x = eval(scfeval)
    scftempdispval.set(scfvalue)
    scfvalue = str(x)
    if scfvalue[len(scfvalue)-1] == '0' :
        scfvalue = scfvalue[:len(scfvalue)-2]
    scfdispval.set(scfvalue)
    scfanscheck = 1

# Functions for settings page

def set_go_back() :
    global var
    var.set(last_frame)
    option_changed()

def visit_github() :
    webbrowser.open("https://github.com/korathbasil/PyCalc")

## General elements for all mode ##
##===============================##

topfrm = Frame(window, height = 40, width = 350, background = color_header_bg[color_theme])
topfrm.pack()
var = StringVar()
var.set("Standard")
var.trace('w',option_changed)
switcher = OptionMenu(topfrm, var, "Standard", "Scientific", "Settings")
switcher.place(x = 7, y = 7)
switcher.configure(bg = color_header_bg[color_theme], fg = color_text[color_theme], highlightthickness = 0, bd = 0, activebackground = color_header_bg[color_theme], font = f3, width = 8)

stdfrm = Frame(window, height = 510, width = 350, bg = color_bg[color_theme])
scffrm = Frame(window, height = 510, width = 350, bg = color_bg[color_theme])
setfrm = Frame(window, height = 550, width = 350, bg = color_bg[color_theme])
set_top_frame = Frame(setfrm, height = 40, width = 350, bg = color_header_bg[color_theme])
set_bottom_frame = Frame(setfrm, height = 510, width = 350, bg = color_bg[color_theme])

## Elements for standard calculator ##
##==================================##

oper = Label(stdfrm, textvariable = dispoper, bg = color_bg[color_theme], fg = color_text[color_theme], font = f2)
oper.place(x = 320, y = 10)
display = Label(stdfrm, textvariable = dispval, bd = 0, bg = color_bg[color_theme], anchor = 'e', fg = color_text[color_theme], justify = RIGHT, font = f1)
display.place(x = 3, y = 75, width =340, height = 50)
stdmemdisp = Label(scffrm, textvariable = scfmemvar, bg = color_bg[color_theme], fg = color_text[color_theme], font = f2 )
stdmemdisp.place(x = 10, y = 10, height = 30, width = 30)

stdbtMC = Button(stdfrm, text = "MC", bg = color_bg[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_bg[color_theme], activebackground = color_bg[color_theme], font = f3, command = lambda : stdcheckmem(1))
stdbtMC.place(x = 39, y = 165, height = 63, width = 63)
stdbtMRC = Button(stdfrm, text = "MRC", bg = color_bg[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_bg[color_theme], activebackground = color_bg[color_theme], font = f3, command = lambda : stdcheckmem(2))
stdbtMRC.place(x = 108, y = 165, height = 63, width = 63)
stdbtMadd = Button(stdfrm, text = "M+", bg = color_bg[color_theme], fg = color_text[color_theme],bd = 0, highlightbackground = color_bg[color_theme], activebackground = color_bg[color_theme], font = f3, command = lambda : stdcheckmem(3))
stdbtMadd.place(x = 177, y = 165, height = 63, width = 63)
stdbtMsub = Button(stdfrm, text = "M-", bg = color_bg[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_bg[color_theme], activebackground = color_bg[color_theme], font = f3, command = lambda : stdcheckmem(4))
stdbtMsub.place(x = 246, y = 165, height = 63, width = 63)


bt7 = Button(stdfrm, text = "7", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("7"))
bt7.place(x = 3, y = 231, width = 66, height = 66)
bt8 = Button(stdfrm, text = "8", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("8"))
bt8.place(x = 72, y = 231, width = 66, height = 66)
bt9 = Button(stdfrm, text = "9", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("9"))
bt9.place(x = 141, y = 231, width = 66, height = 66)
bt4 = Button(stdfrm, text = "4", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("4"))
bt4.place(x = 3, y = 300, width = 66, height = 66)
bt5 = Button(stdfrm, text = "5", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("5"))
bt5.place(x = 72, y = 300, width = 66, height = 66)
bt6 = Button(stdfrm, text = "6", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("6"))
bt6.place(x = 141, y = 300, width = 66, height = 66)
bt1 = Button(stdfrm, text = "1", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("1"))
bt1.place(x = 3, y = 369, width = 66, height = 66)
bt2 = Button(stdfrm, text = "2", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("2"))
bt2.place(x = 72, y = 369, width = 66, height = 66)
bt3 = Button(stdfrm, text = "3", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("3"))
bt3.place(x = 141, y = 369, width = 66, height = 66)
btDot = Button(stdfrm, text = ".", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda :add_disp("."))
btDot.place(x = 3, y = 438, width = 66, height = 66)
bt0 = Button(stdfrm, text = "0", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda :add_disp("0"))
bt0.place(x = 72, y = 438, width = 66, height = 66)
btPerc = Button(stdfrm, text = "%", font = f2, bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : do_perc())
btPerc.place(x = 141, y = 438, width = 66, height = 66)

btDel = Button(stdfrm, text = "C", font = f2, bg = color_btlevel4[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : rm_disp())
btDel.place(x = 210, y = 231, width = 66, height = 66)
btCLR = Button(stdfrm, text = "AC", font = f2, bg = color_btlevel1[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel1[color_theme], activebackground = color_btlevel1[color_theme], command = lambda : clrscr())
btCLR.place(x = 279, y = 231, width = 66, height = 66)
btMul = Button(stdfrm, text = "*", font = f2, bg = color_btlevel4[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : operation(3))
btMul.place(x = 210, y = 300, width = 66, height = 66)
btDiv = Button(stdfrm, text = "÷", font = f2, bg = color_btlevel4[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : operation(4))
btDiv.place(x = 279, y = 300, width = 66, height = 66)
btAdd = Button(stdfrm, text = "+", font = f2, bg = color_btlevel4[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : operation(1))
btAdd.place(x = 210, y = 369, width = 66, height = 66)
btSub = Button(stdfrm, text = "-", font = f2, bg = color_btlevel4[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : operation(2))
btSub.place(x = 279, y = 369, width = 66, height = 66)
btEq = Button(stdfrm, text = "=", font = f2, bg = color_btlevel2[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel2[color_theme], activebackground = color_btlevel2[color_theme], command = lambda : result(1))
btEq.place(x = 210, y = 438, width = 135, height = 66)

## Elements for Scientic calculator ##
##==================================##

scfdisplay1 = Label(scffrm, textvariable = scfdispval, bg = color_bg[color_theme], fg = color_text[color_theme], anchor = 'e', justify = RIGHT, font = f4)
scfdisplay1.place(x = 5, y = 40, height = 60, width = 340)
scfdisplay2 = Label(scffrm, textvariable = scftempdispval, bg = color_bg[color_theme], fg = color_text[color_theme], anchor = 'e', justify = RIGHT, font = f3)
scfdisplay2.place(x = 5, y = 0, height = 40, width = 340)

scfmemdisp = Label(stdfrm, textvariable = stdmemvar, bg = color_bg[color_theme], fg = color_text[color_theme], font = f2 )
scfmemdisp.place(x = 10, y = 10, height = 30, width = 30)

scfbtsin = Button(scffrm, text = "sin", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_trig(1))
scfbtsin.place(x = 5, y = 105, height = 55, width = 55)
scfbtcos = Button(scffrm, text = "cos", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_trig(2))
scfbtcos.place(x = 5, y = 162, height = 55, width = 55)
scfbttan = Button(scffrm, text = "tan", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_trig(3))
scfbttan.place(x = 5, y = 219, height = 55, width = 55)
scfbtcsc = Button(scffrm, text = "csc", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_trig(4))
scfbtcsc.place(x = 62, y = 105, height = 55, width = 55)
scfbtsec = Button(scffrm, text = "sec", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_trig(5))
scfbtsec.place(x = 62, y = 162, height = 55, width = 55)
scfbtcot = Button(scffrm, text = "cot", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_trig(6))
scfbtcot.place(x = 62, y = 219, height = 55, width = 55)

scfMC = Button(scffrm, text = "MC", bd = 0, bg = color_btlevel6[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme], command = lambda : scfcheckmem(1))
scfMC.place(x = 119, y = 162, height = 55, width = 55)
scfDel = Button(scffrm, text = "DEL", bd = 0, bg = color_btlevel6[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme], command = lambda : scfrm_disp())
scfDel.place(x = 233, y = 105, height = 55, width = 55)
scfClr = Button(scffrm, text = "AC", bg = color_btlevel1[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel1[color_theme], activebackground = color_btlevel1[color_theme], bd = 0, font = f2, command = lambda : scfclrscr())
scfClr.place(x = 290, y = 105, height = 55, width = 55)
scfMRC = Button(scffrm, text = "MRC", bd = 0, bg = color_btlevel6[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme], command = lambda : scfcheckmem(2))
scfMRC.place(x = 176, y = 162, height = 55, width = 55)
scfMadd = Button(scffrm, text = "M+", bd = 0, bg = color_btlevel6[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme], command = lambda : scfcheckmem(3))
scfMadd.place(x = 233, y = 162, height = 55, width = 55)
scfMsub = Button(scffrm, text = "M-", bd = 0, bg = color_btlevel6[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme], command = lambda : scfcheckmem(4))
scfMsub.place(x = 290, y = 162, height = 55, width = 55)
scfbtlb = Button(scffrm, text = "(", bd = 0, bg = color_btlevel6[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme], command = lambda :add_scfdisp("("))
scfbtlb.place(x = 119, y = 105, height = 55, width = 55)
scfbtrb = Button(scffrm, text = ")", bd = 0, bg = color_btlevel6[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel6[color_theme], activebackground = color_btlevel6[color_theme], command = lambda :add_scfdisp(")"))
scfbtrb.place(x = 176, y = 105, height = 55, width = 55)

scfbt7 = Button(scffrm, text = "7", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("7"))
scfbt7.place(x = 5, y = 276, height = 55, width = 55)
scfbt8 = Button(scffrm, text = "8", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("8"))
scfbt8.place(x = 62, y = 276, height = 55, width = 55)
scfbt9 = Button(scffrm, text = "9", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("9"))
scfbt9.place(x = 119, y = 276, height = 55, width = 55)
scfbt4 = Button(scffrm, text = "4", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("4"))
scfbt4.place(x = 5, y = 333, height = 55, width = 55)
scfbt5 = Button(scffrm, text = "5", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("5"))
scfbt5.place(x = 62, y = 333, height = 55, width = 55)
scfbt6 = Button(scffrm, text = "6", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("6"))
scfbt6.place(x = 119, y = 333, height = 55, width = 55)
scfbt1 = Button(scffrm, text = "1", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("1"))
scfbt1.place(x = 5, y = 390, height = 55, width = 55)
scfbt2 = Button(scffrm, text = "2", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("2"))
scfbt2.place(x = 62, y = 390, height = 55, width = 55)
scfbt3 = Button(scffrm, text = "3", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("3"))
scfbt3.place(x = 119, y = 390, height = 55, width = 55)
scfbt0 = Button(scffrm, text = "0", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("0"))
scfbt0.place(x = 5, y = 447, height = 55, width = 55)
scfbt00 = Button(scffrm, text = "00", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("00"))
scfbt00.place(x = 62, y = 447, height = 55, width = 55)
scfbtDot = Button(scffrm, text = ".", bg = color_btlevel3[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], font = f2, activebackground = color_btlevel3[color_theme], command = lambda :add_scfdisp("."))
scfbtDot.place(x = 119, y = 447, height = 55, width = 55)


scfbtrot = Button(scffrm, text = "√x", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_power(1))
scfbtrot.place(x = 119, y = 219, height = 55, width = 55)
scfbtxy = Button(scffrm, text = "xy", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_power(2))
scfbtxy.place(x = 176, y = 219, height = 55, width = 55)
scfbtx10 = Button(scffrm, text = "x10", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_power(3))
scfbtx10.place(x = 233, y = 219, height = 55, width = 55)
scfbtPi = Button(scffrm, text = "π", bd = 0, bg = color_btlevel5[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel5[color_theme], activebackground = color_btlevel5[color_theme], command = lambda : scfdo_extrafn(1))
scfbtPi.place(x = 290, y = 219, height = 55, width = 55)

scfbtx3 = Button(scffrm, text = "x³", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : scfdo_power(4))
scfbtx3.place(x = 176, y = 276, height = 55, width = 55)
scfbt1x = Button(scffrm, text = "¹⁄x", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : scfdo_extrafn(2))
scfbt1x.place(x = 233, y = 276, height = 55, width = 55)
scfbtNF = Button(scffrm, text = "x !", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : scfdo_extrafn(3))
scfbtNF.place(x = 290, y = 276, height = 55, width = 55)
scfbtx2 = Button(scffrm, text = "x²", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : scfdo_power(5))
scfbtx2.place(x = 176, y = 333, height = 55, width = 55)
scfbtPerc = Button(scffrm, text = "%", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : scfdo_perc())
scfbtPerc.place(x = 176, y = 390, height = 55, width = 55)
scfbtSign = Button(scffrm, text = "+/-", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], command = lambda : scfdo_extrafn(4))
scfbtSign.place(x = 176, y = 447, height = 55, width = 55)

scfbtMul = Button(scffrm, text = "*", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], font = f2, command = lambda : scfdo_oper("*"))
scfbtMul.place(x = 233, y = 333, height = 55, width = 55)
scfbtDiv = Button(scffrm, text = "/", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], font = f2, command = lambda : scfdo_oper("/"))
scfbtDiv.place(x = 290, y = 333, height = 55, width = 55)
scfbtAdd = Button(scffrm, text = "+", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], font = f2, command = lambda : scfdo_oper("+"))
scfbtAdd.place(x = 233, y = 390, height = 55, width = 55)
scfbtSub = Button(scffrm, text = "-", bd = 0, bg = color_btlevel4[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel4[color_theme], activebackground = color_btlevel4[color_theme], font = f2, command = lambda : scfdo_oper("-"))
scfbtSub.place(x = 290, y = 390, height = 55, width = 55)
scfbtEq = Button(scffrm, text = "=", bg = color_btlevel2[color_theme], fg = color_text[color_theme], highlightbackground = color_btlevel2[color_theme], activebackground = color_btlevel2[color_theme], bd = 0, font = f2, command = lambda : scfresult())
scfbtEq.place(x = 233, y = 447, height = 55, width = 112)


# Elements in settings page


set_back_button = Button(setfrm, image = arrow_color[color_theme], bg = color_header_bg[color_theme], highlightbackground = color_header_bg[color_theme], activebackground = color_header_bg[color_theme], bd = 0, command = set_go_back)
set_back_button.place(x = 6, y = 11)
set_header = Label(setfrm, text = "Settings", bg = color_header_bg[color_theme], fg = color_text[color_theme], highlightbackground = color_header_bg[color_theme], font = f3)
set_header.place(x = 35, y =9)
theme  = Label(setfrm, text = "Themes", font = f5, bg = color_bg[color_theme], fg = color_text[color_theme], highlightbackground = color_bg[color_theme])
theme.place(x = 25, y = 75)
light_theme = Label(setfrm, image = light_theme_img, bg = color_bg[color_theme])
light_theme.place(x = 55, y = 125, height = 150, width = 100)
dark_theme = Label(setfrm, image = dark_theme_img, bg = color_bg[color_theme])
dark_theme.place(x = 195, y = 125, height = 150, width = 100)
light_theme_button = Radiobutton(setfrm, text = "Light", variable = theme_variable, value = 1, bg = color_bg[color_theme], fg = color_text[color_theme], highlightbackground = color_bg[color_theme]) 
light_theme_button.place(x = 70, y = 285)
dark_theme_button = Radiobutton(setfrm, text = "Dark", variable = theme_variable, value = 0, bg = color_bg[color_theme], fg = color_text[color_theme], highlightbackground = color_bg[color_theme]) 
dark_theme_button.place(x = 210, y = 285)
apply_button = Button(setfrm, text = "Apply", relief = GROOVE, bg = color_header_bg[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_header_bg[color_theme], activebackground = color_header_bg[color_theme], command = color_changed, font = f5)
apply_button.place(x = 250, y = 325)

about_text = Label(setfrm, text = "About", font = f5, bg = color_bg[color_theme], fg = color_text[color_theme], highlightbackground = color_bg[color_theme])
about_text.place(x = 25, y = 375)
creator_text = Label(setfrm, text = "Creator : Bazil Korath", bg = color_bg[color_theme], fg = color_text[color_theme], highlightbackground = color_bg[color_theme])
creator_text.place(x = 55, y = 410)
github_text = Label(setfrm, text = "Visit Github repository  ", bg = color_bg[color_theme], fg = color_text[color_theme], highlightbackground = color_bg[color_theme])
github_text.place(x = 55, y = 430)
github_button = Button(setfrm, image = github_image[color_theme], bd = 0, highlightbackground = color_bg[color_theme], activebackground = color_bg[color_theme], bg = color_bg[color_theme], fg = color_text[color_theme], command = visit_github)
github_button.place(x = 190, y = 410)

# Grouping elements  with same color changes so  changing them all at once is easy

color_main =  light_theme_button, dark_theme_button, set_bottom_frame,theme, stdfrm, scffrm, setfrm, oper, display, stdmemdisp, stdbtMC, stdbtMRC, stdbtMadd, stdbtMsub, scfdisplay1, scfdisplay2
color_main2 = light_theme_button, dark_theme_button, stdmemdisp, stdbtMC, stdbtMRC, stdbtMadd, stdbtMsub
color_main3 = set_top_frame, topfrm
color_level1 = btCLR, scfClr
color_level2 = btEq, scfbtEq
color_level3 = bt7, bt8, bt9, bt4, bt5, bt6, bt1, bt2, bt3, btDot, bt0, btPerc, scfbt7, scfbt8, scfbt9, scfbt4, scfbt5, scfbt6, scfbt1, scfbt2, scfbt3, scfbt0, scfbt00, scfbtDot
color_level4 = btDel, btAdd, btSub, btMul, btDiv, scfbtAdd, scfbtSub, scfbtDiv, scfbtMul, scfbtx3, scfbtx2, scfbt1x, scfbtNF, scfbtSign, scfbtPerc
color_level5 = scfbtsin, scfbtcos, scfbttan, scfbtcsc, scfbtsec, scfbtcot, scfbtrot, scfbtx10, scfbtx10, scfbtxy, scfbtPi
color_level6 = scfbtlb, scfbtrb, scfMC, scfMRC, scfMadd, scfMsub, scfDel
color_text_group = switcher, oper, display, stdmemdisp, stdbtMC, stdbtMRC, stdbtMadd, stdbtMsub, scfdisplay1, scfdisplay2, btCLR, scfClr, btEq, scfbtEq, bt7, bt8, bt9, bt4, bt5, bt6, bt1, bt2, bt3, btDot, bt0, btPerc, scfbt7, scfbt8, scfbt9, scfbt4, scfbt5, scfbt6, scfbt1, scfbt2, scfbt3, scfbt0, scfbt00, scfbtDot, btDel, btAdd, btSub, btMul, btDiv, scfbtAdd, scfbtSub, scfbtDiv, scfbtMul, scfbtx3, scfbtx2, scfbt1x, scfbtNF, scfbtSign, scfbtPerc, scfbtlb, scfbtrb, scfMC, scfMRC, scfMadd, scfMsub, scfDel, scfbtsin, scfbtcos, scfbttan, scfbtcsc, scfbtsec, scfbtcot, scfbtrot, scfbtx10, scfbtx10, scfbtxy, scfbtPi


option_changed()
window.mainloop()
