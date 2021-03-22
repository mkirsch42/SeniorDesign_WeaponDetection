import cv2
import asyncio

class VideoInput():
    def __init__(self, input_device):
        self._capture = cv2.VideoCapture(input_device)

    async def __aiter__(self):
        while True:
            ok, frame = await asyncio.get_event_loop().run_in_executor(None, self._capture.read)
            if ok:
                yield frame
            else:
                break
    
    def __len__(self):
        return float('inf')