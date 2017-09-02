from PIL import ImageGrab
import cv2
import numpy as np

"""
A module for capturing various objects in MapleStory(KMS).
Only for 800*600, with the program running on the top left corner of the screen.
"""

def capture_all(format=0):
    """
    Captures whole game screen.
    Returnes the captured image

    Fields
    - format: the format of returned image(0 for PIL, 1 for OpenCv)
    """
    pil_image = ImageGrab.grab(bbox=(0.26,800,600))
    if format == 0:
        image = pil_image
    elif format == 1:
        image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return image

def capture_arrow_collection(format=0):
    """
    Captures the arrows on minigame for collection.
    Returnes the list of 4 arrows.

    Fields
    - foramt: the format of returned image(0 for PIL, 1 for OpenCV)
    """
    img = []
    img.append(ImageGrab.grab(bbox=(248,231,276,259)))
    img.append(ImageGrab.grab(bbox=(341,231,369,259)))
    img.append(ImageGrab.grab(bbox=(434,231,462,259)))
    img.append(ImageGrab.grab(bbox=(527,231,555,259)))

    if format == 1:
        for i in len(img):
            img[i] = cv2.cvtColor(np.array(img[i]), cv2.COLOR_RGB2BGR)

    return img

def templateMatch(image,template):
    """
    Template matching function(Grayscale).
    returns the top-seft location of matching place with tuple(x,y).

    Fields
    - image: source image
    - template: template image 
    """
    threshold = 0.8
    image_gray = cv2.cvtColor(image,cv2.color_BGR2Gray)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(image_gray,template,cv2.TM_CCOEFF_NORMED)
    _a,_b,_c,loc = cv2.minMaxLoc(res)
    return loc

