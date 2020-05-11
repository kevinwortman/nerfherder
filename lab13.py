#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab13.py

from autograde import *

import time

def grade_lab13():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-drill/drill.cpp', 'TODO')
    match2 = print_matching_lines('./2-ttt/ttt.cpp', 'TODO')
    if not (match1 or match2):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-drill', 'drill.cpp')
    compiles_cleanly_in_subdir('2-ttt', 'ttt.cpp')

    print('---- 1-drill test cases ---')
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', [])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['0'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['10', '20', '30'])
    commandline_test_case_in_subdir('1-drill', 'drill.cpp', ['5', '4', '3'])

    print('---- drill.cpp contents, look for:\n' +
          '  - fill constructor\n' +
          '  - list initialization\n' +
          '  - [ ]\n' +
          '  - creating numbers as indicated\n' +
          '                                       ----')
    print_file('./1-drill/drill.cpp')

    print('---- 2-ttt test cases ---')

    def coord(i):
        return str(i) + '\n'

    def coords(i, j):
        return coord(i) + coord(j)

    def moves(*pairs):
        str = ''
        for pair in pairs:
            i, j = pair
            str += coords(i, j)
        return str

    play_every_square = ''
    for i in range(3):
        for j in range(3):
            play_every_square += coords(i, j)

    # 1
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((0,0),(2,2)) + play_every_square,
                                    timeout=1)
    # 2
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=coord(-1)+coord(3)+coord(0)+play_every_square,
                                    timeout=1)
    # 3
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=coord(0)+coord(-1)+coord(3)+coord(0)+play_every_square,
                                    timeout=1)
    # 4
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((0,0),(1,1),(0,0)) + play_every_square,
                                    timeout=1)
    # 5
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((0,0),(0,2),(1,1),(0,2),(1,1)),
                                    timeout=1)
    # 6
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((0,0),(0,2),(0,0),(1,1),(0,0),(2,0)),
                                    timeout=1)
    # 7
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((0,0),(0,0),(0,1),(0,0),(0,2)),
                                    timeout=1)
    # 8
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((0,0),(1,0),(0,0),(1,1),(0,0),(1,2)),
                                    timeout=1)
    # 9
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((1,0),(0,0),(1,1),(0,0),(2,1)),
                                    timeout=1)
    # 10
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((2,2),(0,0),(2,2),(1,0),(2,2),(2,0)),
                                    timeout=1)
    # 11
    commandline_test_case_in_subdir('2-ttt', 'ttt.cpp', [],
                                    stdin_string=moves((0,0),(0,2),(0,1),(1,0),(1,2),(1,1),(2,0),(2,2),(2,1)),
                                    timeout=1)

    print('---- ttt.cpp contents, look for style ----')
    print_file('./2-ttt/ttt.cpp')

in_each_repo(grade_lab13)
