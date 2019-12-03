def build_path(wire_path):
    points = [(0, 0)]
    for indication in wire_path:
        start = points[-1]
        x, y = start[0], start[1]
        dir = indication[0]
        steps = int(indication[1:])
        if dir == 'R':
            points += [(x, y + i + 1) for i in range(steps)]
        if dir == 'U':
            points += [(x + i + 1, y) for i in range(steps)]
        if dir == 'L':
            points += [(x, y - i - 1) for i in range(steps)]
        if dir == 'D':
            points += [(x - i - 1, y) for i in range(steps)]
    return points


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        arr = [line.split(',') for line in f.readlines()]
    wire_path_1 = [x.replace('\n', '') for x in arr[0]]
    wire_path_2 = [x.replace('\n', '') for x in arr[1]]

    path_1 = build_path(wire_path_1)
    path_2 = build_path(wire_path_2)

    intersections = list(set(path_1).intersection(path_2))
    intersections.remove((0, 0))
    # Part 1
    print(min([abs(point[0]) + abs(point[1]) for point in intersections]))
    # Part 2
    print(min([path_1.index(point) + path_2.index(point) for point in intersections]))
