from typing import Optional, Tuple


def number_of_containing_overlaps(raw_pairs: list[str]) -> int:
    containing_overlaps = 0
    for raw_pair in raw_pairs:
        first, second = raw_pair.split(",")
        first_from, first_to = first.split("-")
        second_from, second_to = second.split("-")
        if int(first_from) >= int(second_from) and int(first_to) <= int(second_to):
            containing_overlaps += 1
        elif int(second_from) >= int(first_from) and int(second_to) <= int(first_to):
            containing_overlaps += 1
    return containing_overlaps


# Copied from day 22 last year
def find_overlap_in_one_dimension(first_from: int, first_to: int, second_from: int, second_to: int) -> Optional[Tuple[int, int]]:
    if second_from <= first_from:
        if second_to < first_from:
            return None
        if second_to <= first_to:
            return first_from, second_to
        return first_from, first_to
    if second_from <= first_to:
        if second_to <= first_to:
            return second_from, second_to
        return second_from, first_to
    return None


def number_of_overlaps(raw_pairs: list[str]) -> int:
    overlaps = 0
    for raw_pair in raw_pairs:
        first, second = raw_pair.split(",")
        first_from, first_to = first.split("-")
        second_from, second_to = second.split("-")
        if find_overlap_in_one_dimension(int(first_from), int(first_to), int(second_from), int(second_to)):
            overlaps += 1
    return overlaps
