import tensorflow as tf
from tkinter import *
import MapleGrab
from ArrowNet import *

"""
Set up the neural network for arrow puzzle
"""


"""
Initialize GUI
"""
root = Tk()
lbl = Label(root, text="MapleStory Automated Collection")
lbl.pack()

btn = Button(root, text="Start Collection!")
btn.pack()

root.mainloop()

