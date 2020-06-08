#!/usr/bin/env python3

import tkinter
import tkinter.ttk
import cv2
import PIL.Image, PIL.ImageTk
import const
import videocam

class VMS:
    """
    Main class, make a global window;
    @param {Object} window : Main window;
    @param {String} title : Name the app;
    @param {Vector2x} geometry  : Window size after minimizing;
    @return {Object} I guess this is object;
    @example VMS(tkinter.Tk(), "Video Manager Studio Classic 0.1", '800x600');
    """
    def __init__(self, window, title):
        #Parameters;
        self._window = window
        self._window.title(title)
        self._window.geometry("")
        self._window.iconbitmap('icon.ico')

        self._window.minsize(width = const.SCREEN_W, height=const.SCREEN_H)
        self._window.config(bg=const.FIRSTCOLOR)
        self._window.wm_state('zoomed')

        self._cameras = []
  
        self._imgNovid = PIL.ImageTk.PhotoImage(PIL.Image.open(f"src/img/novid_{const.SIZE_VIEWCAM_X}x{const.SIZE_VIEWCAM_Y}.jpg"))

        self.nodeStatusbar()

        self._canvas = tkinter.Canvas(window, 
            width = (const.SIZE_VIEWCAM_X)*(const.MAXCAMERAS//4), 
            height = (const.SIZE_VIEWCAM_Y)*(const.MAXCAMERAS//4), 
            bg=const.FIRSTCOLOR, highlightthickness=0)
        self._canvas.pack(side = "right", fill = "y", padx = 5)

        #Node init;
        self.onInitDevice()

        self.nodeInspector()
        self.nodeToolBar()
        self.nodeNovid()
        #end;
 
        self._window.mainloop()

    "Section Node Begin;"
    def nodeNovid(self):
        # Area without cameras;
        for i in range(const.MAXCAMERAS):
            self._canvas.create_image((const.SIZE_VIEWCAM_X+5)*(i%4), (const.SIZE_VIEWCAM_Y+5)*(i//4), image = self._imgNovid, anchor = tkinter.NW)

    def nodeInspector(self):
        #Inspector of cameras;
        self._styleInspector = tkinter.ttk.Style()
        self._styleInspector.configure("Inspector.Treeview.Heading", font=('Arial', 10,'bold')) # Modify the font of the headings
        self._styleInspector.layout("Inspector.Treeview", [('Inspector.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        self._inspector = tkinter.ttk.Treeview(self._window, style="Inspector.Treeview")
        self._inspector["columns"] = ("Status")

        self._inspector.column("#0", width = 120)
        self._inspector.column("Status", width = 120)

        self._inspector.heading("#0", text = "Name", anchor = tkinter.NW)
        self._inspector.heading("Status", text = "Status", anchor = tkinter.NW)

        #Level - 1
        self._namepack = self._inspector.insert("", 1, text = "Pack", values = (""))
        for i in range(len(const.LISTCAM)):
            self._inspector.insert(self._namepack, "end", text = f"#{i+1} Camera", values = (self._cameras[i].getStatus()))

        self._inspector.pack(side = "left", fill = "y")

        
    def nodeStatusbar(self):
        #Status and footer;
        self._footer = tkinter.Frame(self._window, height = 16, bg=const.THREECOLOR, highlightthickness = 0)

        self._status = tkinter.Label(self._footer, text = "Good")
        self._status.pack(side = "right")
        self._footer.pack(side = "bottom", fill = "x", anchor = tkinter.SW)
        
    def nodeToolBar(self):
        #Toolbar create:
        self._toolbar = tkinter.Menu(self._window)
        self._window.config(menu=self._toolbar)
        
        #Toolbar items:
        #   1. Actions -> (Start Stream)(Exit);
        #

        self._actionItems = tkinter.Menu(self._toolbar)
        self._actionItems.add_command(label="Start Stream", command=lambda: self.updDevice())
        self._actionItems.add_command(label="Exit", command=self.onExit)
        self._toolbar.add_cascade(label="Actions", menu=self._actionItems)
    "Section Node End;"

    def onExit(self):
        #This is function for exit;
        self._window.quit()

    def onInitDevice(self):
        #Init all cam-device and start on screen;
        for i in range(len(const.LISTCAM)):
            self._cameras.append(videocam.VideoCamera(const.LISTCAM[f'Camera_{i}'], self._canvas)) #Add all cameras on list;
            self._status.config(text = f"{i+1} Device(s): Done") #Range begin with 0, so plus 1;
            print(f"№{i}: Done")

    def updDevice(self):
        #Update stream frame by camera;
        for i in range(len(const.LISTCAM)):
            self._cameras[i].updFrame(i,i, self._window)

        self._actionItems.entryconfig(1, state=tkinter.DISABLED) #Turn off the button so that the user doesn’t call the thread again;
        self._status.config(text = f"{len(const.LISTCAM)} Device(s): Started")

        
    