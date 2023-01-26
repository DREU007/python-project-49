"""Progression game.

User has to give missing value in progression"""
from brain_games.common_core import core_algorithm
from random import randint


def single_progression_game():
    """Assign progression, exclude one item and invite user to guess it.
    Return correct answer."""
    num_items = randint(5, 10)
    start_psn = randint(1, 100)
    step = randint(1, 20)
    progression_list = [
        str(start_psn + item * step) for item in range(num_items)]
    missing_item = randint(0, num_items - 1)
    answer = progression_list[missing_item]
    progression_list[missing_item] = '..'

    invite_msg = ('What number is missing in the progression?\n'
                  f'Question: {" ".join(progression_list)}')
    print(invite_msg)
    return answer


def main():
    """Start progression game."""
    core_algorithm(single_progression_game)