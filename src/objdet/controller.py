import asyncio

class Controller():
    def __init__(self, input_source, model):
        self.input_source = input_source
        self.model = model
        self._handlers = []
    
    async def __aiter__(self):
        async for image in self.input_source:
            result = await self.model.detect(image[0])
            await asyncio.gather(*[handler.on_detect(result) for handler in self._handlers])
            yield result
    
    async def main_loop(self, num_loops=0):
        n = 0
        async for _ in self:
            n += 1
            if n == num_loops: break
        return n

    async def shutdown(self):
        await asyncio.gather(*[handler.shutdown() for handler in self._handlers])

    def add_handler(self, handler):
        self._handlers.append(handler)