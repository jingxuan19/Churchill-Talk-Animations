from manim import *
import random
import numpy as np

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

class Slide7(Scene):
    def construct(self):
        originaleq = MathTex("H(", "X", ") =", r"\sum_{x \in X}", "P(x)", "log(", "P(x)", ")")
        probseq = MathTex("H(", r"p_1, \dots, p_n", ") =", r"\sum_{i \in [1,n]}", "p_i", "log(", "p_i", ")")
        probveceq = MathTex("H(", r"\vec{p}", ") =", r"\sum_{p \in \vec{p}}", "p", "log(", "p", ")")

        self.add(originaleq)
        self.play(TransformMatchingTex(originaleq, probseq))
        self.wait()
        self.play(TransformMatchingTex(probseq, probveceq))
        self.wait()

class Slide8Eq(Scene):
    def construct(self):
        X = MathTex(r"X\sim\begin{cases} "
                        r"p \quad\quad x \leq pivot\\"
                        r"1-p \quad x > pivot\\"
                    r"\end{cases}")
        self.add(X.shift(2*UP))
        staticX = X.copy()
        self.wait()
        H = MathTex("H(X) = ", "-", "p", "log_2", "p", "-", "(", "1-p", ")", "log_2", "(", "1-p", ")")
        self.add((staticX))
        self.play(TransformMatchingShapes(X, H))


        self.wait()

class Slide8Graph(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 1.4, 0.5], y_range=[0, 1.4, 0.5], x_length=5, y_length=5, axis_config= {"include_tip": False, "color": GREEN}, color="Green").add_coordinates()
        axes_labels = axes.get_axis_labels(x_label="p", y_label="H(X)")

        def H(p):
            if (p == 0) or (p == 1):
                return 0
            return p*np.log2((1-p)/p)-np.log2(1 - p)

        graph = axes.plot(H, x_range=[0, 1], color=RED)

        l = Line((-0.7, 1.1, 0), (-0.7, -2.5, 0))
        l2 = Line((-2.5, 1.1, 0), (-0.7, 1.1, 0))
        dashed = DashedVMobject(l)
        dashed2 = DashedVMobject(l2)


        self.play(DrawBorderThenFill(axes), Write(axes_labels))
        self.play(Create(graph))
        self.play(Create(dashed2))
        self.play(Create(dashed))

        self.wait()

