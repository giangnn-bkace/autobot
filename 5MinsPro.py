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
y_pad = 0

prod_house_pos = ((410, 495), (535, 560), (585, 535), (640, 510), (585, 585), (635, 560), (685, 535))
house_pos = ((560, 345), (525, 360), (500, 375), (470, 390), (440, 405), (405, 420), (375, 435), (345, 450), (310, 465),
             (605, 360), (575, 375), (545, 390), (510, 405), (480, 420), (450, 440), (420, 455), (390, 470),
             (640, 380), (605, 390), (575, 410), (545, 425), (510, 440), (480, 455), (450, 470),
             (680, 400), (650, 415), (620, 430), (590, 450), (560, 460), (530, 480), (500, 490), (470, 510), (440, 525),
             (720, 415), (685, 430), (650, 445), (620, 460), (590, 480), (560, 490), (510, 515), (470, 540))
min5_pos = (515, 360)
exit_pos = (18, 150)
tab_pos = (30, 15)

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
    turn = 0
    while(1):
        mousePos(tab_pos)
        leftClick()
        if turn % 12 == 0:
            for i in range(len(house_pos)):
                mousePos(exit_pos)
                leftClick()
                mousePos(house_pos[i])
                leftClick()
        start_product()
        mousePos(exit_pos)
        time.sleep(270)
        mousePos(tab_pos)
        leftClick()
        time.sleep(25)
        mousePos(tab_pos)
        leftClick()
        gather_product()
        turn = turn + 1
if __name__ == '__main__':
    main()