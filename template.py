import timeit
import os


def answer_to_clipboard(answer):
    os.system(f"echo '{answer}' | pbcopy")


start_time = timeit.default_timer()

with open("DAYNUMBER.txt", "r+") as f:
    puzzle_input = [i for i in f.read().splitlines()]


end_time = timeit.default_timer()
print(f"Completed in {round(timeit.default_timer()-start_time, 4)}s.")