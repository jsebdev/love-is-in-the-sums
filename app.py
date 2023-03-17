import sys

from utils import file_exists, read_input_from_args, read_input_from_file, the_task

if __name__ == '__main__':
    args = sys.argv

    # if wrong number of arguments
    if len(args) < 2 or len(args) > 3:
        print(
            'Usage: python app.py [<list of comma separated numbers> <target> | <filename>]')
        print("if using a file as input\nthe first line of file should contain a list of\nnumbers separated by comma and a target, separated by a space", end="\n\n")
        exit(1)

    # if the inputs are in a file
    if len(args) == 2:
        filename = args[1]
        if not file_exists(filename):
            print(f'File "{filename}" not found', end="\n\n")
            exit(1)
        try:
            numbers_list, target = read_input_from_file(filename)
        except SyntaxError as e:
            print(e)
            print(
                'Expected format: "<list of comma separated numbers> <target>"', end="\n\n")
            exit(1)

    # if the inputs are in the command line arguments
    if len(args) == 3:
        try:
            numbers_list, target = read_input_from_args(args[1], args[2])
        except SyntaxError as e:
            print(e)
            print(
                'Expected format: "<list of comma separated numbers> <target>"', end="\n\n")
            exit(1)

    # calculate the pairs
    pairs = the_task(numbers_list, target)

    # print the pairs
    for pair in pairs:
        print(f'{pair[0]},{pair[1]}')
