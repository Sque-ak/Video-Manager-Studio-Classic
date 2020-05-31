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

        self.urlListCam = {
        'Camera_0': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov',
        'Camera_1': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov'} 

        self.cameras = []

        #Make grid of windows;
        self.canvas = [i for i in range(len(self.urlListCam))]
        for i in range(len(self.urlListCam)):
            self.cameras.append(videocam.VideoCamera(self.urlListCam['Camera_' + str(i)])) #Add all cameras on list.
            self.canvas[i] = tkinter.Canvas(window, width = const.SIZE_VIEWCAM, height = const.SIZE_VIEWCAM, bg=const.SECONDCOLOR, highlightthickness=0)
            #self.canvas[i].grid(row = i//4, column = i%4)
            self.canvas[i].place(x = (const.SIZE_VIEWCAM+5)*(i%4), y = (const.SIZE_VIEWCAM+5)*(i//4)) 
            print("№" + str(i) + ": Done")


        self.nodeToolBar()
        self.nodeStatusBar()

        self.delay = 15
        self.updateStream()
        self.window.mainloop()


    #Rpeater frame;
    def updateStream(self):
        #Update frame of cameras.
        self.stream = [i for i in range(len(self.urlListCam))]
        for i in range(len(self.urlListCam)):
            self.stream[i] = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(self.cameras[i].getFrame()))
            self.canvas[i].create_image(0, 0, image = self.stream[i], anchor = tkinter.NW)
        
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
  