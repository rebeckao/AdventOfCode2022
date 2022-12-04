from unittest import TestCase

from src.day_04_camp_cleanup import number_of_containing_overlaps
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_number_of_containing_overlaps_example(self):
        input_data = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
        ]
        actual = number_of_containing_overlaps(input_data)
        self.assertEqual(2, actual)

    def test_number_of_containing_overlaps_actual(self):
        input_data = lines_from_file("day04.txt")
        actual = number_of_containing_overlaps(input_data)
        self.assertEqual(490, actual)
