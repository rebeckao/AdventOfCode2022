from unittest import TestCase

from src.day_07_no_space_left import sum_of_small_directory_sizes, size_of_directory_to_delete
from src.utils.utils import lines_from_file


class Test(TestCase):
    def test_sum_of_small_directory_sizes_example(self):
        input_data = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
        ]
        actual = sum_of_small_directory_sizes(input_data)
        self.assertEqual(95437, actual)

    def test_sum_of_small_directory_sizes_with_duplicate_names(self):
        input_data = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir d",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd d",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
        ]
        actual = sum_of_small_directory_sizes(input_data)
        self.assertEqual(95437, actual)

    def test_sum_of_small_directory_sizes_actual(self):
        input_data = lines_from_file("day07.txt")
        actual = sum_of_small_directory_sizes(input_data)
        self.assertEqual(1423358, actual)

    def test_size_of_directory_to_delete_example(self):
        input_data = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
        ]
        actual = size_of_directory_to_delete(input_data)
        self.assertEqual(24933642, actual)

    def test_size_of_directory_to_delete_actual(self):
        input_data = lines_from_file("day07.txt")
        actual = size_of_directory_to_delete(input_data)
        self.assertEqual(545729, actual)
