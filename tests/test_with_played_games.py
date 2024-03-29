import pytest

from chess_engine.movement.validate_move import is_move_valid
from chess_engine.notation.forsyth_edwards_notation import Fen
from chess_engine.notation.portable_game_notation import PortableGameNotation
from chess_engine.notation.portable_game_notation import generate_move_text
from chess_engine.notation.portable_game_notation import get_an_from_pgn_game
from chess_engine.notation.portable_game_notation import PGNGame


def get_games() -> list[PGNGame]:
    magnus = PortableGameNotation('test_data/magnus_carlsen_latest_games.pgn')
    hikaru = PortableGameNotation('test_data/hikaru_nakamura_latest_games.pgn')
    return magnus.games + hikaru.games


@pytest.mark.played_games
@pytest.mark.parametrize("game", get_games())
def test_against_played_games(game: PGNGame):
    fen = Fen()
    for reg_move, pgn_move in zip(get_an_from_pgn_game(game), game.pgn_moves):
        white_reg = reg_move.white_move
        black_reg = reg_move.black_move
        if reg_move.white_move is not None:
            white_pgn = generate_move_text(fen, white_reg.from_an, white_reg.dest_an, white_reg.target_fen)
            assert pgn_move.white_move == white_pgn, f' {pgn_move.white_move}  {white_pgn}'
            assert_valid_move(fen, white_reg.from_an, white_reg.dest_an, white_reg.target_fen)
        if reg_move.black_move is not None:
            black_pgn = generate_move_text(fen, black_reg.from_an, black_reg.dest_an, black_reg.target_fen)
            assert pgn_move.black_move == black_pgn, f' {pgn_move.black_move}  {black_pgn}'
            assert_valid_move(fen, black_reg.from_an, black_reg.dest_an, black_reg.target_fen)


def assert_valid_move(fen: Fen, from_an, dest_an, target_fen) -> None:
    assert is_move_valid(from_an.index, dest_an.index, fen)
    fen.make_move(from_an.index, dest_an.index, target_fen)
