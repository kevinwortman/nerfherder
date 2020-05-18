#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab14.py

from autograde import *

import time

def grade_lab14():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-drill/drill.cpp', 'TODO')
    if not (match1):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-drill', 'drill.cpp')

    print('---- 1-drill test cases ---')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', [])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1', '2'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1', '2', '3'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1', '2', '3', '4'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1', '2', '3', '4', '5'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['1', '2', '3', '4'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['4', '3', '2', '1'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['100', '200'])

    print('---- drill.cpp contents, look for:\n' +
          '  - C-string\n' +
          '  - two switch statements\n' +
          '  - C-style array\n' +
          '                                       ----')
    print_file('./1-drill/drill.cpp')

    print('---- 2-reflect test cases ---')


    print('---- reflected.txt contents, look for question answers ----')
    print_file('./2-reflect/reflect.txt')

in_each_repo(grade_lab14)
