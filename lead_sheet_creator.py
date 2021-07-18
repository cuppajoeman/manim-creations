import math
from manim import *
from SongData import *
from text_helpers import *

class TableAnimation(Scene):
    def construct(self):

        print(self.camera.frame_width, self.camera.frame_height)

        # TABLE CONSTRUCTION

        self.camera.background_color = WHITE

        def generate_repeat_symbol_with_spaces():
            return r"\%"

        repeat_symbol = generate_repeat_symbol_with_spaces()

        scale = 6

        class TableContext:
            def __init__(self, table, width=scale * 1, height=scale * math.sqrt(2)):
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

        def create_table(t_ctx, tex_table_data, table_color=WHITE):
            table = VGroup()
            for row in tex_table_data:
                for table_entry in row:
                    if table_entry.double_entry:
                        first = table_entry.first_content
                        second = table_entry.second_content
                        rect_f = Rectangle(
                            width=t_ctx.cell_width / 2, height=t_ctx.cell_height, color=table_color
                        )
                        rect_s = Rectangle(
                            width=t_ctx.cell_width / 2, height=t_ctx.cell_height, color=table_color
                        )
                        apply_cell_sizing(t_ctx, first, half_size=True)
                        apply_cell_sizing(t_ctx, second, half_size=True)
                        rect_f.add(first)
                        rect_s.add(second)
                        rect = VGroup(rect_f, rect_s).arrange(buff=0)
                    else:
                        content = table_entry.content
                        rect = Rectangle(
                            width=t_ctx.cell_width, height=t_ctx.cell_height, color=table_color
                        )
                        apply_cell_sizing(t_ctx, content)
                        rect.add(content)

                    table.add(rect)

            table.arrange_in_grid(buff=0, cols=4)

            return table

        # drawing of tables

        class TableEntry:
            def __init__(self, content, double_entry=False, font_color=BLACK):
                self.double_entry = double_entry
                self.raw_content = content
                if self.double_entry:
                    self.first_content = MathTex(content[0], color=font_color)
                    self.second_content = MathTex(content[1], color=font_color)
                else:
                    self.content = MathTex(content, color=font_color)
                # if double entry is true, then content is an array of length 2

        def is_RIC_notation(txt):
            return "|" in txt

        def construct_table_series_RIC_addition_key_intervals(
            t_ctx, funcs=[RIC_to_latex, RIC_to_addition_step, RIC_to_key_intervals], table_color=WHITE
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
                table_series.append(create_table(t_ctx, step_table, table_color))
            return table_series


        def draw_table(table, title, font_color=WHITE):
            self.add(Tex(title, color=font_color).next_to(table, UP))
            self.add(table)

        t_ctx = TableContext(it_could_happen_to_you)

        tables = construct_table_series_RIC_addition_key_intervals(t_ctx, table_color=BLACK)

        print(tables)

        chord_table, key_interval_table = tables[0], tables[1]


        draw_table(chord_table, "It Could Happen To You", BLACK)


