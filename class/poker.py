import random

class Card(object):
  def __init__(self, suite, face):
    self._suite = suite
    self._face = face
  
  @property
  def suite(self):
    return self._suite

  @property
  def face(self):
    return self._face

  def __str__(self):
    if self._face == 1:
      fact_str = 'A'
    elif self._face == 11:
      fact_str = 'J'
    elif self._face == 12:
      fact_str = 'Q'
    elif self._face == 13:
      fact_str = 'K'
    else:
      fact_str = str(self._face)
    return '%s%s' % (self._suite, fact_str)

  def __repr__(self):
    return self.__str__()

class Poker(object):

  def __init__(self):
    self._cards = [Card(suite, face) 
                   for suite in '♠♥♣♦'
                   for face in range(1, 14)]
    self._current = 0

  @property
  def cards(self):
    return self._cards

  def shuffle(self):
    self._current = 0
    random.shuffle(self._cards)
  
  @property
  def next(self):
    card = self._cards[self._current]
    self._current += 1
    return card
  
  @property
  def has_next(self):
    return self._current < len(self._cards)

class Player(object):

  def __init__(self, name):
    self._name = name
    self._cards_on_hand = []
  
  @property
  def name(self):
    return self._name

  @property
  def cards_on_hand(self):
    return self._cards_on_hand

  def get(self, card): 
    self._cards_on_hand.append(card)
  
  def arrange(self, card_key):
    self._cards_on_hand.sort(key = card_key)

def get_key(card):
  return (card.face, card.suite)

def main():
  p = Poker()
  p.shuffle()
  players = [Player('GG'), Player("KK"), Player("JJ"), Player("LL")]
  for _ in range(13):
    for player in players:
      player.get(p.next)
  for player in players:
    print(player.name + ':', end=' ')
    player.arrange(get_key)
    print(player.cards_on_hand)

if __name__ == '__main__':
  main()
