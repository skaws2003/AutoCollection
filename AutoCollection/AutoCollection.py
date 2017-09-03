import tensorflow as tf
from tkinter import *
import MapleGrab
from ArrowNet import *
import cv2

"""
Factors
"""
#The directory of the trained model
meta_path = 'D:/OneDrive/MapleData/tfrecords/Arrow_classifier.meta'
network_path = 'D:/OneDrive/MapleData/tfrecords/Arrow_classifier'
#Our character and targets
template_path_target = ['D:/OneDrive/MapleData/Resources/target_flower_violet.bmp',
                        'D:/OneDrive/MapleData/Resources/target_mine_black.bmp']
template_path_chara = 'D:/OneDrive/MapleData/Resources/Mercedes.bmp'
#templates initialization
template_target = []
for i in range(len(template_path_target)):
    template_target.append(cv2.imread(template_path_target[i]))
template_chara = cv2.imread(template_path_chara)


"""
Set up the neural network for arrow puzzle
"""
print("Loading graph...")
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

trained_network = tf.train.import_meta_graph(meta_path)
trained_network.restore(sess, network_path)
print("Loading success!")


"""
Not yet implemented
"""
def next_command():
    print("command!")

"""
Main Loop
"""
def main_loop():
    print("Main loop start!")
    while True:
        #Screenshot, find target
        print("Finding target...")
        img = MapleGrab.capture_all(MapleGrab.CAPTURE_CV)
        dist = MapleGrab.get_multi_distance(img,template_chara,template_target)
        if dist == None:
            #if nothing found
            print("Nothing found...")
        else:
            #if something found
            print("found!")
        
        #Get proper action
        #Send action to the keyboard
        #delay


"""
Initialize GUI
"""
root = Tk()
lbl = Label(root, text="MapleStory Automated Collection")
lbl.pack()

btn = Button(root, text="Start Collection!",command=main_loop)
btn.pack()

root.mainloop()

