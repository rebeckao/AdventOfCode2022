from unittest import TestCase

from src.day_08_treetop_tree_house import visible_trees
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_visible_trees_example(self):
        input_data = [
            "30373",
            "25512",
            "65332",
            "33549",
            "35390",
        ]
        actual = visible_trees(input_data)
        self.assertEqual(21, actual)

    def test_visible_trees_actual(self):
        input_data = lines_from_file("day08.txt")
        actual = visible_trees(input_data)
        self.assertEqual(1792, actual)
