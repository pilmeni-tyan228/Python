import pygame as pg
w = 800
h = 600
fps = 30


class Player:
    def __init__(self, color, x, y, radius, speed):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_UP] and (self.y - self.radius - self.speed >= 0):
            self.y -= self.speed
        if key[pg.K_DOWN] and (self.y + self.radius + self.speed <= h):
            self.y += self.speed
        if key[pg.K_LEFT] and (self.x - self.radius - self.speed >= 0):
            self.x -= self.speed
        if key[pg.K_RIGHT] and (self.x + self.radius + self.speed <= w):
            self.x += self.speed

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)


class Bomb:
    def __init__(self, color, x, y, radius, speed):
        self.init_parameters = [color, x, y, radius, speed]
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed

        self.len = 50
        self.max_radius = 100
        self.detonation = False

    def is_collide(self, obj):
        return (self.radius + self.len + obj.radius)**2 > (self.x - obj.x)**2 + (self.y - obj.y)**2

    def move(self):
        if self.x > 600:
            self.detonation = True

        if self.detonation:
            self.radius += 5
            if self.radius > self.max_radius:
                self.x = self.init_parameters[1]
                self.radius = self.init_parameters[3]
                self.detonation = False
        else:
            self.x += self.speed

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)


def change_all(boombuk, pl):
    pl.move()
    boombuk.move()
    if boombuk.is_collide(pl):
        boombuk.detonation = True


def draw_all(boombuk, window, pl):
    window.fill((0, 0, 0))
    boombuk.draw(window)
    pl.draw(window)
    pg.display.update()


def main():
    pg.init()
    window = pg.display.set_mode((w, h))
    boombuk = Bomb((40, 50, 60), 50, 240, 30, 3)
    pl = Player((60, 230, 100), 50, 240, 30, 5)

    ticker = pg.time.Clock()
    while True:
        change_all(boombuk, pl)
        draw_all(boombuk, window, pl)
        ticker.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


main()
