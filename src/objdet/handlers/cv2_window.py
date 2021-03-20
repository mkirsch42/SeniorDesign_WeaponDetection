import cv2
from .detection_handler import DetectionHandler

class CV2WindowOutput(DetectionHandler):
    def __init__(self, window_name, window_flags = cv2.WINDOW_NORMAL, annotated_images=None):
        self.window_name = window_name
        self.annotated_images = annotated_images
        cv2.startWindowThread()
        cv2.namedWindow(self.window_name, window_flags)
    
    def wait_for_key(self):
        cv2.waitKey(0)
    
    def close_window(self):
        cv2.destroyWindow(self.window_name)

    def on_detect(self, result):
        if self.annotated_images is not None:
            image = result.annotated_image(**self.annotated_images)
        else:
            image = result.image
        cv2.imshow(self.window_name, image)
        cv2.waitKey(1)
