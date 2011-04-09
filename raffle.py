# -*- coding: utf-8 -*-
import random

class Raffler(object):

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def raffle(self):
        return random.randint(self.min, self.max)

def notify_raffled_number(droid, number):
    droid.notify("O número sorteado foi: %d!" % number)

def ask_maximum_number(droid):
    return int(droid.dialogGetResponse("Número máximo", "Qual o número de inscritos?").result)
