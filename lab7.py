#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab7.py

from autograde import *

import time

def grade_lab7():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-mult/mult.cpp', 'TODO')
    match2 = print_matching_lines('./2-duration/duration.cpp', 'TODO')
    match3 = print_matching_lines('./3-hilo/hilo.cpp', 'TODO')
    if not (match1 or match2 or match3):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-mult', 'mult.cpp')
    compiles_cleanly_in_subdir('2-duration', 'duration.cpp')
    compiles_cleanly_in_subdir('3-hilo', 'hilo.cpp')

    print('---- 1-mult test cases ---')
    commandline_test_case_in_subdir('1-mult', 'mult.cpp', [],
                                    stdin_string='x\n')
    commandline_test_case_in_subdir('1-mult', 'mult.cpp', [],
                                    stdin_string='1\n')
    commandline_test_case_in_subdir('1-mult', 'mult.cpp', [],
                                    stdin_string='2\n')
    commandline_test_case_in_subdir('1-mult', 'mult.cpp', [],
                                    stdin_string='3\n')
    commandline_test_case_in_subdir('1-mult', 'mult.cpp', [],
                                    stdin_string='4\n')
    commandline_test_case_in_subdir('1-mult', 'mult.cpp', [],
                                    stdin_string='9\n')

    print('---- mult.cpp contents (look for if/else chain) ----')
    print_file('./1-mult/mult.cpp')

    print('---- 2-duration test cases ---')
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', [])
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['1', '2'])
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['80'])
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['605'])
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['7565'])
    commandline_test_case_in_subdir('2-duration', 'duration.cpp', ['0'])

    print('---- 3-hilo test cases ---')
    repeat_with_delay(lambda: commandline_test_case_in_subdir('3-hilo', 'hilo.cpp', [], stdin_string='3\n3\n'),
                      4)
    commandline_test_case_in_subdir('3-hilo', 'hilo.cpp', ['5'], stdin_string='5\n')
    commandline_test_case_in_subdir('3-hilo', 'hilo.cpp', ['5'], stdin_string='1\n5\n')
    commandline_test_case_in_subdir('3-hilo', 'hilo.cpp', ['1'], stdin_string='5\n1\n')
    commandline_test_case_in_subdir('3-hilo', 'hilo.cpp', ['3'], stdin_string='1\n2\n')
    commandline_test_case_in_subdir('3-hilo', 'hilo.cpp', [], stdin_string='x\n')
    commandline_test_case_in_subdir('3-hilo', 'hilo.cpp', ['5'], stdin_string='1\nx\n')

in_each_repo(grade_lab7)
