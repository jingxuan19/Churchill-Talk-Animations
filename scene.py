from manim import *
import random

HOME = "C:\manim\Manim_7_July\Projects\\assets\Images"
HOME2 = "C:\manim\Manim_7_July\Projects\\assets\SVG_Images"

# This is for SVG Files to be imported. It is the directory from my PC

class Slide2(Scene):
    def construct(self):
        X = Square(2).set_fill(RED, opacity=0.5).shift(UP+LEFT)
        updatedsample1 = Square(4).set_fill(GREEN, opacity=0.5)
        updatedsample2 = Rectangle(width=2, height=4).set_fill(GREEN, opacity=0.5).shift(LEFT)
        updatedsample3 = Square(2).set_fill(GREEN, opacity=0.5).shift(UP+LEFT)
        S = Square(4)

        texx = MathTex("x").shift(UP+LEFT)
        tex0 = Tex("0", " bits").shift((4*RIGHT))
        tex1 = Tex("1", " bit").shift((4*RIGHT))
        tex2 = Tex("2", " bits").shift((4*RIGHT))

        createx = [FadeIn(updatedsample1), Create(X), Create(texx), FadeIn(tex0)]
        cut1 = [Transform(updatedsample1, updatedsample2), TransformMatchingShapes(tex0, tex1, shift=DOWN)]
        cut2 = [Transform(updatedsample2, updatedsample3), TransformMatchingShapes(tex1, tex2, shift=DOWN)]


        self.add(S)
        self.wait()
        self.play(AnimationGroup(*createx))
        self.wait()
        self.play(AnimationGroup(*cut1))
        self.wait()
        self.remove(updatedsample1)
        self.play(AnimationGroup(*cut2))
        self.wait(2)

class Slide4Optimal(Scene):
    def construct(self):
        arr3 = Rectangle(width=2.0, height=1.0, grid_xstep=1.0).shift(RIGHT)
        arr2 = Rectangle(width=1, height=1, grid_xstep=1).shift(0.5*LEFT)
        arr1 = Rectangle(width=1, height=1, grid_xstep=1).shift(1.5*LEFT)
        texx = MathTex("x").shift(1.5*LEFT)
        xcell = Group(arr1, texx)

        text = Tex("Split 0.5").shift(UP)
        informationtex = [Tex("0", " bits").shift(1.5*DOWN), Tex("1", " bit").shift(1.5*DOWN), Tex("2", " bits").shift(1.5*DOWN)]

        arr2.generate_target()
        xcell.generate_target()
        arr3.generate_target()

        arr3.target.shift(0.5*RIGHT)
        xcell.target.shift(0.5*LEFT)
        arr2.target.shift(0.5*LEFT)

        split1 = [MoveToTarget(arr3), MoveToTarget(arr2), MoveToTarget(xcell), TransformMatchingShapes(informationtex[0], informationtex[1], shift=DOWN)]
        self.add(arr2, xcell, arr3, text, informationtex[0])
        self.wait()
        self.play(AnimationGroup(*split1))
        self.wait()

        arr3.target.shift(0.5*RIGHT)
        xcell.target.shift(0.5*LEFT)
        arr2.target.shift(0.5*RIGHT)
        split1 = [MoveToTarget(arr3), MoveToTarget(arr2), MoveToTarget(xcell), TransformMatchingShapes(informationtex[1], informationtex[2], shift=DOWN)]
        self.play(AnimationGroup(*split1))
        self.wait()

