import pygame as pg
w = 800
h = 600
fps = 60


class Tobik:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)


def change_all(tobiks):
    for tob in tobiks:
        tob.move()


def draw_all(window, tobiks):
    window.fill((0, 0, 0))
    for tob in tobiks:
        tob.draw(window)
    pg.display.update()


def main():
    pg.init()
    window = pg.display.set_mode((w, h))
    tobiks = []
    ticker = pg.time.Clock()
    while True:
        change_all(tobiks)

        draw_all(window, tobiks)

        ticker.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                tob = Tobik(x, y, 50, (200, 30, 150), 9)
                tobiks.append(tob)


main()
