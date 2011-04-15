# -*- coding: utf-8 -*-
import android
import random

PADRAO = '200'

class Raffler(object):

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def raffle(self):
        return random.randint(self.min, self.max)

def notify_raffled_number(droid, number):
    droid.dialogCreateAlert("Sorteio", "O número sorteado foi: %d!" % number)
    droid.dialogSetPositiveButtonText("Ok")
    droid.dialogShow()

def ask_maximum_number(droid):
    droid.dialogCreateInput("Número máximo", "Qual o número de inscritos?", PADRAO)
    droid.dialogSetPositiveButtonText("Sortear")
    droid.diagloSetNegativeButtonText("Cancelar")
    droid.dialogShow()
    max_number =  int(droid.dialogGetResponse().result['value'])
    return max_number

def do_raffle(droid):
    droid.addOptionsMenuItem("Novo sorteio", "do_raffle", None, "star_on")
    droid.addOptionsMenuItem("Sair", "exit", None, "star_off")

    response = { 'name' : 'do_raffle' }
    while response['name'] != 'exit':
        response = droid.eventWait(10000).result
        droid.dialogDismiss()
        max_number = ask_maximum_number(droid)
        raffled_number = Raffler(min=1, max=max_number).raffle()
        notify_raffled_number(droid, raffled_number)

if __name__ == '__main__':
    droid = android.Android()
    do_raffle(droid)
