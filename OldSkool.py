# Old_Skool - an experiment in writing an old skool 8-bit graphics demo in python, to help learn Python
# Old_Skool © 2021 by George Moore is licensed under Attribution-NonCommercial-ShareAlike 4.0 International

import pygame
import math
import random
import time

pygame.init()

x_min = 0
y_min = 0
x_max = 800
y_max = 800

line_colour = (255,255,255)
line_width = 3
line_start = (200, 200)
line_end = (600, 600)

x_origin = x_max/2
y_origin = y_max/2
radius = 400
length = 300
points = 360
pointAngle = int(360/points)
range_min = 0
range_max = 360


screen = pygame.display.set_mode((x_max, y_max))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]: done = True

    x = 0
    y = 0
    for angle in range (range_min, range_max, pointAngle):

        rads = math.radians(angle)
        x = math.cos(rads) * length
        y = math.sin(rads) * length

        rnd_red = random.randint(0, 255)
        rnd_green = random.randint(0, 255)
        rnd_blue = random.randint(0, 255)
        line_colour = (rnd_red, rnd_green, rnd_blue)

        pygame.draw.line(screen, line_colour, (x+radius, y+radius), (0+radius, 0+radius), line_width);

    time.sleep(0.25)
    pygame.display.flip()

