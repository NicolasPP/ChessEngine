import pytest

from chess_engine.movement.piece_movement import get_available_moves
from chess_engine.notation.forsyth_edwards_notation import Fen


def test_base_moves():
    assert len(get_available_moves(36, Fen('8/8/8/8/4b3/8/8/8 b KQkq - 0 1'))) is 13


def test_possible_takes():
    assert len(get_available_moves(36, Fen('8/8/8/3P1P2/4b3/3P1P2/8/8 b KQkq - 0 1'))) is 4


def test_fully_blocked():
    assert len(get_available_moves(36, Fen('8/8/8/3p1p2/4b3/3p1p2/8/8 b KQkq - 0 1'))) is 0


def test_blocked_possible_take():
    assert len(get_available_moves(36, Fen('8/8/8/3P1p2/4b3/3p1P2/8/8 b KQkq - 0 1'))) is 2


def test_blocked_take():
    assert len(get_available_moves(36, Fen('8/8/8/5p2/4b3/3p1p2/2P3P1/8 b KQkq - 0 1'))) is 4


@pytest.mark.parametrize("from_index,is_white_turn", [(2, False), (5, False), (61, True), (58, True)])
def test_default_fen(from_index: int, is_white_turn: bool):
    assert len(get_available_moves(from_index, Fen(), is_white_turn)) is 0