class Slide12(Scene):
    def construct(self):
        lotp = Tex("Law of Total Probability").shift(UP)
        psum = MathTex(r"\int_{a}^{b}p(x)dx", "=", "1")
        law = VGroup(lotp, psum)

        self.play(Create(law))

        law.generate_target()
        law.target.shift(2.5*UP).scale(0.8)

        self.play(MoveToTarget(law))

        constraint = MathTex("g(x)", "=", r"\int_{a}^{b}p(x)dx", "-", "1").shift(1.5*UP + 3*RIGHT)
        H = MathTex("H(x) =", r"\int p(x)", "ln(p(x))", "dx").shift(1.5*UP + 3*LEFT)
        law.add(psum.copy())
        self.play(FadeIn(H), TransformMatchingTex(psum, constraint))

        sconstraint = constraint.copy()
        law.add(constraint, H)
        law.add(H.copy(), sconstraint)
        lagrangian = MathTex(r"\mathbb{L}", "=", "\int p(x)", "ln(p(x))", "dx", "-", r"\lambda", r"\int_{a}^{b}p(x)dx", "-", "1").shift(UP)
        self.play(law.animate.scale(0.8).shift(0.5*UP))
        self.play(TransformMatchingTex(H, lagrangian), TransformMatchingTex(constraint, lagrangian))

        law.add(lagrangian, lagrangian.copy())
        differential = MathTex(r"\frac{\delta \mathbb{L}}{\delta p(x)}", "=", "ln(p(x))", "+", "1", "-", "\lambda", "=", "0").shift(0.5*UP)
        self.play(law.animate.scale(0.8).shift(0.5*UP))
        self.play(TransformMatchingTex(lagrangian, differential))

        law.add(differential)
        law.add(differential.copy())
        eq = MathTex("ln(p(x))", "=", "\lambda", "-", "1")
        eq2 = MathTex("ln(", "p(x)", ")", "=", r"\lambda - 1")
        self.play(law.animate.scale(0.8).shift(0.2 * UP))
        self.play(TransformMatchingTex(differential, eq))
        self.add(eq2)
        self.remove(eq)

        eq3 = MathTex("p(x)", "=", r"e^{\lambda - 1}")
        self.play(TransformMatchingTex(eq2, eq3))

        law.add(sconstraint.copy())
        eq4 = MathTex("g(x)", "=", r"\int_{a}^{b}p(x)dx", "-", "1").shift(DOWN)
        eq4a = MathTex("g(x)", "=", r"\int_{a}^{b}","p(x)", "dx", "-", "1").shift(DOWN)
        self.play(TransformMatchingTex(sconstraint, eq4))
        self.add(eq4a)
        self.remove(eq4)
        eq5 = MathTex(r"\int_{a}^{b}", "p(x)", "dx", "=", "1").shift(DOWN)
        self.play(TransformMatchingTex(eq4a, eq5))
        eq6 = MathTex(r"\int_{a}^{b}", r"e^{\lambda - 1}", "dx", "=", "1").shift(DOWN)
        self.add(eq3.copy())
        self.play(TransformMatchingTex(eq5, eq6), TransformMatchingTex(eq3, eq6))

        self.add(eq6.copy())
        eq7 = MathTex(r"e^{\lambda - 1}", "(", "b-a", ")", "=", "1").shift(2*DOWN)
        self.play(TransformMatchingTex(eq6, eq7))
        eq8 = MathTex(r"e^{\lambda - 1}", "=", r"\frac{1}{b-a}").shift(2*DOWN)
        self.play(TransformMatchingTex(eq7, eq8))

        self.add(eq3.copy(), eq8.copy())
        eq9 = MathTex("p(x)", "=", r"e^{\lambda - 1}").shift(3*DOWN)
        self.play(TransformMatchingTex(eq3, eq9))
        eq10 = MathTex("p(x)", "=", r"\frac{1}{b-a}").shift(3*DOWN)
        self.play(TransformMatchingTex(eq8, eq10), TransformMatchingTex(eq9, eq10))
        self.wait()


class Slide13(Scene):
    def construct(self):
        circles = []
        for i in range(16):
            circles.append(Circle(radius=0.2, color=BLUE, fill_opacity=1).shift(4*LEFT+i*0.5*RIGHT+2*UP))
        circles = VGroup(*circles)
        self.play(Create(circles))

        bins = NumberLine(x_range=[0, 4, 1], length=4, include_numbers=False).shift(DOWN)
        self.play(Create(bins))

        tempcircles = VGroup()
        for i in range(1, 5):
            for j in range(1, 5):
                tempcircles.add(Circle(radius=0.2, color=BLUE, fill_opacity=1).shift((1.25-i*0.5)*DOWN+(2.5-j)*LEFT))

        self.play(Transform(circles, tempcircles))
        self.wait()

