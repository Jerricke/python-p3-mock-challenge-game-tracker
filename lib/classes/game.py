class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value

    def results(self, new_result=None):
        from classes.result import Result

        if new_result:
            self._results.append(new_result)
        return self._results

        pass

    def players(self, new_player=None):
        from classes.player import Player

        if new_player:
            self._players.append(new_player)
        return self._players

        pass

    def average_score(self, player):
        res = []
        for r in self._results:
            if r.player == player:
                res.append(r.score)
        return sum(res) / len(res)
        pass
