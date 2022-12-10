from dataclasses import dataclass
from typing import Any


@dataclass
class Directory:
    parent: Any
    children: dict[str, Any]
    name: str

    def total_size(self) -> int:
        size = 0
        for child in self.children:
            size += self.children[child].total_size()
        return size


@dataclass
class File:
    size: int

    def total_size(self) -> int:
        return self.size


def sum_of_small_directory_sizes(raw_input: list[str]) -> int:
    all_directories = parse_file_system(raw_input)
    sum_of_sizes = 0
    for directory in all_directories:
        size = directory.total_size()
        if size <= 100000:
            sum_of_sizes += size
    return sum_of_sizes


def parse_file_system(raw_input) -> list[Directory]:
    root = Directory(None, dict(), "/")
    all_directories = [root]
    current_directory = root
    for line in raw_input[1:]:
        if line.startswith("$ cd "):
            target = line[5:]
            if target == "..":
                current_directory = current_directory.parent
                continue
            else:
                current_directory = current_directory.children[target]
        elif line == "$ ls":
            continue
        else:
            if line.startswith("dir "):
                dir_name = line[4:]
                new_directory = Directory(current_directory, dict(), dir_name)
                current_directory.children[dir_name] = new_directory
                all_directories.append(new_directory)
            else:
                file_size, name = line.split(" ")
                current_directory.children[name] = File(int(file_size))
    return all_directories
