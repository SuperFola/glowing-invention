# import drawing lib
import pygame
# game constants
from constants import *


# this object will represent a button (with which the user can interract)
class Button:
    def __init__(self, xpos, ypos, xsize, ysize, text, color, font, font_color):
        self.xpos = xpos
        self.ypos = ypos
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
        self.font_color = font_color
        # font is a pygame SysFont object
        # we use the render method to create an image from a text message,
        # with size and an anti-aliasing boolean
        self.font = font
        self.text = self.create_texts(text)

    def create_texts(self, txt):
        if isinstance(txt, list):
            n = []
            for t in txt:
                n.append(self.font.render(t, True, self.font_color))
            return n
        else:
            return [self.font.render(txt, True, self.font_color)]

    def render(self, win):
        # we draw a rect using pygame.draw module
        # we give the window, the color and then the rect defining
        # the rectangle
        pygame.draw.rect(win, self.color, (self.xpos, self.ypos, self.xsize, self.ysize))
        # we draw the text on the window
        for i, txt in enumerate(self.text):
            win.blit(txt, (self.xpos, self.ypos + i * 20))

    def collide(self, xmouse, ymouse):
        # we check if the (xmouse, ymouse) is in the button rect
        if self.xpos <= xmouse <= self.xpos + self.xsize and self.ypos <= ymouse <= self.ypos + self.ysize:
            # we return the boolean True if the mouse clicked on the button
            return True
        else:
            # otherwise we return the boolean False
            return False