class Slide4Suboptimal(Scene):
    def construct(self):
        arr4 = Square(1).shift(1.5*RIGHT)
        arr3 = Square(1).shift(0.5*RIGHT)
        arr2 = Square(1).shift(0.5*LEFT)
        arr1 = Square(1).shift(1.5*LEFT)
        texx = MathTex("x").shift(1.5*LEFT)
        xcell = Group(arr1, texx)
        informationtex = [Tex("0", " bits").shift(1.5*DOWN), Tex("0.415", " bits").shift(1.5*DOWN), Tex("1", " bit").shift(1.5*DOWN), Tex("2", " bits").shift((1.5*DOWN))]

        text = Tex("Split 0.75").shift(UP)

        arr2.generate_target()
        arr4.generate_target()
        xcell.generate_target()
        arr3.generate_target()

        arr3.target.shift(0.5*LEFT)
        arr4.target.shift(0.5*RIGHT)
        xcell.target.shift(0.5*LEFT)
        arr2.target.shift(0.5*LEFT)

        split = [MoveToTarget(arr4), MoveToTarget(arr3), MoveToTarget(arr2), MoveToTarget(xcell), TransformMatchingShapes(informationtex[0], informationtex[1], shift=DOWN)]
        self.add(arr2, xcell, arr3, arr4, text, informationtex[0])
        self.wait()
        self.play(AnimationGroup(*split))
        self.wait()

        arr4.target.shift(0.5*RIGHT)
        arr3.target.shift(0.5*RIGHT)
        xcell.target.shift(0.5*LEFT)
        arr2.target.shift(0.5*LEFT)
        split = [MoveToTarget(arr4), MoveToTarget(arr3), MoveToTarget(arr2), MoveToTarget(xcell), TransformMatchingShapes(informationtex[1], informationtex[2], shift=DOWN)]

        self.play(AnimationGroup(*split))
        self.wait()

        arr4.target.shift(0.5*RIGHT)
        arr3.target.shift(0.5*RIGHT)
        xcell.target.shift(0.5*LEFT)
        arr2.target.shift(0.5*RIGHT)
        split = [MoveToTarget(arr4), MoveToTarget(arr3), MoveToTarget(arr2), MoveToTarget(xcell), TransformMatchingShapes(informationtex[2], informationtex[3], shift=DOWN)]

        self.play(AnimationGroup(*split))
        self.wait()

class Slide4Suboptimal2(Scene):
    def construct(self):
        arr2 = Rectangle(width=3, height=1, grid_xstep=1).shift(0.5*LEFT)
        arr1 = Square(1).shift(1.5*RIGHT)
        texx = MathTex("x").shift(1.5*RIGHT)
        xcell = Group(arr1, texx)

        text = Tex("Split 0.75").shift(UP)
        informationtex = [Tex("0", " bits").shift(1.5*DOWN), Tex("2", " bits").shift((1.5*DOWN))]


        arr2.generate_target()
        xcell.generate_target()

        xcell.target.shift(0.5*RIGHT)
        arr2.target.shift(0.5*LEFT)

        split = [MoveToTarget(arr2), MoveToTarget(xcell), TransformMatchingShapes(informationtex[0], informationtex[1], shift=DOWN)]
        self.add(arr2, xcell, text, informationtex[0])
        self.wait()
        self.play(AnimationGroup(*split))
        self.wait()

class Slide6(Scene):
    def construct(self):
        staticexpprob = MathTex("E", "(", "{}", "X", "{}", ") =", r"\sum_{x \in X}", "{}", "x", "P(x)")
        expprob = MathTex("E", "(", "{}", "X", "{}", ") =", r"\sum_{x \in X}", "{}", "x", "P(x)")
        expinfo = MathTex("E", "(", "{I(}", "X", ")", ") =", r"\sum_{x \in X}", "I(", "x", ")", "P(x)")
        entropy = MathTex("H", "(", "X", ") =", r"\sum_{x \in X}", "P(x)", "(", "-", "log_2P(x)", ")").shift(1.5*DOWN)
        staticexpinfo = MathTex("E", "(", "{I(}", "X", ")", ") =", r"\sum_{x \in X}", "I(", "x", ")", "P(x)")
        entropy2 = MathTex("H", "(", "X", ") =", "-", r"\sum_{x \in X}", "P(x)", "log_2P(x)").shift(1.5*DOWN)

        self.add(expprob, staticexpprob)
        self.wait()

        staticexpprob.generate_target()
        staticexpprob.target.shift(1.5*UP)
        animations = [TransformMatchingTex(expprob, expinfo), MoveToTarget(staticexpprob)]

        self.play(AnimationGroup(*animations))
        self.wait(2)
        self.add(staticexpinfo)
        self.play(TransformMatchingTex(expinfo, entropy))
        self.wait()
        self.play(TransformMatchingTex(entropy, entropy2))
        self.wait()

