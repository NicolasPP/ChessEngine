import pytest

from chess_engine.movement.validate_move import is_destination_valid
from chess_engine.movement.validate_move import is_from_correct_side
from chess_engine.movement.validate_move import is_material_insufficient
from chess_engine.movement.validate_move import is_move_valid
from chess_engine.movement.validate_move import is_side_valid
from chess_engine.movement.validate_move import is_stale_mate
from chess_engine.notation.forsyth_edwards_notation import Fen


@pytest.mark.parametrize("from_fen_val,is_white_turn,expected",
                         [('p', True, False), ('P', True, True), ('p', False, True), ('P', False, False)])
def test_is_from_correct_side(from_fen_val: str, is_white_turn: bool, expected: bool):
    assert is_from_correct_side(from_fen_val, is_white_turn) is expected


@pytest.mark.parametrize("from_index,dest_index,fen,expected", [
    (28, 20, Fen("8/8/8/4P3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 1, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 7, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 55, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 56, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 4, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 24, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 31, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 60, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 11, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 13, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 18, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 22, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 34, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 38, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 43, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 45, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
])
def test_is_destination_valid(from_index: int, dest_index: int, fen: Fen, expected: bool):
    assert is_destination_valid(from_index, dest_index, fen) is expected


@pytest.mark.parametrize("from_index,dest_index,fen,expected", [
    (1, 1, Fen(), False),
    (0, 1, Fen(), False),
    (0, 63, Fen(), True),
    (4, 0, Fen("r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1"), True)
])
def test_is_side_valid(from_index: int, dest_index: int, fen: Fen, expected: bool):
    assert is_side_valid(from_index, dest_index, fen) is expected


@pytest.mark.parametrize("fen,from_index,expected", [
    (Fen(), 16, False),
    (Fen(), 0, False),
    (Fen(), 63, True)

])
def is_from_valid(fen: Fen, from_index: int, expected: bool):
    assert is_from_valid(fen, from_index) is expected


@pytest.mark.parametrize("from_index,dest_index,fen,expected", [
    (48, 32, Fen(), True),
    (48, 24, Fen(), False),
    (28, 1, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 7, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 55, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 56, Fen("8/8/8/4B3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 4, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 24, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 31, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 60, Fen("8/8/8/4R3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 11, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 13, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 18, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 22, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 34, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 38, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 43, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
    (28, 45, Fen("8/8/8/4N3/8/8/8/8 w KQkq - 0 1"), True),
])
def test_is_move_valid(from_index: int, dest_index: int, fen: Fen, expected: bool):
    assert is_move_valid(from_index, dest_index, fen) is expected


@pytest.mark.parametrize("fen", [
    Fen("k7/2Q5/8/8/8/8/8/7K w - - 0 1"),
    Fen("k7/7R/8/7p/5p1P/b4N2/8/RQ5K b - - 0 1")
])
def test_is_stale_mate(fen: Fen):
    assert is_stale_mate(fen)


@pytest.mark.parametrize("fen,expected", [
    (Fen("k7/8/8/8/8/8/8/7K w KQkq - 0 1"), True),
    (Fen("k7/8/8/8/8/8/8/6KN w KQkq - 0 1"), True),
    (Fen("k7/8/8/8/8/8/8/5KNN w KQkq - 0 1"), True),
    (Fen("kb6/8/8/8/8/8/8/6KB w KQkq - 0 1"), True),
    (Fen("kn6/8/8/8/8/8/8/6KN w KQkq - 0 1"), True),
    (Fen("kb6/8/8/8/8/8/8/6KN w KQkq - 0 1"), True),
    (Fen("kn6/8/8/8/8/8/8/5KNN w KQkq - 0 1"), False),
    (Fen("k7/8/8/8/8/8/8/5KBB w KQkq - 0 1"), False),
    (Fen("kp6/8/8/8/8/8/8/7K w KQkq - 0 1"), False),
])
def test_is_material_insufficient(fen: Fen, expected: bool):
    assert is_material_insufficient(fen) == expected