class Slide15(Scene):
    def construct(self):
        guesser = Tex("Guesser").align_on_border(UL)
        gm = Tex("Game Master").align_on_border(UR)

        word = []
        uword = VGroup()
        i = 0
        for c in list("COFFEE"):
            letter = Tex(c).scale(2).shift((2.5-i)*LEFT)
            word.append(letter)
            uword.add(Underline(letter))
            i += 1

        starting = VGroup(guesser, gm, uword, Underline(guesser), Underline(gm))

        self.play(Create(starting))
        self.wait(2)

        #Guess: E
        guess = Tex("E?").scale(1.5).next_to(guesser, DOWN).set_color(YELLOW)
        ans = Tex(r"\checkmark").scale(1.5).next_to(gm, DOWN)
        self.play(FadeIn(guess, shift=DOWN))
        self.play(Create(ans), FadeIn(word[-1], shift=UP), FadeIn(word[-2], shift=UP))

        #Guess: A
        guess2 = Tex("A?").scale(1.5).next_to(guesser, DOWN).set_color(YELLOW)
        ans2 = Cross(guess2).next_to(gm, DOWN)
        self.play(TransformMatchingShapes(guess, guess2))
        self.play(FadeOut(ans, shift=DOWN), FadeIn(ans2, shift=DOWN))

        banned = VGroup(Cross(Tex("A")).shift(DOWN+3*LEFT), Tex("A").shift(DOWN+3*LEFT).set_opacity(0.5))
        self.play(TransformMatchingShapes(guess2, banned), TransformMatchingShapes(ans2, banned))

        #Guess: O
        guess = Tex("O?").scale(1.5).next_to(guesser, DOWN).set_color(YELLOW)
        ans = Tex(r"\checkmark").scale(1.5).next_to(gm, DOWN)
        self.play(ChangeSpeed(FadeIn(guess, shift=DOWN), speedinfo={0: 2}))
        self.play(ChangeSpeed(AnimationGroup(Create(ans), FadeIn(word[1], shift=UP)), speedinfo={0: 2}))

        #Guess: B
        guess2 = Tex("B?").scale(1.5).next_to(guesser, DOWN).set_color(YELLOW)
        ans2 = Cross(guess2).next_to(gm, DOWN)
        self.play(ChangeSpeed(FadeTransform(guess, guess2), speedinfo={0: 2}))
        self.play(ChangeSpeed(AnimationGroup(FadeOut(ans, shift=DOWN), FadeIn(ans2, shift=DOWN)), speedinfo={0: 2}))

        banned2 = VGroup(Cross(Tex("B")).next_to(banned, RIGHT), Tex("B").next_to(banned, RIGHT).set_opacity(0.5))
        self.play(ChangeSpeed(AnimationGroup(TransformMatchingShapes(guess2, banned2), TransformMatchingShapes(ans2, banned2)), speedinfo={0: 2}))

        #Guess: F
        guess = Tex("F?").scale(1.5).next_to(guesser, DOWN).set_color(YELLOW)
        ans = Tex(r"\checkmark").scale(1.5).next_to(gm, DOWN)
        self.play(ChangeSpeed(FadeIn(guess, shift=DOWN), speedinfo={0: 2}))
        self.play(ChangeSpeed(AnimationGroup(Create(ans), FadeIn(word[2], shift=UP), FadeIn(word[3], shift=UP)), speedinfo={0: 2}))
        self.wait()
        self.remove(guess, ans)

        #Guess everything
        lettersleft = list("DGHIJKLMNPQRSTUVWXYZ")
        letter = banned2.copy()
        ans3 = Cross(guess2).next_to(gm, DOWN)
        lettermobs = [ans3]
        for i in range(10):
            c = lettersleft.pop(0)
            lettermobs.append(VGroup(Cross(Tex(c)).next_to(letter, RIGHT), Tex(c).next_to(letter, RIGHT).set_opacity(0.5)))
            letter = lettermobs[-1]
        c = lettersleft.pop(0)
        lettermobs.append(VGroup(Cross(Tex(c)).next_to(banned, DOWN), Tex(c).next_to(banned, DOWN).set_opacity(0.5)))
        letter = lettermobs[-1]
        for c in lettersleft:
            lettermobs.append(VGroup(Cross(Tex(c)).next_to(letter, RIGHT), Tex(c).next_to(letter, RIGHT).set_opacity(0.5)))
            letter = lettermobs[-1]


        self.play(ChangeSpeed(Create(VGroup(*lettermobs)), speedinfo={0: 2}))
        self.play(FadeOut(ans3), FadeIn(Tex("$>$:(").next_to(gm, DOWN)), Create(Tex(":/").next_to(guesser, DOWN)))

        self.wait()

