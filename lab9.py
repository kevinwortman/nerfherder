#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab9.py

from autograde import *

import time

def grade_lab9():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-drill/drill.cpp', 'TODO')
    match2 = print_matching_lines('./2-interval/interval.cpp', 'TODO')
    match3 = print_matching_lines('./3-rectangle/rectangle.cpp', 'TODO')
    match4 = print_matching_lines('./4-search/search.cpp', 'TODO')
    if not (match1 or match2 or match3 or match4):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-drill', 'drill.cpp')
    compiles_cleanly_in_subdir('2-interval', 'interval.cpp')
    compiles_cleanly_in_subdir('3-rectangle', 'rectangle.cpp')
    compiles_cleanly_in_subdir('4-search', 'search.cpp')

    print('---- 1-drill test cases ---')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', [])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1', '2', '3'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1', '2'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['-1', '-2'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['10', '-10'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['5', '20'])

    print('---- 2-average test cases ---')
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', [])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['1', '2'])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['-1'])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['10000'])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['40000'])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['90000'])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['190000'])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['290000'])
    commandline_test_case_in_subdir('2-interval', 'interval.cpp', ['1000000'])

    print('---- 3-rectangle test cases ---')
    commandline_test_case_in_subdir('3-rectangle', 'rectangle.cpp', [],
                                    stdin_string='4\n5\n')
    commandline_test_case_in_subdir('3-rectangle', 'rectangle.cpp', [],
                                    stdin_string='a\n')
    commandline_test_case_in_subdir('3-rectangle', 'rectangle.cpp', [],
                                    stdin_string='4\na\n')

    print('---- rectangle.cpp contents, look for if (!cin) ----')
    print_file('./3-rectangle/rectangle.cpp')

    print('---- 4-search test cases ---')
    commandline_test_case_in_subdir('4-search', 'search.cpp', [])
    commandline_test_case_in_subdir('4-search', 'search.cpp', ['1', '2'])
    commandline_test_case_in_subdir('4-search', 'search.cpp', ['ae86'])
    commandline_test_case_in_subdir('4-search', 'search.cpp', ['e30'])
    commandline_test_case_in_subdir('4-search', 'search.cpp', ['p0420'])
    commandline_test_case_in_subdir('4-search', 'search.cpp', ['yj'])

in_each_repo(grade_lab9)
