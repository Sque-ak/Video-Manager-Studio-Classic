#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod
import const, cv2

class VidCamera():
    
    def __init__(self, empetyCamera: TypeVidCam) -> None:
        #init @param: {cam_epety} empetyCamera for add camera to the case; 
        self._empetyCamera = empetyCamera

    @property
    def empetyCamera(self) -> TypeVidCam:
        return self._empetyCamera 

    @empetyCamera.setter
    def empetyCamera(self, empetyCamera: TypeVidCam) -> None:
        # Change type the camera;
        self._empetyCamera = empetyCamera

    # Functions ...
    def createCamera(self, ip_port: str, username: str, password: str, typestream: int, channel: int) -> str:
        """ Options for the camera @param {str} id_port - this is adress the camera;
        {str} username and password - to the camera but you can use None if haven't;
        {int} typestream - if 0 then main stream else if 1 then sub stream;
        {int} channel... just channel; """
        self._empetyCamera.setStreamUrl(ip_port, username, password, typestream, channel)
    
    def createCamera(self, ip_port: str) -> str:
        """ Options for the camera @param {str} id_port - this is adress the camera; """
        self._empetyCamera.setStreamUrl(ip_port)

    def getStream(self) -> str:
        return self._empetyCamera.getStreamUrl()

    def getStatus(self) -> str:
        return self._empetyCamera.status
    # Function ends ...

class TypeVidCam(ABC):

    @abstractmethod
    def getStreamUrl(self) -> VideoCapture:
        return self.__url

    @abstractmethod
    def setStreamUrl(self) -> None:
        pass

    @abstractmethod
    def getFrame(self) -> dst:
        pass

    @property
    @abstractmethod
    def status(self) -> str:
        return
    
    @status.setter
    def status(self, txt: str) -> None:
        pass

class RTSPCam(TypeVidCam):
    """RTSP IP cameras enable users to stream live video;
    @example rtsp://<username>:<password>@<ip>:<port>/cam/realmonitor?channel=<channelNo>&subtype=<typeNo>;"""

    __status : str = 'none'

    def setStreamUrl(self, ip_port: str, username: str, password: str, typestream: int, channel: int) -> None:
        """Make the url to the camera"""
        self.__url = f"rtsp://{username}:{password}@{ip_port}/cam/realmonitor?channel={channel}&subtype={typestream}"

    def setStreamUrl(self, ip_port: str) -> None:
        """Make the url to the camera"""
        self.__url = f"{ip_port}"
            
    def getStreamUrl(self) -> VideoCapture:
        if cv2.VideoCapture(self.__url).isOpened():
            self.status = "Connected"
            return cv2.VideoCapture(self.__url)
        else:
            self.status = "Disconnected"
            return None

    def getFrame(self) -> dst:
        self.__ret, self.__frame = self.getStreamUrl().read()
        #Setting the frame;
        if self.__ret:
            self.__frame = cv2.resize(self.__frame,(const.SIZE_VIEWCAM_X, const.SIZE_VIEWCAM_Y))
            #Convert to BGR;
            return (cv2.cvtColor(self.__frame, cv2.COLOR_BGR2RGB))
        else:
            self.status = f"Bad frame!\n URL: {self.__frame}"
            return None

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, txt: str) -> None:
        self.__status = txt

    def __del__(self) -> None:
        if self.getStreamUrl().isOpened():
            self.getStreamUrl().release()

#if __name__ == "__main__":

#    context = VidCamera(RTSPCam())
#    context.createCamera("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_175k.mov")
#    print(f" Client: Good!\n URL:{context.getStream()}\n Camera: {context.getStatus()}")
