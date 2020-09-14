"""
Program: average_scores.py
Author: Cara Krug
Last date modified: 09/13/2020

Write the tests and program average_scores.py to read in one person's names, first and last, their age and three scores out of 100.
Take the three scores and find the average, storing into a variable.
"""
def average():
    score1 = input("Enter score #1: ")
    score2 = input("Enter score #2: ")
    score3 = input("Enter score #3: ")
    return float(score1) + float(score2) + float(score3) / 3


def main():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    average_score = average()
    print("%s, %s age: %d average grade: %.2f" % (last_name, first_name, age, average_score))


if __name__ == '__main__':
    main()