class Slide16(Scene):
    def construct(self):
        word = []
        uword = VGroup()
        i = 0
        for c in list("BINARY"):
            letter = Tex(c).scale(2).shift((2.5 - i) * LEFT + 2*UP)
            word.append(letter)
            uword.add(Underline(letter))
            i += 1

        self.play(Create(uword))
        self.wait()

        lettermobs = VGroup()
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        c = letters.pop(0)
        templetter = Tex(c).shift(3*LEFT)
        cletter = templetter.copy()
        lettermobs.add(templetter)
        for i in range(12):
            c = letters.pop(0)
            templetter = Tex(c).next_to(templetter, RIGHT)
            lettermobs.add(templetter)
        c = letters.pop(0)
        templetter = Tex(c).next_to(cletter, DOWN).shift(0.1*LEFT)
        lettermobs.add(templetter)
        for i in range(12):
            c = letters.pop(0)
            templetter = Tex(c).next_to(templetter, RIGHT)
            lettermobs.add(templetter)

        self.play(Create(lettermobs))
        self.wait()

        self.play(FadeIn(VGroup(*word), shift=UP))

        self.wait()


class Slide20(Scene):
    def construct(self):
        sequence = [2, 4, 6]

        nummobs = VGroup()
        for i in range(len(sequence)):
            nummobs.add(MathTex(sequence[i]).scale(2).shift((4-i)*LEFT))

        self.play(Create(nummobs))
        self.wait()

        qm = Tex("?").scale(2)
        self.play(Create(qm))
        self.wait()

        EIGHT = MathTex(8).scale(2)
        eq1 = MathTex("f(x) =", "2", "x").shift(DOWN*2)
        self.play(FadeOut(qm, shift=DOWN), FadeIn(EIGHT, shift=DOWN), FadeIn(eq1))
        self.wait(2)

        FOURTEEN = MathTex(14).scale(2)
        eq2 = MathTex("f(x) =", "x^3-6x^2+13", "x", "-6").shift(DOWN*2)
        self.play(FadeOut(EIGHT, shift=DOWN), FadeIn(FOURTEEN, shift=DOWN), TransformMatchingTex(eq1, eq2))

        self.wait()

class Slide21(Scene):
    def construct(self):
        Occamrazor = Text("Occam's razor").to_edge(UP)
        self.play(Write(Occamrazor))
        self.play(Create(Underline(Occamrazor)))
        definition = Tex("Entia non sunt multiplicanda praeter necessitatem").next_to(Occamrazor, DOWN).shift(DOWN)
        self.play(Write(definition))
        self.wait()
        endef = Tex("The simplest explanation is usually the best one.").next_to(Occamrazor, DOWN).shift(DOWN)
        self.play(TransformMatchingShapes(definition, endef))

        self.wait()

class Slide22(Scene):
    def construct(self):
        H1 = MathTex("H_1: f(x) =", "a", "x+", "b").to_edge(UP).set_color_by_tex("a", YELLOW).set_color_by_tex("b", YELLOW)
        H2 = MathTex("H_2: f(x) =", "a", "x^3+", "b", "x^2+", "c", "x+", "d").next_to(H1, DOWN).set_color_by_tex("a", YELLOW).set_color_by_tex("b", YELLOW).set_color_by_tex("c", YELLOW).set_color_by_tex("d", YELLOW)
        self.play(Create(H1), Create(H2))
        self.wait(6)

        PHGD = MathTex("P(H|D)").shift(UP)
        PHGDE = MathTex("P(H|D)", r"= \frac{P(D|H)P(H)}{P(D)}").shift(UP)
        self.play(Create(PHGD))
        self.play(TransformMatchingTex(PHGD, PHGDE))
        self.wait(6)

        PHGDR = MathTex(r"\frac{P(H_1|D)}{P(H_2|D)}", "=", r"\frac{P(H_1)}{P(H_2)}\frac{P(D|H_1)}{P(D|H_2)}").shift(DOWN)
        self.add(PHGDE.copy())
        self.play(TransformMatchingShapes(PHGDE, PHGDR))

        self.wait()

