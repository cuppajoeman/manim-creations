from manim import *
from data import *
from MathematicalMusicData import *
from SongData import *
from classes import *
from text_helpers import *


class MathematicalMusic(Scene):
    def construct(self):

        display_text(self, Tex("A new Musical Notation"))

        for page in pages_of_content:
            display_text(
                self,
                VGroup(
                    *[create_fitted_text(self, paragraph) for paragraph in page]
                ).arrange(DOWN, buff=1.0),
            )
            # this is cringe
            if page in before_def_page:
                if page == before_canonical:
                    title = "Canonical Mapping"
                    content = definitions[title]
                    d = create_definition(self, title, content)
                elif page == before_adding:
                    title = "Adding a Number to a Note"
                    content = definitions[title]
                    d = create_definition(self, title, content)
                elif page == before_interval:
                    title = "Interval"
                    content = definitions[title]
                    d = create_definition(self, title, content)
                elif page == before_ric:
                    title = "Rooted Interval Collection"
                    content = definitions[title]
                    d = create_definition(self, title, content)

                self.play(FadeIn(d))
                self.wait(10)
                self.play(FadeOut(d))


class GuitarBasics(Scene):
    def construct(self):

        display_text(self, Tex("An Introduction To Guitar"))

        def display_pagefull(page_of_data):
            # a page of data is an array of latex strings
            text_vgroup = VGroup()
            for data in page_of_data:
                text_vgroup.add(create_fitted_text(self, data))
            text_vgroup.arrange(DOWN, buff=1.0)

            display_text(self, text_vgroup)

        for page in how_it_works:
            display_pagefull(page)

        for page in conventions:
            display_pagefull(page)

        for page in tuning:
            display_pagefull(page)

        fretboard, fretboard_annotations = draw_fretboard(self)

        fretboard_vgr = VGroup(fretboard, fretboard_annotations)

        # for now we are going to do the animation and text manually, but in the future
        # we should find a way to automate it

        def display_fretboard_examples(examples):
            for fbex in examples:
                print(fbex)
                text_data, voicing_list = fbex

                fretboard_text = create_fitted_text(self, text_data).next_to(
                    fretboard, DOWN
                )
                display_text(self, fretboard_text, remove=False)

                play_voicing_series_simple(self, voicing_list)

                # doing this manually - because it wasn't removed
                self.play(FadeOut(fretboard_text))

            # move to single page again

        display_fretboard_examples(fretboard_examples_with_animation_data)

        self.play(FadeOut(fretboard_vgr))

        for page in fretboard_examples:
            display_pagefull(page)

        self.play(FadeIn(fretboard_vgr))

        display_fretboard_examples(anchor_point_examples_with_animation_data)

        display_fretboard_examples(
            constructing_basic_interval_collections_fretboard_examples
        )

        self.play(FadeOut(fretboard_vgr))

        for page in conclusion:
            print("conclusion", page)
            display_pagefull(page)


