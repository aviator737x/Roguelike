from RogueConstants import start_health, start_attack


class Character:
    def __init__(self):
        self.symbol = ' '
        self.array_symbol = b' '
        self.x = 0
        self.y = 0
        self.health = start_health
        self.attack = start_attack

    def set_position(self, x, y):
        self.x = x
        self.y = y

    # TODO: implement battle
    # None if nobody wins
    @staticmethod
    def battle(players):
        lossers = set()
        players = list(players)
        for player1 in range(len(players)):
            for player2 in range(len(players)):
                if player1 != player2:
                    players[player1].health -= players[player2].attack
                    players[player2].health -= players[player1].attack
            if players[player1].health <= 0:
                lossers.add(players[player1])
        if lossers:
            return lossers
        return None
