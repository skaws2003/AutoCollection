from PIL import ImageGrab
import cv2
import numpy as np

"""
A module for capturing various objects in MapleStory(KMS).
Only for 800*600, with the program running on the top left corner of the screen.
"""

#constant
CAPTURE_CV = 0
CAPTURE_PIL = 1
CAPTURE_CV_GRAY = 2
def capture_all(format=0):
    """
    Captures whole game screen.
    Returnes the captured image

    Fields
    - format: the format of returned image(0:OpenCV,1:PIL,2:Gray(OpenCV))
    """
    pil_image = ImageGrab.grab(bbox=(0,26,800,600))
    if format == 0:
        image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    elif format == 1:
        image = pil_image
    elif format == 2:
        image = cv2.cvtColor(np.array(pil_image),cv2.COLOR_RGB2GRAY)
    return image

def capture_arrow_collection(format=0):
    """
    Captures the arrows on minigame for collection.
    Returnes the list of 4 arrows.

    Fields
    - foramt: the format of returned image(0:OpenCV,1:PIL,2:Gray(OpenCV)
    """
    img = []
    img.append(ImageGrab.grab(bbox=(248,257,276,285)))
    img.append(ImageGrab.grab(bbox=(341,257,369,285)))
    img.append(ImageGrab.grab(bbox=(434,257,462,285)))
    img.append(ImageGrab.grab(bbox=(527,257,555,285)))

    if format == 0:
        for i in range(len(img)):
            img[i] = cv2.cvtColor(np.array(img[i]), cv2.COLOR_RGB2BGR)
    elif format == 2:
        for i in range(len(img)):
            img[i] = cv2.cvtColor(np.array(img[i]), cv2.COLOR_RGB2GRAY)
    return img

def match_template(image,template,thresh=0.8):
    """
    Template matching function(Grayscale).
    Returns the top-left location of matching place with tuple(x,y).
    If nothing found, returns None.

    Fields
    - image: source image
    - template: template image 
    - thresh: threshold
    """
    
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
    _a,_b,_c,loc = cv2.minMaxLoc(res)
    if loc < thresh:
        return None
    return loc

def get_distance(image,temp_chara,temp_target,thresh=(0.8,0.8)):
    """
    Calculates the distance from the character to target.
    Returnes the (x,y) difference.

    Fields
    - image: source image
    - charaTemp: character recognizing template
    - targetTemp: target template
    - thresh: threshold(character,target)
    """

    targetPos = match_template(image,temp_target,thresh=thresh[1])
    charaPos = match_template(image,temp_chara,thresh=thresh[0])
    if targetPos == None or charaPos == None:
        return None
    return targetPos - charaPos

def get_multi_distance(image,temp_chara,temp_target,thresh=(0.8,0.8)):
    """
    Calculates the distance from the character to a target.
    This does not finds the closest one, but just finds first one founded.
    Returnes the (x,y) difference.

    Fields
    - image: source image
    - charaTemp: character recognizing template
    - targetTemp: target template
    - thresh: threshold(character,target)
    """
    for temp in temp_target:
        dist = get_distance(image,temp_chara,temp_target,thresh)
        if dist != None:
            return dist
        return None
