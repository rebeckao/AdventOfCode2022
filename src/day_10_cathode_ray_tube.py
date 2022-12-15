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


def visualize_signal(raw_lines: list[str]) -> list[str]:
    output = [""]
    current_output_line = 0
    cycle = 1
    x = 1
    for index, line in enumerate(raw_lines):
        current_cycle = cycle
        start_x = x

        if len(output[current_output_line]) == 40:
            current_output_line += 1
            output.append("")
        current_position_on_line = (current_cycle - current_output_line * 40) - 1
        if abs(start_x - current_position_on_line) < 2:
            output[current_output_line] += "#"
        else:
            output[current_output_line] += "."

        if line == "noop":
            cycle = current_cycle + 1
        else:
            current_cycle += 1
            if len(output[current_output_line]) == 40:
                current_output_line += 1
                output.append("")
            current_position_on_line = (current_cycle - current_output_line * 40) - 1
            if abs(start_x - current_position_on_line) < 2:
                output[current_output_line] += "#"
            else:
                output[current_output_line] += "."

            cycle = current_cycle + 1
            _, value = line.split(" ")
            x = x + int(value)
    for line in output:
        print(line)
    return output
