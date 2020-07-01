#!/usr/bin/env python3
from tkinter import Tk

import sys
sys.path.append('src')
import const, app

if __name__ == "__main__":
    app.VMS(Tk(), const.NAMEAPP + " " + const.VERSION)