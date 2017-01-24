#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os
import pyganim
import Blocks

MOVE_SPEED = 7
WIDTH_CH = 22
HEIGHT_CH = 32
JUMP_POWER = 10
GRAVITY = 0.35
ICON_DIR = os.path.dirname(__file__)
ANIMATION_DELAY = 0.1
SUPER_SPEED_ANIMATION_DELAY = 0.05
COLOR = "#888888"
ANIMATION_RIGTH = [("%s/sprites/r1.png" % ICON_DIR),
                   ("%s/sprites/r2.png" % ICON_DIR),
                   ("%s/sprites/r3.png" % ICON_DIR),
                   ("%s/sprites/r4.png" % ICON_DIR),
                   ("%s/sprites/r5.png" % ICON_DIR)]
ANIMATION_LEFT = [("%s/sprites/l1.png" % ICON_DIR),
                  ("%s/sprites/l2.png" % ICON_DIR),
                  ("%s/sprites/l3.png" % ICON_DIR),
                  ("%s/sprites/l4.png" % ICON_DIR),
                  ("%s/sprites/l5.png" % ICON_DIR)]
ANIMATION_STAY = [("%s/sprites/0.png" % ICON_DIR, 0.1)]
ANIMATION_JUMP = [("%s/sprites/j.png" % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [("%s/sprites/jr.png" % ICON_DIR, 0.1)]
ANIMATION_JUMP_LEFT = [("%s/sprites/jl.png" % ICON_DIR, 0.1)]
#ANIMATION_SIT = [("%s/sprites/d.png" % ICON_DIR, 0.1)]
#ANIMATION_SPRINT = []
#ANIMATION_FALL = []


class Character(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.yvel = 0
        self.xvel = 0
        self.onGround = False
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH_CH, HEIGHT_CH))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH_CH, HEIGHT_CH)
        self.image.set_colorkey(Color(COLOR))
        Animation = []
        for anim in ANIMATION_RIGTH:
            Animation.append((anim, ANIMATION_DELAY))
        self.AnimRight = pyganim.PygAnimation(Animation)
        self.AnimRight.play()

        Animation = []
        for anim in ANIMATION_RIGTH:
            Animation.append((anim, SUPER_SPEED_ANIMATION_DELAY))
        self.AnimSuperRight = pyganim.PygAnimation(Animation)
        self.AnimSuperRight.play()

        Animation = []
        for anim in ANIMATION_LEFT:
            Animation.append((anim, ANIMATION_DELAY))
        self.AnimLeft = pyganim.PygAnimation(Animation)
        self.AnimLeft.play()

        Animation = []
        for anim in ANIMATION_LEFT:
            Animation.append((anim, SUPER_SPEED_ANIMATION_DELAY))
        self.AnimSuperLeft = pyganim.PygAnimation(Animation)
        self.AnimSuperLeft.play()

        self.AnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.AnimStay.play()
        self.AnimStay.blit(self.image, (x, y))

        self.AnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.AnimJump.play()

        self.AnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.AnimJumpLeft.play()

        self.AnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.AnimJumpRight.play()


    def update(self, left, right, up, shift, platforms):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.image.fill(Color(COLOR))
                self.AnimJump.blit(self.image, (0, 0))
        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.AnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.AnimLeft.blit(self.image, (0, 0))

        if left and shift:
            self.xvel = -MOVE_SPEED*2
            self.image.fill(Color(COLOR))
            if up:
                self.AnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.AnimSuperLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.AnimJumpRight.blit(self.image, (0, 0))
            else:
                self.AnimRight.blit(self.image, (0, 0))

        if right and shift:
            self.xvel = MOVE_SPEED*2
            self.image.fill(Color(COLOR))
            if up:
                self.AnimJumpRight.blit(self.image, (0, 0))
            else:
                self.AnimSuperRight.blit(self.image, (0, 0))

        if not (left or right):
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.AnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY
            #if (self.yvel > 0): FALL

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:

            if sprite.collide_rect(self, p):

                if isinstance(p, Blocks.DeathBlock):
                    self.death()

                elif isinstance(p, Blocks.BlockTeleport):
                    self.teleportating(p.goX, p.goY)

                else:

                    if xvel > 0:
                        self.rect.right = p.rect.left

                    if xvel < 0:
                        self.rect.left = p.rect.right

                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0

    def death(self):
        self.AnimStay.blit(self.image, (0, 0))
        time.wait(500)
        self.teleportating(self.startX, self.startY)

    def teleportating(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
