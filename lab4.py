#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab4.py

from autograde import *

def grade_lab4():
    # partner names
    print_line_number('./1-drill/drill.cpp', 2)
    print_line_number('./2-age/age.cpp', 2)
    print_line_number('./3-volume/volume.cpp', 2)
    print_line_number('./4-calories/calories.cpp', 2)

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-drill/drill.cpp', 'TODO')
    match2 = print_matching_lines('./2-age/age.cpp', 'TODO')
    match3 = print_matching_lines('./3-volume/volume.cpp', 'TODO')
    match4 = print_matching_lines('./4-calories/calories.cpp', 'TODO')
    if not (match1 or match2 or match3 or match4):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-drill', 'drill.cpp')
    compiles_cleanly_in_subdir('2-age', 'age.cpp')
    compiles_cleanly_in_subdir('3-volume', 'volume.cpp')
    compiles_cleanly_in_subdir('4-calories', 'calories.cpp')

    print('---- 1-drill test cases ---')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', [])

    print('---- 2-age test cases ---')
    commandline_test_case_in_subdir('2-age', 'age.cpp', ['2020', '2001'])
    commandline_test_case_in_subdir('2-age', 'age.cpp', ['2020', '1969'])
    commandline_test_case_in_subdir('2-age', 'age.cpp', ['1977', '1956'])
    commandline_test_case_in_subdir('2-age', 'age.cpp', [])

    print('---- 3-volume test cases ---')
    commandline_test_case_in_subdir('3-volume', 'volume.cpp', ['1'])
    commandline_test_case_in_subdir('3-volume', 'volume.cpp', ['0'])
    commandline_test_case_in_subdir('3-volume', 'volume.cpp', ['355'])
    commandline_test_case_in_subdir('3-volume', 'volume.cpp', [])

    print('---- volume.cpp, (look for constants) ---')
    print_file('./3-volume/volume.cpp')

    print('---- 4-calories test cases ---')
    commandline_test_case_in_subdir('4-calories', 'calories.cpp', ['41', '0', '0'])
    commandline_test_case_in_subdir('4-calories', 'calories.cpp', ['0.6', '5.3', '6.3'])
    commandline_test_case_in_subdir('4-calories', 'calories.cpp', ['0', '0', '0'])
    commandline_test_case_in_subdir('4-calories', 'calories.cpp', [])

    print('---- calories.cpp, (look for constants) ---')
    print_file('./4-calories/calories.cpp')

in_each_repo(grade_lab4)
