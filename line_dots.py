from manim import *


def coord(x,y,z=0):
    return np.array([x,y,z])

class LineDots(Scene):
    def construct(self):
        points = [(0,3), (1, -2), (3, 1), (-2, 2.5), (-3, -1)]
        dots = VGroup(*[Dot(coord(x,y)) for x,y in points])
        self.add(NumberPlane())
        self.add(dots)

