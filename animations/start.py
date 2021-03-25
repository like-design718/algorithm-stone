from manimlib import *

class MonotonicStack(Scene):
    def show(self, arr, offset):
        list_of_squares = [Square().scale(0.6) for i in arr]
        squares = VGroup(*list_of_squares)
        squares.arrange(buff=0.)
        squares.shift(offset)

        self.play(
            ShowCreation(squares)
        )

        nums = [Text(str(i), font_size=20) for i in arr]
        for i in range(len(arr)):
            nums[i].move_to(squares[i].get_center())
            self.add(nums[i])

        self.wait(5)

    def construct(self):
        self.show([73, 74, 75, 71, 69, 72, 76, 73], UP*3)
        # 
        
