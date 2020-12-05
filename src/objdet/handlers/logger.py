from abc import abstractmethod

import cv2
from ..detection.results import BoundingBox, DetectionResult
from .detection_handler import DetectionHandler
import json
from pathlib import Path

class Logger(DetectionHandler):
    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __len__(self):
        pass

class FilesystemLogger(Logger):
    def __init__(self, base_dir, log_file='_log.json'):
        self._path = Path(base_dir)
        self._path.mkdir(exist_ok=True)
        self._logfile = self._path / log_file
        try:
            with self._logfile.open() as f:
                self._json = json.load(f)
        except FileNotFoundError:
            self._json = {'detections':[]}

    def __iter__(self):
        return iter(self.parse_detection(obj) for obj in self._json['detections'])

    def __len__(self):
        return len(self._json['detections'])
    
    def parse_detection(self, obj):
        image = cv2.imread(str(self._path / obj['image']))
        bboxes = [BoundingBox(**bbox) for bbox in obj['bboxes']]
        return DetectionResult(image, bboxes)
