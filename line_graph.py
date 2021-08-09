from manim import *
from numuse import  converters
import numuse.music
from fractions import Fraction
import math
import graph_music_data


SCALE = 12

def create_line_graph(x_values, y_values, x_start, x_end, width, height ):
    plane = NumberPlane(
        #x_range = (math.floor(min(x_values)), math.ceil(max(x_values))),
        x_range = (x_start, x_end),
        y_range = (min(y_values)-1, max(y_values)+1),
        #x_length = self.camera.frame_width - 2 * x_padding,
        x_length = width,
        #y_length = self.camera.frame_height - 2 * y_padding,
        y_length = height,
        #axis_config={"include_numbers": True},
        axis_config={"include_numbers": False},
    )
    plane.center()
    line_graph = plane.get_line_graph(
        x_values = x_values,
        y_values = y_values,
        line_color=GOLD_E,
        vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
        vertex_dot_radius=1/8,
        stroke_width = 5,
    )
    labels = VGroup()


    offset_scale = 0.5
    for i in range(len(x_values)):
        x_pos = x_values[i]
        y_pos = y_values[i]
        # assuming plot of more than 2 notes
        assert len(x_values) >= 2
        if i == 0:
            #about to figure out the direction of it 
            y_next = y_values[i+1]
            if y_next > y_pos:
                # put text 
                annotate_offset = [0, offset_scale]
            else:
                annotate_offset = [0, -offset_scale]
        elif i == len(x_values)-1:
            y_prev = y_values[i-1]
            if y_prev > y_pos:
                # put text 
                annotate_offset = [0, offset_scale]
            else:
                annotate_offset = [0, -offset_scale]
        else:
            y_prev = y_values[i-1]
            y_next = y_values[i+1]
            between = y_prev <= y_pos <= y_next or y_prev >= y_pos >= y_next
            if between:
                # downhill
                if y_prev >= y_pos:
                    annotate_offset = [0, offset_scale]
                else:
                    annotate_offset = [0, -offset_scale]
            elif y_pos <= y_prev:
                # v formation put text in v
                annotate_offset = [0, offset_scale]
            elif y_pos >= y_prev:
                # mountain top put text under peak
                annotate_offset = [0, -offset_scale]

        # add z componenent
        annotate_offset.append(0)
        label = Tex(str(y_values[i] % 12), color=WHITE).scale(.5)
        print(annotate_offset)
        #labels.add(label.next_to(line_graph["vertex_dots"][i], np.array(annotate_offset)))
        labels.add(label.move_to(line_graph["vertex_dots"][i]))


    return VGroup(plane, line_graph, labels)



class LineGraphExample(Scene):
    def construct(self):


        self.camera.background_color = WHITE
        
        width=SCALE* 1
        height=SCALE * math.sqrt(2)



        all_graphs = VGroup()
        points = []
        measures = converters.parse_music_measures(graph_music_data.st_thomas)
        num_lines = len(measures) // 4
        graph_height = height / num_lines
        m = numuse.music.Music(measures, 120)

        def convert_points_to_x_y_list(points):
            return zip(*points)

        point_row = []
        measure_count = 0
        for measure in m.measures:
            # TODO remove hardcoded 4
            if measure_count % 4 == 0 and measure_count != 0:
                x_vals, y_vals = convert_points_to_x_y_list(point_row)
                points.append((x_vals, y_vals))
                point_row = []

            for line in measure.lines:
                for moment in line.moments:
                    if len(moment.notes.notes) != 0:
                       point_row.append((moment.time, list(moment.notes.notes)[0].note))
            measure_count += 1
        #print([float(x) for x in x_vals], [float(y) for y in y_vals])

        # adds in the last one
        points.append(tuple(convert_points_to_x_y_list(point_row)))


        # If the input was less than one measure
        if measure_count <= 4:
            points.append(tuple(convert_points_to_x_y_list(point_row)))

        graphs = []
        start_idx = 0
        for point_row in points:
            row_length = 4 * 4
            x_vals, y_vals = point_row
            graphs.append(create_line_graph(x_vals, y_vals, start_idx, start_idx + row_length, width, graph_height))
            start_idx += row_length

        all_graphs = VGroup(*graphs)
        #all_graphs.arrange(DOWN, buff=0.5)
        all_graphs.arrange(DOWN,buff=0)

        #print(all_graphs.height)
        #config.frame_height = all_graphs.height 
        #config.frame_size = (1080, all_graphs.height * Pixels)
        self.add(all_graphs)
        self.add(Tex("St. Thomas", color=BLACK).next_to(all_graphs, UP))