class TableAnimation(Scene):
    def construct(self):

        print(self.camera.frame_width, self.camera.frame_height)

        # TABLE CONSTRUCTION

        def generate_repeat_symbol_with_spaces():
            return r"\%"

        repeat_symbol = generate_repeat_symbol_with_spaces()

        class TableContext:
            def __init__(self, table, width=12, height=6):
                # assuming non-empty table
                self.table = table
                self.num_rows = len(table)
                self.num_cols = len(table[0])

                self.x_padding = 0.5
                self.y_padding = 0.2

                self.cell_width = width / self.num_cols
                self.cell_height = height / self.num_rows

                print(self.cell_width, self.cell_height)

                self.content_width = width / self.num_cols - 2 * self.x_padding
                self.content_height = height / self.num_rows - 2 * self.y_padding

        def apply_cell_sizing(t_ctx, cell, half_size=False):

            if cell.width > cell.height:
                cell.scale_to_fit_width(t_ctx.content_width / (2 if half_size else 1))
            elif cell.height >= cell.width:
                cell.scale_to_fit_height(t_ctx.content_height)

            if cell.get_tex_string() == repeat_symbol:
                cell.scale(1 / 2)

        def create_table(t_ctx, tex_table_data):
            table = VGroup()
            for row in tex_table_data:
                for table_entry in row:
                    if table_entry.double_entry:
                        first = table_entry.first_content
                        second = table_entry.second_content
                        rect_f = Rectangle(
                            width=t_ctx.cell_width / 2, height=t_ctx.cell_height
                        )
                        rect_s = Rectangle(
                            width=t_ctx.cell_width / 2, height=t_ctx.cell_height
                        )
                        apply_cell_sizing(t_ctx, first, half_size=True)
                        apply_cell_sizing(t_ctx, second, half_size=True)
                        rect_f.add(first)
                        rect_s.add(second)
                        rect = VGroup(rect_f, rect_s).arrange(buff=0)
                    else:
                        content = table_entry.content
                        rect = Rectangle(
                            width=t_ctx.cell_width, height=t_ctx.cell_height
                        )
                        apply_cell_sizing(t_ctx, content)
                        rect.add(content)

                    table.add(rect)

            table.arrange_in_grid(buff=0, cols=4)

            return table

        # drawing of tables

        class TableEntry:
            def __init__(self, content, double_entry=False):
                self.double_entry = double_entry
                self.raw_content = content
                if self.double_entry:
                    self.first_content = MathTex(content[0])
                    self.second_content = MathTex(content[1])
                else:
                    self.content = MathTex(content)
                # if double entry is true, then content is an array of length 2

        def is_RIC_notation(txt):
            # c'mon you can do better than this lamo
            return txt[0].isnumeric()

        def construct_table_series_RIC_addition_key_intervals(
            t_ctx, funcs=[RIC_to_latex, RIC_to_addition_step, RIC_to_key_intervals]
        ):
            table_series = []
            # RIC (base repr in latex)
            for fun_step in funcs:
                step_table = []
                for row in t_ctx.table:
                    table_row = []
                    for entry in row:
                        if type(entry) == list:
                            first_entry = entry[0]
                            second_entry = entry[1]
                            # assuming both are RIC's
                            if not is_RIC_notation(first_entry):
                                first_processed = first_entry
                            else:
                                first_processed = fun_step(first_entry)
                            if not is_RIC_notation(second_entry):
                                second_processed = second_entry
                            else:
                                second_processed = fun_step(second_entry)

                            table_row.append(
                                TableEntry(
                                    [first_processed, second_processed],
                                    double_entry=True,
                                )
                            )
                        elif not is_RIC_notation(entry):
                            table_row.append(TableEntry(entry))
                        else:
                            # it's RIC
                            table_row.append(TableEntry(fun_step(entry)))

                    step_table.append(table_row)
                table_series.append(create_table(t_ctx, step_table))
            return table_series

        def draw_table_series(tables, title):
            i = 0
            self.play(Write(Tex(title).next_to(tables[0], UP)))
            for table in tables:
                curr_table = table

                if i == 0:
                    self.play(FadeIn(curr_table))
                    self.wait()
                else:
                    self.play(ReplacementTransform(prev_table, curr_table))
                    self.wait()

                prev_table = curr_table
                i += 1

        t_ctx = TableContext(all_diatonics)

        # draw_table_series(construct_table_series_RIC_addition_key_intervals(blues_base), "12-bar Blues")
        draw_table_series(
            construct_table_series_RIC_addition_key_intervals(t_ctx),
            r"All Diatonic Chords",
        )


fretboard_width = 3
nut_to_bridge = 16
num_frets = 24
num_strings = 6
final_fret_position = nut_to_bridge / (2 ** (num_frets / 12))
fretboard_length = nut_to_bridge - final_fret_position


