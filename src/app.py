#!/usr/bin/env python3

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import const
import videocam

"""
Main class, make a global window;

@param {Object} window : Main window;
@param {String} title : Name the app;
@param {Vector2x} geometry  : Window size after minimizing;
@return {Object} I guess this is object;
@example VMS(tkinter.Tk(), "Video Manager Studio Classic 0.1", '800x600');
"""
class VMS:
    def __init__(self, window, title, geometry):
        #Parameters;
        self.window = window
        self.window.title(title)
        self.window.geometry(geometry)

        self.window.minsize(width = 1200, height=800)
        self.window.config(bg=const.FIRSTCOLOR)
        self.window.wm_state('zoomed')

        self.cameras = []

        #Loading img part:
        self.imgNovid = PIL.ImageTk.PhotoImage(PIL.Image.open("src/img/novid_" + str(const.SIZE_VIEWCAM) + ".jpg"))
        #end;

        #Make grid of windows but canvas alone;
        for i in range(len(const.LISTCAM)):
            self.cameras.append(videocam.VideoCamera(const.LISTCAM['Camera_' + str(i)])) #Add all cameras on list.

            self.canvas = tkinter.Canvas(window, 
                width = (const.SIZE_VIEWCAM)*(const.MAXCAMERAS//4), 
                height = (const.SIZE_VIEWCAM)*(const.MAXCAMERAS//4), 
                bg=const.SECONDCOLOR, highlightthickness=0)
                
            self.canvas.place(relx = 1, rely = 0, anchor = tkinter.NE) 
            print("№" + str(i) + ": Done")

        self.nodeToolBar()
        self.nodeStatusBar()
        self.nodeNovid()

        self.delay = 15
        self.updateStream()
        self.window.mainloop()

    # Area without cameras;
    def nodeNovid(self):
        for i in range(const.MAXCAMERAS):
            self.canvas.create_image((const.SIZE_VIEWCAM+5)*(i%4), 
                (const.SIZE_VIEWCAM+5)*(i//4), 
                image = self.imgNovid, anchor = tkinter.NW)


    #Rpeater frame;
    def updateStream(self):
        #Update frame of cameras.
        self.stream = [i for i in range(len(const.LISTCAM))]
        for i in range(len(const.LISTCAM)):
            self.stream[i] = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(self.cameras[i].getFrame()))

            self.canvas.create_image((const.SIZE_VIEWCAM+5)*(i%4), 
                (const.SIZE_VIEWCAM+5)*(i//4), 
                image = self.stream[i], anchor = tkinter.NW)
        
        self.window.after(self.delay, func=lambda: self.updateStream())

    #Inspector of cameras;
    def nodeInspector(self):
        pass

    #Status bar;
    def nodeStatusBar(self):
        self.statusbar = tkinter.Canvas(self.window, height = 16, bg=const.THREECOLOR, highlightthickness = 0)
        self.statusbar.place(rely = .98, relwidth = 1)

        self.status = tkinter.Label(text = const.STATUSAPP)
        self.status.place(rely = .97, relx = .01)

    #Toolbar;
    def nodeToolBar(self):
        #Toolbar create:
        toolbar = tkinter.Menu(self.window)
        self.window.config(menu=toolbar)
        
        #Toolbar items:
        #   1. File -> (Exit);
        #

        fileItem = tkinter.Menu(toolbar)
        fileItem.add_command(label="Exit", command=self.onExit)
        toolbar.add_cascade(label="File", menu=fileItem)

    #This is function for exit;
    def onExit(self):
        self.window.quit()
  