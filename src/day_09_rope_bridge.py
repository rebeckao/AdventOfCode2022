def positions_tail_visited(raw_lines: list[str]) -> 0:
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
    visited = set()
    visited.add("0_0")
    for line in raw_lines:
        direction, raw_steps = line.split(" ")
        steps = int(raw_steps)
        for _ in range(0, steps):
            # head
            if direction == "R":
                head_x += 1
            elif direction == "L":
                head_x -= 1
            elif direction == "D":
                head_y += 1
            elif direction == "U":
                head_y -= 1
            # tail
            x_diff = head_x - tail_x
            y_diff = head_y - tail_y
            if abs(x_diff) >= 1 and abs(y_diff) >= 1 and (abs(x_diff) > 1 or abs(y_diff) > 1):
                tail_x += int(x_diff / abs(x_diff))
                tail_y += int(y_diff / abs(y_diff))
            else:
                if head_x > tail_x + 1:
                    tail_x += 1
                elif head_x < tail_x - 1:
                    tail_x -= 1
                if head_y > tail_y + 1:
                    tail_y += 1
                elif head_y < tail_y - 1:
                    tail_y -= 1
            visited.add(str(tail_x) + "_" + str(tail_y))
    return len(visited)


def positions_tail_visited_for_longer_rope(raw_lines: list[str]) -> 0:
    knot_xs = [0 for _ in range(0, 10)]
    knot_ys = [0 for _ in range(0, 10)]
    visited = set()
    visited.add("0_0")
    for line in raw_lines:
        direction, raw_steps = line.split(" ")
        steps = int(raw_steps)
        for _ in range(0, steps):
            # head
            if direction == "R":
                knot_xs[0] += 1
            elif direction == "L":
                knot_xs[0] -= 1
            elif direction == "D":
                knot_ys[0] += 1
            elif direction == "U":
                knot_ys[0] -= 1
            # tails
            for knot_index in range(1, 10):
                new_x, new_y = move_knot(knot_xs[knot_index - 1], knot_ys[knot_index - 1], knot_xs[knot_index], knot_ys[knot_index])
                knot_xs[knot_index] = new_x
                knot_ys[knot_index] = new_y
            visited.add(str(knot_xs[9]) + "_" + str(knot_ys[9]))
    return len(visited)


def move_knot(head_x, head_y, tail_x, tail_y) -> (int, int):
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    if abs(x_diff) >= 1 and abs(y_diff) >= 1 and (abs(x_diff) > 1 or abs(y_diff) > 1):
        tail_x += int(x_diff / abs(x_diff))
        tail_y += int(y_diff / abs(y_diff))
    else:
        if head_x > tail_x + 1:
            tail_x += 1
        elif head_x < tail_x - 1:
            tail_x -= 1
        if head_y > tail_y + 1:
            tail_y += 1
        elif head_y < tail_y - 1:
            tail_y -= 1
    return tail_x, tail_y
