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

        self.window.minsize(width = const.SCREEN_W, height=const.SCREEN_H)
        self.window.config(bg=const.FIRSTCOLOR)
        self.window.wm_state('zoomed')

        self.cameras = []
  
        self.imgNovid = PIL.ImageTk.PhotoImage(PIL.Image.open(f"src/img/novid_{const.SIZE_VIEWCAM}.jpg"))

        self.canvas = tkinter.Canvas(window, 
            width = (const.SIZE_VIEWCAM)*(const.MAXCAMERAS//4), 
            height = (const.SIZE_VIEWCAM)*(const.MAXCAMERAS//4), 
            bg=const.SECONDCOLOR, highlightthickness=0)
        self.canvas.place(relx = 1, rely = 0, anchor = tkinter.NE) 

        #Node init;
        self.nodeInspector()
        self.nodeToolBar()
        self.nodeStatusbar()
        self.nodeNovid()
        #end;
        self.onInitDevice()
        self.window.mainloop()

    "Section Node Begin;"
    # Area without cameras;
    def nodeNovid(self):
        for i in range(const.MAXCAMERAS):
            self.canvas.create_image((const.SIZE_VIEWCAM+5)*(i%4), (const.SIZE_VIEWCAM+5)*(i//4), image = self.imgNovid, anchor = tkinter.NW)

    #Inspector of cameras;
    def nodeInspector(self):
        pass
        
    #Status and footer;
    def nodeStatusbar(self):
        self.footer = tkinter.Canvas(self.window, height = 16, bg=const.THREECOLOR, highlightthickness = 0)
        self.footer.place(rely = .98, relwidth = 1)

        self.status = tkinter.Label(text = "Good")
        self.status.place(rely = .97, relx = .01)
        
    #Toolbar;
    def nodeToolBar(self):
        #Toolbar create:
        self.toolbar = tkinter.Menu(self.window)
        self.window.config(menu=self.toolbar)
        
        #Toolbar items:
        #   1. Actions -> (Start Stream)(Exit);
        #

        self.actionItems = tkinter.Menu(self.toolbar)
        self.actionItems.add_command(label="Start Stream", command=lambda: self.updDevice())
        self.actionItems.add_command(label="Exit", command=self.onExit)
        self.toolbar.add_cascade(label="Actions", menu=self.actionItems)
    "Section Node End;"

    #This is function for exit;
    def onExit(self):
        self.window.quit()

    #Init all cam-device and start on screen;
    def onInitDevice(self):
        for i in range(len(const.LISTCAM)):
            self.cameras.append(videocam.VideoCamera(const.LISTCAM[f'Camera_{i}'], self.canvas)) #Add all cameras on list;
            self.status.config(text = f"{i+1} Device(s): Done") #Range begin with 0, so plus 1;
            print(f"№{i}: Done")

    def updDevice(self):
        for i in range(len(const.LISTCAM)):
            self.cameras[i].updFrame(i,i, self.window)

        self.actionItems.entryconfig(1, state=tkinter.DISABLED) #Turn off the button so that the user doesn’t call the thread again;
        self.status.config(text = f"{len(const.LISTCAM)} Device(s): Started")

        
    