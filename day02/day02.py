import timeit
import os
from collections import defaultdict
from math import prod


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("02.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]


def part_a(puzzle_input, cube_counts) -> int:
    game_num_sum = 0
    cube_power = 0

    for line in puzzle_input:
        game_num, parts = line.split(":")
        game_num = int(game_num.split()[-1])
        grabs = [
            [int(x) if idx % 2 == 0 else x for idx, x in enumerate(grab.split())]
            for grab in parts.strip().replace(",", "").split(";")
        ]

        valid_grabs = True
        max_cube_counts = defaultdict(int)
        for grab in grabs:
            grab_counts = defaultdict(int)
            for set in [grab[i : i + 2] for i in range(0, len(grab), 2)]:
                grab_counts[set[1]] += set[0]

            for color in grab_counts:
                if grab_counts[color] > max_cube_counts[color]:
                    max_cube_counts[color] = grab_counts[color]

            if not all(grab_counts[k] <= cube_counts[k] for k in grab_counts.keys()):
                valid_grabs = False

        cube_power += prod(max_cube_counts.values())

        if valid_grabs:
            game_num_sum += game_num

    return game_num_sum, cube_power


def part_b(puzzle_input, cube_counts) -> int:
    return 0


#
# puzzle_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

cube_counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

part_a_answer, part_b_answer = part_a(puzzle_input, cube_counts)
print(f"Part a: {part_a_answer}")
answer_to_clipboard(part_a_answer)

# part_b_answer = part_b(puzzle_input)
print(f"Part b: {part_b_answer}")
answer_to_clipboard(part_b_answer)


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")
