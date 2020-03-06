#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab4.py

from autograde import *

import time

DIE_TRIALS = 5

def grade_lab5():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-drill/drill.cpp', 'TODO')
    match2 = print_matching_lines('./2-d20/d20.cpp', 'TODO')
    match3 = print_matching_lines('./3-die/die.cpp', 'TODO')
    match4 = print_matching_lines('./4-dash/dash.cpp', 'TODO')
    if not (match1 or match2 or match3 or match4):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-drill', 'drill.cpp')
    compiles_cleanly_in_subdir('2-d20', 'd20.cpp')
    compiles_cleanly_in_subdir('3-die', 'die.cpp')
    compiles_cleanly_in_subdir('4-dash', 'dash.cpp')

    print('---- 1-drill test cases ---')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', [],
                                    stdin_string='1\n2.3\negg\n')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', [],
                                    stdin_string='x\n')

    print('---- 2-d20 test cases ---')
    repeat_with_delay(lambda: commandline_test_case_in_subdir('2-d20', 'd20.cpp', []),
                      DIE_TRIALS)

    print('---- 3-die test cases ---')
    def die_trial(sides):
        commandline_test_case_in_subdir('3-die', 'die.cpp', [str(sides)])
    repeat_with_delay(lambda: die_trial(4), DIE_TRIALS)
    repeat_with_delay(lambda: die_trial(100), DIE_TRIALS)
    repeat_with_delay(lambda: die_trial(1), DIE_TRIALS)

    print('---- 4-dash test cases ---')
    repeat_with_delay(lambda: commandline_test_case_in_subdir('4-dash', 'dash.cpp', ['A', 'B', 'C']),
                      DIE_TRIALS)

in_each_repo(grade_lab5)