class RandomNumbers:
    def construct(self):

        numbers = VGroup()
        for x in range(28):
            num = DecimalNumber()
            numbers.add(num)

        def randomize_numbers(numbers):
            for num in numbers:
                value = random.uniform(0, 1)
                num.set_value(value)
                if value > 0.1:
                    num.set_color(GREEN)
                else:
                    num.set_color(RED)

        randomize_numbers(numbers)

        numbers.set(width=0.38)
        numbers.arrange(RIGHT, buff=0.1)
        numbers.to_edge(UR)

        def get_results(numbers):
            results = VGroup()
            for num in numbers:
                if num.get_value() > 0.1:
                    result = (
                        SVGMobject(f"{HOME2}\\green_tick.svg")
                        .set_color(GREEN_C)
                        .set(width=0.3)
                    )
                else:
                    result = (
                        SVGMobject(f"{HOME2}\\cross.svg")
                        .set_color(RED_C)
                        .set(width=0.3)
                    )

                result.next_to(num, DOWN, buff=0.2)
                results.add(result)
            return results

        for k in range(10):
            self.play(UpdateFromFunc(numbers, randomize_numbers))
            self.wait()
            result = get_results(numbers)
            self.play(Write(result))
            self.wait()

            k = 0
            for num in numbers:
                if num.get_value() > 0.1:
                    k += 1
            total = k

            box = SurroundingRectangle(result)
            self.play(Create(box))
            self.play(FadeOut(box), FadeOut(result))

        self.wait()


