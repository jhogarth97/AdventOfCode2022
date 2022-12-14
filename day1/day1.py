""" 
This module reads a file and figures out what the highest calorie count by any elf is.
This is done as part of the AdventOfCode challenges going on through December 2022.
Take part: https://adventofcode.com/2022
"""

from typing import Optional


def read_list_and_list_of_elves_with_calories(calorie_intake_file: str) -> list:
    """
    This method takes in a string and separates the calorie intake into different elves.
    The list of elves is returned. 
    If there are no calories in the file, an empty list is returned.
    """
    calories_per_elf = calorie_intake_file.split("\n\n")
    elves = []
    for calories in calories_per_elf:
        elves.append([int(x) for x in calories.split("\n")])
    return elves
    
def find_the_most_calories_held_by_elf(elves_with_calories: list, number_of_backup_elves:int = 0) -> Optional[int]:
    """
    This method finds the highest calorie collection within all the elves.
    If there are no elves, the answer given is None.
    """

    if not elves_with_calories:
        return None

    calories_summed_up_per_elf = sorted([sum(x) for x in elves_with_calories], reverse=True)[0:number_of_backup_elves+1]
    
    if number_of_backup_elves == 0:
        return calories_summed_up_per_elf[0]
    
    return calories_summed_up_per_elf
    


if __name__ == "__main__":

    file = open("day1/elf_list.txt", "r", encoding="utf-8").read()
    elves = read_list_and_list_of_elves_with_calories(file)

    # Day 1 part 1
    most_calories = find_the_most_calories_held_by_elf(elves)
    print(most_calories) # 69177

    # Day 1 part 2
    most_calories = find_the_most_calories_held_by_elf(elves, 2)
    print(sum(most_calories)) # 207456

