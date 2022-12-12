from unittest import TestCase

from src.day_09_rope_bridge import positions_tail_visited
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_positions_tail_visited_example(self):
        input_data = [
            "R 4",
            "U 4",
            "L 3",
            "D 1",
            "R 4",
            "D 1",
            "L 5",
            "R 2",
        ]
        actual = positions_tail_visited(input_data)
        self.assertEqual(13, actual)

    def test_positions_tail_visited_actual(self):
        input_data = lines_from_file("day09.txt")
        actual = positions_tail_visited(input_data)
        self.assertEqual(6057, actual)
