#!/usr/bin/env python3
import cv2
import const
import tkinter
import PIL.Image, PIL.ImageTk

class VideoCamera:
    """
    Make a videocamera;

    @param {String} url : RTSP url;
    @param {Object} canvas: Canvas for drawing the camera;
    @return {Object};
    @example VideoCamera("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov");
    """
    def __init__(self, url = 0, canvas = 0):
        self._canvas = canvas 
        self._urlCam = cv2.VideoCapture(url)
        if not self._urlCam.isOpened():
           raise ValueError("URL rtsp is wrong!", url)

        self.width = self._urlCam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self._urlCam.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        #Destroy the camera;
        if self._urlCam.isOpened():
            self._urlCam.release()

    def getFrame(self):
        #Get frame of the camera;
        #@return {{Boolean}ret, {array}frame};
        ret, frame = self._urlCam.read()
        frame = cv2.resize(frame,(const.SIZE_VIEWCAM, const.SIZE_VIEWCAM))
        #Convert to BGR;
        return (cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def updFrame(self, indX, indY, window):
        """
        Update frame of the camera;
        @param {integer} indX: index number by x;
        @param {integer} indY: index number by y;
        @param {object} window: main window for update;
        """
        self._stream = PIL.ImageTk.PhotoImage(PIL.Image.fromarray(self.getFrame()))
        self._canvas.create_image((const.SIZE_VIEWCAM+5)*(indX%4), (const.SIZE_VIEWCAM+5)*(indY//4), image = self._stream, anchor = tkinter.NW)
        window.after(const.DELAY, func=lambda: self.updFrame(indX, indY, window))