
import random

"""
A module for producing movement in Maplestory
"""

KEYOP_RELEASE = 0
KEYOP_PRESS = 1
KEYOP_RELEASE_ALL = 2

modifier = {"KEY_LEFT_CTRL": 128,
                "Key_LEFT_SHIFT": 129,
                "KEY_LEFT_ALT": 130,
                "KEY_UP_ARROW": 218,
                "KEY_DOWN_ARROW": 217,
                "KEY_LEFT_ARROW": 216,
                "KEY_RIGHT_ARROW": 215,
                "KEY_ESC": 177,
                "KEY_INSERT": 209,
                "KEY_DELETE	": 212,
                "KEY_PAGE_UP": 211,
                "KEY_PAGE_DOWN": 214,
                "KEY_HOME": 210,
                "KEY_END": 213,
                "KEY_F1": 194,
                "KEY_F2": 195,
                "KEY_F3": 196,
                "KEY_F4": 197,
                "KEY_F5": 198,
                "KEY_F6": 199,
                "KEY_F7": 200,
                "KEY_F8": 201,
                "KEY_F9": 202,
                "KEY_F10": 203,
                "KEY_F11": 204,
                "KEY_F12": 205}

def get_keyval(key):
    """
    Receives a key string, return corresponding value.

    Field
    - key: the key string e.g.'a'
    """
    if len(key) == 1:
        return ord(key)
    else:
        return modifier(key)


class Keyop(object):
    """
    Base Class for every Keyboard operation
    """
    def __init__(self,key):
        """
        Field
        - key: a key character(string) to press
        """
        self.keyval=get_keyval(key)
        self.random_delay = int(random.random()*10)

        
class Keyop_press(Keyop):
    def __init__(self,key,duration):
        """
        Field
        - key: a key characetr(or string) to press
        - duration: a minimum duration it should pressed
        """
        Keyop.__init__(self,key)
        self.duration = duration



class Keyop_touch(Keyop):
    def __init__(self,key,delay):
        """
        Field
        - key: a key character(or string) to press
        - delay: how long should I wait?
        """
        Keyop.__init__(self,key)
        self.delay = delay


class Keyop_delay(Keyop):
    def __init__(self,duration):
        """
        Field
        - duration: the amount of delay
        """
        Keyop.__init__(self,duration)
        self.duration = duration


class Timetable(object):
    def __init__(self):
        self.oper_list = []
        self.oper_string = "" #format:(delay(후딜),key,operation)

    def append(self,keyop):
        """
        Appends operation to the timetable

        Fields
        - keyop: a key operation object
        """
        self.oper_list.append([keyop])

    def attach(self,keyop):
        """
        Attaches a operation to the last element.

        Fields
        - keyop: a key operation object
        """
        self.oper_list[-1].append(keyop)

    def build_string(self):
        """
        from existing key operation list, builds a string to send to the leonardo device
        """
        #list for basic keyboard operation
        #stores a tuple(time,key,operation)
        key_list = []
        #선딜 추가
        max_time = random.randrange(100,150)
        for operset in self.oper_list:
            max_time_temp = max_time
            same_start=0
            for oper in operset:
                max_time_local = max_time + same_start*100
                if(isinstance(oper,Keyop_delay)):
                    max_time_local += oper.delay
                    max_time_local += oper.random_delay
                    if max_time_temp < max_time_local: max_time_temp=max_time_local   
                elif(isinstance(oper,Keyop_touch)):
                    key_list.append((max_time_local,oper.keyval,KEYOP_PRESS))
                    randnum=random.randrange(70,130)
                    max_time_local += randnum
                    key_list.append((max_time_local,oper.keyval,KEYOP_RELEASE))
                    max_time_local += oper.delay
                    max_time_local += oper.random_delay
                    if max_time_temp < max_time_local: max_time_temp=max_time_local
                elif(isinstance(oper,Keyop_press)):
                    key_list.append((max_time_local,oper.keyval,KEYOP_PRESS))
                    max_time_local += oper.duration
                    if max_time_temp < max_time_local: max_time_temp=max_time_local
                same_start += 1
            max_time = max_time_temp
            key_list.append((max_time,0,KEYOP_RELEASE_ALL))
        #sort the operation by the time order
        sorted(key_list,key=lambda first: first[0])

        def time_string(op):
            op_str = ""
            op_str += str(op[0]) + "," + str(op[1]) + "," + str(op[2])
            return op_str

        self.oper_string = ""
        for i in range(len(key_list)-1):
            self.oper_string += time_string((key_list[i+1][0] - key_list[i][0], key_list[i][1], key_list[i][2])) + ":"
        self.oper_string += time_string((100,key_list[-1][1],key_list[-1][2]))


class Movement_mercedes(object):
    def __init__(self):
        self.table = Timetable()

    def double_jump(self):
        print("jump")
