from manim import *
from data import *
from MathematicalMusicData import *
from SongData import *
from classes import *
from text_helpers import *
import numuse.music
import numuse.converters
import instmuse.converters
from fractions import Fraction

import instmuse.stringed_instrument
from typing import List, Dict

fretboard_width = 3
nut_to_bridge = 16
num_frets = 24
num_strings = 6
final_fret_position = nut_to_bridge / (2 ** (num_frets / 12))
fretboard_length = nut_to_bridge - final_fret_position

def draw_fretboard(self):
    r"""
    nut____________fretboard_length_______________                      Bridge
     |                                            |                        |
     |                                            | fretboard_width        |
     |                                            |                        |
     |____________________________________________|                        |

     \___________________________nut_to_bridge_____________________________/
    """

    string_names = [
        r"\overline{4}_L",
        r"\overline{9}",
        r"\overline{2}",
        r"\overline{7}",
        r"\overline{11}",
        r"\overline{4}_H",
    ]

    # true length of fretboard is the location of the nut
    # minus the final fret (well there's a bit more but we don't care)

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
        r"""EXPLANATION
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


def play_MGNCs(self, MGNCs: List[numuse.music.Moment], measure_length: float, beats_in_a_measure: int):
    """
    Given a list of voicings in the format specified by draw voicing
    draw the voicings as a series in time
    """
    if len(MGNCs) != 0:
        animation_duration = 0
        for i in range(len(MGNCs)):
            curr_MGNC =  MGNCs[i]
            markers = get_fret_markers(curr_MGNC.notes.modular_grid_positions, curr_MGNC.notes.modular_grid_labels)
            markers_gr = VGroup(*markers)

            # This line will have to change when I implement change of tempo
            duration = (curr_MGNC.duration / beats_in_a_measure) * measure_length

            if i == 0:
                # on the first iteration
                fade = FadeIn(markers_gr)
                animation_duration = fade.get_run_time()
                self.play(fade)
                self.wait(duration - animation_duration)
                if len(MGNCs) == 1:
                    self.play(FadeOut(markers_gr))
                    break
            else:
                replace_transform = ReplacementTransform(prev_markers_gr, markers_gr)
                self.play(replace_transform)
                self.wait(duration - replace_transform.get_run_time())
                # have to fade out on the last iteration
                if i == len(MGNCs) - 1:
                    self.play(FadeOut(markers_gr))

            prev_markers_gr = markers_gr

        return markers_gr

def get_fret_markers(fretboard_positions: Dict[int, int], fretboard_labels: Dict[int, str]):
    # TODO use VGroup check what they said in discord
    fret_markers = []
    for string_pos, fret_pos in fretboard_positions.items():
        label = fretboard_labels[string_pos]

        x = -nut_to_bridge / (2 ** (fret_pos / 12))
        x += nut_to_bridge - fretboard_length / 2  # See shift explanation

        y = -fretboard_width / 2 + fretboard_width / 6 * string_pos
        y += fretboard_width / 6 * 1 / 2  # in the middle

        if fret_pos != 0:
            # Then fret_pos > 0
            prev_x = -nut_to_bridge / (2 ** ((fret_pos - 1) / 12))
            prev_x += nut_to_bridge - fretboard_length / 2  # See shift explanation

            fret_dist = x - prev_x

            behind_fret_position = fret_dist * 1 / 4

            v = [x - behind_fret_position, y, 0]
        else:
            v = [x, y, 0]

        # Because it doesn't need to be half as small after 12 steps
        text_scale = 1 / (1.5 ** (fret_pos / 12))

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


class FretboardAnimation(Scene):
    def construct(self):

        draw_fretboard(self)

        b = 1
        # half
        h = 1 / 2
        # thirds
        t = Fraction(b, 3)
        # two thirds
        tt = 2 * t

        main =[ 
            [("(X X 9 10 10 11) ", [4*b])],
            [("(X X 9 9 10 10) ", [4*b])],
            [("(X X 9 7 10 9) ", [4*b])],
            [("(X X 9 9 8 10) ", [4*b])],
            [("(X X 7 9 7 10)", [4*b])],
            [("(X X 7 9 6 10)", [4*b])],
            [("(8 X 7 7 6 X)", [4*b])],
            [("(8 X 7 7 6 X)", [4*b])],
            [("(7 X 6 7 5 X)", [4*b])],
            [("(7 X 6 7 5 X)", [4*b])],
            [("(X 5 X 5 5 X) (X 5 X 5 6 X)", [2*b, 2*b])],
            [("(X 5 X 5 6 5)", [4*b])],
            [("(X 5 X 5 5 X) (X 5 X 5 5 4)", [2*b, 2*b])],
            [("(X 5 X 5 5 4)", [4*b])],
            ]

        main2 =[ 
            [("(X X 9 10 10 11) (X X 9 9 10 10)", [3*b, b])],
            [("(X X 9 9 10 10) (X X 9 7 10 9)", [2*b, 2*b])],
            [("(X X 9 9 8 10) ", [4*b])],
            [("(X X 7 9 7 10)", [4*b])],
            [("(X X 7 9 6 10)", [4*b])],
            [("(8 X 7 7 6 X)", [4*b])],
            [("(8 X 7 7 6 X)", [4*b])],
            [("(7 X 6 7 5 X)", [4*b])],
            [("(7 X 6 7 5 X)", [4*b])],
            [("(X 5 X 5 5 X) (X 5 X 5 6 X)", [2*b, 2*b])],
            [("(X 5 X 5 6 5)", [4*b])],
            [("(X 5 X 5 5 X) (X 5 X 5 5 4)", [2*b, 2*b])],
            [("(X 5 X 5 5 4)", [4*b])],
            ]
        # TODO develop the equiavlent form of rootedintervalcollection but for modulargridnotecollection
        two_five_one = [
            [("(X X 10 10 10 12) (X X 10 10 10 13)", [2*b, 2*b])],
            *main,
            [("(X 4 X 5 5 4)", [4*b])],
            [("(X 3 X 4 4 3)", [4*b])],
            [("(X 3 X 4 4 3) (X 5 X 6 6 5)", [2*b, 2*b])],
            [("(X 7 X 8 9 7) (X 9 X 9 9 9)", [2*b, 2*b])],
            [("(X 11 X 11 11 11) (X 10 X 10 10 10)", [2*b, 2*b])],
            [("(X 10 X 10 10 12) (X 10 X 10 10 10)", [2*b, 2*b])],
            *main2,
            [("(X 5 X 4 5 3)", [4*b])],
            [("(X 5 X 4 5 3)", [4*b])],
            [("(X 3 5 4 5 X)", [4*b])],
            [("(X 3 5 4 5 3)", [4*b])],


        ]

        #print(generate_MGNCs_from_MG_shorthand("(X 5 X 5 5 5) (X X 5 7 6 7) (X 3 5 4 5 X)"))
        measures = numuse.converters.parse_music_measures(two_five_one, instmuse.converters.generate_MGNCs_from_MG_shorthand)
        m = numuse.music.Music(measures, 122)

        print("PLUGG", m.measure_length)

        play_MGNCs(self, m.continuous, m.measure_length, m.beats_in_a_measure)

