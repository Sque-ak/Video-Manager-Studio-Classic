#!/usr/bin/env python3

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import const

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

        self.window.config(bg=const.FIRSTCOLOR)
        self.window.wm_state('zoomed')

        #Make a window grid;
        self.testcamera = VideoCamera("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov")
        self.canvas = tkinter.Canvas(window, width = 200, height = 200)
        self.canvas.pack(expand=True)

        self.delay = 20
        self.update()

        self.window.mainloop()

    #Rpeater frame;
    def update(self):
        ret, frame = self.testcamera.get_frame()

        if ret:
            self.picter = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.picter, anchor = tkinter.NW)
            
        self.window.after(self.delay, self.update)


"""
Make a videocamera;

@param {String} url : RTSP url;
@return {Object};
@example VideoCamera("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov");
"""
class VideoCamera:
    def __init__(self, url = 0):
        self.urlCam = cv2.VideoCapture(url)
        if not self.urlCam.isOpened():
           raise ValueError("URL rtsp is wrong!", url)
        self.width = self.urlCam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.urlCam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        

    #Destroy the camera; 
    def __del__(self):
        if self.urlCam.isOpened():
            self.urlCam.release()

    #Get frame with camera;
    #@return {{Boolean}ret, {array}frame}
    def get_frame(self):
        if self.urlCam.isOpened():
            ret, frame = self.urlCam.read()
            frame = cv2.resize(frame,(200,200))
            #Convert to BGR if is true.
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

if __name__ == "__main__":
    VMS(tkinter.Tk(), const.NAMEAPP + " " + const.VERSION, '800x600')