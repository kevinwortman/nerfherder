#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab3.py

from autograde import *

def grade_lab3():
    # partner names
    print_line_number('./1-variables/variables.cpp', 2)
    print_line_number('./2-arguments/arguments.cpp', 2)
    print_line_number('./3-sandwich/sandwich.cpp', 2)

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-variables/variables.cpp', 'TODO')
    match2 = print_matching_lines('./2-arguments/arguments.cpp', 'TODO')
    match3 = print_matching_lines('./3-sandwich/sandwich.cpp', 'TODO')
    if not (match1 or match2 or match3):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-variables', 'variables.cpp')
    compiles_cleanly_in_subdir('2-arguments', 'arguments.cpp')
    compiles_cleanly_in_subdir('3-sandwich', 'sandwich.cpp')

    print('---- 1-variables test cases ---')
    commandline_test_case_in_subdir('1-variables', 'variables.cpp', [])

    print('---- 2-arguments test cases ---')
    commandline_test_case_in_subdir('2-arguments', 'arguments.cpp', [])
    commandline_test_case_in_subdir('2-arguments', 'arguments.cpp', ['x'])
    commandline_test_case_in_subdir('2-arguments', 'arguments.cpp', ['x', 'y'])
    commandline_test_case_in_subdir('2-arguments', 'arguments.cpp', ['x', 'y', 'z'])
    commandline_test_case_in_subdir('2-arguments', 'arguments.cpp', ['1', '2', '3'])
    commandline_test_case_in_subdir('2-arguments', 'arguments.cpp', ['1', '2', '3', '4'])

    print('---- 3-sandwich test cases ---')
    commandline_test_case_in_subdir('3-sandwich', 'sandwich.cpp', ['tuna', 'wheat', 'lettuce'])
    commandline_test_case_in_subdir('3-sandwich', 'sandwich.cpp', ['tomato', 'rye', 'basil'])

in_each_repo(grade_lab3)
