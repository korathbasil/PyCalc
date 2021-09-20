from tkinter import Button

from config import fonts
from config import colors



class TypeOne (Button):
    def __init__(self, frame,text, placement_x, placement_y, command, color_theme_id):
        
        super(frame, text = text, font = fonts.size_20, bg = colors.button_type_1[color_theme_id], activeforeground = colors.text[color_theme_id], fg = colors.text[color_theme_id], bd = 0, highlightbackground = colors.button_type_1[color_theme_id], activebackground = colors.button_type_1[color_theme_id], command = lambda : add_disp(text))

        self.place(x = placement_x, y = placement_y, width = 66, height = 66)
