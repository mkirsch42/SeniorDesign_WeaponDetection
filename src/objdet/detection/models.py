from abc import ABC, abstractmethod
from .labels import label_registry
from .results import BoundingBox, DetectionResult
from pyyolo import YOLO

class DetectionModel(ABC):
    def __init__(self, labels=None):
        self._labels = labels

    @abstractmethod
    def detect(self, image):
        pass

class YOLOModel(DetectionModel):
    def __init__(self, *args, **kwargs):
        self._yolo = YOLO(*args, **kwargs)
        self._labels = label_registry(self._yolo.alt_names)
    
    def detect(self, image):
        bboxes_raw = self._yolo.detect(image)
        bboxes = [BoundingBox(*bbox.view(), self._labels[bbox.name], bbox.prob) for bbox in bboxes_raw]
        return DetectionResult(image, bboxes)