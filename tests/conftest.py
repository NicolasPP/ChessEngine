from chess_engine.movement.piece_movement import PieceMovement


def pytest_sessionstart(session):
    PieceMovement.load()
