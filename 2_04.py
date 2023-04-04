import pygame as pg
from random import randint
fps = 60
w_w = 800
w_h = 600


class Kolobok:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.speed = 5
        self.color = color
        self.radius = radius
        self.black = False
        self.manage = True

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_p]:
            self.black = not self.black
        if key[pg.K_m]:
            self.manage = not self.manage

        if self.manage:
            if key[pg.K_UP] and (self.y - self.speed >= self.radius):
                self.y -= self.speed
            if key[pg.K_DOWN] and (self.y + self.speed <= w_h - self.radius):
                self.y += self.speed
            if key[pg.K_RIGHT] and (self.x + self.speed <= w_w - self.radius):
                self.x += self.speed
            if key[pg.K_LEFT] and (self.x - self.speed >= self.radius):
                self.x -= self.speed
        else:
            x, y = pg.mouse.get_pos()
            self.x = x
            self.y = y

    def draw(self, window):
        if self.black:
            pg.draw.circle(window, (0, 0, 0), (self.x, self.y), self.radius)
        else:
            self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
            pg.draw.circle(window, self.color, (self.x, self.y), self.radius)


def change_all(vasya):
    vasya.move()


def draw_all(window, vasya):
    vasya.draw(window)
    pg.display.update()


def main():
    pg.init()
    window = pg.display.set_mode((w_w, w_h))
    vasya = Kolobok(50, 50, (133, 233, 43), 30)


    ticker = pg.time.Clock()
    while True:
        change_all(vasya)
        draw_all(window, vasya)
        ticker.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


main()
