from pathlib import Path
import cv2
import random
import asyncio

class ImageDirectory():
    def __init__(self, base_dir, scramble=False, loop=True):
        self._path = Path(base_dir)
        self._scramble = scramble
        self._loop = loop

    async def __aiter__(self):
        images = sorted(self._path.glob('*.jpg'))
        while True:
            if self._scramble:
                random.shuffle(images)
            for image_path in images:
                yield (await asyncio.get_event_loop().run_in_executor(None, cv2.imread, str(image_path)), image_path.name)
            if not self._loop:
                break
    
    def __len__(self):
        return len(self._path.glob('*'))