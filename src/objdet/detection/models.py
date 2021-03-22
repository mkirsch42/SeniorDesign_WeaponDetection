from abc import ABC, abstractmethod
from .labels import label_registry
from .results import BoundingBox, DetectionResult
from pyyolo import YOLO
import asyncio
from concurrent.futures import ProcessPoolExecutor

class DetectionModel(ABC):
    def __init__(self, labels=None):
        self._labels = labels

    @abstractmethod
    async def detect(self, image):
        pass

    async def shutdown(self):
        pass

class NoModel(DetectionModel):
    async def detect(self, image):
        return DetectionResult(image, [])

class YOLOModel(DetectionModel):
    def __init__(self, *args, **kwargs):
        self._yolo = YOLO(*args, **kwargs)
        self._labels = label_registry(self._yolo.alt_names)
    
    async def detect(self, image):
        bboxes_raw = self._yolo.detect(image)
        bboxes = [BoundingBox(*bbox.view(), self._labels[bbox.name], bbox.prob) for bbox in bboxes_raw]
        return DetectionResult(image, bboxes)