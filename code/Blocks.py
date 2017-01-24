#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import os

BLOCK_HEIGHT = 32
BLOCK_WIDTH = 32
BLOCK = (BLOCK_WIDTH, BLOCK_HEIGHT)
ICON_DIR = os.path.dirname(__file__)
BLOCK_COLOR = "#000000"
ANIMATION_TELEPORT = [("%s\sprites\portal1.png" % ICON_DIR),
                      ("%s\sprites\portal2.png" % ICON_DIR)]

class Block(sprite.Sprite):
    def __init__(self, x ,y):
        sprite.Sprite.__init__(self)

        self.image = image.load("%s\sprites\platform.png" % ICON_DIR)
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)


class DeathBlock(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.image = image.load("%s\sprites\death.png" % ICON_DIR)
        self.image.set_colorkey(Color(BLOCK_COLOR))

class BlockTeleport(Block):
    def __init__(self, x, y, goX, goY):
        Block.__init__(self, x, y)
        self.goX = goX
        self.goY = goY
        self.image = Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.set_colorkey(Color(BLOCK_COLOR))
        Animation = []
        for anim in ANIMATION_TELEPORT:
            Animation.append((anim, 0.3))
        self.Animation = pyganim.PygAnimation(Animation)
        self.Animation.play()
    def update(self):
        self.image.fill(Color(BLOCK_COLOR))
        self.Animation.blit(self.image, (0,0))

