import RockPaperScissors


def test_player_tie_with_r():
    player_input = "r"
    cpu_input = "r"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "tie"


def test_player_win_with_r():
    player_input = "r"
    cpu_input = "s"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "win"


def test_player_lose_with_r():
    player_input = "r"
    cpu_input = "p"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "lose"


def test_player_tie_with_p():
    player_input = "p"
    cpu_input = "p"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "tie"


def test_player_win_with_p():
    player_input = "p"
    cpu_input = "r"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "win"


def test_player_lose_with_p():
    player_input = "p"
    cpu_input = "s"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "lose"


def test_player_tie_with_s():
    player_input = "s"
    cpu_input = "s"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "tie"


def test_player_win_with_s():
    player_input = "s"
    cpu_input = "p"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "win"


def test_player_lose_with_s():
    player_input = "s"
    cpu_input = "r"
    assert RockPaperScissors.get_player_result(player_input, cpu_input) == "lose"
