def sum_of_signal_strengths(raw_lines: list[str]) -> int:
    cycle = 1
    signal_strength_sum = 0
    cycle_to_check = 20
    x = 1
    for index, line in enumerate(raw_lines):
        start_cycle = cycle
        start_x = x
        if line == "noop":
            cycle = start_cycle + 1
        else:
            cycle = start_cycle + 2
            _, value = line.split(" ")
            x = x + int(value)
        if int(start_cycle) <= int(cycle_to_check) < int(cycle):
            signal_strength_sum += start_x * cycle_to_check
            cycle_to_check += 40
    return signal_strength_sum
