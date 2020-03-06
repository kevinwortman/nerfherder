
import os, pathlib, subprocess, time

CURRENT_DIRECTORY = 0

def in_each_repo(function, root_path = CURRENT_DIRECTORY):
    if root_path == CURRENT_DIRECTORY:
        root_path = pathlib.PosixPath()
    for child in root_path.iterdir():
        # skip __pycache__
        if child.is_dir() and child != '__pycache__':
            in_subdir(lambda path: assess_one_repo(function), child)
    print_banner()

def in_subdir(function, child_name):
    current_dir = current_path()
    subdir = current_dir / child_name
    os.chdir(subdir)
    result = function(subdir)
    os.chdir(current_dir)
    return result

def assess_one_repo(function):
    print_banner()
    parent = current_path()
    repo_dir_name = parent.parts[-1]
    print(str(repo_dir_name))
    return function()

def current_path():
    return pathlib.PosixPath(os.getcwd())

def print_banner():
    print('=' * 79)

def print_repo_name(path):
    print(path.parts[-1])

# return True on success, False on failure
def print_line_number(path, line_number_from_1):
    ok = True
    print(' line ' + str(line_number_from_1) + ' of ' + str(path) + ':')
    try:
        with open(path) as f:
            lines = f.readlines()
            index = line_number_from_1 - 1
            if (index < 0) or (index >= len(lines)):
                print('(that line does not exist)')
                ok = False
            else:
                print(lines[index])
    except OSError:
        print('(file does not exist)')
        ok = False
    return ok

# return True if there was at least one match, False otherwise
def print_matching_lines(path, substring):
    found_match = False
    try:
        with open(path) as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if substring in line:
                    print('line ' + str(i+1) + ' of ' + str(path) + ': ' + line)
                    found_match = True
    except OSError:
        print('(' + str(path) + ' does not exist)')
    return found_match

def print_file(path):
    try:
        with open(path) as f:
            print(f.read())
    except OSError:
        print('(' + str(path) + ' does not exist)')

def compiles_cleanly_in_subdir(subdir, source_filename):
    in_subdir(lambda path: compiles_cleanly(source_filename), subdir)

def compiles_cleanly(source_filename):
    result = True
    print(str(source_filename) + ' compiles cleanly:', end='')
    messages = command(['g++', source_filename])
    if not messages:
        print('YES')
    else:
        print('NO, messages:')
        for line in messages.splitlines()[:COMPILE_MESSAGE_LINE_LIMIT]:
            print(line)
        result = False
    print('')
    return result

# return a tuple (output, exit_code)
def output_and_exit_code(args, stdin_string=None):
    proc = subprocess.run(args,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT,
                          text=True,
                          input=stdin_string)
    return (proc.stdout, proc.returncode)

# If the command succeeds (exit code 0), return None.
# Otherwise return a string with stdout and stderr, probably containing error messages.
def command(args):
    messages, exit_code = output_and_exit_code(args)
    if exit_code == 0:
        return None
    else:
        return messages

def print_output_and_exit_code_in_subdir(subdir, source_filename):
    print('running ' + source_filename + '...')

    def subdir_stuff(path):
        print('  ', end='')
        if compiles_cleanly(source_filename):
            output, exit_code = output_and_exit_code(['./a.out'])
            print('  EXIT CODE = ' + str(exit_code), 'OUTPUT ON NEXT LINE:')
            print(output + '(end of output)\n')

    in_subdir(subdir_stuff, subdir)

def commandline_test_case_in_subdir(subdir, source_filename, arguments, stdin_string=None):
    print('running ' + source_filename + '...')

    def subdir_stuff(path):
        print('  ', end='')
        if compiles_cleanly(source_filename):
            command = ['./a.out'] + arguments
            print('$ ./a.out ' + ' '.join(arguments))
            output, exit_code = output_and_exit_code(command, stdin_string)
            print('-OUTPUT BEGINS-')
            print(output)
            print('-OUTPUT ENDS-')

    in_subdir(subdir_stuff, subdir)

def git_log():
    output, exit_code = output_and_exit_code(['git', 'log'])
    print('git log:\n' + output)

# default seconds is slightly larger than 1 so that C++ srand(time(0)) will
# have a different seed.
def repeat_with_delay(function, count, seconds=1.01):
    for i in range(count):
        if i > 0:
            time.sleep(seconds)
        function()
