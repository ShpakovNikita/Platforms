#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from Character import*
from pygame import*
from Block import*
from Camera import*

WIDTH = 800
LENGTH = 640
SCREEN = (WIDTH, LENGTH)
BACKGROUND_COLOR = "#004400"


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, LENGTH))
    pygame.display.set_caption("Platforms")
    background = Surface(SCREEN)
    hero = Character(55, 55)
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)

    level = [
        "-----------------------------------",
        "-                                 -",
        "-                         -----   -",
        "-                                 -",
        "-            --                   -",
        "-                                 -",
        "-                         -----   -",
        "-                                 -",
        "-        -----                    -",
        "--                                -",
        "-                                 -",
        "-                ------           -",
        "-                                 -",
        "-                                 -",
        "-      -------                    -",
        "-                                 -",
        "-                                 -",
        "-                                 -",
        "-                ---              -",
        "-                             --- -",
        "-         ----                    -",
        "-                                 -",
        "-----------------------------------"]

    total_level_width = len(level[0]) * BLOCK_WIDTH
    total_level_height = len(level) * BLOCK_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    timer = pygame.time.Clock()
    left = right = up = shift = False
    background.fill(Color(BACKGROUND_COLOR))
    x = 0
    y = 0
    for cow in level:
        for element in cow:
            if element == "-":
                block = Block(x, y)
                entities.add(block)
                platforms.append(block)

            x += BLOCK_WIDTH

        y += BLOCK_HEIGHT
        x = 0

    while 1:
        timer.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            if e.type == KEYDOWN and (e.key == K_LEFT or e.key == K_a):
                left = True
            if e.type == KEYDOWN and (e.key == K_RIGHT or e.key == K_d):
                right = True
            if e.type == KEYDOWN and (e.key == K_UP or e.key == K_w):
                up = True
            if e.type == KEYDOWN and e.key == K_LSHIFT:
                shift = True

            if e.type == KEYUP and (e.key == K_RIGHT or e.key == K_d):
                right = False
            if e.type == KEYUP and (e.key == K_LEFT or e.key == K_a):
                left = False
            if e.type == KEYUP and (e.key == K_UP or e.key == K_w):
                up = False
            if e.type == KEYUP and e.key == K_LSHIFT:
                shift = False
        screen.blit(background, (0, 0))
        hero.update(left, right, up, shift, platforms)
        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()





if __name__ == "__main__":
    main()