import datetime
import os
import re

import requests

"""
Create folders and download AoC input for all available days not yet done.

TODO:
* Add any error handling
* Check if folder is created but input hasn't been downloaded
* Folder creation -> function?

This is all kinda messy, but as a first pass and first time using requests,
not a terrible showing. Only intended for use by me anyway, so if something
breaks, 🤷🏼‍♂️
"""

v = True

token = os.getenv("AOC_SESSION")

today = min(datetime.datetime.today().day, 25)
month = datetime.datetime.today().month
year = datetime.datetime.today().year

dir_list = sorted(os.listdir(os.path.expanduser(".")))
folders = [f for f in dir_list if re.search(r"day[0-9]{2}", f) and os.path.isdir(f)]

max_date = max([int(folder[-2:]) for folder in folders]) if len(folders) > 0 else 0


def copy_template(day_number, output_path):
    day_number = str(day_number).zfill(2)
    with open("template.py", "r+") as f:
        template = f.readlines()

    template = [line.replace("DAYNUMBER", day_number) for line in template]

    with open(
        os.path.join(output_path, "day" + day_number + ".py"), "w"
    ) as template_file:
        template_file.writelines(template)


def download_input(token, day=None, year=None):
    if day == None:
        day = datetime.datetime.today().day
    if year == None:
        year = datetime.datetime.today().year

    url = "https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input"
    r = requests.get(url, cookies={"session": token})

    if (
        r.content
        == b"Puzzle inputs differ by user.  Please log in to get your puzzle input.\n"
    ):
        print("Token invalid. No input downloaded. Exiting.")
        exit(1)
    elif not r.ok:
        print("An unspecified error occured in requesting data. Exiting.")
        exit(1)
    else:
        return r.content


if today > max_date and month == 12:
    if v:
        if max_date == 0:
            print("No folders exist.")
        else:
            print("Last folder is day{}.".format(str(max_date).zfill(2)))

    new_dates = range(max_date + 1, today + 1)

    for d in new_dates:
        if v:
            print("Preparing day {}.".format(d))

        new_dir = "day" + str(d).zfill(2)
        os.mkdir(new_dir)

        if v:
            print("\tCreated folder {}.".format(new_dir))
            print("\tDownloading input file.")

        with open(os.path.join(new_dir, str(d).zfill(2) + ".txt"), "wb") as input_file:
            input_file.write(download_input(token, d, year))

        if v:
            print("\tCreating template file.")

        copy_template(d, new_dir)

        if v:
            print("Day {} complete.".format(d))
elif month != 12:
    print("It's not December! Advent of Code starts December 1st.")
elif today == max_date:
    print("All folders already created.")
else:
    print("I missed something.")