class Slide23(Scene):
    def construct(self):
        PHGDR = MathTex(r"\frac{P(H_1|D)}{P(H_2|D)}", "=", r"\frac{P(H_1)}{P(H_2)}", r"\frac{P(D|H_1)}{P(D|H_2)}").shift(3*UP)
        brace1 = Brace(PHGDR[2], DOWN)
        brace1_label = brace1.get_text("Bias")
        PHGDRWB = MathTex(r"\frac{P(H_1|D)}{P(H_2|D)}", "=", r"\frac{P(D|H_1)}{P(D|H_2)}").shift(3*UP)

        self.play(Write(PHGDR), GrowFromCenter(brace1), Write(brace1_label))
        self.wait(10)
        self.play(TransformMatchingTex(PHGDR, PHGDRWB), FadeOut(brace1), FadeOut(brace1_label))

        PDGH = MathTex("P(D|H)")
        self.play(Write(PDGH))
        self.wait(2)

        PDGH.generate_target()
        PDGH.target.shift(4*RIGHT+UP)
        self.play(MoveToTarget(PDGH))
        self.wait(2)

        #a1
        a1line = NumberLine(
            x_range=[-20, 20],
            length=3,
            color=BLUE,
            include_numbers=False, numbers_to_include=[-20,20]).to_edge(LEFT).shift(UP)
        a1_parameter = ValueTracker(0)
        labela1 = MathTex("a = ", "{:.0f}".format(a1_parameter.get_value())).next_to(a1line, UP)
        a1_marker = Dot(color=YELLOW).add_updater(
            lambda mob: mob.move_to(a1line.number_to_point(a1_parameter.get_value())), ).update()

        #b1
        b1_parameter = ValueTracker(1)
        labelb1 = MathTex("b = ", "{:.0f}".format(b1_parameter.get_value())).next_to(a1line, DOWN)
        b1line = NumberLine(
            x_range=[-20, 20],
            length=3,
            color=BLUE,
            include_numbers=False, numbers_to_include=[-20, 20]).next_to(labelb1, DOWN)

        b1_marker = Dot(color=RED).add_updater(
            lambda mob: mob.move_to(b1line.number_to_point(b1_parameter.get_value())), ).update()

        #a2
        a2line = NumberLine(
            x_range=[-20, 20],
            length=3,
            color=BLUE,
            include_numbers=False, numbers_to_include=[-20,20]).next_to(a1line, RIGHT)
        a2_parameter = ValueTracker(2)
        labela2 = MathTex("a = ", "{:.0f}".format(a2_parameter.get_value())).next_to(a2line, UP)
        a2_marker = Dot(color=GREEN).add_updater(
            lambda mob: mob.move_to(a2line.number_to_point(a2_parameter.get_value())), ).update()

        # b2
        b2_parameter = ValueTracker(3)
        labelb2 = MathTex("b = ", "{:.0f}".format(b1_parameter.get_value())).next_to(a2line, DOWN)
        b2line = NumberLine(
            x_range=[-20, 20],
            length=3,
            color=BLUE,
            include_numbers=False, numbers_to_include=[-20, 20]).next_to(labelb2, DOWN)

        b2_marker = Dot(color=ORANGE).add_updater(
            lambda mob: mob.move_to(b2line.number_to_point(b2_parameter.get_value())), ).update()

        # c
        c_parameter = ValueTracker(4)
        labelc = MathTex("c = ", "{:.0f}".format(c_parameter.get_value())).next_to(b2line, DOWN)
        cline = NumberLine(
            x_range=[-20, 20],
            length=3,
            color=BLUE,
            include_numbers=False, numbers_to_include=[-20, 20]).next_to(labelc, DOWN)

        c_marker = Dot(color=PURPLE).add_updater(
            lambda mob: mob.move_to(cline.number_to_point(c_parameter.get_value())), ).update()

        # d
        d_parameter = ValueTracker(5)
        labeld = MathTex("d = ", "{:.0f}".format(d_parameter.get_value())).next_to(cline, DOWN)
        dline = NumberLine(
            x_range=[-20, 20],
            length=3,
            color=BLUE,
            include_numbers=False, numbers_to_include=[-20, 20]).next_to(labeld, DOWN)

        d_marker = Dot(color=PINK).add_updater(
            lambda mob: mob.move_to(dline.number_to_point(d_parameter.get_value())), ).update()


        self.play(DrawBorderThenFill(VGroup(a1line, b1line, a2line, b2line, cline, dline)), Create(VGroup(a1_marker, b1_marker, a2_marker, b2_marker, c_marker, d_marker)))
        self.play(
            UpdateFromAlphaFunc(
                a1_parameter,
                lambda mob, alpha: mob.set_value(20*np.sin(alpha * 2*PI)),
                run_time=6
            ), UpdateFromFunc(labela1, lambda m: m.become(MathTex("a = ", "{:.0f}".format(a1_parameter.get_value())).next_to(a1line, UP))),
            UpdateFromAlphaFunc(
                b1_parameter,
                lambda mob, alpha: mob.set_value(-20 * np.sin(alpha * 2 * PI)),
                run_time=6
            ), UpdateFromFunc(labelb1, lambda m: m.become(MathTex("b = ", "{:.0f}".format(b1_parameter.get_value())).next_to(a1line, DOWN))),
            UpdateFromAlphaFunc(
                a2_parameter,
                lambda mob, alpha: mob.set_value(20 * np.cos(alpha * 2 * PI)),
                run_time=6
            ), UpdateFromFunc(labela2, lambda m: m.become(MathTex("a = ", "{:.0f}".format(a2_parameter.get_value())).next_to(a2line, UP))),
            UpdateFromAlphaFunc(
                b2_parameter,
                lambda mob, alpha: mob.set_value(-20 * np.cos(alpha * 2 * PI)),
                run_time=6
            ), UpdateFromFunc(labelb2, lambda m: m.become(MathTex("b = ", "{:.0f}".format(b2_parameter.get_value())).next_to(a2line, DOWN))),
            UpdateFromAlphaFunc(
                c_parameter,
                lambda mob, alpha: mob.set_value(20 * np.sin(alpha * 2 * PI)),
                run_time=6
            ), UpdateFromFunc(labelc, lambda m: m.become(MathTex("c = ", "{:.0f}".format(c_parameter.get_value())).next_to(b2line, DOWN))),
            UpdateFromAlphaFunc(
                d_parameter,
                lambda mob, alpha: mob.set_value(20 * np.cos(alpha * 2 * PI)),
                run_time=6
            ), UpdateFromFunc(labeld, lambda m: m.become(MathTex("d = ", "{:.0f}".format(d_parameter.get_value())).next_to(cline, DOWN))),

        )
        self.wait(2)

        PDGH1 = MathTex("P(D|H_1)", "=", r"\frac{1}{41}\frac{1}{41}").next_to(PDGH, DOWN)
        PDGH2 = MathTex("P(D|H_2)", "=", r"\frac{1}{41}\frac{1}{41}\frac{1}{41}\frac{1}{41}").next_to(PDGH1, DOWN)
        PHGDR = MathTex(r"\frac{P(H_1|D)}{P(H_2|D)}", "=", "1681/1").next_to(PDGH2, 2*DOWN)

        self.play(Write(PDGH1), Write(PDGH2))
        self.play(Write(PHGDR))

        self.wait()

class Slide24(Scene):
    def construct(self):
        pdfDGH = MathTex("P(D|H)")
        pdfDGHE = MathTex("P(D|H)", "=" r"\int P(D|", r"\vec{w}", ",H)P(", r"\vec{w}", "|H)d", r"\vec{w}")

        self.add(pdfDGH)
        self.wait()
        self.play(TransformMatchingTex(pdfDGH, pdfDGHE))
        self.wait(2)

        pdfDGHES = MathTex("P(D|H)", "=" r"\int P(D|", "w", ",H)P(", "w", "|H)d", "w")
        self.play(TransformMatchingTex(pdfDGHE, pdfDGHES))

        self.wait()