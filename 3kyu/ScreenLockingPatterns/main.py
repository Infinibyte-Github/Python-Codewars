def count_patterns_from(firstPoint, length):
    lockScreen = [[1,2,3],[4,5,6],[7,8,9]]
    point_map = {
        'A': (0, 0), 'B': (0, 1), 'C': (0, 2),
        'D': (1, 0), 'E': (1, 1), 'F': (1, 2),
        'G': (2, 0), 'H': (2, 1), 'I': (2, 2)
    }
    visited = []

    def nextPoint(point_x, point_y, remaining_steps):
        if remaining_steps == 0:
            return 1
        count = 0
        visited.append(lockScreen[point_x][point_y])
        try:
            # Top-left diagonal movement
            if lockScreen[point_x - 1][point_y - 1] and lockScreen[point_x - 1][point_y - 1] not in visited:
                count += nextPoint(point_x - 1, point_y - 1, remaining_steps - 1)

            # Left movement
            if lockScreen[point_x][point_y - 1] and lockScreen[point_x][point_y - 1] not in visited:
                count += nextPoint(point_x, point_y - 1, remaining_steps - 1)

            # Top movement
            if lockScreen[point_x - 1][point_y] and lockScreen[point_x - 1][point_y] not in visited:
                count += nextPoint(point_x - 1, point_y, remaining_steps - 1)

            # Skip one vertical up (requires middle point visited)
            if lockScreen[point_x - 2][point_y] and lockScreen[point_x - 1][point_y] in visited:
                count += nextPoint(point_x - 2, point_y, remaining_steps - 1)

            # Top-left skip diagonal (requires middle point visited)
            if lockScreen[point_x - 2][point_y - 2] and lockScreen[point_x - 1][point_y - 1] in visited:
                count += nextPoint(point_x - 2, point_y - 2, remaining_steps - 1)

            # Skip one horizontal left (requires middle point visited)
            if lockScreen[point_x][point_y - 2] and lockScreen[point_x][point_y - 1] in visited:
                count += nextPoint(point_x, point_y - 2, remaining_steps - 1)

            # Top-right diagonal movement
            if lockScreen[point_x - 1][point_y + 1] and lockScreen[point_x - 1][point_y + 1] not in visited:
                count += nextPoint(point_x - 1, point_y + 1, remaining_steps - 1)

            # Right movement
            if lockScreen[point_x][point_y + 1] and lockScreen[point_x][point_y + 1] not in visited:
                count += nextPoint(point_x, point_y + 1, remaining_steps - 1)

            # Skip one horizontal right (requires middle point visited)
            if lockScreen[point_x][point_y + 2] and lockScreen[point_x][point_y + 1] in visited:
                count += nextPoint(point_x, point_y + 2, remaining_steps - 1)

            # Top-right skip diagonal (requires middle point visited)
            if lockScreen[point_x - 2][point_y + 2] and lockScreen[point_x - 1][point_y + 1] in visited:
                count += nextPoint(point_x - 2, point_y + 2, remaining_steps - 1)

            # Bottom-left diagonal movement
            if lockScreen[point_x + 1][point_y - 1] and lockScreen[point_x + 1][point_y - 1] not in visited:
                count += nextPoint(point_x + 1, point_y - 1, remaining_steps - 1)

            # Bottom movement
            if lockScreen[point_x + 1][point_y] and lockScreen[point_x + 1][point_y] not in visited:
                count += nextPoint(point_x + 1, point_y, remaining_steps - 1)

            # Skip one vertical down (requires middle point visited)
            if lockScreen[point_x + 2][point_y] and lockScreen[point_x + 1][point_y] in visited:
                count += nextPoint(point_x + 2, point_y, remaining_steps - 1)

            # Bottom-left skip diagonal (requires middle point visited)
            if lockScreen[point_x + 2][point_y - 2] and lockScreen[point_x + 1][point_y - 1] in visited:
                count += nextPoint(point_x + 2, point_y - 2, remaining_steps - 1)

            # Bottom-right diagonal movement
            if lockScreen[point_x + 1][point_y + 1] and lockScreen[point_x + 1][point_y + 1] not in visited:
                count += nextPoint(point_x + 1, point_y + 1, remaining_steps - 1)

            # Skip one diagonal down-right (requires middle point visited)
            if lockScreen[point_x + 2][point_y + 2] and lockScreen[point_x + 1][point_y + 1] in visited:
                count += nextPoint(point_x + 2, point_y + 2, remaining_steps - 1)

            # Adding large diagonal skips like (2, 1) or (1, 2) movements:

            # Skip two steps down-right
            if lockScreen[point_x + 2][point_y + 1] and lockScreen[point_x + 2][point_y + 1] not in visited:
                count += nextPoint(point_x + 2, point_y + 1, remaining_steps - 1)

            # Skip two steps down-left
            if lockScreen[point_x + 2][point_y - 1] and lockScreen[point_x + 2][point_y - 1] not in visited:
                count += nextPoint(point_x + 2, point_y - 1, remaining_steps - 1)

            # Skip two steps up-right
            if lockScreen[point_x - 1][point_y + 2] and lockScreen[point_x - 1][point_y + 2] not in visited:
                count += nextPoint(point_x - 1, point_y + 2, remaining_steps - 1)

            # Skip two steps up-left
            if lockScreen[point_x - 1][point_y - 2] and lockScreen[point_x - 1][point_y - 2] not in visited:
                count += nextPoint(point_x - 1, point_y - 2, remaining_steps - 1)

            # Skip two steps down-left
            if lockScreen[point_x + 1][point_y - 2] and lockScreen[point_x + 1][point_y - 2] not in visited:
                count += nextPoint(point_x + 1, point_y - 2, remaining_steps - 1)

            # Skip two steps down-right
            if lockScreen[point_x + 1][point_y + 2] and lockScreen[point_x + 1][point_y + 2] not in visited:
                count += nextPoint(point_x + 1, point_y + 2, remaining_steps - 1)

            # Skip two steps up-right
            if lockScreen[point_x - 2][point_y + 1] and lockScreen[point_x - 2][point_y + 1] not in visited:
                count += nextPoint(point_x - 2, point_y + 1, remaining_steps - 1)

            # Skip two steps up-left
            if lockScreen[point_x - 2][point_y - 1] and lockScreen[point_x - 2][point_y - 1] not in visited:
                count += nextPoint(point_x - 2, point_y - 1, remaining_steps - 1)

        except:
            pass

        visited.pop()

        return count

    if length == 1:
        return 1
    start_x, start_y = point_map[firstPoint]
    return nextPoint(start_x, start_y, length - 1)



output = count_patterns_from('E', 4)
print(output)