import math


def maxHeight(wallPositions, wallHeights):

    maximum_height = 0
    # initialize the output to 0

    for i in range(len(wallPositions) - 1):

        # set up the initials
        curr_position = wallPositions[i]
        next_position = wallPositions[i + 1]
        curr_height = wallHeights[i]
        next_height = wallHeights[i + 1]

        interval = next_position - curr_position - 1
        height_diff = abs(next_height - curr_height)

        if interval > height_diff:
            remaining_space = interval - height_diff
            max_height = math.ceil(remaining_space / 2) + max(curr_height, next_height)

            # update the result
            if max_height > maximum_height:
                maximum_height = max_height

        elif interval <= height_diff:
            if interval == 0:
                max_height = 0
            # in this case no mud wall could be built
            # since there's no space between two cement walls
            else:
                max_height = interval + min(curr_height, next_height)

            # update the result
            if max_height > maximum_height:
                maximum_height = max_height

    return maximum_height