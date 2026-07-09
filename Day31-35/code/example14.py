"""Exemplo orientado a objetos usando enums.
Um enum é ideal quando um valor deve vir de um conjunto fixo de opções."""
from enum import Enum, unique

import random


@unique
class Suite(Enum):
    """Naipe de cartas."""
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """Carta de jogo."""
    
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        suites = ('♠️', '♥️', '♣️', '♦️')
        faces = ('', 'A', '2', '3', '4', '5', '6', 
                 '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{suites[self.suite.value]} {faces[self.face]}'


class Poker():
    """Baralho de cartas."""
    
    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """Embaralhe o baralho."""
        self.index = 0
        random.shuffle(self.cards)

    def deal(self):
        """Distribua uma carta."""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        """Se há mais cartões."""
        return self.index < len(self.cards)


class Player():
    """Jogador."""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """Pegue um cartão."""
        self.cards.append(card)

    def arrange(self):
        """Classifique as cartas em mãos."""
        self.cards.sort(key=lambda card: (card.suite, card.face))


def main():
    """Ponto de entrada do programa."""
    poker = Poker()
    poker.shuffle()
    players = [
        Player('East Heretic'), Player('West Venom'),
        Player('South Emperor'), Player('North Beggar')
    ]
    while poker.has_more:
        for player in players:
            player.get_card(poker.deal())
    for player in players:
        player.arrange()
        print(player.name, end=': ')
        print(player.cards)


if __name__ == '__main__':
    main()
