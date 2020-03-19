#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab8.py

from autograde import *

import time

def grade_lab8():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-args/args.cpp', 'TODO')
    match2 = print_matching_lines('./2-average/average.cpp', 'TODO')
    match3 = print_matching_lines('./3-max/max.cpp', 'TODO')
    match4 = print_matching_lines('./4-phone/phone.cpp', 'TODO')
    if not (match1 or match2 or match3 or match4):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-args', 'args.cpp')
    compiles_cleanly_in_subdir('2-average', 'average.cpp')
    compiles_cleanly_in_subdir('3-max', 'max.cpp')
    compiles_cleanly_in_subdir('4-phone', 'phone.cpp')

    print('---- 1-args test cases ---')
    commandline_test_case_in_subdir('1-args', 'args.cpp', ['cat', 'dog'])
    commandline_test_case_in_subdir('1-args', 'args.cpp', ['a', 'b', 'c'])
    commandline_test_case_in_subdir('1-args', 'args.cpp', [])

    print('---- args.cpp contents (look for range-based for, and no other kinds of loop) ----')
    print_file('./1-args/args.cpp')

    print('---- 2-average test cases ---')
    commandline_test_case_in_subdir('2-average', 'average.cpp', [])
    commandline_test_case_in_subdir('2-average', 'average.cpp', ['5', '7'])
    commandline_test_case_in_subdir('2-average', 'average.cpp', ['101', '13', '19'])
    commandline_test_case_in_subdir('2-average', 'average.cpp', ['0'])

    print('---- average.cpp contents (look for range-based for, and no other kinds of loop) ----')
    print_file('./2-average/average.cpp')

    print('---- 3-max test cases ---')
    commandline_test_case_in_subdir('3-max', 'max.cpp', [])
    commandline_test_case_in_subdir('3-max', 'max.cpp', ['1', '2', '3'])
    commandline_test_case_in_subdir('3-max', 'max.cpp', ['3', '2', '1'])
    commandline_test_case_in_subdir('3-max', 'max.cpp', ['0'])

    print('---- max.cpp contents (look for range-based for, and no other kinds of loop) ----')
    print_file('./3-max/max.cpp')

    print('---- 4-phone test cases ---')
    commandline_test_case_in_subdir('4-phone', 'phone.cpp', [])
    commandline_test_case_in_subdir('4-phone', 'phone.cpp', ['123'])
    commandline_test_case_in_subdir('4-phone', 'phone.cpp', ['12345678'])
    commandline_test_case_in_subdir('4-phone', 'phone.cpp', ['123-4567'])
    commandline_test_case_in_subdir('4-phone', 'phone.cpp', ['(765) 4321'])

    print('---- phone.cpp contents (look for range-based for, and no other kinds of loop) ----')
    print_file('./4-phone/phone.cpp')

in_each_repo(grade_lab8)
