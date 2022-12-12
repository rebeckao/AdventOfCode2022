from unittest import TestCase

from src.day_09_rope_bridge import positions_tail_visited, positions_tail_visited_for_longer_rope
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

    def test_positions_tail_visited_for_longer_rope_short_example(self):
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
        actual = positions_tail_visited_for_longer_rope(input_data)
        self.assertEqual(1, actual)

    def test_positions_tail_visited_for_longer_rope_large_example(self):
        input_data = [
            "R 5",
            "U 8",
            "L 8",
            "D 3",
            "R 17",
            "D 10",
            "L 25",
            "U 20",
        ]
        actual = positions_tail_visited_for_longer_rope(input_data)
        self.assertEqual(36, actual)

    def test_positions_tail_visited_for_longer_rope_actual(self):
        input_data = lines_from_file("day09.txt")
        actual = positions_tail_visited_for_longer_rope(input_data)
        self.assertEqual(2514, actual)
