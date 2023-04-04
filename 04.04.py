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


def change_all(tob):
    tob.move()


def draw_all(window, tob):
    window.fill((0, 0, 0))
    tob.draw(window)
    pg.display.update()


def main():
    pg.init()
    window = pg.display.set_mode((w, h))
    tob = Tobik(50, 50, 50, (200, 30, 150), 9)
    ticker = pg.time.Clock()

    while True:
        change_all(tob)

        draw_all(window, tob)

        ticker.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                tob.x = x
                tob.y = y


main()
