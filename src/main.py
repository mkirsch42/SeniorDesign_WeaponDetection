from objdet.controller import Controller
from objdet.handlers import *
from objdet.inputs import ImageDirectory
from objdet.detection.models import YOLOModel, NoModel
import time
import asyncio

controller = Controller(
    ImageDirectory('/input/testIR3', scramble=True, loop=True),
    YOLOModel(
        '/input/model_IR/obj.cfg',
        '/input/model_IR/obj4.weights',
        '/input/model_IR/obj.data'
    ))
    # NoModel())

# window_output = CV2WindowOutput('YOLO', annotated_images={'font_scale':0.4, 'font_thickness':1, 'padding':1})
# controller.add_handler(window_output)

loop = asyncio.get_event_loop()

websocket_output = WebsocketOutput()
loop.run_until_complete(websocket_output.connect('ws://webserver:3030'))
controller.add_handler(websocket_output)


start = time.time()

n = loop.run_until_complete(controller.main_loop())

end = time.time()

loop.run_until_complete(controller.shutdown())
loop.close()

print(f'{n} images in {end-start} seconds')
print(f'{1000 * (end-start)/n} ms per image', flush=True)

# window_output.wait_for_key()
# window_output.close_window()
