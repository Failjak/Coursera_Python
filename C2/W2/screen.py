#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math


# =======================================================================================
# Класс для работы с векторами
# =======================================================================================

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, vec):
        """"возвращает разность двух векторов"""
        return Vec2d(self.x - vec.x, self.y - vec.y)

    def __add__(self, vec):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + vec.x, self.y + vec.y)

    def __len__(self):
        """возвращает длину вектора"""
        return Vec2d(math.sqrt(self.x ** 2 + self.y ** 2))

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x * k, self.y * k)

    def int_pair(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return self.x, self.y


# =======================================================================================
# Класс замкнутых линий
# =======================================================================================
class Polyline:
    SCREEN_DIM = (800, 600)

    def __init__(self, points=None, speeds=None):
        self.points = points or []
        self.speeds = speeds or []

    def append(self, coord, speed):
        """функуия добавления точки"""
        self.points.append(Vec2d(coord[0], coord[1]))
        self.speeds.append(speed)

    # def append_curve(self):
    #     """функция добавления кривой"""
    #     if len(self.all_points[-1]) > 2:
    #         self.all_points.append([])
    #         self.points = self.all_points[-1]
    #
    #         self.all_speeds.append([])
    #         self.speeds = self.all_speeds[-1]

    def delete(self):
        self.points.pop()
        self.speeds.pop()

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for i, point in enumerate(self.points):
            point.x = point.x + self.speeds[i][0]
            point.y = point.y + self.speeds[i][1]

            if point.x > SCREEN_DIM[0] or point.x < 0:
                self.speeds[i] = (-self.speeds[i][0], self.speeds[i][1])
            if point.y > SCREEN_DIM[1] or point.y < 0:
                self.speeds[i] = (self.speeds[i][0], -self.speeds[i][1])

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
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
    """функция отрисовки экрана справки программы"""
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
# Класс Knot
# =======================================================================================
class Knot(Polyline):
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
# Класс управления скоростью
# =======================================================================================
class SpeedRedact:
    """ Class for editing the speed of points. """
    def __init__(self, speeds=None, max_speed=10):
        self.__max_speed = max_speed
        self.speeds = speeds or []

    def increase(self, booster=1.1):
        """ Increasing the speed of points. """
        for i in range(len(self.speeds)):
            self.speeds[i] = self.speeds[i][0] * booster, self.speeds[i][1] * booster

    def decrease(self, brake=1.1):
        """ Decreasing the speed of points. """
        for i in range(len(self.speeds)):
            self.speeds[i] = self.speeds[i][0] / brake, self.speeds[i][1] / brake


# =======================================================================================
# Класс для добавления кривых
# =======================================================================================
class Curves(Polyline, SpeedRedact):
    """ Managing curves. """
    def __init__(self, curves=None):
        Polyline.__init__(self)
        SpeedRedact.__init__(self)
        self.__curves = curves or []

    def increase(self, booster=1.1):
        for polyline in self.__curves:
            pass

    def clear(self):
        """ Deleting all curves. """
        self.__curves = []

    def append_curve(self, polyline):
        """ Append curve. """
        self.__curves.append(polyline)

    def get_last_curve(self):
        return self.__curves[-1]

    def delete(self):
        if len(self.__curves) != 1:
            self.__curves[-1].delete()
            if len(self.__curves[-1].points) == 0:
                self.__curves.pop()

        elif len(self.__curves[-1].points) > 3:
            self.__curves[0].delete()

    def draw_curves(self, style="points", width=3, color=(255, 255, 255)):
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
# Основная программа
# =======================================================================================
SCREEN_DIM = (800, 600)

if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
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