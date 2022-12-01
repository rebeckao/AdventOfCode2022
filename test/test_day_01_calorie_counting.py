from unittest import TestCase

from src.day_01_calorie_counting import most_calories_of_single_elf, most_calories_of_top_three_elves
from src.utils.utils import lines_from_file


class TestDay01(TestCase):
    def test_most_calories_of_single_elf_example(self):
        input_data = [
            "1000",
            "2000",
            "3000",
            "",
            "4000",
            "",
            "5000",
            "6000",
            "",
            "7000",
            "8000",
            "9000",
            "",
            "10000"
        ]
        actual = most_calories_of_single_elf(input_data)
        self.assertEqual(24000, actual)

    def test_most_calories_of_single_elf_actual(self):
        input_data = lines_from_file("day01.txt")
        actual = most_calories_of_single_elf(input_data)
        self.assertEqual(72017, actual)

    def test_most_calories_of_top_three_elves_example(self):
        input_data = [
            "1000",
            "2000",
            "3000",
            "",
            "4000",
            "",
            "5000",
            "6000",
            "",
            "7000",
            "8000",
            "9000",
            "",
            "10000"
        ]
        actual = most_calories_of_top_three_elves(input_data)
        self.assertEqual(45000, actual)

    def test_most_calories_of_top_three_elves_actual(self):
        input_data = lines_from_file("day01.txt")
        actual = most_calories_of_top_three_elves(input_data)
        self.assertEqual(212520, actual)
