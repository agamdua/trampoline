from simulate_game import Game, Player

class TestSimulation(object):
    @classmethod
    def setup_class(self):
        self.user = Player("User")
        self.ai = Player("AI")
        self.game = Game(self.user, self.ai)

    def test_game_won(self):
        self.user.moves = [0,1,2]
        assert Game.won(self.user) == True
        self.user.moves = [0,4,8]
        assert Game.won(self.user) == True
        self.user.moves = [1,5,8]
        assert Game.won(self.user) == False
        self.user.moves = [7,4,2]
        assert Game.won(self.user) == False
