import timeit
import os


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("01.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def part_a(puzzle_input) -> int:
    sum = 0
    for line in puzzle_input:
        digits = [digit for digit in line if digit.isdigit()]
        sum += int(digits[0]+digits[-1])

    return sum


def part_b(puzzle_input) -> int:
    sum = 0

    for line in puzzle_input:
        digits = []

        while line:
            if line[0].isdigit():
                digits.append(line[0])
            elif any(line.startswith(k) for k in digit_map):
                for k in digit_map:
                    if line.startswith(k):
                        digits.append(digit_map[k])
                        break

            line = line[1:]

        line_value = int(digits[0]+digits[-1])
        sum += line_value

    return sum


part_a_answer = part_a(puzzle_input)
print(f"Part a: {part_a_answer}")
answer_to_clipboard(part_a_answer)

part_b_answer = part_b(puzzle_input)
print(f"Part b: {part_b_answer}")
answer_to_clipboard(part_b_answer)

end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")