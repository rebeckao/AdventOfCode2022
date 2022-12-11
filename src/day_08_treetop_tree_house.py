def visible_trees(raw_lines: list[str]) -> int:
    max_y = len(raw_lines)
    max_x = len(raw_lines[0])
    visibilities = [[0 for _ in raw_lines[0]] for _ in raw_lines]
    max_heights_from_top = [-1 for _ in raw_lines[0]]
    for y_index, line in enumerate(raw_lines):
        max_height_from_left = -1
        for x_index, tree in enumerate(line):
            height = int(tree)
            if height > max_height_from_left:
                max_height_from_left = height
                visibilities[y_index][x_index] = 1
            if height > max_heights_from_top[x_index]:
                max_heights_from_top[x_index] = height
                visibilities[y_index][x_index] = 1

    max_heights_from_bottom = [-1 for _ in raw_lines[0]]
    for y_index_reversed, line in enumerate(raw_lines[::-1]):
        max_height_from_right = -1
        for x_index_reversed, tree in enumerate(line[::-1]):
            height = int(tree)
            y_index = max_y - y_index_reversed - 1
            x_index = max_x - x_index_reversed - 1
            if height > max_height_from_right:
                max_height_from_right = height
                visibilities[y_index][x_index] = 1
            if height > max_heights_from_bottom[x_index]:
                max_heights_from_bottom[x_index] = height
                visibilities[y_index][x_index] = 1

    return sum([sum(visible_tree) for visible_tree in visibilities])


def highest_scenic_score(raw_lines: list[str]) -> int:
    max_y = len(raw_lines)
    max_x = len(raw_lines[0])
    max_scenic_score = 0
    for y in range(0, max_y):
        for x in range(0, max_x):
            current_height = int(raw_lines[y][x])
            seen_left, seen_right, seen_above, seen_below = 0, 0, 0, 0
            for left_x in reversed(range(0, x)):
                seen_left += 1
                if int(raw_lines[y][left_x]) >= current_height:
                    break
            for right_x in range(x + 1, max_x):
                seen_right += 1
                if int(raw_lines[y][right_x]) >= current_height:
                    break
            for above_y in reversed(range(0, y)):
                seen_above += 1
                if int(raw_lines[above_y][x]) >= current_height:
                    break
            for below_y in range(y + 1, max_y):
                seen_below += 1
                if int(raw_lines[below_y][x]) >= current_height:
                    break
            scenic_score = seen_left * seen_right * seen_above * seen_below
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score
