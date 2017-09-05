import tensorflow as tf
from tkinter import *
import MapleImage
from ArrowNet import *
import cv2
import time

"""
Factors
"""
#The directory of the trained model
meta_path = 'D:/OneDrive/MapleData/tfrecords/Arrow_classifier.meta'
network_path = 'D:/OneDrive/MapleData/tfrecords/Arrow_classifier'
#Our character and targets
template_target_path = ['D:/OneDrive/MapleData/Resources/target_flower_violet.bmp',
                        'D:/OneDrive/MapleData/Resources/target_mine_black.bmp']
template_chara_path = 'D:/OneDrive/MapleData/Resources/chara_mercedes.bmp'
template_chara_minimap_path = 'D:/OneDrive/MapleData/Resources/minimap_chara.bmp'

#templates initialization
template_target = []
for i in range(len(template_target_path)):
    template_target.append(cv2.imread(template_target_path[i]))
template_chara = cv2.imread(template_chara_path)
template_chara_minimap = cv2.imread(template_chara_minimap_path)



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



def seek_movement(image):
    print("\tLet's seek")
    #from minimap, find the location of character.
    minimap = MapleImage.crop_minimap_collection(image)
    loc = MapleImage.match_template_bgr(minimap,template_chara_minimap,0.9)
    #decide what to do
    visited_right = 0
    visited_left = 0


def collect_movement(dist):
    print("\tLet's collect")
    #from distance, decide what to do.

"""
Main Loop
"""
def main_loop():
    print("Main loop start!")
    while True:
        #Screenshot, find target
        print("Finding target...")
        img = MapleImage.capture_all(MapleImage.CAPTURE_CV)
        dist = MapleImage.get_distance_bgr_multi(img,template_chara,template_target,thresh=(0.8,0.9))
        if dist == None:
            #if nothing found
            print("Nothing found...")
            
        else:
            #if something found
            print("found! (%d,%d)" % (dist[0],dist[1]))
            
        #delay
        time.sleep(1)

def prototype():
    img = MapleImage.capture_all(MapleImage.CAPTURE_CV)
    img = MapleImage.crop_minimap_collection(img)
    loc = MapleImage.match_template_bgr(img,template_chara_minimap,thresh=0.7)
    if loc == None:
        print("not found!")
        cv2.imshow("what?",img)
    else:
        print(loc)

"""
Initialize GUI
"""
root = Tk()
lbl = Label(root, text="MapleStory Automated Collection")
lbl.pack()

btn = Button(root, text="Start Collection!",command=main_loop)
btn.pack()

root.mainloop()

