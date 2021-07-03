from manim import *
from numuse import  converters
import numuse.music
from fractions import Fraction

def create_line_graph(self, x_vals, y_vals):
    x_padding = 1
    #y_padding = 1
    #print((min(y_vals)-1, max(y_vals)+1))
    print(self.camera.frame_width - 2 * x_padding)
    plane = NumberPlane(
        x_range = (0, max(x_vals)),
        y_range = (min(y_vals)-1, max(y_vals)+1),
        #x_length = self.camera.frame_width - 2 * x_padding,
        x_length = 12,
        #y_length = self.camera.frame_height - 2 * y_padding,
        y_length = 3,
        axis_config={"include_numbers": True},
    )
    plane.center()
    line_graph = plane.get_line_graph(
        x_values = x_vals,
        y_values = y_vals,
        line_color=GOLD_E,
        vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
        stroke_width = 4,
    )
    return VGroup(plane, line_graph)

class LineGraphExample(Scene):
    def construct(self):
        b = 1
        # half
        h = 1 / 2
        # thirds
        t = Fraction(b, 3)
        # two thirds
        tt = 2 * t

        jens_solo_arps = [
            [("0' 4' 7' 11' R", [tt, t, tt, t + b, b])],
            [("R 7' 4' 7' 7'", [tt, t, tt, t + b, b])],
            [("9' 6' R", [b + tt, t + b, b])],
            [("6' 2' 9' 6' 0'' 9' R", [tt, t, tt, t, tt, t, b])],
            #[("5' 2' 9' 0'' 5'", [tt, t, tt, t + b, b])],
            #[("2' 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
            #[("4' 4' 4' 0'", [b, tt, t + b, b])],
            #[("11 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
            #[("4' 0' R 4' R 4' R 4'", [tt, t, tt, t, tt, t, tt, t])],
            #[("7' 4' 7' 7' R 11'", [tt, t, tt, t, 1 + tt, t])],
            #[("0'' 0'' 9' R 9' 6'", [b, tt, t, tt, t, b])],
            #[("R 2' 2' 2' R", [b, b, tt, t, b])],
            #[("0'' 0'' 9' R 9' 5'", [b, tt, t, tt, t, b])],
            #[("R 2' 11 5' 2' 11 7", [b, tt, t, tt, t, tt, t])],
            #[("4' 0' R 4' 0' R", [tt, t, tt, t, b, b])],
            #[("7' 4' 7' 10' R", [tt, t, tt, t + b, b])],
            #[("R 9 0' 9 0' 9", [b, b, tt, t, tt, t])],
            #[("5 9 0' 4' R", [tt, t, tt, t + b, b])],
            #[("R 0' 4' 0' R", [b, b, tt, t, b])],
            #[("9 0' 5 R", [b, tt, t + b, b])],
            #[("2' R 0'' 6' 9' 6'", [b, b, tt, t, tt, t])],
            #[("0'' 0'' 9' R", [b, tt, t + b, b])],
            #[("9' R 9' 2' 5' 2'", [b, b, tt, t, tt, t])],
            #[("11 11 2' R", [b, tt, t + b, b])],
            #[("4' 0' 7' 0' R 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t + b])],
            #[("7' 11' R", [tt, t + b, b])],
            #[("6' 2' 9' 2' R 9'", [tt, t, tt, t, b, b])],
            #[("0'' 6' R 9' R", [tt, t, tt, t + b, b])],
            #[("9' 2' R 5' 2'", [tt, t, tt, t + b, b])],
            #[("5' 11 R 2' 5'", [tt, t, tt, t + b, b])],
            #[("4' 0' 7' 4' 7' 11'", [tt, t, tt, t, tt, t + b])],
            #[("R", [4 * b])],
        ]

        all_graphs = VGroup()
        points = []
        measures = converters.parse_music_measures(jens_solo_arps)
        m = numuse.music.Music(measures, 120)

        point_row = []
        measure_count = 0
        for measure in m.measures:
            # TODO remove hardcoded 4
            if measure_count % 4 == 0 and measure_count != 0:
                x_vals, y_vals = zip(*point_row)
                print(x_vals, y_vals)
                points.append((x_vals, y_vals))
                point_row = []
            for line in measure.lines:
                for moment in line.moments:
                    if len(moment.notes.notes) != 0:
                       point_row.append((moment.time, list(moment.notes.notes)[0].note))
            measure_count += 1
        #print([float(x) for x in x_vals], [float(y) for y in y_vals])

        graphs = []
        for point_row in points:
            x_vals, y_vals = point_row
            graphs.append(create_line_graph(self, x_vals, y_vals))

        all_graphs = VGroup(*graphs)
        all_graphs.arrange(DOWN, buff=0.5)
        #print(all_graphs.height)
        #config.frame_height = all_graphs.height 
        #config.frame_size = (1080, all_graphs.height * Pixels)
        self.add(all_graphs)

