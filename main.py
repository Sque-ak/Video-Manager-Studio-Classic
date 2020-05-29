#!/usr/bin/env python3

import tkinter as tk
import const

class Main(tk.Frame):
    def __init__(self, canvas):
        super().__init__(canvas)

        self.nodeInit()

    def nodeInit(self):
        #Toolbar create:
        toolbar = tk.Menu(self.master)
        self.master.config(menu=toolbar)
        
        #Toolbar items:
        #   1. File -> (Exit)
        #

        fileItem = tk.Menu(toolbar)
        fileItem.add_command(label="Exit", command=self.onExit)
        toolbar.add_cascade(label="File", menu=fileItem)

    def onExit(self):
        self.quit()

def main():
    #Config Main Window
    canvas = tk.Tk()
    canvas.wm_state('zoomed')
    canvas.geometry('800x600')
    canvas.config(bg="#252525")
    canvas.title(const.NAMEAPP + " " + const.VERSION)

    app = Main(canvas)
    app.pack()
    canvas.mainloop()

if __name__ == "__main__":
    main()