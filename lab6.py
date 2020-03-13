#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab4.py

from autograde import *

import time

def grade_lab6():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-sphere/sphere.cpp', 'TODO')
    match2 = print_matching_lines('./2-duration/duration.cpp', 'TODO')
    match3 = print_matching_lines('./3-interest/interest.cpp', 'TODO')
    match4 = print_matching_lines('./4-stocks/stocks.cpp', 'TODO')
    if not (match1 or match2 or match3 or match4):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-sphere', 'sphere.cpp')
    compiles_cleanly_in_subdir('2-duration', 'duration.cpp')
    compiles_cleanly_in_subdir('3-interest', 'interest.cpp')
    compiles_cleanly_in_subdir('4-stocks', 'stocks.cpp')

    print('---- 1-sphere test cases ---')
    commandline_test_case_in_subdir('1-sphere', 'sphere.cpp', ['3'])
    commandline_test_case_in_subdir('1-sphere', 'sphere.cpp', ['4'])
    commandline_test_case_in_subdir('1-sphere', 'sphere.cpp', ['5'])

    print('---- 2-duration test cases ---')
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['1000'])
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['7565'])
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['0'])

    print('---- 3-interest test cases ---')
    commandline_test_case_in_subdir('3-interest', 'interest.cpp', [],
                                    stdin_string='1000\n0\n0\n')
    commandline_test_case_in_subdir('3-interest', 'interest.cpp', [],
                                    stdin_string='300\n200\n100\n')

    print('---- 4-dash test cases ---')
    def stocks_trial(deposit):
        commandline_test_case_in_subdir('4-stocks', 'stocks.cpp', [], stdin_string=str(deposit) + '\n')
    repeat_with_delay(lambda: stocks_trial(1000), 3)
    stocks_trial(0)

in_each_repo(grade_lab6)
