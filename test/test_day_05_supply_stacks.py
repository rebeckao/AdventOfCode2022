from unittest import TestCase

from src.day_05_supply_stacks import crates_on_top
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_crates_on_top_example(self):
        input_data = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
        ]
        actual = crates_on_top(input_data)
        self.assertEqual("CMZ", actual)

    def test_crates_on_top_actual(self):
        input_data = lines_from_file("day05.txt")
        actual = crates_on_top(input_data)
        self.assertEqual("GRTSWNJHH", actual)
