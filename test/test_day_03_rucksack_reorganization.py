from unittest import TestCase

from src.day_03_rucksack_reorganization import sum_of_priorities_of_overlaps, sum_of_priorities_for_badges
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_sum_of_priorities_of_overlaps_example(self):
        input_data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
        actual = sum_of_priorities_of_overlaps(input_data)
        self.assertEqual(157, actual)

    def test_sum_of_priorities_of_overlaps_actual(self):
        input_data = lines_from_file("day03.txt")
        actual = sum_of_priorities_of_overlaps(input_data)
        self.assertEqual(7845, actual)

    def test_sum_of_priorities_for_badges_example(self):
        input_data = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
        actual = sum_of_priorities_for_badges(input_data)
        self.assertEqual(70, actual)

    def test_sum_of_priorities_for_badges_actual(self):
        input_data = lines_from_file("day03.txt")
        actual = sum_of_priorities_for_badges(input_data)
        self.assertEqual(2790, actual)
