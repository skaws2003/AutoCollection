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


def match_template_gray(image,template,thresh=0.8):
    """
    Template matching function(Grayscale).
    Returns the top-left location of matching place with tuple(x,y).
    If nothing found, returns None.

    Fields
    - image: source image
    - template: template image 
    - thresh: threshold
    """
    
    res = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
    _a,maxima,_c,loc = cv2.minMaxLoc(res)
    if maxima < thresh:
        return None
    return loc


def match_template_bgr(image,template,thresh=0.8):
    """
    Template matching function(bgr).
    Returns the top-left location of matching place with tuple(x,y).
    If nothing found, returns None.

    Fields
    - image: source image
    - template: template image 
    - thresh: threshold
    """
    img_b, img_g, img_r = cv2.split(image)
    temp_b, temp_g, temp_r = cv2.split(template)
    res_b = cv2.matchTemplate(img_b,temp_b,cv2.TM_CCOEFF_NORMED)
    res_g = cv2.matchTemplate(img_g,temp_g,cv2.TM_CCOEFF_NORMED)
    res_r = cv2.matchTemplate(img_r,temp_r,cv2.TM_CCOEFF_NORMED)
    res = res_b/3 + res_g/3 + res_r/3
    _a,maxima,_c,loc = cv2.minMaxLoc(res)
    if maxima < thresh:
        return None
    return loc


def get_distance_gray(image,temp_chara,temp_target,thresh=(0.8,0.8)):
    """
    Calculates the distance from the character to target.
    Returnes the (x,y) difference.

    Fields
    - image: source image
    - charaTemp: character recognizing template
    - targetTemp: target template
    - thresh: threshold(character,target)
    """

    targetPos = match_template_gray(image,temp_target,thresh=thresh[1])
    charaPos = match_template_gray(image,temp_chara,thresh=thresh[0])
    if targetPos == None or charaPos == None:
        return None
    return (targetPos[0] - charaPos[0], targetPos[1] - charaPos[1])


def get_distance_bgr(image,temp_chara,temp_target,thresh=(0.8,0.8)):
    """
    Calculates the distance from the character to target.
    Returnes the (x,y) difference.

    Fields
    - image: source image
    - charaTemp: character recognizing template
    - targetTemp: target template
    - thresh: threshold(character,target)
    """

    targetPos = match_template_bgr(image,temp_target,thresh=thresh[1])
    charaPos = match_template_bgr(image,temp_chara,thresh=thresh[0])
    if targetPos == None or charaPos == None:
        return None
    return (targetPos[0] - charaPos[0], targetPos[1] - charaPos[1])


def get_distance_gray_multi(image,temp_chara,temp_target,thresh=(0.8,0.8)):
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
        dist = get_distance_gray(image,temp_chara,temp,thresh)
        if dist != None:
            return dist
    return None


def get_distance_bgr_multi(image,temp_chara,temp_target,thresh=(0.8,0.8)):
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
        dist = get_distance_bgr(image,temp_chara,temp,thresh)
        if dist != None:
            return dist
    return None