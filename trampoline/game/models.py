from django.db import models

# Third party
from mptt.models import MPTTModel, TreeForeignKey

# Custom
from user import User

PLAYERS = (
    ('ai', 'Computer'),
    ('us', 'User'),
)

MOVES = (
    ('X', 'X'),
    ('O', 'O'),
)

class Game(MPTTModel):
    player = models.CharField(max_length = 2,
                              choices = PLAYERS)
    player_move = models.CharField(max_length = 1,
                                   choices = MOVES)
    previous_move = TreeForeignKey('self',
                                    null=True,
                                    blank=True,
                                    related_name='children')
    end = models.BooleanField(default=False)