def draw_fretboard(self):
    """
    nut____________fretboard_length_______________                      Bridge
     |                                            |                        |
     |                                            | fretboard_width        |
     |                                            |                        |
     |____________________________________________|                        |

     \___________________________nut_to_bridge_____________________________/
    """

    string_names = [
        "\overline{4}_L",
        "\overline{9}",
        "\overline{2}",
        "\overline{7}",
        "\overline{11}",
        "\overline{4}_H",
    ]

    # true length of fretboard is the location of the nut
    # minus the final fret (well there's a bit more but we don't care)

    animations = []

    fretboard = VGroup()
    fretboard_annotations = VGroup()

    # animations.append(FadeIn(Rectangle(fill_color="#663300",fill_opacity=1,height=fretboard_width,width=fretboard_length)))
    fretboard.add(
        Rectangle(
            fill_color="#663300",
            fill_opacity=1,
            height=fretboard_width,
            width=fretboard_length,
        )
    )

    # We add one because there are 24 metal frets, not 23!
    # In fact there will be 25 total frets if you include the nut
    for i in range(num_frets + 1):
        """EXPLANATION
        Since this is a decreasing sequence
        where the gaps between the intervals
        is also decreasing, we need to make
        it negative to go in the right direction,
        in otherwords we are fixing this situation          and turning it into this (below)

        ____________________A____________________    ____________________B____________________
        |                   .                   |    |                   .                   |
        | final_fret_position                   |    |                   .                   |
        |                   . \                 |    |                   .                   |
        |                   .  | |  |   |    |  |    |  |    |   |  | |  .                   |
        |......................|.|..|...|....|..|    |..|....|...|..|.|......................|
        |                  /.  | |  |   |    |  |    |  |    |   |  | |  .                   |
        |                 / .               /   |    |                   .                   |
        |bridge at origin      nut_to_bridge    |    |                   .                   |
        |                   .                   |    |                   .                   |
        |_______________________________________|    |_______________________________________|

        """
        x = -nut_to_bridge / (2 ** (i / 12))
        """
                                                Shift Explanation
        Consider a rectangle centered at the origin width width fretboard_length overlapping on diagram B, then
        consider what would need to be added so that the first fret will line up with the left side of the rectangle
        """
        x += nut_to_bridge - fretboard_length / 2
        fret = Line(
            [x, -fretboard_width / 2, 0], [x, fretboard_width / 2, 0]
        ).set_color("#2d2e59")
        # animations.append(FadeIn(fret))
        fretboard.add(fret)

        text_scale = 1 / (2 ** (i / 12))
        fret_text = Tex(str(i)).scale(text_scale).next_to(fret, UP)
        # animations.append(Write(fret_text))
        fretboard_annotations.add(fret_text)

    for i in range(num_strings):
        # From top to bottom
        y = -fretboard_width / 2 + fretboard_width / 6 * i
        y += fretboard_width / 6 * 1 / 2  # in the middle

        string = Line(
            [-fretboard_length / 2, y, 0], [fretboard_length / 2, y, 0]
        ).set_color("#7b7676")
        fretboard.add(string)

        string_text = MathTex(string_names[i]).scale(0.75).next_to(string, LEFT)
        # animations.append(Write(string_text))
        fretboard_annotations.add(string_text)

    self.play(FadeIn(fretboard))
    self.play(Write(fretboard_annotations))
    # self.play(AnimationGroup(*animations, lag_ratio=0.01))

    self.wait()

    return [fretboard, fretboard_annotations]


def get_fret_markers(self, labelled_fretboard_positions):
    # TODO use VGroup check what they said in discord
    fret_markers = []
    for fretboard_position in labelled_fretboard_positions:
        fret_num = fretboard_position[0]
        string_num = fretboard_position[1]
        label = fretboard_position[2]

        x = -nut_to_bridge / (2 ** (fret_num / 12))
        x += nut_to_bridge - fretboard_length / 2  # See shift explanation

        y = -fretboard_width / 2 + fretboard_width / 6 * string_num
        y += fretboard_width / 6 * 1 / 2  # in the middle

        if fret_num != 0:
            # Then fret_num > 0
            prev_x = -nut_to_bridge / (2 ** ((fret_num - 1) / 12))
            prev_x += nut_to_bridge - fretboard_length / 2  # See shift explanation

            fret_dist = x - prev_x

            behind_fret_position = fret_dist * 1 / 4

            v = [x - behind_fret_position, y, 0]
        else:
            v = [x, y, 0]

        # Because it doesn't need to be half as small after 12 steps
        text_scale = 1 / (1.5 ** (fret_num / 12))

        # fret_marker = LabeledDot(Tex(label,color=BLACK).scale(text_scale)).move_to(v)
        # fret_marker = LabeledDot(Tex(label,color=BLACK)).scale_to_fit_height(fretboard_width * 1/2).scale(text_scale).move_to(v)
        fret_marker = (
            LabeledDot(Tex(label, color=BLACK))
            .scale_to_fit_height(fretboard_width / 6)
            .scale(text_scale)
            .move_to(v)
        )

        fret_markers.append(fret_marker)

    return fret_markers


def play_voicing_series_simple(self, voicings, BPM=120):
    """
    Given a list of voicings in the format specified by draw voicing
    draw the voicings as a series in time
    """
    if len(voicings) != 0:
        animation_duration = 0
        for i in range(len(voicings)):
            voicing = get_fret_markers(self, voicings[i].fretboard_representation)
            voicing_gr = VGroup(*list(voicing))

            def bpm_to_measure_length(BPM, beats_in_a_measure=4):
                # returns in seconds
                beats_per_second = BPM * 1 / 60
                seconds_per_beat = 1 / beats_per_second
                measure_length = seconds_per_beat * beats_in_a_measure

                return measure_length

            duration = voicings[i].duration * bpm_to_measure_length(BPM)

            if i == 0:
                # on the first iteration
                fade = FadeIn(voicing_gr)
                animation_duration = fade.get_run_time()
                self.play(fade)
                self.wait(duration - animation_duration)
                if len(voicings) == 1:
                    self.play(FadeOut(voicing_gr))
                    break
            else:
                replace_transform = ReplacementTransform(prev_voicing_gr, voicing_gr)
                self.play(replace_transform)
                self.wait(duration - replace_transform.get_run_time())
                # have to fade out on the last iteration
                if i == len(voicings) - 1:
                    self.play(FadeOut(voicing_gr))

            prev_voicing_gr = voicing_gr

        return voicing_gr


