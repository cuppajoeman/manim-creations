from manim import *

def display_text(self, text_vgroup, box_text=False, run_time=-1, end_wait_time=-1, remove=True):
    # the amount of time it takes to write should
    # be at the same rate that a human reads
    # on average 250 wpm - average word is 4.7 chars
    # 1175 chars per minute 19.58 chars per second
    # therefore if you have n characters, the amount of time
    # you will need is n/19.58 or approximately n/20

    total_chars = sum(len(tmob.get_tex_string()) for tmob in text_vgroup)

    reading_time = total_chars/30

    print(reading_time, text_vgroup[0].get_tex_string())

    self.play(Write(text_vgroup))

    if box_text:
        framebox = SurroundingRectangle(text_vgroup)
        self.play(Create(framebox))

    if end_wait_time == -1:
        self.wait(reading_time)
    else:
        self.wait(end_wait_time)

    # Todo might have to return the framebox so the user can have
    # a pointer to it

    if remove:
      self.play(FadeOut(text_vgroup))

      if box_text:
        self.play(FadeOut(framebox))


def create_fitted_text(self, latex):
    tex = Tex(latex)
    x_padding = 1
    tex.scale_to_fit_width(self.camera.frame_width - 2 * x_padding)
    return tex

def create_definition(self, title_tex, content_tex):
    x_padding = 1
    y_padding = 1
    x_inner_padding = 1
    y_inner_padding = 1

    width = self.camera.frame_width - 2 * x_padding
    height = self.camera.frame_height - 2 * y_padding

    content_width = width - 2 * x_inner_padding

    header = Rectangle(color="#298050", fill_color="#298050", fill_opacity=1,width=width, height=1/2)
    header.add(Tex("Definition:").next_to(header.get_left(), direction=RIGHT, buff=0.2))
    title = Tex(title_tex)
    header.add(title)
    body = Rectangle(fill_color="#c8fade", color="#298050", fill_opacity=1,width=width, height=height)


    body.add(Tex(content_tex).set_color(BLACK).scale_to_fit_width(content_width))

    definition = VGroup(header, body).arrange(DOWN, buff=0)

    return definition

def extract_key_root_and_intervals(RIC):
    # Note this returns a string right now
    # because that's how I am working - with strings.
    data = RIC.split("|")
    key_root = data[0].strip()
    intervals = data[1].strip().split()

    return [key_root, intervals]


def RIC_to_latex(RIC):
    # takes in the form
    # "11 | 0 2 4 5"

    key_root, intervals = extract_key_root_and_intervals(RIC)

    intervals = " \ ".join(intervals)

    full_str = key_root +  r"^{\hspace{-0.1cm}\urcorner}" + r" \mid " + intervals

    return r'{}'.format(full_str)

def add_key_notation(intervals_str):
    output = ""
    for i in intervals_str.split():
        output += (i + r"^{\hspace{-0.1cm}\urcorner} \ ") 
    # slice off final spaces
    return output[:-3]

def RIC_to_addition_step(RIC):
    
    key_root, intervals = extract_key_root_and_intervals(RIC)

    temp_string = ""
    for i in intervals:
        temp_string += "(" + key_root + "+" + i + ") "

    return add_key_notation(temp_string)

def RIC_to_key_intervals(RIC):
    key_root, intervals = extract_key_root_and_intervals(RIC)

    temp_string = ""
    for i in intervals:
        temp_string += str((int(key_root) + int(i)) % 12) + " "

    return add_key_notation(temp_string)
