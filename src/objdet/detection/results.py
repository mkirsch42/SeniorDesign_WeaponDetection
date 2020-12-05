import cv2

class BoundingBox():
    def __init__(self, x, y, w, h, label, confidence):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label
        self.confidence = confidence
    
    def draw_on_image(self, 
        image, 
        font_face=cv2.FONT_HERSHEY_SIMPLEX, 
        outline_thickness=4, 
        font_scale=1,
        font_thickness=2,
        padding=2):
        label_text = f'{self.label.name}({self.label.priority}) : {self.confidence:.2f}'
        (label_w, label_h), baseline = cv2.getTextSize(label_text,
            font_face,
            font_scale,
            font_thickness)

        # import pdb; pdb.set_trace()
        cv2.rectangle(image,
            _int_coords(self.x, self.y), 
            _int_coords(self.x+self.w, self.y+self.h), 
            self.label.color,
            int(outline_thickness))
        cv2.rectangle(image,
            _int_coords(self.x - outline_thickness/2, self.y - label_h - 2*padding),
            _int_coords(self.x + label_w + 2*padding - outline_thickness/2, self.y),
            self.label.color,
            int(cv2.FILLED))
        cv2.putText(image,
            label_text,
            _int_coords(self.x+padding-outline_thickness/2, self.y-padding),
            font_face,
            font_scale,
            self.label.foreground_color(),
            font_thickness)

class DetectionResult():
    def __init__(self, image, bboxes):
        self.image = image
        self.bboxes = bboxes
        self._annotated_image = None
    
    def priority(self, conf_scaling=False):
        return sum((bbox.confidence if conf_scaling else 1) * bbox.label.priority for bbox in self.bboxes)

    def annotated_image(self, *args, **kwargs):
        if self._annotated_image is None:
            self._annotated_image = self.image.copy()
            for bbox in self.bboxes:
                bbox.draw_on_image(self._annotated_image, *args, **kwargs)
        return self._annotated_image


def _int_coords(x, y):
    return (int(x), int(y))