# -*- coding: utf-8 -*-
"""
Created on Mon May 21 01:03:21 2018

@author: giang
"""

import ImageGrab
import os
import time
import win32api, win32con

x_pad = 0
y_pad = 90

prod_house_pos = ((600, 435), (695, 440), (650, 460), (650, 415), (700, 390), (750, 415), (815, 280))
min5_pos = (515, 270)
exit_pos = (10, 55)

def screenGrab():
    box = (x_pad, y_pad, x_pad+828, y_pad+634)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)
    print "Click."

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    print "Left Down."

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)
    print "Left Release."

def mousePos(cord):
    print cord[0]
    print cord[1]
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y

def start_product():
    for i in range(len(prod_house_pos)):
        mousePos(exit_pos)
        leftClick()
        mousePos(prod_house_pos[i])
        leftClick()
        mousePos(min5_pos)
        leftClick()

def gather_product():
    mousePos(exit_pos)
    leftClick()
    mousePos(exit_pos)
    leftClick()
    mousePos(exit_pos)
    leftClick()
    mousePos(exit_pos)
    leftClick()
    mousePos(exit_pos)
    leftClick()
    for i in range(len(prod_house_pos)):
        mousePos(exit_pos)
        leftClick()
        mousePos(prod_house_pos[i])
        leftClick()
    
def main():
    while(1):
        start_product()
        time.sleep(300)
        gather_product()
        time.sleep(1)
if __name__ == '__main__':
    main()