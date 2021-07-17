#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math


# =======================================================================================
# A class for working with vectors
# =======================================================================================

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, vec):
        """" The return difference of two vectors. """
        return Vec2d(self.x - vec.x, self.y - vec.y)

    def __add__(self, vec):
        """ The returns sum of two vectors"""
        return Vec2d(self.x + vec.x, self.y + vec.y)

    def __len__(self):
        """ The returns vector lenght. """
        return Vec2d(math.sqrt(self.x ** 2 + self.y ** 2))

    def __mul__(self, k):
        """ The returns product of a vector by a number. """
        return Vec2d(self.x * k, self.y * k)

    def int_pair(self):
        """
        The returns coordinates defining the vector (coordinates of the end point of the vector).

        Coordinates start points of the vector match with start coordinate system point (0, 0)
        """
        return self.x, self.y


# =======================================================================================
# Class closed line
# =======================================================================================
class Polyline:
    """ Managing polyline. """
    SCREEN_DIM = (800, 600)

    def __init__(self, points=None, speeds=None):
        self.points = points or []
        self.speeds = speeds or []

    def append(self, coord, speed):
        """ Adding a point."""
        self.points.append(Vec2d(coord[0], coord[1]))
        self.speeds.append(speed)

    def delete(self):
        """ Deleting a point."""
        self.points.pop()
        self.speeds.pop()

    def set_points(self):
        """ Recalculation of reference point. """
        for i, point in enumerate(self.points):
            point.x = point.x + self.speeds[i][0]
            point.y = point.y + self.speeds[i][1]

            if point.x > Polyline.SCREEN_DIM[0] or point.x < 0:
                self.speeds[i] = (-self.speeds[i][0], self.speeds[i][1])
            if point.y > Polyline.SCREEN_DIM[1] or point.y < 0:
                self.speeds[i] = (self.speeds[i][0], -self.speeds[i][1])

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """ Drawing points on the screen. """
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.points[p_n].x), int(self.points[p_n].y)),
                                 (int(self.points[p_n + 1].x), int(self.points[p_n + 1].y)), width)
        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.x), int(p.y)), width)


def draw_help():
    """ Drawing the help to the program. """
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["Z", "Delete last reference point"])
    data.append(["SPACE", "Add new curve"])
    data.append(["Up", "Increase speed"])
    data.append(["Down", "Decrease speed"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Class Knot
# =======================================================================================
class Knot(Polyline):
    """"""
    def __init__(self, points=None, count=0):
        super().__init__()
        self.points = points or []
        self.count = count

    def __get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return (points[deg] * alpha) + (self.__get_point(points, alpha, deg - 1) * (1 - alpha))

    def __get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.__get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(self.__get_points(ptn, self.count))
        return res


# =======================================================================================
# Speed control class
# =======================================================================================
class SpeedRedact:
    """ Class for editing the speed of points. """
    def __init__(self, speeds=None, max_speed=10):
        self.__max_speed = max_speed
        self.speeds = speeds or []

    @staticmethod
    def activation(value):
        return abs(1/math.tanh(value))

    def increase(self):
        """ Increasing the speed of points. """
        for i in range(len(self.speeds)):
            value = self.speeds[i]
            self.speeds[i] = value[0] * self.activation(value[0]), value[1] * self.activation(value[1])

    def decrease(self):
        """ Decreasing the speed of points. """
        for i in range(len(self.speeds)):
            value = self.speeds[i]
            self.speeds[i] = value[0] / self.activation(value[0]), value[1] / self.activation(value[1])


# =======================================================================================
# Class for adding curves
# =======================================================================================
class Curves(Polyline):
    """ Managing curves. """
    def __init__(self, curves=None):
        Polyline.__init__(self)
        self.__curves = curves or []

    def increase(self):
        """ Increasing the speed for all curves. """
        for polyline in self.__curves:
            speed_redact = SpeedRedact(polyline.speeds)
            speed_redact.increase()

    def decrease(self):
        """ Decreasing the speed for all curves. """
        for polyline in self.__curves:
            speed_redact = SpeedRedact(polyline.speeds)
            speed_redact.decrease()

    def clear(self):
        """ Deleting all curves. """
        self.__curves = []

    def append_curve(self, polyline):
        """ Append curve. """
        self.__curves.append(polyline)

    def get_last_curve(self):
        return self.__curves[-1]

    def delete(self):
        """ Deleting curves. """
        if len(self.__curves) != 1:
            self.__curves[-1].delete()
            if len(self.__curves[-1].points) == 0:
                self.__curves.pop()

        elif len(self.__curves[-1].points) > 3:
            self.__curves[0].delete()

    def draw_curves(self, style="points", width=3, color=(255, 255, 255)):
        """ Drawing curves. """
        for polyline in self.__curves:
            if style == "points":
                polyline.draw_points()

            elif style == "line":
                knot = Knot(polyline.points, steps)
                curve = Polyline(knot.get_knot())
                curve.draw_points(style, width, color)

    def set_points(self):
        for polyline in self.__curves:
            polyline.set_points()


# =======================================================================================
# Main program
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(Polyline.SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    polyline = Polyline()
    curves = Curves([polyline, ])

    steps = 35
    working = True
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    curves.clear()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

                if event.key == pygame.K_UP:
                    curves.increase()
                if event.key == pygame.K_DOWN:
                    curves.decrease()

                if event.key == pygame.K_SPACE:
                    curves.append_curve(Polyline())
                    polyline = curves.get_last_curve()

                if event.key == pygame.K_z:
                    curves.delete()

            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.append(event.pos, (random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        curves.draw_curves()
        curves.draw_curves("line", 3, color)

        if not pause:
            curves.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)