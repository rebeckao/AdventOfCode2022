class Play:
    THEIR_ROCK = "A"
    THEIR_PAPER = "B"
    THEIR_SCISSORS = "C"
    YOUR_ROCK = "X"
    YOUR_PAPER = "Y"
    YOUR_SCISSORS = "Z"


def score(instruction: str) -> int:
    their_play, your_play = instruction.split(" ")
    match their_play:
        case Play.THEIR_ROCK:
            match your_play:
                case Play.YOUR_ROCK:
                    return 1 + 3
                case Play.YOUR_PAPER:
                    return 2 + 6
                case Play.YOUR_SCISSORS:
                    return 3 + 0
                case _:
                    raise Exception("Not ok play from you: " + your_play)
        case Play.THEIR_PAPER:
            match your_play:
                case Play.YOUR_ROCK:
                    return 1 + 0
                case Play.YOUR_PAPER:
                    return 2 + 3
                case Play.YOUR_SCISSORS:
                    return 3 + 6
                case _:
                    raise Exception("Not ok play from you: " + your_play)
        case Play.THEIR_SCISSORS:
            match your_play:
                case Play.YOUR_ROCK:
                    return 1 + 6
                case Play.YOUR_PAPER:
                    return 2 + 0
                case Play.YOUR_SCISSORS:
                    return 3 + 3
                case _:
                    raise Exception("Not ok play from you: " + your_play)
        case _:
            raise Exception("Not ok play from them: " + their_play)


def score_after_instructions(raw_instructions: list[str]) -> int:
    return sum([score(instruction) for instruction in raw_instructions])


class Outcome:
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


def score_given_outcome(instruction: str) -> int:
    their_play, desired_outcome = instruction.split(" ")
    match their_play:
        case Play.THEIR_ROCK:
            match desired_outcome:
                case Outcome.LOSE:
                    return 3 + 0
                case Outcome.DRAW:
                    return 1 + 3
                case Outcome.WIN:
                    return 2 + 6
                case _:
                    raise Exception("Not ok play from you: " + desired_outcome)
        case Play.THEIR_PAPER:
            match desired_outcome:
                case Outcome.LOSE:
                    return 1 + 0
                case Outcome.DRAW:
                    return 2 + 3
                case Outcome.WIN:
                    return 3 + 6
                case _:
                    raise Exception("Not ok play from you: " + desired_outcome)
        case Play.THEIR_SCISSORS:
            match desired_outcome:
                case Outcome.LOSE:
                    return 2 + 0
                case Outcome.DRAW:
                    return 3 + 3
                case Outcome.WIN:
                    return 1 + 6
                case _:
                    raise Exception("Not ok play from you: " + desired_outcome)
        case _:
            raise Exception("Not ok play from them: " + their_play)


def score_after_instructions_with_outcomes(raw_instructions: list[str]) -> int:
    return sum([score_given_outcome(instruction) for instruction in raw_instructions])
