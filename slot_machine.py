import random

class SlotMachine:
    def __init__(self):
        self.symbols = ('X', 'O', 'J')
        self.money = 0
        self.wins = 0
        self.losses = 0

    def _get_symbol(self):
        return random.choice(self.symbols)

    def play(self, bet):
        self.money -= bet
        symbols = (self._get_symbol(), self._get_symbol(), self._get_symbol())
        if symbols[0] == symbols[1] == symbols[2]:
            self.wins += 1
            self.money += 2 * bet
            return symbols, 'WIN ' + str(2 * bet)
        else:
            self.losses += 1
            return symbols, 'LOSE ' + str(bet)