class FretboardAnimation(Scene):
    def construct(self):

        draw_fretboard(self)

        voicings = [
            Voicing([[3, 0, "0"], [4, 2, "11"], [4, 3, "4"], [3, 4, "7"]], 1),
            Voicing([[5, 0, "2"], [5, 2, "0"], [5, 3, "5"], [5, 4, "9"]], 1),
            Voicing([[7, 0, "4"], [7, 2, "2"], [7, 3, "9"], [7, 4, "11"]], 1),
            Voicing([[8, 0, "5"], [9, 2, "4"], [9, 3, "9"], [8, 4, "0"]], 1),
            Voicing([[10, 0, "7"], [10, 2, "5"], [11, 3, "11"], [10, 4, "2"]], 1),
            Voicing([[12, 0, "9"], [12, 2, "7"], [12, 3, "0"], [12, 4, "4"]], 1),
            Voicing([[14, 0, "11"], [14, 2, "9"], [14, 3, "2"], [13, 4, "5"]], 1),
            Voicing([[15, 0, "0"], [16, 2, "11"], [16, 3, "4"], [15, 4, "7"]], 1),
            Voicing([[17, 0, "2"], [17, 2, "0"], [17, 3, "5"], [17, 4, "9"]], 1),
            Voicing([[19, 0, "4"], [19, 2, "2"], [19, 3, "9"], [19, 4, "11"]], 1),
            Voicing([[20, 0, "5"], [21, 2, "4"], [21, 3, "9"], [20, 4, "0"]], 1),
            Voicing([[22, 0, "7"], [22, 2, "5"], [23, 3, "11"], [22, 4, "2"]], 1),
            Voicing([[24, 0, "9"], [24, 2, "7"], [24, 3, "0"], [24, 4, "4"]], 1),
        ]

        play_voicing_series_simple(self, voicings)


class BluesImprov(Scene):
    def construct(self):

        draw_fretboard(self)

        voicings = [
            Voicing(
                [[12, 1, "$0$"], [12, 3, "$10$"], [13, 4, "$3$"], [12, 5, "$7$"]], 4
            ),
            Voicing(
                [
                    [12, 1, "$0$"],
                    [10, 2, "$3$"],
                    [10, 3, "$8$"],
                    [13, 4, "$3$"],
                    [10, 5, "$5$"],
                ],
                2,
            ),
            Voicing([[7, 2, "$0$"], [9, 3, "$7$"], [8, 4, "$10$"], [8, 5, "$3$"]], 2),
            Voicing([[9, 2, "$2$"], [9, 3, "$7$"], [8, 4, "$10$"], [10, 5, "$5$"]], 1),
            Voicing(
                [[10, 2, "$3$"], [10, 3, "$8$"], [10, 4, "$0$"], [10, 5, "$5$"]], 1
            ),
            Voicing(
                [[10, 2, "$3$"], [12, 3, "$10$"], [10, 4, "$0$"], [12, 5, "$7$"]], 2
            ),
            Voicing(
                [
                    [0, 1, "$0$"],
                    [5, 2, "$10$"],
                    [5, 3, "$3$"],
                    [0, 4, "$2$"],
                    [0, 5, "$7$"],
                ],
                4,
            ),
            Voicing(
                [
                    [3, 0, "$10$"],
                    [0, 1, "$0$"],
                    [3, 2, "$8$"],
                    [0, 3, "$10$"],
                    [1, 4, "$3$"],
                ],
                2,
            ),
            Voicing([[5, 0, "$0$"], [5, 3, "$3$"], [7, 4, "$9$"], [7, 5, "$2$"]], 2),
            Voicing([[7, 1, "$7$"], [7, 3, "$5$"], [8, 4, "$10$"], [7, 5, "$2$"]], 1),
            Voicing([[8, 1, "$8$"], [7, 3, "$5$"], [10, 4, "$0$"], [8, 5, "$3$"]], 1),
            Voicing(
                [[12, 1, "$0$"], [12, 3, "$10$"], [13, 4, "$3$"], [12, 5, "$7$"]], 2
            ),
        ]

        play_voicing_series_simple(self, voicings, 152)
