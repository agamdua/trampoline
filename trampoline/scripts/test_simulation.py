from simulate_game import Game, Player

class TestPLayer(object):
    @classmethod
    def setup_class(self):
        self.user = Player("User")
        self.ai = Player("AI")

    def test_user_creation(self):
        assert self.user.description == "User"
        assert self.user.moves == []

    def test_ai_creation(self):
        assert self.ai.description == "AI"
        assert self.ai.moves == []
