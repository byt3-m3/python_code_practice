from abc import ABC


class Player(ABC):
    def challenge(self, player) -> (bool, str):
        pass


class Rock(Player):
    def challenge(self, player: Player) -> (bool, str):
        if isinstance(player, Lizzard):
            return True, "Rock Crushes Lizzard"

        if isinstance(player, Scissors):
            return True, "Rock Crushes Scissors"

        return False, ""

class Scissors(Player):
    def challenge(self, player: Player) -> (bool, str):
        if isinstance(player, Paper):
            return True, "Scissors cuts paper"

        if isinstance(player, Lizzard):
            return True, "Scissors decapitates lizard"

        return False, ""

class Paper(Player):
    def challenge(self, player: Player) -> (bool, str):
        if isinstance(player, Rock):
            return True, "Paper covers rock"

        if isinstance(player, Spock):
            return True, "Paper disproves spock"

        return False, ""

class Lizzard(Player):
    def challenge(self, player: Player) -> (bool, str):
        if isinstance(player, Spock):
            return True, "Lizard poisons spock"

        if isinstance(player, Paper):
            return True, "Lizard eats paper"

        return False, ""


class Spock(Player):
    def challenge(self, player: Player) -> (bool, str):
        if isinstance(player, Rock):
            return True, "Spock vaporizes rock"

        if isinstance(player, Scissors):
            return True, "Spock smashes scissors"

        return False, ""


def build_player(player_type):
    type_map = {
        "spock": Spock,
        "scissor": Scissors,
        "rock": Rock,
        "lizard": Lizzard,
        "paper": Paper,
    }
    _player = type_map.get(player_type)
    if _player:
        return _player()
    else:
        return None



def result(p1: str, p2: str):
    # your excellent code here
    _p1 = build_player(p1.lower())
    _p2 = build_player(p2.lower())
    if _p1 is None or _p2 is None:
        return "Oh, Unknown Thing"

    if type(_p1) == type(_p2):
        return "Draw!"

    results, msg = _p1.challenge(_p2)
    if results:
        return "Player 1 won!"
    else:
        return "Player 2 won!"


print(result("Spock", "Rock"))
print(result("r0ck", "Paper"))