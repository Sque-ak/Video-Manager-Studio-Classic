#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import tkinter, tkinter.ttk -> PyQT must be better;
from __future__ import annotations
from PyQt5 import QtCore, QtGui, QtWidgets
from abc import ABC, abstractmethod
import PIL.Image, PIL.ImageTk, cv2
import const, videocam

class Window(ABC):
    """ This is global window;
    @param {Object} window : Main window;
    @param {String} title : Name the app;
    @param {Vector2x} geometry  : Window size after minimizing;
    @return {Object} I guess this is object;
    @example VMS(tkinter.Tk(), "Video Manager Studio Classic 0.1", '800x600'); """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component) -> None:
        self._parent = parent

    def setupUi(self, VMS):
        VMS.setObjectName("VMS")
        VMS.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(VMS)
        self.centralwidget.setObjectName("centralwidget")
        VMS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VMS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        VMS.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(VMS)
        self.statusBar.setObjectName("statusBar")
        VMS.setStatusBar(self.statusBar)
        self.actionOptions = QtWidgets.QAction(VMS)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAbout = QtWidgets.QAction(VMS)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(VMS)
        self.actionExit.setObjectName("actionExit")
        self.menuActions.addAction(self.actionOptions)
        self.menuActions.addAction(self.actionAbout)
        self.menuActions.addAction(self.actionExit)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(VMS)
        QtCore.QMetaObject.connectSlotsByName(VMS)

    def retranslateUi(self, VMS):
        _translate = QtCore.QCoreApplication.translate
        VMS.setWindowTitle(_translate("VMS", "Video Manager Studio Classic"))
        self.menuActions.setTitle(_translate("VMS", "Actions"))
        self.actionOptions.setText(_translate("VMS", "Options"))
        self.actionAbout.setText(_translate("VMS", "About"))
        self.actionExit.setText(_translate("VMS", "Exit"))


    def __new__(cls) -> instance: #Global window must be one!
        if not hasattr(cls, 'instance'):
            cls.instance = super(VMS, cls).__new__(cls)
        return cls.instance