from cvlib.object_detection import (
    detect_common_objects,
    draw_bbox,
)
import cv2

image = cv2.imread('input/test.bmp')
detected_objects = detect_common_objects(image)
image = draw_bbox(image, *detected_objects)

cv2.imshow('YOLO', image)
cv2.waitKey(0)
cv2.destroyAllWindows()