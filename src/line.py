class Line:
    def __init__(self, a, b):
        self.__pointa = a
        self.__pointb = b

    def draw(self, canvas, color):
        canvas.create_line(
            self.__pointa.x,
            self.__pointa.y,
            self.__pointb.x,
            self.__pointb.y,
            fill=color,
            width=2,
        )
