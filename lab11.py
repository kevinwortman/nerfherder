#
# To run this:
# cd into the directory full of repos
# $ python3 PATH/TO/lab11.py

from autograde import *

import time

def grade_lab11():
    # partner names
    print_file('./CREDITS.txt')

    # TODO comments removed?
    print("Searching for TODO comments:")
    match1 = print_matching_lines('./1-million/million.cpp', 'TODO')
    match2 = print_matching_lines('./2-encrypt/encrypt.cpp', 'TODO')
    match3 = print_matching_lines('./3-decrypt/decrypt.cpp', 'TODO')
    match4 = print_matching_lines('./4-hilo/hilo.cpp', 'TODO')
    if not (match1 or match2 or match3 or match4):
        print('(none found)')

    print('')
    compiles_cleanly_in_subdir('1-million', 'million.cpp')
    compiles_cleanly_in_subdir('2-encrypt', 'encrypt.cpp')
    compiles_cleanly_in_subdir('3-decrypt', 'decrypt.cpp')
    compiles_cleanly_in_subdir('4-hilo', 'hilo.cpp')

    print('---- 1-million test cases ---')
    commandline_test_case_in_subdir('1-million', 'million.cpp', [], timeout=2)
    commandline_test_case_in_subdir('1-million', 'million.cpp', ['1', '2', '2'], timeout=2)
    commandline_test_case_in_subdir('1-million', 'million.cpp', ['-1', '1'], timeout=2)
    commandline_test_case_in_subdir('1-million', 'million.cpp', ['1', '-1'], timeout=2)
    commandline_test_case_in_subdir('1-million', 'million.cpp', ['50000', '9'], timeout=2)
    commandline_test_case_in_subdir('1-million', 'million.cpp', ['5000', '100'], timeout=2)
    commandline_test_case_in_subdir('1-million', 'million.cpp', ['100000', '5'], timeout=2)
    commandline_test_case_in_subdir('1-million', 'million.cpp', ['1000000', '1'], timeout=2)

    print('---- 2-encrypt test cases ---')
    commandline_test_case_in_subdir('2-encrypt', 'encrypt.cpp', [])
    commandline_test_case_in_subdir('2-encrypt', 'encrypt.cpp', ['1', '2', '3'])
    commandline_test_case_in_subdir('2-encrypt', 'encrypt.cpp', ['27', 'hello'])
    commandline_test_case_in_subdir('2-encrypt', 'encrypt.cpp', ['1', '657'])
    commandline_test_case_in_subdir('2-encrypt', 'encrypt.cpp', ['12', 'meetontuesday'])
    commandline_test_case_in_subdir('2-encrypt', 'encrypt.cpp', ['25', 'helloworld'])

    print('---- 3-decrypt test cases ---')
    commandline_test_case_in_subdir('3-decrypt', 'decrypt.cpp', [])
    commandline_test_case_in_subdir('3-decrypt', 'decrypt.cpp', ['1', '2', '3'])
    commandline_test_case_in_subdir('3-decrypt', 'decrypt.cpp', ['27', 'hello'])
    commandline_test_case_in_subdir('3-decrypt', 'decrypt.cpp', ['1', '657'])
    commandline_test_case_in_subdir('3-decrypt', 'decrypt.cpp', ['12', 'yqqfazfgqepmk'])
    commandline_test_case_in_subdir('3-decrypt', 'decrypt.cpp', ['25', 'gdkknvnqkc'])

    print('---- 4-hilo test cases ---')
    commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', ['1', '2'], timeout=2)
    commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', ['30'], timeout=2)
    commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', ['1'],
                                    stdin_string='0\n'*5, timeout=2)
    commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', [],
                                    stdin_string='0\n'*5, timeout=2)
    commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', ['1'],
                                    stdin_string='2\n'*5, timeout=2)
    commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', ['2'],
                                    stdin_string='1\n3\n2\n', timeout=2)
    commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', ['5'],
                                    stdin_string='5\n', timeout=2)
    for i in range(3):
        commandline_test_case_in_subdir('4-hilo', 'hilo.cpp', ['5'],
                                        stdin_string='0\n'*5, timeout=2)

    print('---- hilo.cpp contents, look for constants ----')
    print_file('./4-hilo/hilo.cpp')

in_each_repo(grade_lab11)
