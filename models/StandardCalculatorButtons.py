from tkinter import Button

from config import colors


class TypeOne (Button):
    def __init__(self, text, placement_x, placement_y, command, color_theme_id):
        super(frame_standard, text = "7", font = f2, bg = color_btlevel3[color_theme], activeforeground = color_text[color_theme], fg = color_text[color_theme], bd = 0, highlightbackground = color_btlevel3[color_theme], activebackground = color_btlevel3[color_theme], command = lambda : add_disp("7"))
