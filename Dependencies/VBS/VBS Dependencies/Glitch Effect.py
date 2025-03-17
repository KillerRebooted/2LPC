import win32gui
import win32api
import mss
from PIL import Image
import sys
import os
import cv2
import numpy as np
import glitchart
import random
import winsound
import time

#Get file path based on whether code is running as a Python Script or an Executable
def get_path(relative_path):
    """ Get the correct path whether running as .py or .exe """
    if getattr(sys, 'frozen', False):  # Check if running as an .exe
        base_path = sys._MEIPASS  # Temp folder where PyInstaller extracts files
    else:
        base_path = os.path.dirname(__file__)  # Normal script directory
    
    return os.path.join(base_path, relative_path)

def mouse_evt(event, x, y, flags, param):
    # Mouse is Moving
    if event == cv2.EVENT_MOUSEMOVE:
        win32api.SetCursor(None)

def glitch_effect(flicker, iter=1):

    SPI_SETANIMATION = 0x49  # or 0x00000049
    
    win32gui.SystemParametersInfo(SPI_SETANIMATION, 0, 3)

    with mss.mss() as mss_instance:

        img = mss_instance.grab(mss_instance.monitors[0])

        img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

        img.save(get_path("image.png"))
        
        cv2.namedWindow("Glitch Effect", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Glitch Effect", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setMouseCallback("Glitch Effect", mouse_evt)

        start_time = time.time()

        img = np.array(Image.open(get_path("image.png")).convert("RGB"))
        img = img[:, :, ::-1].copy()

        cv2.imshow('Glitch Effect', img)
        cv2.waitKey(75)
        
        if not flicker:

            played = False

            while time.time() - start_time < iter:
            
                glitchart.png(get_path("image.png"), max_amount=50)

                img = np.array(Image.open("image_glitch.png").convert("RGB"))
                img = img[:, :, ::-1].copy()

                cv2.imshow("Glitch Effect", img)
                if not played:
                    winsound.PlaySound(get_path("Glitch Sound.wav"), winsound.SND_ASYNC)
                    played = True
                else:
                    played = False
                cv2.waitKey(50)

        else:
            
            for i in range(iter):

                glitchart.png(get_path("image.png"), max_amount=50)

                img = np.array(Image.open("image_glitch.png").convert("RGB"))
                img = img[:, :, ::-1].copy()

                cv2.imshow("Glitch Effect", img)
                winsound.PlaySound(get_path("Glitch Sound.wav"), winsound.SND_ASYNC)
                cv2.waitKey(100)

                img = np.array(Image.open(get_path("image.png")).convert("RGB"))
                img = img[:, :, ::-1].copy()

                cv2.imshow('Glitch Effect', img)
                cv2.waitKey(100)

                time.sleep(0.1*random.randint(3, 8))

        cv2.destroyAllWindows()

        os.remove(get_path("image.png"))
        os.remove("image_glitch.png")

    win32gui.SystemParametersInfo(SPI_SETANIMATION, 1, 3)

if __name__ == "__main__":

    print("Running Glitch Effect...")
    glitch_effect(flicker=True, iter=4)
