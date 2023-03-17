# Love is in the sums

This program finds the pairs from a list of integers that add up to a target.

## Requirements

- Python >= 3.8

## How to use

You can invoke this program and give the list of integers and the target as the first and second arguments respectively.
Example:

```
$ python app.py 1,0,8,-4,-3 -3
$ -4,1
$ -3,0
```

Or you can input the arguments from a file. Pass the name of the file as the first argument. Make sure that the first line of the file contains both the list of integers separated by commas, and then the target separated by spaces.
Example:

```
$ cat input_file.txt
$ 1,0,8,-4,-3 -3
$ python app.py input_file.txt
$ -4,1
$ -3,0
```

## How to test

To test the program run the following command:

```
$ python -m unittest app_test.py
.......
$ ----------------------------------------------------------------------
$ Ran 7 tests in 0.003s
$
$ OK
```
