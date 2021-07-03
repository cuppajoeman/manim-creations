# By Cigar666 & 數心 & 无懈可击99
from manim import *
import random

class Cube_array(VGroup):
    """
    Cube_array类
    方块阵列类，算是魔方类的基类吧
    ========================================
    center: 阵列中心位置
    cube_size: 每个方块的大小
    gap: 每个方块之间的空隙
    fill_color / fill_opacity: 方块的fill_color / fill_opacity
    stroke_color / stroke_width: 方块棱上的stroke_color和stroke_width
    resolution: 指方块阵列的尺寸，3*3*3的意思就是横纵竖都是3个方块
    faces: 方块的面
    """
    def __init__(self, center = ORIGIN, cube_size = 0.5, gap = 0, fill_color = BLUE, fill_opacity = 0.75, stroke_color = WHITE, stroke_width = 0, resolution= (3, 3, 3), **kwargs):
        VGroup.__init__(self, **kwargs)
        self.cube_size = cube_size
        self.gap = gap
        self.fill_color = fill_color
        self.fill_opacity = fill_opacity
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.resolution = resolution
        self.create_cubes()  # 创建方块阵列
        self.move_to(center) # 移动到指定中心
        self.faces = self.get_all_faces() # 添加阵列里所有方块的六个面
        # self.classify_faces()
        self.get_outer_faces()
    def create_cubes(self):
        size, gap = self.cube_size, self.gap
        u, v, w = self.resolution[0], self.resolution[1], self.resolution[2]
        for i in range(u):
            for j in range(v):
                for k in range(w):
                    # box_ijk = MyBox(pos=(size + gap) * ((j - v/2 + 1/2) * RIGHT + (i - u/2 + 1/2) * UP + (k - w/2 + 1/2) * OUT),
                    #                 bottom_size=[size, size], box_height=size, fill_color=self.fill_color,
                    #                 opacity=self.fill_opacity, stroke_color=self.stroke_color, stroke_width=self.stroke_width)
                    box_ijk = Cube(side_length=size, fill_color=self.fill_color, fill_opacity=self.fill_opacity,
                                   stroke_color=self.stroke_color, stroke_width=self.stroke_width)
                    box_ijk.shift((size + gap) * ((j - v/2 + 1/2) * RIGHT + (i - u/2 + 1/2) * UP + (k - w/2 + 1/2) * OUT))

                    # if self.reset_color:
                    #     box_ijk.reset_color()
                    self.add(box_ijk)
    def scale_each_cube(self, scale_factor): # scale每个方块
        for cube in self:
            cube.scale(scale_factor)
    def rotate_each_cube(self, angle, axis=OUT, **kwargs): # 旋转每个方块
        for cube in self:
            cube.rotate(angle, axis=OUT, **kwargs)
    def get_all_faces(self): # 得到所有方块的六个面
        faces = VGroup()
        for cube in self:
            faces.add(*cube)
        return faces
    def get_faces_by_range(self, max, min, dim=3): # 根据坐标来筛面
        max, min = (min, max) if max < min else (max, min)
        faces = VGroup()
        for face in self.faces:
            if face.get_center()[dim-1] <= max and face.get_center()[dim-1] >= min:
                faces.add(face)
        return faces
    def get_top_face(self, err=1e-3): # 得到顶面
        a = self.get_zenith()[2]
        self.top_faces = self.get_faces_by_range(a+err, a-err, dim=3)
        return self.top_faces
    def get_bottom_face(self, err=1e-3): # 得到底面
        a = self.get_nadir()[2]
        self.bottom_faces = self.get_faces_by_range(a+err, a-err, dim=3)
        return self.bottom_faces
    def get_front_face(self, err=1e-3): # 得到前面
        a = self.get_bottom()[1]
        self.front_faces = self.get_faces_by_range(a+err, a-err, dim=2)
        return self.front_faces
    def get_back_face(self, err=1e-3): # 得到后面
        a = self.get_top()[1]
        self.back_faces = self.get_faces_by_range(a+err, a-err, dim=2)
        return self.back_faces
    def get_left_face(self, err=1e-3): # 得到左面
        a = self.get_left()[0]
        self.left_faces = self.get_faces_by_range(a+err, a-err, dim=1)
        return self.left_faces
    def get_right_face(self, err=1e-3): # 得到右面
        a = self.get_right()[0]
        self.right_faces = self.get_faces_by_range(a+err, a-err, dim=1)
        return self.right_faces
    def classify_faces(self):
        max_or_min = np.array([self.get_top()[1], self.get_bottom()[1], self.get_right()[0], self.get_left()[0],
                      self.get_zenith()[2], self.get_nadir()[2]])
        print(max_or_min)
        self.outer_faces, self.inner_faces = VGroup(), VGroup()
        err = 1e-4 * self.cube_size ** 2
        for face in self.faces:
            x, y, z = face.get_center()[0], face.get_center()[1], face.get_center()[2]
            a = abs((max_or_min - x) * (max_or_min - y) * (max_or_min - z))
            print('before:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
            if abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/(self.cube_size/2) ** 6 < err:
                print('outer:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
                self.outer_faces.add(face)
            else:
                print('inner:', abs(a[0] * a[1] * a[2] * a[3] * a[4] * a[5])/self.cube_size ** 6)
                self.inner_faces.add(face)
            # a0 = abs(max_or_min - x)[0] * abs(max_or_min - x)[1]
            # a1 = abs(max_or_min - y)[2] * abs(max_or_min - y)[3]
            # a2 = abs(max_or_min - z)[4] * abs(max_or_min - z)[5]
            # if a0 < err or a1 < err or a2 < err:
            #     self.outer_faces.add(face)
            #     print('outer')
            # else:
            #     print('inner')
            #     self.inner_faces.add(face)
        # return self.outer_faces, self.inner_faces
    def get_outer_faces(self):
        self.outer_faces = VGroup(self.get_top_face(), self.get_bottom_face(),
                                  self.get_front_face(), self.get_back_face(),
                                  self.get_left_face(), self.get_right_face())
        return self.outer_faces
    # def get_innter_faces(self):
    #     return self.inner_faces

class Rubik_Cube(Cube_array):
    """
    Rubik_Cube类
    魔方类
    ==========================
    size: 魔方的大小
    order: 魔方一行方块的数量
    base_color: 内部颜色
    colors: 六个面的颜色
    """
    #[GREEN, BLUE_D, WHITE, YELLOW, RED_D, ORANGE]
    def __init__(self, size = 3, order = 3, base_color = LIGHT_GREY, colors = [YELLOW, WHITE, GREEN, BLUE_D, RED_D, ORANGE], **kwargs):
        Cube_array.__init__(self, cube_size=size/order, resolution=(order, order, order), fill_color=base_color, **kwargs)
        self.scale_each_cube(0.9)
        self.order = order
        self.size = size
        self.colors = colors
        self.setup_color()
    def setup_color(self): # 给魔方的六个面设置一下颜色
        self.top_faces.set_color(self.colors[0])
        self.bottom_faces.set_color(self.colors[1])
        self.front_faces.set_color(self.colors[2])
        self.back_faces.set_color(self.colors[3])
        self.left_faces.set_color(self.colors[4])
        self.right_faces.set_color(self.colors[5])
    def get_layer(self, layer=[1], dim=3):
        faces = VGroup()
        if type(layer) == int:
            a = self.size/2 - 0.5 * self.cube_size - (layer-1) * self.cube_size + self.get_center()[dim-1]
            faces.add(self.get_faces_by_range(a + self.cube_size/2, a - self.cube_size/2, dim=dim))
        else:
            for i in layer:
                a = self.size/2 - 0.5 * self.cube_size - (i-1) * self.cube_size + self.get_center()[dim-1]
                faces.add(self.get_faces_by_range(a + self.cube_size/2, a - self.cube_size/2, dim=dim))
        return faces

class Rubik_Scene(ThreeDScene):
    """
    Rubik_Scene类
    魔方场景类
    ==========================
    size: 魔方的大小
    order: 魔方一行方块的数量
    base_color: 内部颜色
    colors: 六个面的颜色

    """
    def setup(self): # 一些基本配置
        self.rubik = []
        self.camera_init = {            
            'phi': 52.5 * DEGREES,
            'gamma': 0,
            'theta': -45 * DEGREES
        }
        self.set_camera_orientation(**self.camera_init)

    def add_rubik(self, order = 3, size = 4.2, **kwargs):
        self.rubik.append(Rubik_Cube(order = order, size = size, **kwargs))

    def construct(self):
        pass  # 在子类中实现

    def rotate_rubik(self, rubik_cube, layer, dim, quarter=1, run_time=0.8, reverse=False, anim = True, **kwargs):
        # layer, dim决定要转的层
        # dim: 1 左右 2 前后 3 上下
        # quarter决定转多少下
        # run_time是运行时间
        # 默认顺时针，reverse的话就是逆时针
        # anim 决定是否为动画
        theta = quarter * PI/2 * (1 if reverse else -1)
        axis = [RIGHT, DOWN, OUT][dim-1]
        if layer != 0:
            layer_rotate = [layer] if type(layer) == int else layer
            layer_stay = []
            for i in range(1, rubik_cube.order + 1):
                if not i in layer_rotate:
                    layer_stay.append(i)
            if len(layer_stay) != 0:
                if anim:
                    self.play(
                            Rotating(rubik_cube.get_layer(layer_rotate, dim = dim), radians = theta, axis = axis, run_time = run_time),
                            Rotating(rubik_cube.get_layer(layer_stay, dim = dim), radians = 0, axis = axis, run_time = run_time), 
                            **kwargs
                    )
                else:
                    rubik_cube.get_layer(layer_rotate, dim = dim).rotate(angle = theta, axis = axis)
            else:
                if anim:
                    self.play(
                        Rotating(rubik_cube.get_layer(layer_rotate, dim = dim), radians = theta, axis = axis, run_time = run_time, **kwargs)
                    )
                else:
                    rubik_cube.get_layer(layer_rotate, dim = dim).rotate(angle = theta, axis = axis)
        else:
            layer_rotate = range(1, rubik_cube.order + 1)
            if anim:
                self.play(
                    Rotating(rubik_cube.get_layer(layer_rotate, dim = dim), radians = theta, axis = axis, run_time = run_time, **kwargs)
                )
            else:
                rubik_cube.get_layer(layer_rotate, dim = dim).rotate(angle = theta, axis = axis)

    # 直接利用公式来旋转魔方
    def rotate_rubik_by_single_formula(self, rubik_cube, str, run_time = 0.8, anim = True, inv = 1):
        # layer, dim决定要转的层
        # dim: 1 左右 2 前后 3 上下
        if len(str) == 1:
            str = str + ' '
        quarter_dict = {' ': 1, '\'': -1, '2': 2, '2\'': -2, '3': 3, '3\'': -3}
        if str[0] == 'U':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 1, dim = 3, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim) # 1 顺时针，-1逆时针
        if str[0] == 'R':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 1, dim = 1, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim) 
        if str[0] == 'F':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 3, dim = 2, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim) 
        if str[0] == 'D':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 3, dim = 3, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim) 
        if str[0] == 'L':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 3, dim = 1, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim) 
        if str[0] == 'B':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 1, dim = 2, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim) 

        if str[0] == 'x':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 0, dim = 1, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim)
        if str[0] == 'y':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 0, dim = 3, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim)
        if str[0] == 'z':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 0, dim = 2, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim)

        if str[0] == 'u':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = [1, 2], dim = 3, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim) # 1 顺时针，-1逆时针
        if str[0] == 'r':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = [1, 2], dim = 1, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim) 
        if str[0] == 'f':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = [2, 3], dim = 2, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim) 
        if str[0] == 'd':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = [2, 3], dim = 3, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim) 
        if str[0] == 'l':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = [2, 3], dim = 1, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim) 
        if str[0] == 'b':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = [1, 2], dim = 2, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim)   
            
        if str[0] == 'E':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 2, dim = 3, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim)
        if str[0] == 'M':
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 2, dim = 1, quarter = quarter_dict[str[1:]] * (-inv), run_time = run_time, anim = anim)
        if str[0] == 'S':         
            self.rotate_rubik(rubik_cube = rubik_cube, layer = 2, dim = 2, quarter = quarter_dict[str[1:]] * inv, run_time = run_time, anim = anim) 
    
    def rotate_rubik_by_simple_formula(self, rubik_cube, str, run_time_per_formula = 0.8, wait_time = 0.5, anim = True):
        i = 0
        strlen = len(str)
        while (i < strlen):
            j = i + 1
            while (j < strlen):
                if not str[j].isalpha() and str[j] != '*':
                    j += 1
                else:
                    break
            if (j < strlen and str[j] == '*'):
                self.rotate_rubik_by_single_formula(rubik_cube = rubik_cube, str = str[i:j], run_time = run_time_per_formula, anim = anim, inv = -1)
                i = j + 1
            else:
                self.rotate_rubik_by_single_formula(rubik_cube = rubik_cube, str = str[i:j], run_time = run_time_per_formula, anim = anim, inv = 1)
                i = j
    
    def rotate_rubik_by_formula(self, rubik_cube, seq, run_time_per_formula = 0.8, anim = True):
        stack = []
        sequence = []
        seq = "(" + seq.replace(" ", "") + ")"
        seqlen = len(seq)
        i = 0
        while (i < seqlen):
            if (seq[i].isalpha()):
                j = i + 1
                while (j < seqlen):
                    if not seq[j].isalpha() and seq[j] != '(' and seq[j] != ')':
                        assert (seq[j].isdigit() or seq[j] == '\'')
                        j += 1
                    else:
                        break
                sequence.append(seq[i:j])
                if (seq[j] != ")"):
                    while (len(stack) > 0 and stack[-1] == '*'):
                        sequence.append(stack.pop())
                    stack.append("+")
                i = j
            elif (seq[i] == '('):
                stack.append("(")
                i += 1
            elif (seq[i] == ')'):
                while (len(stack) > 0 and stack[-1] != "("):
                    sequence.append(stack.pop())
                if (len(stack) == 0):
                    assert(len(stack) > 0)
                else:
                    stack.pop()
                    j = i + 1
                    num = 1
                    while (j < seqlen):
                        if seq[j].isdigit():
                            j += 1
                        else:
                            break
                    if (j > i + 1):
                        num = int(seq[i+1:j])
                    if (j < seqlen and seq[j] == '\''):
                        num = -num
                        j += 1
                    sequence.append(str(num))
                    sequence.append("*")
                    if (j < len(seq) and seq[j] != ")"):
                        while (len(stack) > 0 and stack[-1] == '*'):
                            sequence.append(stack.pop())
                        stack.append("+")
                    i = j
            else:
                assert(seq[i].isalpha() or seq[i] == '(' or seq[i] == ')')
        assert(len(stack) == 0)
        for i in range(len(sequence)):
            if (sequence[i] != "+" and sequence[i] != "*"):
                stack.append([sequence[i]])
            elif (sequence[i] == "+"):
                tmp = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            else:
                tmp, num = stack[-2], int(stack[-1][0])
                stack.pop()
                stack.pop()
                if (num >= 0):
                    stack.append(tmp * num)
                else:
                    tmp.reverse()
                    for i in range(len(tmp)):
                        tmp[i] += "*"
                    stack.append(tmp * (-num))
        print(stack)
        assert(len(stack) == 1)
        self.rotate_rubik_by_simple_formula(rubik_cube = rubik_cube, str = "".join(stack[0]), run_time_per_formula = run_time_per_formula, anim = anim)
    
    def shuffle(self, rubik_cube, anim = True, total_time = 3, steps = 15, ** kwargs):
        # 将魔方打乱
        sym_seq = ["U", "R", "F", "D", "L", "B", "x", "y", "z", "E", "M", "S"]
        formula_seq = []

        for i in range(steps):
            ran = sym_seq[random.randint(0, len(sym_seq) - 1)]
            rand_no = random.randint(0, 1)
            if rand_no:
                formula_seq.append(ran)
            else:
                formula_seq.append(ran+ r"'")

        random.shuffle(formula_seq)

        for formula in formula_seq:
            self.rotate_rubik_by_single_formula(rubik_cube = rubik_cube, str = formula, anim = anim, run_time = total_time / steps, **kwargs)

class Test_MultipleRubik(Rubik_Scene):
    def construct(self):
        #center = 4 * LEFT, 

        # center = 0.5 * LEFT
        self.add_rubik(size = 2)
        self.add_rubik(size = 2)
        self.add_rubik(size = 2)
        self.add(self.rubik[0], self.rubik[1], self.rubik[1])
        self.play(self.rubik[1].animate.move_to(4 * LEFT), self.rubik[2].animate.move_to(4 * UP))
        
        self.rotate_rubik_by_formula(rubik_cube = self.rubik[1], seq = r"(URU'R')3", run_time_per_formula = 0.3)
        self.rotate_rubik_by_formula(rubik_cube = self.rubik[2], seq = r"(U'R'UR)3", run_time_per_formula = 0.3)
        self.rotate_rubik_by_formula(rubik_cube = self.rubik[2], seq = r"URFDLB", run_time_per_formula = 0.3)
        self.wait()
