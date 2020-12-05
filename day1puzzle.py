import itertools
puzzle_input_messy = open('day1_puzzle_entry_1.txt', 'r').readlines()
puzzle_input = [int(x.replace("\n",'')) for x in puzzle_input_messy]

for a, b, c in itertools.combinations(puzzle_input, 3):
    if (a+b+c==2020):
        print(a*b*c)
        break