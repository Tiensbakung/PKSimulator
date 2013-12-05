import time

from basesprite import BaseSprite
import bins

class BallSprite(BaseSprite):

    def __init__(self, name, size, position, heading=0):
        BaseSprite.__init__(self, size, position, heading, 'Ball.png')
        self.name = name
        self.score_red = 0
        self.score_blue = 0
        self.t0 = time.time()

    def update(self):
        dt = time.time() - self.t0
        if bins.bin_red.collidepoint(self.rect.center):
            if dt >= 10:
                self.score_red += 1
                self.t0 = time.time()
        elif bins.bin_blue.collidepoint(self.rect.center):
            if dt >= 10:
                self.score_blue += 1
                self.t0 = time.time()
        else:
            self.t0 = time.time()
        super(BallSprite, self).update()
