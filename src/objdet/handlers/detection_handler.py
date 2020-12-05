from abc import ABC, abstractmethod

class DetectionHandler(ABC):
    @abstractmethod
    def on_detect(self, result):
        pass