# -*- coding: utf-8 -*-
"""
Created on Mon May 21 01:03:21 2018

@author: giang
"""

import ImageGrab
import os
import time

def screenGrab():
    box = (188, 155, 828, 634)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')
    
def main():
    screenGrab()
        
if __name__ == '__main__':
    main()