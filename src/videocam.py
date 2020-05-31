#!/usr/bin/env python3
import cv2
import const

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
    #@return {{Boolean}ret, {array}frame};
    def getFrame(self):
        ret, frame = self.urlCam.read()
        frame = cv2.resize(frame,(const.SIZE_VIEWCAM, const.SIZE_VIEWCAM))
        #Convert to BGR;
        return (cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
