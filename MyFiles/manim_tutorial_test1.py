from manimlib.imports import *

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([-1,1,0]))

        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.add(line)
        
class SquareToCircle(Scene):
    def construct(self):
        
        
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)
        
        title = TextMobject(
            "International ", "Mathematical ", "Olympiad",
        )
        title.scale(1.25)
        logo = ImageMobject("/Users/madhu/Documents/MadhuPersonal/learning/regression-class-cluster/Supervisor.jpg")
        logo.set_height(5)

        group = Group(logo, title)
        group.arrange(RIGHT)
        group.to_edge(UP, buff=MED_SMALL_BUFF)

        #self.add(title, logo)
        self.play(ShowCreation(logo))

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        
class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))
        
class MoreShapesMyfun(Scene):
    CONFIG = {
        "num_countries": 130,
        "use_real_images": True,
        # "use_real_images": False,
        "include_labels": False,
        "camera_config": {"background_color": BLACK},
        "random_seed": 6,
        "year": 2020,
        "n_flag_rows": 10,
        "reorganize_students": True,
    }
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(RIGHT,RIGHT*5,color=MAROON_C)
        print('Right : ',RIGHT)
        pointer.get_top()
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        print('OUT : ',OUT)

        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        # self.add(pointer)
        self.play(GrowArrow(pointer))
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(ScaleInPlace(square,2))
        self.play(GrowArrow(arrow))
        # self.play(ApplyFunction('2x+y=3',arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))


class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))