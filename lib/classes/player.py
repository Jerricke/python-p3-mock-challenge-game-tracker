class Player:
    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value

    def results(self, new_result=None):
        from classes.result import Result

        if new_result:
            self._results.append(new_result)
        return self._results

        pass

    def games_played(self, new_game=None):
        from classes.game import Game

        if new_game:
            self._games_played.append(new_game)
        return self._games_played
        pass

    def played_game(self, game):
        return game in self._games_played
        pass

    def num_times_played(self, game):
        count = 0
        for g in self._games_played:
            if game == g:
                count += 1
        return count
        pass

    @classmethod
    def highest_scored(cls, game):
        pass
