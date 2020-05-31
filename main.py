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

        self.urlListCam = {
        'Camera_0': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov',
        'Camera_1': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov',
        'Camera_2': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov',
        'Camera_3': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov',
        'Camera_4': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov',
        'Camera_5': 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov'}

        self.cameras = []

        #Make grid of windows;
        self.canvas = [i for i in range(len(self.urlListCam))]
        for i in range(len(self.urlListCam)):
            self.cameras.append(VideoCamera(self.urlListCam['Camera_' + str(i)])) #Add all cameras on list.
            self.canvas[i] = tkinter.Canvas(window, width = 200, height = 200, bg=const.SECONDCOLOR, highlightthickness=0)
            self.canvas[i].grid(row = i//4, column = i%4)


        self.delay = 15
        self.update_stream()
        self.window.mainloop()

    #Rpeater frame;
    def update_stream(self):
        #Update frame of cameras.
        self.stream = [i for i in range(len(self.urlListCam))]
        for i in range(len(self.urlListCam)):
            self.stream[i] = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(self.cameras[i].get_frame()))
            self.canvas[i].create_image(0, 0, image = self.stream[i], anchor = tkinter.NW)
        
        self.window.after(self.delay, func=lambda: self.update_stream())
  
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
        
    def get_url(self):
        return self.urlCam

    #Destroy the camera;
    def __del__(self):
        if self.urlCam.isOpened():
            self.urlCam.release()

    #Get frame with camera;
    #@return {{Boolean}ret, {array}frame};
    def get_frame(self):
        ret, frame = self.urlCam.read()
        frame = cv2.resize(frame,(200,200))
        #Convert to BGR;
        return (cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


if __name__ == "__main__":
    VMS(tkinter.Tk(), const.NAMEAPP + " " + const.VERSION, '800x600')