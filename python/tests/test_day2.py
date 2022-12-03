import pytest
from ..day2 import *

@pytest.mark.parametrize("your_hand, their_hand, expected", [(1,1,4),
(2,1,1), (3,1,7), (1,2,8), (2,2,5), (3,2,2), (3, 3, 6), (1, 3, 3), (2, 3, 9)])
def test_play_round(your_hand, their_hand, expected):
    assert play_round(your_hand,their_hand) == expected

@pytest.mark.parametrize('entry, expected', [
    ("A X", (1, 1)), ("B X", (2, 1)), ("C X", (3, 1)), ( "A Y", (1, 2)),
    ("B Y" , (2, 2)), ("C Y", (3, 2)), ("A Z", (1, 3)), ("B Z", (2, 3)), 
    ("C Z", (3, 3)) 
    ])
def test_decode(entry: str, expected):
    assert decode(entry) == expected

@pytest.mark.parametrize('entry, expected', [
    ('A Y', (1,1)), ('B X', (2, 1)), ('C Z', (3,1)),
    ('A X', (1, 3)), ('A Z', (1, 2)), ('B Y', (2, 2)),
    ('C Y', (3, 3))
])
def test_decode_second(entry, expected):
    assert decode_second(entry) == expected
