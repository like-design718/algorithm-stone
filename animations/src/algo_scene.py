﻿from manimlib import *
import random
from datetime import datetime
from .algo_config import *
from .algo_logo import *

class AlgoScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        random.seed(datetime.now())

    def show_sticky_label(text):
        leet = Text(text, color=GOLD_E).center().scale(0.2).to_edge(UP).shift(UP*0.2)
        self.play(ShowCreation(leet))

    def start_logo(self, animate=True, stay=False):
        self.camera.background_rgba = [1, 1, 1, 0.5]
        v = self.create_six_background()
        self.add(v)
        
        if animate:
            self.play(ShowCreation(v))
        
        text = VGroup(
            Text("ACM", font=AlgoFontName, color="#1fa0cf").scale(0.5),
            Text("算法日常", font=AlgoFontName, color="#93582e").scale(0.5)
        ).arrange(buff=0.1)

        self.add(text)

        if animate:
            self.play(Write(text))

        logo = AlgoLogo().scale(0.15).next_to(text, direction=LEFT)
        self.add(logo)

        if animate:
            self.play(ShowCreation(logo))

        group = VGroup(logo, text)

        if animate:
            self.play(group.arrange, run_time=1)
            self.wait()
        else:
            group.arrange()

        if not stay:
            if animate:
                self.play(group.scale, 0.3, run_time=1.5, rate_func=smooth)
                self.wait(0.3)
                self.play(group.to_edge, DL, run_time=1, rate_func=smooth)
            else:
                group.scale(0.3)
                group.to_edge(DL)
        return group

    def create_serif_font(self, msg, color=WHITE):
        return Text(msg, font=AlgoSerifFontName, color=color)

    def init_message(self, msg, delay=3):
        self.subtitle_message = Text(msg, font=AlgoFontName, stroke_width=0, stroke_opacity=0.5, 
            stroke_color=None).scale(0.3).to_edge(DOWN).shift(UP*0.5).set_color("#333")
        self.play(Write(self.subtitle_message))
        self.wait(delay)
        return self.subtitle_message

    def init_messaged(self, msg, delay=0):
        return self.init_message(msg, delay=delay)

    def show_message(self, msg, delay=3):
        self.remove(self.subtitle_message)
        m = Text(msg, font=AlgoFontName, stroke_width=0, stroke_opacity=0.5, 
            stroke_color=None).scale(0.3).to_edge(DOWN).shift(UP*0.5).set_color("#333")
        self.subtitle_message = m
        self.play(ShowIncreasingSubsets(m), run_time=len(msg)*0.2)
        self.wait(delay)

    def show_messaged(self, msg, delay=0):
        self.show_message(msg, delay)

    def rand_color(self):
        r = lambda: random.randint(100, 255)+100
        return '#%02X%02X%02X' % (r(),r(),r())

    def finish(self):
        self.wait(10)

    def create_six_background(self):
        v = VGroup()

        for i in range(0, 9):
            last = None
            for j in range(0, 21):
                r = 0
                if i % 2 == 1:
                    r = RIGHT*(0.5*math.sqrt(3.0))
                op = abs(4-i)
                l = list(Color("#f6f6f6").range_to(Color("#ffffff"), 7))
                p = Polygon(*self.polygon(6), color=l[op]).shift(i*DOWN*1.5+r)
                if last != None:
                    p.next_to(last, RIGHT, buff=0)
                v.add(p)
                last = p

        v.center().scale(0.5)
        return v

    def polygon(self, sides, radius=1, rotation=0, translation=None):
        one_segment = math.pi * 2 / sides

        points = [
            [math.sin(one_segment * i + rotation) * radius,
            math.cos(one_segment * i + rotation) * radius, 0]
            for i in range(sides)]

        if translation:
            points = [[sum(pair) for pair in zip(point, translation)]
                    for point in points]

        return points

    def finish_scene(self, msg):
        self.show_messaged(msg)
        # add image
        code = ImageMobject("assets/code3.png").scale(0.3)
        self.play(ShowCreation(code))
