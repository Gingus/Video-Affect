# encoding: utf8
from __future__ import unicode_literals
# import tkinter as tk
# import tkinter.ttk as ttk
from PIL import Image, ImageTk,ImageFilter
import numpy as np
from time import sleep
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


class Videoaffectapp:
    """Main doc string"""
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        fpath = os.path.join(os.path.dirname(__file__), "Video_Affect_App.ui")
        builder.add_from_file(fpath)
        mainwindow = builder.get_object('mainwindow', master)
        self.is_on = False

        builder.connect_callbacks(self)
        builder.import_variables(self, 'is_on')
        self.canvas = self.builder.get_object('Video_Canvas')
        self.label = self.builder.get_object('label1')  # ('label_video_feed')

    def affectButton1Pressed(self, event=None):
        """Colour change using """
        pass
    # PIL.Image.effect_noise(size, sigma)
    # Generate Gaussian noise centered around 128.
    # Parameters size – The requested
    # size in pixels, as a 2 - tuple: (width, height).
    # sigma – Standard deviation of noise.

    def affectButton2Pressed(self):
        """Flip image left to right"""
        self.is_on = not self.is_on
        label = self.builder.get_object('label1')  # ('label_video_feed')

        if self.is_on:
            print(self.is_on)
            video_name = '<video0>'
            video = imageio.get_reader(video_name)

            for image in video.iter_data():
                if not self.is_on:
                    break
                """video feed for the label"""
                # Updated from CamPCVisvis to display on a canvas instead of a label
                # image_on = ImageTk.PhotoImage(image=Image.fromarray(image))
                arry = np.array([[25, 25, 25], [0, 0, 0], [0, 0, 0]])
                image_on = Image.fromarray(arry.astype('uint8'))
                # imtype = (type(image_on))
                # print("image_on_update =", imtype)
                # # image_on_update =
                # image_on_update = image_on_update.resize((450, 350), Image.ANTIALIAS)
                label.config(image=image_on)
                # label.image = image
                label.update()
                # image_on = ImageTk.PhotoImage(image=Image.fromarray(image))
                # label.config(image=image_on)
                # label.image = image_on
                # label.update()

                # cv_img = cv2.cvtColor(cv2.imread("home.png"), cv2.COLOR_BGR2RGB)
                # photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

        else:
            puppy_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\asleep_puppy.jpg'
            off_image = Image.open(puppy_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
            print(self.is_on)
        label.update()

        # puppy_image = Image.open('C:\\Users\\gingu\\Desktop\\Gubu Saves\\CamPCVisvis\\asleep_puppy.jpg')
        # puppy_image.show()
        # update_puppy = puppy_image.transpose(Image.FLIP_LEFT_RIGHT)
        # update_puppy.show()
        # sleep(5)
        # puppy_image.close()
    # Find an example!!
    # https://pythonexamples.org/python-pillow-flip-image-vertical-horizontal/
    # Image.transpose(method)
    # where method – Possible values
    # of method are,
    # PIL.Image.FLIP_LEFT_RIGHT
    # PIL.Image.FLIP_TOP_BOTTOM
    # PIL.Image.ROTATE_90
    # PIL.Image.ROTATE_180
    # PIL.Image.ROTATE_270
    # PIL.Image.TRANSPOSE or PIL.Image.TRANSVERSE.

    def affectButton3Pressed(self, event=None):
        """Apply radial gradient using PIL"""
        pass
    # PIL.Image.radial_gradient(mode)[source]
    # Generate 256x256 radial gradient from black to
    # white, centre to edge.
    # Parameters mode – Input mode.

    def affectButton4Pressed(self, event=None):
        """Apply linear gradient using PIL"""
        pass
    # PIL.Image.linear_gradient(mode)[source]
    # Generate 256x256 linear gradient
    # from black to white, top to bottom.
    # Parameters mode – Input mode.

    def affectButton5Pressed(self, event=None):
        """Rotate Image using PIL"""
        pass
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
        self.is_on = not self.is_on
        label = self.builder.get_object('label1')  # ('label_video_feed')
        # canvas = self.canvas

        # ## https://www.tutorialspoint.com/how-to-update-an-image-in-a-tkinter-canvas

        if self.is_on:
            print(self.is_on)
            video_name = '<video0>'
            video = imageio.get_reader(video_name)

            for image in video.iter_data():
                if not self.is_on:
                    break
                """video feed for the label"""
                # # https://towardsdatascience.com/lightning-fast-video-reading-in-python-c1438771c4e6
                # https://programtalk.com/python-examples/Image.fromarray/
                # Updated from CamPCVisvis to display on a canvas instead of a label
                image_on = ImageTk.PhotoImage(image=Image.fromarray(image))
                label.config(image=image_on)
                label.image = image_on
                label.update()

                # def toTk(self):
                #     if self.image is None: return None
                #     self.imagetk = ImageTk.PhotoImage(
                #         image=Image.fromarray(
                #             cv.cvtColor(self.image, cv.COLOR_BGR2RGB), "RGB"))
                #     return self.imagetk

        else:
            puppy_image = 'C:\\Users\\gingu\\Desktop\\Gubu Saves\\Video Affect\\asleep_puppy.jpg'
            off_image = Image.open(puppy_image)
            off_image_update = off_image.resize((450, 350), Image.ANTIALIAS)
            show_image_off = ImageTk.PhotoImage(off_image_update)
            label.configure(image=show_image_off)
            label.image = show_image_off
            print(self.is_on)
        label.update()

# Testing quit and destroy to turn off camera if it's still switched on when the app is quit out of!
    def quit(self):
        """To make destroy the root window and shut off the camera feed"""
        self.is_on = False
        print(self.is_on)
        root.quit()

    # def callback(self, event=None):
    #     pass
    #
    # def run(self):
    #     self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = Videoaffectapp(root)
    root.mainloop()
    Videoaffectapp.quit()  # Videoaffectapp.quit()


# https://github.com/alejandroautalan/pygubu/issues/68
# https://stackoverflow.com/questions/68189294/how-to-display-the-video-in-tkinter-canvas-frame-by-frame
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

