from abc import ABC, abstractmethod

class DetectionHandler(ABC):
    @abstractmethod
    async def on_detect(self, result):
        pass

    async def shutdown(self):
        pass