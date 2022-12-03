def sum_of_priorities_of_overlaps(raw_rucksacks: list[str]) -> int:
    priorities = 0
    for rucksack in raw_rucksacks:
        compartment_size = int(len(rucksack) / 2)
        first_compartment = set(rucksack[0:compartment_size])
        second_compartment = set(rucksack[compartment_size:])
        overlapping_item_type = first_compartment.intersection(second_compartment).pop()
        priorities += priority(overlapping_item_type)
    return priorities


def priority(item_type: str):
    if item_type.isupper():
        return 26 + ord(item_type) - 64
    return ord(item_type) - 96
