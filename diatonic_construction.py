
from manim import *
from MathematicalMusicData import *
from numpy import *
from text_helpers import *

class DiatonicConstruction(Scene):
   def construct(self):
       base_radius = 2
       a = Circle(base_radius)
       
       interval_collections = {
           "Major" : r"$\overline{\mathcal{K}}$ 2 $\circ$ 2 $\circ$ 1 $\circ$ 2 $\circ$ 2 $\circ$ 2 $\circ$ 1".split(),
           "Natural Minor" : r"$\overline{\mathcal{K}}$ 2 $\circ$ 1 $\circ$ 2 $\circ$ 2 $\circ$ 1 $\circ$ 2 $\circ$ 2".split(),
           "Harmonic Minor" : r"$\overline{\mathcal{K}}$ 2 $\circ$ 1 $\circ$ 2 $\circ$ 2 $\circ$ 1 $\circ$ 3 $\circ$ 1".split(),
           "Melodic Minor" : r"$\overline{\mathcal{K}}$ 2 $\circ$ 1 $\circ$ 2 $\circ$ 2 $\circ$ 2 $\circ$ 2 $\circ$ 1".split(),
       }

       def generate_and_draw_RIC(intervals, idx_to_position, num_elements, start_pos, skip_list, x_shift):

           arrow_group = VGroup()

           start_note = sum(intervals[:start_pos])
            
           total = 0
           index = 0

           num_intervals = len(intervals)

           text_list = []
           for skip in skip_list:
               for i in range(skip):
                   total += intervals[(start_pos + index) % num_intervals]
                   index += 1
               text_list.append(total)
           # We don't care about the intervals between, those are there for looks
           start_pos = start_pos * 2
           for i, skip in enumerate(skip_list):
               start_point = a.point_from_proportion(idx_to_position[start_pos % num_elements])
               # because half of them are notes
               new_pos = start_pos + skip*2
               end_point = a.point_from_proportion(idx_to_position[new_pos % num_elements])

               # move points outward a little bit

               outward_scale = 1.1

               start_point *= outward_scale
               end_point *= outward_scale

               dist_between = np.linalg.norm(start_point - end_point)

               arrow_rad = dist_between/2

               arrow = CurvedArrow(start_point, end_point, radius=arrow_rad)

               middle = arrow.get_arc_center() * arrow_rad * 1.4

               arrow.add(Tex("+" + str(text_list[i])).move_to(middle))

               arrow_group.add(arrow)

               start_pos = new_pos


           RIC_string = str(int(start_note)) + r" | 0 " + ' '.join([str(x) for x in text_list])


           RIC_mob = MathTex(RIC_to_latex(RIC_string))

           return [RIC_mob.shift(x_shift), arrow_group.shift(x_shift)]

       def construct_all_rics(custom_text, shift_list):

           intervals = [int(x) for x in custom_text if "c" not in x]
           num_intervals = len(intervals)
           num_elements = len(custom_text)
           circle_group = VGroup()
           # +1 to account for 1 and 0 being at the same position
           values = np.linspace(0,1,num_elements + 1)
           idx_to_position = {i: values[i] for i in range(num_elements)}

           for idx, val in idx_to_position.items():
               circle_group.add(Tex(custom_text[idx]).move_to(a.point_from_proportion(val)))

           self.play(Create(circle_group))
           construction_shift = [self.camera.frame_width/2 * 1/3 * -1, 0, 0]
           self.play(circle_group.animate.move_to(construction_shift))

           RICs = VGroup()

           for i in range(num_intervals):

               new_RIC, arrow_group = generate_and_draw_RIC(intervals, idx_to_position, num_elements, i, [2,2,2], construction_shift)

               self.play(Create(arrow_group, lag_ratio = 1))

               self.play(LaggedStart(FadeIn(new_RIC), FadeOut(RICs), lag_ratio = 0.5))

               RICs.add(new_RIC.copy())

               x_pos = self.camera.frame_width * 1/2 *  1/2

               if len(RICs) != 0:
                   RICs.arrange(DOWN, buff=0.2).set_x(x_pos)

               self.play(FadeIn(RICs), FadeOut(new_RIC), FadeOut(arrow_group))

            # leave it there for a while
           self.wait(5)
           self.play(FadeOut(RICs),FadeOut(circle_group))

       display_text(self,Tex("Diatonic Chord Construction"))

       pages_of_content = [
               [
               r"Now that we have a good foundation in the new notation, we can start putting it to use and seeing how well it performs.",
               r"The first task it will have is to construct the diatonic chords of a scale.",
               r"I'll explain what this means on the next page.",
               ],
               [
               r"Given a key, the diatonic chords of a scale are constructed by stacking relative intervals of size 3 or 4 onto each note of the scale.",
               r"Additionally the notes in each of the chords must be from the key.",
               r"So the diatonic chords of a key are simply rooted interval collections such that the notes produced by these interval collections are also part of the key. And that there is a specific gap size we need between consecutive intervals.",
               ],
               [
               r"It turns out that the four main types of scales have the property that when their relative interval patterns are laid out into a circle, it's always the case that the sum of any two consecutive intervals is always 3 or 4.",
               r"This means that an equivalent way to construct the diatonic chords is to lay out the relative intervals in a circle and then jump every second note (meaning you go over two relative intervals).",
               r"Another thing to note is how many notes you want in your chords, the simplest way would to have 2 or 3 notes, but we are going to build interval collections with 4 notes, as these chords have more color/complexity. To construct chords with 4 notes you need to do 3 jumps.",
               ],
               [
               r"We will start the construction of the interval collections by starting with a circle which represents the relative interval jumps that define the current scale we are working with.",
               r"Notice that between each of the intervals there is a small circle, each small circle represents a note that is constructed by adding the previous relative interval to the last note.",
               r"Finally see that there is one note which is notated by $\overline{\mathcal{K}}$ this is the root of the key. Now, let's get started.",
               ]

       ]

       conclusion_page = [
               r"I hope you enjoyed seeing the power of using this notation we have developed, and how it allows us to work at different levels of complexity",
               r"If you have any questions from this video, join the zulip chat room.",
               ]

       for page in pages_of_content:
           display_text(self,VGroup(*[create_fitted_text(self, paragraph) for paragraph in page]).arrange(DOWN, buff=1.0))

       for title, interval_collection_text in interval_collections.items():
           display_text(self,Tex(title))
           construct_all_rics(interval_collection_text, [2,2,2])

       display_text(self,VGroup(*[create_fitted_text(self, paragraph) for paragraph in conclusion_page]).arrange(DOWN, buff=1.0))






