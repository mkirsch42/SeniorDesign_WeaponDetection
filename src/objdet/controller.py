

class Controller():
    def __init__(self, input_source, model):
        self.input_source = input_source
        self.model = model
        self._handlers = []
    
    def __iter__(self):
        for image in self.input_source:
            result = self.model.detect(image[0])
            for handler in self._handlers:
                handler.on_detect(result)
            yield result
    
    def main_loop(self, num_loops=0):
        n = 0
        for _ in self:
            n += 1
            if n == num_loops: break
        return n

    def add_handler(self, handler):
        self._handlers.append(handler)