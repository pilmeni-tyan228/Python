import pygame as pg
import math

w = 800
h = 600
fps = 30


class Skinhed:
    def __init__(self, x, y, radius, speed, color, gun_w ):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed
        self.angle = 90
        self.gun_w = gun_w

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.angle -= 3*math.pi/180
        if key[pg.K_RIGHT]:
            self.angle += 3*math.pi/180

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)

        x_gun = self.x + self.gun_w * math.cos(self.angle)
        y_gun = self.y + self.gun_w * math.sin(self.angle)
        pg.draw.line(window, self.color, (self.x, self.y), (x_gun, y_gun), 5)


def change_all(skiny):
    skiny.move()


def draw_all(window, skiny):
    window.fill((0, 0, 0))
    skiny.draw(window)
    pg.display.update()


def main():
    pg.init()
    window = pg.display.set_mode((w, h))
    skiny = Skinhed(w/2, h/2, 20, 5, (200, 20, 135), 35)
    ticker = pg.time.Clock()
    while True:
        change_all(skiny)
        draw_all(window, skiny)
        ticker.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


main()
