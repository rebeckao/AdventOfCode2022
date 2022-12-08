from unittest import TestCase

from src.day_06_tuning_trouble import characters_before_start_marker
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_characters_before_start_marker_example(self):
        self.assertEqual(7, characters_before_start_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
        self.assertEqual(5, characters_before_start_marker("bvwbjplbgvbhsrlpgdmjqwftvncz"))
        self.assertEqual(6, characters_before_start_marker("nppdvjthqldpwncqszvftbrmjlhg"))
        self.assertEqual(10, characters_before_start_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
        self.assertEqual(11, characters_before_start_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

    def test_characters_before_start_marker_actual(self):
        self.assertEqual(1287, characters_before_start_marker(lines_from_file("day06.txt")[0]))
