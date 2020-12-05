from pathlib import Path
import cv2
import random

class ImageDirectory():
    def __init__(self, base_dir, scramble=False, loop=True):
        self._path = Path(base_dir)
        self._scramble = scramble
        self._loop = loop

    def __iter__(self):
        images = sorted(self._path.glob('*'))
        while True:
            if self._scramble:
                random.shuffle(images)
            for image_path in images:
                yield (cv2.imread(str(image_path)), image_path.name)
            if not self._loop:
                break
    
    def __len__(self):
        return len(self._path.glob('*'))