class Product:
    def __init__(self, name, url, image):
        self.name = name
        self.__image = image
        self.url = url
