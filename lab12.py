#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab12.py

from autograde import *

import time

def grade_lab12():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-drill/drill.cpp', 'TODO')
    match2 = print_matching_lines('./2-style/style.cpp', 'TODO')
    match3 = print_matching_lines('./3-rps/rps.cpp', 'TODO')
    if not (match1 or match2 or match3):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-drill', 'drill.cpp')
    compiles_cleanly_in_subdir('2-style', 'style.cpp')
    compiles_cleanly_in_subdir('3-rps', 'rps.cpp')

    print('---- 1-drill test cases ---')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['Ok', 'abc7.com'], timeout=2)
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['A', 'HashTag'], timeout=2)
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['xyz', 'xyz'], timeout=2)
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['x', 'www.google123.com'], timeout=2)

    print('---- drill.cpp contents, look for break and continue ----')
    print_file('./1-drill/drill.cpp')

    print('---- style.cpp contents, assess style ----')
    print_file('./2-style/style.cpp')

    print('---- 3-rps test cases ---')
    ones = '1\n' * 100
    commandline_test_case_in_subdir('3-rps', 'rps.cpp', [],
                                    stdin_string='-1\n0\n4\n5\n1\n' + ones,
                                    timeout=2)
    commandline_test_case_in_subdir('3-rps', 'rps.cpp', [],
                                    stdin_string='0\n2\n' + ones,
                                    timeout=2)
    commandline_test_case_in_subdir('3-rps', 'rps.cpp', [],
                                    stdin_string='0\n3\n' + ones,
                                    timeout=2)
    print('---- 3-rps games for other test cases')
    print('Look for:\n' +
          'beats rules, ties, won/lost message, round counter')
    for i in range(1, 4):
        print(' -- 3 games, always choosing ' + str(i) + ' --')
        commandline_test_case_in_subdir('3-rps', 'rps.cpp', [],
                                        stdin_string=(str(i) + '\n') * 100,
                                        timeout=2)

in_each_repo(grade_lab12)
