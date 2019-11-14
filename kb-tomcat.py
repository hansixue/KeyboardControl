import os
import subprocess
import sys
import keyboard
import time
from evdev import InputDevice, categorize, ecodes,list_devices

"""
"sudo python3 -m evdev.evtest"  to find the define of a key
"""
#==========find the keyboard with evdev, must sudo============
devices = [InputDevice(path) for path in list_devices()]
for device in devices:
    if device.name=="winkeyless.kr ps2avrGB"  and  device.phys[-1] == "0":
        path = device.path
#禁用笔记本的键盘。要把机械键盘放上去，压到很麻烦。
    if device.name=="AT Translated Set 2 keyboard"  and  device.phys[-1] == "0":
        TPKpath = device.path

TPK=InputDevice(TPKpath)
TPK.grab()

#======define the keyboard=====







dev = InputDevice(path)
dev.grab()
#=====define the key functions======
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
#========every keys===========
        if key.keystate == key.key_down:
            if key.keycode == "KEY_GRAVE":
                keyboard.write("<tltle></")
                for x in range(8):
                    keyboard.send("Left")
            elif key.keycode == "KEY_5":
                os.system("su han firefox  http://127.0.0.1:8080/book/")
            elif key.keycode == "KEY_Y":
                os.system("nohup nautilus -s /opt/tomcat/webapps/book > /dev/null 2>&1 &")
