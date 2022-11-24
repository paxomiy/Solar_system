from solar_vis import *
class Star(DrawableObject):
    def __init__(self):
        """Тип данных, описывающий звезду.
        Содержит массу, координаты, скорость звезды,
        а также визуальный радиус звезды в пикселах и её цвет.
        """

        self.type = "star"
        self.m=0
        """Признак объекта звезды"""

        """Масса звезды"""

        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.Vx = 0
        """Скорость по оси **x**"""

        self.Vy = 0
        """Скорость по оси **y**"""

        self.ax = 0
        """Сила по оси **x**"""

        self.ay = 0
        """Сила по оси **y**"""

        self.R = 5
        """Радиус звезды"""

        self.color = "red"
        """Цвет звезды"""

        self.image = None
        """Изображение звезды"""


class Planet(DrawableObject):
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    def __init__(self):
        """Тип данных, описывающий звезду.
        Содержит массу, координаты, скорость звезды,
        а также визуальный радиус звезды в пикселах и её цвет.
        """

        self.type = "planet"

        """Признак объекта звезды"""
        self.m = 0
        """Масса звезды"""

        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.Vx = 0
        """Скорость по оси **x**"""

        self.Vy = 0
        """Скорость по оси **y**"""

        self.ax = 0
        """Сила по оси **x**"""

        self.ay = 0
        """Сила по оси **y**"""

        self.R = 5
        """Радиус планеты"""

        self.color = "green"
        """Цвет планеты"""

        self.image = None
        """Изображение планеты"""