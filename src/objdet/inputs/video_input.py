import cv2

class VideoInput():
    def __init__(self, input_device):
        self._capture = cv2.VideoCapture(input_device)

    def __iter__(self):
        while True:
            ok, frame = self._capture.read()
            if ok:
                yield frame
            else:
                break
    
    def __len__(self):
        return float('inf')