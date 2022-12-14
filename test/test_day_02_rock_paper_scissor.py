from unittest import TestCase

from src.day_02_rock_paper_scissor import score_after_instructions, score_after_instructions_with_outcomes
from src.utils.utils import lines_from_file


class TestRockPaperScissor(TestCase):
    def test_score_after_instructions_example(self):
        input_data = [
            "A Y",
            "B X",
            "C Z"
        ]
        actual = score_after_instructions(input_data)
        self.assertEqual(15, actual)

    def test_score_after_instructions_actual(self):
        input_data = lines_from_file("day02.txt")
        actual = score_after_instructions(input_data)
        self.assertEqual(12740, actual)

    def test_score_after_instructions_with_outcomes_example(self):
        input_data = [
            "A Y",
            "B X",
            "C Z"
        ]
        actual = score_after_instructions_with_outcomes(input_data)
        self.assertEqual(12, actual)

    def test_score_after_instructions_with_outcomes_actual(self):
        input_data = lines_from_file("day02.txt")
        actual = score_after_instructions_with_outcomes(input_data)
        self.assertEqual(11980, actual)