def get_data_1(self):
    w = 0.2
    t_row1 = (
        VGroup(
            *[
                SVGMobject(f"{HOME2}\\green_tick.svg").set(width=w).set_color(GREEN)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .to_edge(UL, buff=0.25)
    )
    t_row2 = (
        VGroup(
            *[
                SVGMobject(f"{HOME2}\\green_tick.svg").set(width=w).set_color(GREEN)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(t_row1, DOWN, buff=0.25)
    )
    f_row1 = (
        VGroup(
            *[
                SVGMobject(f"{HOME2}\\cross.svg").set(width=w).set_color(RED)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(t_row2, DOWN, buff=0.25)
    )
    f_row2 = (
        VGroup(
            *[
                SVGMobject(f"{HOME2}\\cross.svg").set(width=w).set_color(RED)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(f_row1, DOWN, buff=0.25)
    )
    f_row3 = (
        VGroup(
            *[
                SVGMobject(f"{HOME2}\\cross.svg").set(width=w).set_color(RED)
                for i in range(10)
            ]
        )
        .arrange(RIGHT, buff=0.2)
        .next_to(f_row2, DOWN, buff=0.25)
    )

    result = VGroup(*t_row1, *t_row2, *f_row1, *f_row2, *f_row3)

    return result


class CentralLimitTheorem(Scene):
    def construct(self):

        data = get_data_1(self)
        axes = (
            Axes(x_range=[0, 1.2, 0.1], y_range=[0, 2.5], x_length=10, y_length=4)
            .to_edge(DL)
            .shift(UP * 0.2)
        )

        labels = axes.get_axis_labels(x_label="\\hat{p}", y_label="")

        x_axis_nums = VGroup()
        for i in range(11):
            num = (
                MathTex("\\frac{%3d}{10}" % i)
                .scale(0.6)
                .next_to(axes.x_axis.n2p(i / 10 + 0.05), DOWN, buff=0.1)
            )
            x_axis_nums.add(num)

        sample_counter = Tex("Total samples: ").scale(0.6).to_edge(UR).shift(LEFT * 0.6)
        total_counter = (
            Tex("Sum of Averages: ")
            .scale(0.6)
            .next_to(sample_counter, DOWN, aligned_edge=LEFT, buff=0.4)
        )
        average_counter = (
            MathTex("Average \\ \\hat{p}:  ")
            .scale(0.6)
            .next_to(total_counter, DOWN, aligned_edge=LEFT, buff=0.4)
        )

        self.play(
            LaggedStart(
                Create(data),
                Write(VGroup(sample_counter, total_counter, average_counter)),
                Create(axes),
                Write(x_axis_nums),
                run_time=4,
                lag_ratio=1,
            )
        )
        self.wait()

        data = get_data_1(self)
        sample_count = 10
        possible_outcomes = sample_count + 1

        counter_num = 0
        counter_number = (
            Integer(counter_num).scale(0.5).next_to(sample_counter, RIGHT, buff=0.2)
        )
        counter_number.add_updater(lambda m: m.set_value(counter_num))

        total_sum = 0
        total_number = (
            DecimalNumber(total_sum).scale(0.5).next_to(total_counter, RIGHT, buff=0.2)
        )
        total_number.add_updater(lambda m: m.set_value(total_sum))

        average = 0
        average_num = (
            DecimalNumber(average).scale(0.5).next_to(average_counter, RIGHT, buff=0.2)
        )
        average_num.add_updater(lambda m: m.set_value(average))

        self.add(counter_number, total_number, average_num)

        sums = [0] * possible_outcomes  # This creates an array for possible totals /10

        for s in range(15):
            # THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0, 50), k=sample_count)

            # THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            sample_results = VGroup()
            boxes = VGroup()
            for i, res in enumerate(a):
                res = data[a[i]]
                box = SurroundingRectangle(res)
                sample_results.add(res)
                boxes.add(box)

            moved_result = sample_results.copy()

            self.play(Create(boxes))
            self.play(
                moved_result.animate.arrange(RIGHT * 0.3, buff=0).to_edge(UP),
                FadeOut(boxes),
            )

            # THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i, value in enumerate(a):
                if value < 20:
                    a[i] = 1
                else:
                    a[i] = 0

            prop = DecimalNumber(num_decimal_places=1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set(height=0.2)
            prop.next_to(moved_result, RIGHT, buff=0.3)

            axes_box = SurroundingRectangle(
                moved_result,
                stroke_color=WHITE,
                stroke_width=0.2,
                fill_color=BLUE,
                fill_opacity=0.8,
                buff=0.1,
            )
            stack_in_axes = VGroup(axes_box, moved_result)

            self.play(DrawBorderThenFill(axes_box))
            self.play(Write(prop))

            counter_num += 1

            total_sum += tot / sample_count

            average = (total_sum) / (counter_num)

            self.play(
                stack_in_axes.animate.next_to(x_axis_nums[tot], UP, buff=0)
                .set(width=0.77)
                .shift(UP * sums[tot]),
                FadeOut(prop),
            )

            sums[tot] += stack_in_axes.get_height()

        self.wait()

        for s in range(85):
            # THIS IS CALLING A RANDOM SAMPLE OF NUMBERS TO SELECT FROM
            a = random.sample(range(0, 50), k=sample_count)

            # THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            sample_results = VGroup()
            boxes = VGroup()
            for i, res in enumerate(a):
                res = data[a[i]]
                box = SurroundingRectangle(res)
                sample_results.add(res)
                boxes.add(box)

            moved_result = sample_results.copy()

            self.play(Create(boxes), run_time=0.1)
            self.play(
                moved_result.animate.arrange(RIGHT * 0.3, buff=0).to_edge(UP),
                FadeOut(boxes),
                run_time=0.1,
            )

            # THIS ASSIGNS A VALUE FOR HOW MANY CORRECT WERE SELECTED FROM DATA
            for i, value in enumerate(a):
                if value < 20:
                    a[i] = 1
                else:
                    a[i] = 0

            prop = DecimalNumber(num_decimal_places=1)
            tot = sum(a)
            prop.set_value(tot / sample_count).set(height=0.2)
            prop.next_to(moved_result, RIGHT, buff=0.3)

            axes_box = SurroundingRectangle(
                moved_result,
                stroke_color=WHITE,
                stroke_width=0.2,
                fill_color=BLUE,
                fill_opacity=0.8,
                buff=0.1,
            )
            stack_in_axes = VGroup(axes_box, moved_result)

            self.add(axes_box, prop)
            counter_num += 1
            total_sum += tot / sample_count
            average = (total_sum) / (counter_num)

            self.play(
                stack_in_axes.animate.next_to(x_axis_nums[tot], UP, buff=0)
                .set(width=0.77)
                .shift(UP * sums[tot]),
                FadeOut(prop),
                run_time=0.3,
            )

            sums[tot] += stack_in_axes.get_height()
        self.wait()