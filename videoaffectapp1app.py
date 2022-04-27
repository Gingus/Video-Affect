# encoding: utf8
from __future__ import unicode_literals
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from time import sleep
import sys
import os
import pygubu
import imageio

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "videoaffectapp1app.py")


class Videoaffectapp1App:
    """Main doc string"""
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('frame1', master)
        builder.connect_callbacks(self)
        self.canvas = self.builder.get_object('Video_Canvas')
        self.is_on = not self.is_on

    def affectButton1Pressed(self, event=None):
        """Colour change using """
        pass
    # PIL.Image.effect_noise(size, sigma)
    # Generate Gaussian noise centered around 128.
    # Parameters size – The requested
    # size in pixels, as a 2 - tuple: (width, height).
    # sigma – Standard deviation of noise.

    def affectButton2Pressed(self, event=None):
        """Flip image left to right"""
        puppy_image = Image.open('C:\\Users\\gingu\\Desktop\\Gubu Saves\\CamPCVisvis\\asleep_puppy.jpg')
        puppy_image.show()
        update_puppy = puppy_image.transpose(Image.FLIP_LEFT_RIGHT)
        update_puppy.show()
        sleep(5)
        puppy_image.close()
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

        canvas = self.canvas
        # Define function to update the image
        # ## https://www.tutorialspoint.com/how-to-update-an-image-in-a-tkinter-canvas
        def update_image():
            """Displaying the video feed from to the Tkinter canvas"""
            # canvas.itemconfig(canvas, image=img2)

        if self.is_on:
            print(self.is_on)
            video_name = '<video0>'
            video = imageio.get_reader(video_name)
            canvas.itemconfig(canvas, image=video)

            for image in video.iter_data():
                if not self.is_on:
                    break
                """video feed for the label"""
                # Updated from CamPCVisvis to display on a canvas instead of a label
                image_on = ImageTk.PhotoImage(Image.fromarray(image))
                canvas.itemconfig(image=image_on)
                # canvas.update()
                canvas.pack()
                # label.config(image=image_on)
                # label.image = image_on
                # label.update()

        else:
            show_image_off = ImageTk.PhotoImage(off_image_update)
            canvas.configure(image=show_image_off)
            label.image = show_image_off
            print(self.is_on)
        label.update()

    def callback(self, event=None):
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = Videoaffectapp1App(root)
    app.run()

# https://github.com/alejandroautalan/pygubu/issues/68
# https://stackoverflow.com/questions/68189294/how-to-display-the-video-in-tkinter-canvas-frame-by-frame
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

