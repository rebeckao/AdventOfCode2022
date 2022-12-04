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
