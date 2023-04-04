import pygame as pg
w = 800
h = 600
fps = 30


def change_all():
    pass


def draw_all():
    pass


def main():
    pg.init()
    window = pg.display.set_mode((w, h))
    ticker = pg.time.Clock()
    while True:
        change_all()
        draw_all()
        ticker.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


main()
