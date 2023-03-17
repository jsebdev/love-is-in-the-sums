import re
from pathlib import Path


def file_exists(filename):
    """Check if file exists"""
    filepath = Path(filename)
    return filepath.is_file()


def read_input_from_file(filename):
    """Read the first line of the file and return a tuple of the list of numbers and the target"""
    with open(filename, 'r') as f:
        line = f.readline()
        # using regex just to make the input of the file a little more flexible
        format = re.compile(r"^\s*(-?\d+(\s*,\s*-?\d+)*)\s+(-?\d+)\s*$")
        match = format.match(line)
        if match is None:
            raise SyntaxError(
                f'Invalid input format "{line}" in file {filename}')
        len_groups = len(match.groups())
        numbers_list = match.group(1)
        numbers_list = [int(n) for n in numbers_list.split(',')]
        target = int(match.group(len_groups))
    return (numbers_list, target)


def read_input_from_args(arg_0, arg_1):
    """Read the numbers and target from the command line arguments"""
    try:
        numbers_list = list(map(int, arg_0.split(',')))
    except:
        raise SyntaxError(f'Invalid input format for numbers "{arg_0}"')
    try:
        arg_1 = int(arg_1)
    except:
        raise SyntaxError(f'Invalid input format for target "{arg_1}"')
    return (numbers_list, arg_1)


def the_task(numbers_list, target):
    """The task"""
    pairs = []
    if len(numbers_list) < 2:
        return pairs
    passed_numbers = set()
    for number in numbers_list:
        if number in passed_numbers:
            continue
        passed_numbers.add(number)
        if (lack := target - number) in passed_numbers:
            pairs.append((number, lack))
    return pairs
