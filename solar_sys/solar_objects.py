# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, type, radius, color, mass, coordinates, velocity, Fx, Fy):
        """Признак объекта звезды"""
        self.type = type
        """Масса звезды"""
        self.mass = mass
        """Координата по оси **x**"""
        self.x = coordinates[0]
        """Координата по оси **y**"""
        self.y = coordinates[1]
        """Скорость по оси **x**"""
        self.Vx = velocity[0]
        """Скорость по оси **y**"""
        self.Vy = velocity[1]
        """Сила по оси **x**"""
        self.Fx = Fx
        """Сила по оси **y**"""
        self.Fy = Fy
        """Радиус звезды"""
        self.R = radius
        """Цвет звезды"""
        self.color = color

class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self, type, radius, color, mass, coordinates, velocity, Fx, Fy):
        """Признак объекта звезды"""
        self.type = type
        """Масса звезды"""
        self.mass = mass
        """Координата по оси **x**"""
        self.x = coordinates[0]
        """Координата по оси **y**"""
        self.y = coordinates[1]
        """Скорость по оси **x**"""
        self.Vx = velocity[0]
        """Скорость по оси **y**"""
        self.Vy = velocity[1]
        """Сила по оси **x**"""
        self.Fx = Fx
        """Сила по оси **y**"""
        self.Fy = Fy
        """Радиус звезды"""
        self.R = radius
        """Цвет звезды"""
        self.color = color