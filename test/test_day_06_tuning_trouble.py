from unittest import TestCase

from src.day_06_tuning_trouble import characters_before_start_marker
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_characters_before_start_of_packet__marker_example(self):
        self.assertEqual(7, characters_before_start_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4))
        self.assertEqual(5, characters_before_start_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4))
        self.assertEqual(6, characters_before_start_marker("nppdvjthqldpwncqszvftbrmjlhg", 4))
        self.assertEqual(10, characters_before_start_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4))
        self.assertEqual(11, characters_before_start_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4))

    def test_characters_before_start_of_packet__marker_actual(self):
        self.assertEqual(1287, characters_before_start_marker(lines_from_file("day06.txt")[0], 4))

    def test_characters_before_start_of_message_marker_example(self):
        self.assertEqual(19, characters_before_start_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14))
        self.assertEqual(23, characters_before_start_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14))
        self.assertEqual(23, characters_before_start_marker("nppdvjthqldpwncqszvftbrmjlhg", 14))
        self.assertEqual(29, characters_before_start_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14))
        self.assertEqual(26, characters_before_start_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14))

    def test_characters_before_start_of_message_marker_actual(self):
        self.assertEqual(3716, characters_before_start_marker(lines_from_file("day06.txt")[0], 14))
