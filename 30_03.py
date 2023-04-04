import pygame as pg


class Alybert:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 100
        self.height = 70

    def move(self):
        self.x += 1

    def draw(self, window):
        pg.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))


class Grisha:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = 90
        self.height = 60

    def move(self):
        self.y += 2

    def draw(self, window):
        pg.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))






def change_all(alyberts, grishas):
    for alybert in alyberts:
        alybert.move()
    for g in grishas:
        g.move()


def draw_all(window, alyberts, grishas):
    window.fill((0, 0, 0))
    for alybert in alyberts:
        alybert.draw(window)
    for g in grishas:
        g.draw(window)
    pg.display.update()


def main():
    pg.init()
    window = pg.display.set_mode((800, 600))
    fps = 60
    clock = pg.time.Clock()

    alybert1 = Alybert(50, 50, (0, 100, 0))
    alybert2 = Alybert(50, 130, (0, 0, 200))
    alybert3 = Alybert(50, 210, (150, 0, 0))
    alyberts = [alybert1, alybert2, alybert3]

    grisha = Grisha(40, 90, (50, 50, 50))
    grishas = [grisha]

    while True:
        change_all(alyberts, grishas)
        draw_all(window, alyberts, grishas)
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


main()
