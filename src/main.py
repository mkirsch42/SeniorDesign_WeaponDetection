from cvlib.object_detection import (
    detect_common_objects,
    draw_bbox,
)
import cv2

image = cv2.imread('input/flickr/1000366164.jpg')
print('detecting objects...')
detected_objects = detect_common_objects(image)
image = draw_bbox(image, *detected_objects)

