# Coded by Sami Elsayed

import tkinter as tk
import tkinter.ttk as ttk

# the drawing app
class Drawing(tk.Tk):

    # The constructor, when you open the app for the first time
    def __init__(self):
        super().__init__()
        self.title("The Simple Python Drawing App") # The title of the app
        self.xold = None
        self.yold = None
        self.canvas = None
        self.color = "Black" # The inital color
        self.thickness = 1 # The inital color
        self.tag = ["tag", "0"]
        self.create_widgets()
    
    # The four options on the top of the app: Color, Thickness, Undo, and Clear.
    def create_widgets(self):
        topframe = tk.Frame(self)
        topframe.grid(row = 0, column = 0, pady = 10)

        # Change color widget
        self.col_select = tk.StringVar()
        colorList = ttk.Combobox(topframe, textvariable = self.col_select, value = ['Black', 'Green', 'Brown', 'Red', 'Yellow'], state = "readonly", width = 10) # The list of colors from the dropdown
        colorList.current(0)
        self.option_add('*TCombobox*Listbox.selectBackground', 'skyblue')
        colorList.bind('<<ComboboxSelected>>', self.change_color)
        colorList.grid(row = 0, column = 0, padx = 5)

        # The thickness widget
        self.t_select = tk.StringVar()
        tList = ttk.Combobox(topframe, textvariable = self.t_select, values = [1, 2, 3, 4, 5, 6, 7], state = "readonly", width = 3) # The list of thicknesses from the dropdown
        tList.current(0)
        tList.bind('<<ComboboxSelected>>', self.change_thickness)
        tList.grid(row = 0, column = 1, padx = 5)

        # The Undo widget
        tk.Button(topframe, text = "Undo", bg = "blue", fg = "white", activebackground = "blue4", activeforeground = "white", command = self.undo).grid(row = 0, column = 2, padx = 5)
        tk.Button(topframe, text = "Clear", bg = "brown", fg = "white", activebackground = "brown4", activeforeground = "white", command = self.clear).grid(row = 0, column = 3, padx = 5) # Undoing every color

        self.canvas = tk.Canvas(self, width = 500, height = 500, bg = "white")
        self.canvas.grid(row = 1, column = 0, padx = 10, pady = (0, 10))
        self.canvas.bind('<ButtonRelease-1>', self.on_release)
        self.canvas.bind('<B1-Motion>', self.on_movement)
    
    # To make sure that the color changes, we need this function for it to actually change!
    def change_color(self, event = None):
        self.color = self.col_select.get()
    
    # To make sure that the thickness changes, we need this function for it to actually change!
    def change_thickness(self, event = None):
        self.thickness = int(self.t_select.get())
    
    # The undo function that undos the last change you did
    def undo(self):
        current_tag = int(self.tag[1])
        if current_tag >= 1:
            self.canvas.delete("tag" + str(current_tag - 1))
            self.tag = ['tag', str(current_tag - 1)]
    
    # The clear function that clears all of the colors on the canvas
    def clear(self):
        self.canvas.delete("all")
        self.tag = ['tag', '0']
    
    # How you can draw when you can drag the drawerer??
    def on_movement(self, event):
        tag = "".join(self.tag)
        x_one, y_one = (event.x - self.thickness), (event.y - self.thickness)
        x_two, y_two = (event.x + self.thickness), (event.y + self.thickness)
        event.widget.create_oval(x_one, y_one, x_two, y_two, width = 0, fill = self.color, tag = tag)
        if self.xold is not None and self.yold is not None:
            self.canvas.create_oval(x_one, y_one, x_two, y_two, width = 0, fill = self.color, tag = tag)
            self.canvas.create_line(self.xold, self.yold, event.x, event.y, smooth = True, width = 2 * self.thickness, fill = self.color, tag = tag)
        
        self.xold = event.x
        self.yold = event.y
    
    # Once you release your click
    def on_release(self, event):
        self.xold = None
        self.yold = None
        self.tag = ['tag', str(int(self.tag[1]) + 1)]

Drawing().mainloop()