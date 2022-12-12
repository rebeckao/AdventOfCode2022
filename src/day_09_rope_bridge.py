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
