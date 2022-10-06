from clue_game import ClueGame
from sample_bot import SampleBot
from sample_bort import SampleBort


def main():
    game = ClueGame([SampleBot(),
                     SampleBot(),
                     SampleBot(),
                     SampleBort()])
    game.execute()


main()
