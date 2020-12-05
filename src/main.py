from objdet.controller import Controller
from objdet.handlers import *
from objdet.inputs import ImageDirectory
from objdet.detection.models import YOLOModel
import time

controller = Controller(
    ImageDirectory('/input/test', scramble=True, loop=True),
    YOLOModel(
        '/input/model_2classes/obj.cfg',
        '/input/model_2classes/obj.weights',
        '/input/model_2classes/obj.data'
    ))

window_output = CV2WindowOutput('YOLO')
window_output.wait_for_key()
controller.add_handler(window_output)

start = time.time()

n = controller.main_loop(50)

end = time.time()

print(f'{n} images in {end-start} seconds')
print(f'{1000 * (end-start)/n} ms per image', flush=True)

window_output.wait_for_key()
window_output.close_window()