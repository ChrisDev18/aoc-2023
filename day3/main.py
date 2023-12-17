
def isSpecial(val: str) -> bool:
    return (not val.isdigit()) and (val != '.')


def loadGrid(location: str) -> list[str]:
    with open(location, "r") as file:
        grid = file.readlines()
        for i, row in enumerate(grid):
            grid[i] = row.replace("\n", "")
    return grid


def circle(span: tuple[int, int],
           y: int,
           bounding: tuple[tuple[int, int], tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Returns the coordinates that surround a given span, restricted to values within a bounding box
    :param bounding: the top-left and bottom-right coordinates of the bounding box
    :param span: inclusive tuple of first and last x coordinates
    :param y: the y value of the span
    """
    (start, end) = span
    ((min_x, min_y), (max_x, max_y)) = bounding

    coordinates = []

    # the bounding box has space to the left of the span
    if start-1 >= min_x:
        coordinates.append((start - 1, y))
        if y-1 >= min_y:
            coordinates.insert(0, (start-1, y-1))
        if y+1 <= max_y:
            coordinates.append((start-1, y + 1))

    # the bounding box has space below the span
    if y+1 <= max_y:
        for x in range(start, end+1):
            coordinates.append((x, y+1))

    # the bounding box has space to the right of the span
    if end+1 <= max_x:
        temp = [(end+1, y)]
        if y+1 <= max_y:
            temp.insert(0, (end+1, y+1))
        if y-1 >= min_y:
            temp.append((end+1, y-1))
        coordinates += temp

    # the bounding box has space above the span
    if y-1 >= min_y:
        for x in range(end, start-1, -1):
            coordinates.append((x, y-1))

    return coordinates


def checkValues(coordinates: list[tuple[int, int]], grid: list[str]) -> bool:
    """
    Checks for any special characters in a grid at the given coordinates
    :param grid: the grid to check through
    :param coordinates: the given coordinates to check
    :returns: True if there are special characters, False if not
    """
    for (x, y) in coordinates:
        if isSpecial(grid[y][x]):
            return True
    return False


def calculateGearRatio(coordinates: list[tuple[int, int]], grid: list[str]):
    """
    Calculates the gear ratio given a set of coordinates.
    :param grid: the grid to check through
    :param coordinates: the given coordinates at which to check for numbers
    :returns: the calculated Gear Ratio, or 0 if coordinates do not circle a valid gear
    """

    # extract the different rows to analyse
    y_values: list[int] = []
    for (_, y) in coordinates:
        if y not in y_values:
            y_values.append(y)

    gearNums: list[int] = []

    # analyse each row
    for y in y_values:
        numbers = locateNumbers(grid[y])  # locate numbers on row
        for (x, _) in filter((lambda c: c[1] == y), coordinates):
            for number in numbers:
                ((start, end), n) = number
                if x in list(range(start, end + 1)):
                    gearNums.append(n)
                    numbers.remove(number)  # remove number so there are no duplicate matches

    if len(gearNums) != 2:
        return 0

    return gearNums[0] * gearNums[1]


def locateNumbers(line: str) -> list[tuple[tuple[int, int], int]]:
    """
    Returns a list of numbers located in a given string
    :param line: The string to search through
    :returns: A list of format [((start_x_val, end_x_val), number)]
    """
    numbers: list[tuple[tuple[int, int], int]] = []
    str_num = ''
    start = 0
    end = len(line)-1

    for i, cell in enumerate(line):
        if cell.isdigit():
            str_num += cell
            # if end of line, then end of word
            if i == end:
                number = ((start, i-1), int(str_num))
                numbers.append(number)

        else:
            # if str_num stores number (i.e. it is the end of a number)
            if str_num != '':
                number = ((start, i-1), int(str_num))
                numbers.append(number)
                str_num = ''
            # increment start to prepare for next character
            start = i+1

    return numbers


def locateAsterisks(line: str) -> list[int]:
    """
    Returns a list of asterisks located in a given string
    :param line: The string to search through
    :returns: A list of each asterisk's position
    """
    asterisks: list[int] = []

    for i, char in enumerate(line):
        if char == '*':
            asterisks.append(i)

    return asterisks


def part1(grid: list[str]):
    total = 0

    for y, row in enumerate(grid):
        numbers = locateNumbers(row)

        for number in numbers:
            (span, n) = number
            bounding = ((0, 0), (len(grid[0]) - 1, len(grid) - 1))
            if checkValues(circle(span, y, bounding), grid):
                total += n

    print("The total is:", total)


def part2(grid: list[str]):
    total = 0

    for y, row in enumerate(grid):
        asterisks = locateAsterisks(row)

        for asterisk in asterisks:
            bounding = ((0, 0), (len(grid[0]) - 1, len(grid) - 1))
            total += calculateGearRatio(circle((asterisk, asterisk), y, bounding), grid)

    print("The total of the gear ratios is:", total)


if __name__ == '__main__':
    grid = loadGrid("schematic.txt")
    part1(grid)
    part2(grid)
