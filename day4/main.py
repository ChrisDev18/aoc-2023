
def loadCards(location: str) -> list[tuple[list[int], list[int]]]:
    with open(location, "r") as file:
        lines = file.readlines()
        cards = []
        for row in lines:

            # split into winning and own numbers
            [_, row] = row.replace("\n", "").split(":")
            [winning_list, own_list] = row.split('|')

            # convert each into a list of numbers
            winning = [int(n) for n in winning_list.split()]
            own = [int(n) for n in own_list.split()]

            # add to the cards list
            cards.append((winning, own))

    return cards


def part1(cards: list[tuple[list[int], list[int]]]):
    total = 0
    for (winning, own) in cards:
        matches = 0

        for number in own:
            if number in winning:
                matches += 1

        if matches == 0:
            total += 0
        else:
            total += 1*(2**(matches-1))

    print("Total points:", total)


def part2(cards: list[tuple[list[int], list[int]]]):
    print("Recursion")
    # iterate through each card
    for card in cards:
        print(card)

    totalCards = 0
    for (i, (winning, own)) in enumerate(cards):

        # total the number of matches
        matches = 0
        for number in own:
            if number in winning:
                matches += 1
        print("nMatches:", matches)

        if matches == 0:  # terminating condition
            totalCards += 1
        else:  # recursive condition

            # if last card, end branch
            if len(cards) == 1:
                totalCards += 1
            # if too many matches, truncate
            elif (i + matches + 1) >= len(cards):
                print(f"getting rest of cards")
                totalCards += 1 + part2(cards[i+1:])
            # otherwise, normal
            else:
                print(f"getting the next {matches} cards")
                totalCards += 1 + part2(cards[i+1:(i + matches + 1)])
    return totalCards


if __name__ == '__main__':
    cards = loadCards("scratchcards.txt")
    part1(cards)
    print(part2(cards))
