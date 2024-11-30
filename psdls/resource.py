import sdl2.sdlimage as sdlimage
import gc

class ResourceCollector:
    
    def __init__(self) -> None:
        pass

    def clear(self):
        gc.collect()

class Image:

    def __init__(self, imagepath: str) -> None:
        self.image = sdlimage.IMG_Load(imagepath.encode())

    def free(self):
        sdlimage.IMG_Free(self.image)

class ResourceManager:

    def __init__(self) -> None:
        self.collector = ResourceCollector()

    def load_image(self, imagepath: str) -> Image:
        return Image(imagepath)
    
    def free_image(self, image: Image):
        image.free()
        self.clear()

    def clear(self):
        self.collector.clear()