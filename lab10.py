#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab10.py

from autograde import *

import time

def grade_lab10():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-drill/drill.cpp', 'TODO')
    match2 = print_matching_lines('./2-pin/pin.cpp', 'TODO')
    match3 = print_matching_lines('./3-inf/inf.cpp', 'TODO')
    match4 = print_matching_lines('./4-stats/stats.cpp', 'TODO')
    if not (match1 or match2 or match3 or match4):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-drill', 'drill.cpp')
    compiles_cleanly_in_subdir('2-pin', 'pin.cpp')
    compiles_cleanly_in_subdir('3-inf', 'inf.cpp')
    compiles_cleanly_in_subdir('4-stats', 'stats.cpp')

    print('---- 1-drill test cases ---')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['9'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['100'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['5', 'a', 'b', 'c'])

    print('---- drill.cpp contents, look for loop syntax ----')
    print_file('./1-drill/drill.cpp')

    print('---- 2-pin test cases ---')
    commandline_test_case_in_subdir('2-pin', 'pin.cpp', [],
                                    stdin_string='1234\n')
    commandline_test_case_in_subdir('2-pin', 'pin.cpp', [],
                                    stdin_string='-1\n')
    commandline_test_case_in_subdir('2-pin', 'pin.cpp', [],
                                    stdin_string='-10\n10000\n1000\n')

    print('---- pin.cpp contents, look for do-while loop ----')
    print_file('./2-pin/pin.cpp')

    print('---- 3-inf test cases ---')
    commandline_test_case_in_subdir('3-inf', 'inf.cpp', ['a'])
    commandline_test_case_in_subdir('3-inf', 'inf.cpp', ['a', 'b', 'c'])

    print('---- 4-stats test cases ---')
    commandline_test_case_in_subdir('4-stats', 'stats.cpp', [])
    commandline_test_case_in_subdir('4-stats', 'stats.cpp', ['1', '2', '-1'])
    commandline_test_case_in_subdir('4-stats', 'stats.cpp', ['6', '5', '7'])
    commandline_test_case_in_subdir('4-stats', 'stats.cpp', ['7', '1', '4'])
    commandline_test_case_in_subdir('4-stats', 'stats.cpp', ['1', '2', '3', '4', '5', '6'])

    print('---- stats.cpp contents, look for C-style for loop ----')
    print_file('./4-stats/stats.cpp')

in_each_repo(grade_lab10)
