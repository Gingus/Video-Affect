# Phil Minard
# With help from Sam Cork
# encoding: utf8
from __future__ import unicode_literals
# import tkinter as tk
# import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageFilter  # ,ImageFilter
# import numpy as np
# from time import sleep
import sys
import os
import pygubu
import imageio

try:
    import tkinter as tk
    from tkinter import messagebox
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


class Pictureaffectapp:
    """Main doc string"""
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        fpath = os.path.join(os.path.dirname(__file__), "Video_Affect_App.ui")
        builder.add_from_file(fpath)
        mainwindow = builder.get_object('mainwindow', master)
        self.is_on = False

        self.buttonState = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}

        builder.connect_callbacks(self)
        builder.import_variables(self, 'is_on')
        self.canvas = self.builder.get_object('Video_Canvas')
        self.label = self.builder.get_object('label1')  # ('label_video_feed')

    def resetButtonStates(self, buttonNo=None):
        """Resets all button states"""
        for i in self.buttonState.keys():
            if buttonNo is None or i != buttonNo:
                self.buttonState[i] = False

    def affectButton1Pressed(self):
        """Adds GaussianBlur Noise/Blur filter"""
        self.buttonState[1] = not self.buttonState[1]
        label = self.builder.get_object('label1')  # ('label_video_feed')
        Archie_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\ArchieArcade.jpg'
        self.resetButtonStates(1)
        print('button 1 is ', self.buttonState[1])
        if self.buttonState[1]:
            Archie = Image.open(Archie_image)
            img2_update = Archie.resize((450, 350), Image.ANTIALIAS)
            new_Archie = img2_update.filter(ImageFilter.GaussianBlur(radius=5))
            img = ImageTk.PhotoImage(new_Archie)
            label.configure(image=img)
            label.image = img
        else:
            off_image = Image.open(Archie_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
        label.update()

    def affectButton2Pressed(self):
        """Flip image top to bottom"""
        self.buttonState[2] = not self.buttonState[2]
        label = self.builder.get_object('label1')  # ('label_video_feed')
        puppy_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\asleep_puppy.jpg'
        self.resetButtonStates(2)
        print('button 2 is ', self.buttonState[2])
        if self.buttonState[2]:
            pup = Image.open(puppy_image)
            img2_update = pup.resize((450, 350), Image.ANTIALIAS)
            new_puppy = img2_update.transpose(Image.FLIP_TOP_BOTTOM)
            img = ImageTk.PhotoImage(new_puppy)
            label.configure(image=img)
            label.image = img
        else:
            off_image = Image.open(puppy_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
        label.update()

    def affectButton3Pressed(self):
        """Flip Left to Right"""
        self.buttonState[3] = not self.buttonState[3]
        label = self.builder.get_object('label1')  # ('label_video_feed')
        Mum_and_pups_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\Mum_and_pups.jpg'
        self.resetButtonStates(3)
        print('button 3 is ', self.buttonState[3])
        if self.buttonState[3]:
            mum_and_pups = Image.open(Mum_and_pups_image)
            img2_update = mum_and_pups.resize((450, 350), Image.ANTIALIAS)
            new_Mum_and_pups = img2_update.transpose(Image.FLIP_LEFT_RIGHT)
            img = ImageTk.PhotoImage(new_Mum_and_pups)
            label.configure(image=img)
            label.image = img
        else:
            off_image = Image.open(Mum_and_pups_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
        label.update()
    # PIL.Image.radial_gradient(mode)[source]
    # Generate 256x256 radial gradient from black to
    # white, centre to edge.
    # Parameters mode – Input mode.

    def affectButton4Pressed(self):
        """Rotate 90 degrees"""
        self.buttonState[4] = not self.buttonState[4]
        label = self.builder.get_object('label1')  # ('label_video_feed')
        Phil_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\Phil_Pic.jpg'
        self.resetButtonStates(4)
        print('button 4 is ', self.buttonState[4])
        if self.buttonState[4]:
            phil = Image.open(Phil_image)
            img2_update = phil.resize((450, 350), Image.ANTIALIAS)
            new_phil = img2_update.transpose(Image.ROTATE_90)
            img = ImageTk.PhotoImage(new_phil)
            label.configure(image=img)
            label.image = img
        else:
            off_image = Image.open(Phil_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
        label.update()

    def affectButton5Pressed(self):
        """Emboss"""
        self.buttonState[5] = not self.buttonState[5]
        label = self.builder.get_object('label1')  # ('label_video_feed')
        scoot_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\scoot.jpg'
        self.resetButtonStates(5)
        print('button 3 is ', self.buttonState[5])
        if self.buttonState[5]:
            scooter = Image.open(scoot_image)
            img2_update = scooter.resize((450, 350), Image.ANTIALIAS)
            # new_scooter = img2_update.transpose(Image.Im)  #  FLIP_TOP_BOTTOM)
            new_scooter = img2_update.filter(ImageFilter.EMBOSS)
            img = ImageTk.PhotoImage(new_scooter)
            label.configure(image=img)
            label.image = img
        else:
            off_image = Image.open(scoot_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
        label.update()
    # Rotate:
    # from PIL import Image
    # with Image.open("hopper.jpg") as im:
    #     im.rotate(45).show()
    # PIL.Image.ROTATE_90
    # PIL.Image.ROTATE_180
    # PIL.Image.ROTATE_270

    def onOffPressed(self):
        """Start and stop the video feed
        also call this to make sure the video
        is off when the app has been quit"""
        self.buttonState[6] = not self.buttonState[6]
        label = self.builder.get_object('label1')  # ('label_video_feed')
        # canvas = self.canvas

        # ## https://www.tutorialspoint.com/how-to-update-an-image-in-a-tkinter-canvas

        if self.buttonState[6]:
            print('on/off is ', self.buttonState[6])
            video_name = '<video0>'
            video = imageio.get_reader(video_name)

            for image in video.iter_data():
                if not self.buttonState[6]:
                    break
                """video feed for the label"""
                image_on = ImageTk.PhotoImage(image=Image.fromarray(image))
                label.config(image=image_on)
                label.image = image_on
                label.update()
        else:
            puppy_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\asleep_puppy.jpg'
            off_image = Image.open(puppy_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
        label.update()

# Testing quit and destroy to turn off camera if it's still switched on when the app is quit out of!
    def quit(self):
        """To make destroy the root window and shut off the camera feed"""
        self.is_on = False
        print(self.is_on)
        # root.quit()
        root.destroy()

    # def callback(self, event=None):
    #     pass
    #
    # def run(self):
    #     self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = Pictureaffectapp(root)
    root.mainloop()
    Pictureaffectapp.quit(root)  # Videoaffectapp.quit()


# https://stackoverflow.com/questions/68189294/how-to-display-the-video-in-tkinter-canvas-frame-by-frame
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

