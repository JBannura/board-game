import pygame
from pygame.rect import Rect

def lists():
    
    pos = [0, 0]
    print(pos[0])

def ranging():
    
    teste = range(10, 1, -1)
    for i in teste:
        print(i)

def dict_test():
    
    dict_ = {0: 0}
    
    if 0 in dict_:
        print("oi")
    
    #print()

def rect_():

    rect_ = Rect(0, 0, 2.5, 2.5)
    
    rect_.bottomleft
    
    print(rect_)

def str_():
    
    str = 12
    print(type(str))

def dict_path():
    
    path_dict = {0: 0,
                    1: [1, 1],
                    2: 0,
                    3: [2, -1],
                    4: [1, 1],
                    5: 0,
                    6: 0,
                    7: [1, 4],
                    8: [2, -2],
                    9: [1, 1],
                    10: 0,
                    11: [2, -1],
                    12: 0,
                    13: [2, -1],
                    14: 0,
                    15: 0,
                    16: [2, -2],
                    17: 0,
                    18: [1, 1],
                    19: [2, -2],
                    20: 0,
                    21: [2, -1],
                    22: [1, 1],
                    23: 0,
                    24: 0,
                    25: [1, 1],
                    26: 0,
                    27: [1, 2],
                    28: [2, -1],
                    29: 0,
                    30: [1, 1],
                    31: 0,
                    32: [1, 1],
                    33: 0,
                    34: [2, -1],
                    35: [1, 1],
                    36: 0,
                    37: [2, -1],
                    38: 0,
                    39: [1, 1],
                    40: 0,
                    41: [2, -1],
                    42: 0,
                    43: 0,
                    44: [1, 1],
                    45: 0,
                    46: [2, -1],
                    47: 0}
    
    for i in path_dict:
        print(i)

def path_mat():
    
    a = 5
    b = -1
    
    result = a + b
    
    print(result)

if __name__ == "__main__":
    path_mat()
    