from pygame import *
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

FPS = 60


class Ball(sprite.Sprite):
    def __init__(self, xy=(0, 0), xm=0, ym=0):
        sprite.Sprite.__init__(self)
        self.img_load('evil_balloon_32x32.png')
        self.rect.centerx, self.rect.centery = xy

        self.xmove = xm
        self.ymove = ym

    def update(self):
        self.move()
        self.ballBarrier()

    def move(self):
        self.rect.x += self.xmove
        self.rect.y += self.ymove

    def img_load(self, filename):
        self.image = image.load(filename)
        self.rect = self.image.get_rect()

    def ballBarrier(self):
        """
        Checks to make sure ball is within bounds, adjusts movement speed if it's not
        """
        if self.rect.right > SCREEN_WIDTH:
            self.xmove = random.randint(-2, 0)
        if self.rect.left < 0:
            self.xmove = random.randint(0, 2)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.ymove = random.randint(-2, 0)
        if self.rect.top < 0:
            self.ymove = random.randint(0, 2)


class ball_manager():
    def __init__(self, numballs=5, balls=[]):
        self.blist = balls

        if numballs > 0:
            self.multipleBalls(numballs)  # moved this here so balls get init'd only once

    def update(self):
        """
        Update position of all balls
        """
        for ball in self.blist:
            self.ballMove(ball)

    def add_ball(self, xy=(0, 0), xm=0, ym=0):
        self.blist.append(Ball(xy, xm, ym))  # appends a random ball

    def multipleBalls(self, numballs):
        for i in range(numballs):
            self.add_ball((random.randint(0, SCREEN_WIDTH),
                           random.randint(0, SCREEN_HEIGHT)),
                          random.randint(-2, 2),
                          random.randint(-2, 2))


class Character(sprite.Sprite):
    def __init__(self, xy):
        sprite.Sprite.__init__(self)
        self.img_load()

        self.rect.centerx, self.rect.centery = xy

        self.movementspeed = 1
        self.velocity = 0

    def down(self):
        self.velocity += self.movementspeed

    def up(self):
        self.velocity -= self.movementspeed

    def characterMove(self, dy):
        if self.rect.bottom + dy > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0
        elif self.rect.top + dy < 0:
            self.rect.top = 0
            self.velocity = 0
        else:
            self.rect.y += dy

    def update(self):
        self.characterMove(self.velocity)

    def img_load(self):
        self.image = image.load("scary_clown_32x32.png")
        self.rect = self.image.get_rect()


class Game(object):
    def __init__(self):
        init()
        key.set_repeat(1, 30)
        self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = time.Clock()
        display.set_caption('Game')

        event.set_allowed([QUIT, KEYDOWN, KEYUP])
        self.background = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        display.flip()

        self.sprites = sprite.RenderUpdates()

        self.character = Character((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        self.sprites.add(self.character)

        self.balls = ball_manager(5)

        for ball in self.balls.blist:
            self.sprites.add(ball)

    def run(self):
        running = True
        while running == True:
            self.clock.tick(FPS)
            running = self.handleEvents()
            display.set_caption('game %d fps' % self.clock.get_fps())

            self.sprites.clear(self.screen, self.background)

            for sprite in self.sprites:
                sprite.update()

            dirty = self.sprites.draw(self.screen)
            display.update(dirty)

    def handleEvents(self):
        for e in event.get():
            if e.type == QUIT:
                return False

            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    return False
                if e.key == K_UP:
                    self.character.up()
                if e.key == K_DOWN:
                    self.character.down()
                if e.key == K_r:
                    self.sprites.add(Ball((random.randint(0, SCREEN_WIDTH),
                                           random.randint(0, SCREEN_HEIGHT)),
                                          random.randint(-2, 2),
                                          random.randint(-2, 2)))

        return True


def main():
    game = Game()
    game.run()
    quit()


main()
sys.exit()
