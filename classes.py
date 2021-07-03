
class Voicing():
    def __init__(self, fretboard_representation, duration=4):
        # TODO make it take in "X X (3|4) (5|8) X X" (fret|symbol) X means nothing
        # .split if X nothing else split | and remove (,) ...
        self.fretboard_representation = fretboard_representation
        self.parse_symbols_to_latex()
        # measured in measures
        self.duration = duration

    def parse_symbols_to_latex(self):
        for fret_string_symbol in self.fretboard_representation:
            fret_string_symbol[2] = rf"${str(fret_string_symbol[2])}$"


class PageOfInfo():
    def __init__(self, paragraphs, duration):
        self.fretboard_representation = fretboard_representation
        self.parse_symbols_to_latex()
        # measured in measures
        self.duration = duration

    def parse_symbols_to_latex(self):
        for fret_string_symbol in self.fretboard_representation:
            fret_string_symbol[2] = rf"${str(fret_string_symbol[2])}$"
