#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

BLOCK_HEIGHT = 32
BLOCK_WIDTH = 32
BLOCK = (BLOCK_WIDTH, BLOCK_HEIGHT)
ICON_DIR = os.path.dirname(__file__)

class Block(sprite.Sprite):
    def __init__(self, x ,y):
        sprite.Sprite.__init__(self)
        self.image = image.load("%s\sprites\platform.png" % ICON_DIR)
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)

