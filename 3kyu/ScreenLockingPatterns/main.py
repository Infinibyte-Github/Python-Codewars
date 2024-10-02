def count_patterns_from(firstPoint, length):
    point_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9}
    visited = []

    skip_points = [[0] * 10 for _ in range(10)]

    skip_points[1][3] = skip_points[3][1] = 2
    skip_points[4][6] = skip_points[6][4] = 5
    skip_points[7][9] = skip_points[9][7] = 8
    skip_points[1][7] = skip_points[7][1] = 4
    skip_points[2][8] = skip_points[8][2] = 5
    skip_points[3][9] = skip_points[9][3] = 6
    skip_points[1][9] = skip_points[9][1] = 5
    skip_points[3][7] = skip_points[7][3] = 5

    def nextPoint(point, remaining_steps):
        if remaining_steps == 0:
            return 1
        visited.append(point)
        count = 0
        for next_step in range(1, 10):
            if next_step not in visited and (skip_points[point][next_step] == 0 or skip_points[point][next_step] in visited):
                count += nextPoint(next_step, remaining_steps-1)
        visited.pop()
        return count

    if length == 1:
        return 1

    return nextPoint(point_map[firstPoint], length - 1)

print(count_patterns_from("E", 4))