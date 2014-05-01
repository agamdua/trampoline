from itertools import combinations

class Game(object):
    winning_combinations = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )

    def __init__(self, player_one, player_two):
        self.board = (0,1,2,3,4,5,6,7,8)
        self.possible_moves = list(self.board)
        self.player_one = player_one
        self.player_two = player_two

    @staticmethod
    def won(player):
        if len(player.moves) > 2:
            for seq in combinations(sorted(player.moves), 3):
                if seq in Game.winning_combinations:
                    return True
                else:
                    return False

    def play(self):
        while True:
            if Game.won(self.player_one):
                print self.player_one.description + ' wins!'
                return
            move = self.player_one.make_move(self, self.player_two)
            print move
            print self.possible_moves
            self.possible_moves.remove(move)
            if Game.won(self.player_two):
                print self.player_two.description + ' wins!'
                return
            move = self.player_two.make_move(self, self.player_one)
            print move
            self.possible_moves.remove(move)
            if not self.possible_moves:
                print 'Tie!'
                return
        print 'over'





class Player(object):
    def __init__(self, description):
        self.description = description
        self.moves = []

    def make_move(self, game, opponent):
        score, move = self.minimax(list(game.possible_moves), opponent)
        return move

    def score(self, player_two):
        if Game.won(self):
            return 10
        elif Game.won(self):
            return -10
        elif not set(range(0, 10)) - set(self.moves) - set(player_two.moves):
            return -5
        else:
            return 0

    def minimax(self, possible_moves, opponent):
        if self.over(opponent, possible_moves):
            score = self.score(opponent)
            if self.description == 'AI':
                score *= -1
                return -1, score

        scores = []
        moves = []

        for move in possible_moves:
            self.moves.append(move)
            possible_moves.remove(move)
            scores.append(opponent.minimax(list(possible_moves), self))
            print "Scores: " + str(scores)
            moves.append(move)

            if scores:
                # print scores
                if self.description == "AI":
                    max_score_index = scores.index(max(scores))
                    best_move = moves[max_score_index]

                else:
                    min_score_index = scores.index(min(scores))
                    print min_score_index
                    best_move = moves[min_score_index]
                    return min_score_index

        print min_score_index
        return scores[min_score_index], best_move

    def over(self, opponent, possible_moves):
        return Game.won(self) or Game.won(opponent) or not possible_moves

# user = Player("User")
# ai = Player("AI")
# game = Game(user, ai)
# game.play()
