import cv2
import numpy as np
import random

class Label():
    def __init__(self, name, color, priority=0):
        self.name = name
        self.color = color
        self.priority = priority
    
    def foreground_color(self):
        luminance = cv2.cvtColor(np.uint8([[self.color]]), cv2.COLOR_BGR2GRAY)[0][0]
        return (0,0,0) if luminance > 186 else (255,255,255)

def label_registry(names, colors=None, priorities=None):
    colors = colors or generate_palette(names)
    priorities = priorities or dict()
    return {name : Label(name, colors[name], priorities.get(name, 0)) for name in names}

def generate_palette(names, random_offset=True):
    offset = random.randint(0, 180) if random_offset else 0
    golden_angle = 180 * (1 - 2.0 / (1 + 5 ** 0.5))
    return {name \
        : tuple(map(int, cv2.cvtColor(np.uint8([[(golden_angle * i + offset, 255, 255)]]), cv2.COLOR_HSV2BGR)[0][0])) \
        for i, name in enumerate(names)}
