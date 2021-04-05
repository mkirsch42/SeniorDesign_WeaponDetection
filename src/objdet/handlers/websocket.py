import socketio
from socketio.exceptions import ConnectionError
import cv2
import base64
import asyncio
from .detection_handler import DetectionHandler

class WebsocketOutput(DetectionHandler):
    def __init__(self, annotated_images=None):
        self.annotated_images = annotated_images
        self._conn = socketio.AsyncClient()

    async def connect(self, uri):
        while True:
            try:
                await self._conn.connect(uri)
                break
            except ConnectionError as ex:
                await asyncio.sleep(5)

    async def on_detect(self, result):
        if self.annotated_images is not None:
            image = result.annotated_image(**self.annotated_images)
        else:
            image = result.image
        _, buffer = cv2.imencode('.jpg', image)
        await self._conn.emit('detection', {
            'image': base64.b64encode(buffer),
            'boxes': [
                {
                    'rect': (int(box.x), int(box.y), int(box.w), int(box.h)),
                    'label':
                        {
                            'name': box.label.name
                        }
                }
                for box in result.bboxes
            ]
        })

    async def shutdown(self):
        await self._conn.disconnect()