def snail(snail_map):
    pattern = []
    while len(snail_map)>1:
        pattern += snail_map[0]
        snail_map.pop(0)
        for i in range(0, len(snail_map)):
            pattern += [snail_map[i][-1]]
            snail_map[i].pop(-1)
        pattern += snail_map[-1][::-1]
        snail_map.pop(-1)
        for i in range(len(snail_map)-1, -1, -1):
            pattern += [snail_map[i][0]]
            snail_map[i].pop(0)

    if snail_map:
        pattern += snail_map[0]
    return pattern
