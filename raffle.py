import random

class Raffler(object):

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def raffle(self):
        return random.randint(self.min, self.max)
