
from manim import *
from MathematicalMusicData import *
from numpy import *

class Scratch(Scene):
    def construct(self):
        c = Circle(radius=3)

        self.play(Create(c))

        iterations = []
        for k in range(1, 100):
            for num_elements in range(3, 100):
                values = np.linspace(0,1,num_elements + 1)
                idx_to_value = {i: values[i] for i in range(num_elements)}

                info  = VGroup(Tex(rf"Points: {num_elements}"), Tex(rf"Multiple: {k}")).arrange(DOWN, buff=1).move_to([self.camera.frame_width/2 * 4/6 * -1, 0, 0])

                lines = []

                for idx, val in idx_to_value.items():
                    lines.append(Line(c.point_from_proportion(val), c.point_from_proportion(idx_to_value[(k * idx) % num_elements])))

                l_group = VGroup(info, *lines)
                iterations.append(l_group)

        for vgr in iterations:
            self.play(Create(vgr))
            self.play(FadeOut(vgr))


        #self.play(LaggedStart(*[VGroup(*[VGroup(*[Line(c.point_from_proportion(x), k * c.point_from_proportion(x)) for x in np.linspace(0,1, num_elements + 1)]) for k in range(0, 100)]) for num_elements in range(1, 100)]))

