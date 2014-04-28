from django.db import models
from user import User


PLAYERS = (
    ('ai', 'Computer'),
    ('us', 'User'),
)

MOVES = (
    ('X', 'X'),
    ('O', 'O'),
)

class Game(models.Model):
    player = models.CharField(max_length = 2,
                              choices = PLAYERS)
    player_move = models.CharField(max_length = 1,
                                   choices = MOVES)
    winner = models.CharField(default=None,
                              choices = PLAYERS)
