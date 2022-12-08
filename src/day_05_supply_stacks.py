import re
from collections import defaultdict


def crates_on_top(raw_input: list[str], reverse: bool) -> str:
    stacks = defaultdict(list)
    parsing_stacks = True
    for line in raw_input:
        if parsing_stacks:
            if line.startswith(" 1 "):
                continue
            if len(line) <= 2:
                parsing_stacks = False
                continue
            number_of_stacks_in_line = int((len(line) + 1) / 4)
            for i in range(0, number_of_stacks_in_line):
                crate = line[i * 4 + 1].strip()
                if bool(crate):
                    stacks[i + 1].append(crate)
        else:
            raw_number, raw_origin, raw_target = [x for x in re.split(r'[a-z ]', line) if x]
            number_to_move = int(raw_number)
            origin = int(raw_origin)
            target = int(raw_target)
            crates = stacks[origin][0:number_to_move]
            if reverse:
                crates.reverse()
            stacks[origin] = stacks[origin][number_to_move:]
            stacks[target] = crates + stacks[target]
    return "".join([stacks[stack][0] for stack in range(1, len(stacks) + 1)])
