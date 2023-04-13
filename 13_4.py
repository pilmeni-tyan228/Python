import pygame as pg
import math

w = 800
h = 600
fps = 30


class Bullet:
    def __init__(self, x, y, radius, speed, color, angle):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed
        self.angle = angle

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)


class Skinhed:
    def __init__(self, x, y, radius, speed, color, gun_w ):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed
        self.angle = math.pi/2
        self.gun_w = gun_w
        self.bullets = []

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.angle -= 3*math.pi/180
        if key[pg.K_RIGHT]:
            self.angle += 3*math.pi/180

        x, y = 0, 0
        if key[pg.K_UP]:
            x = self.x + self.speed * math.cos(self.angle)
            y = self.y + self.speed * math.sin(self.angle)
        if key[pg.K_DOWN]:
            x = self.x - self.speed * math.cos(self.angle)
            y = self.y - self.speed * math.sin(self.angle)

        if (self.radius <= x <= w - self.radius) and (self.radius <= y <= h - self.radius):
            self.x = x
            self.y = y

        for bullet in self.bullets:
            bullet.move()

    def shoot(self):
        if pg.mouse.get_pressed(3)[0]:
            bullet = Bullet(self.x, self.y, self.radius/5, self.speed * 2, self.color, self.angle)
            self.bullets.append(bullet)

    def draw(self, window):
        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)

        x_gun = self.x + self.gun_w * math.cos(self.angle)
        y_gun = self.y + self.gun_w * math.sin(self.angle)
        pg.draw.line(window, self.color, (self.x, self.y), (x_gun, y_gun), 5)

        for bullet in self.bullets:
            bullet.draw(window)


def change_all(skiny):
    skiny.move()
    skiny.shoot()


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
