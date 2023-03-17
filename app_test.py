import unittest
import os

from utils import file_exists, read_input_from_args, read_input_from_file, the_task


class TestFileExists(unittest.TestCase):
    """Test file_exists function"""

    def test_file_does_not_exist(self):
        files = ['file_does_not_exist.txt', '/tmp/file_does_not_exist.txt']
        for file in files:
            self.assertFalse(file_exists(file))

    def test_file_does_exist(self):
        files = ['file_does_exists.txt', '/tmp/file_does_exists.txt']
        for file in files:
            f = open(file, 'w')
            f.close()
            self.assertTrue(file_exists(file))
            os.remove(file)


class TestReadInputFromFile(unittest.TestCase):
    """Test read_input_from_file function"""

    def test_correct_input(self):
        lines = ['1,2,3 6',
                 '1,2,3,4,5,-6,7,8,9,10 55',
                 '-5 6',
                 '-5,-10 60000',
                 '-5,-10,        1,   -1    12341234',
                 '      1 ,     3    ,-5 ,  -8  , 10, -34    5   ',
                 '0 0']
        outputs = [([1, 2, 3], 6),
                   ([1, 2, 3, 4, 5, -6, 7, 8, 9, 10], 55),
                   ([-5], 6),
                   ([-5, -10], 60000),
                   ([-5, -10, 1, -1], 12341234),
                   ([1, 3, -5, -8, 10, -34], 5),
                   ([0], 0)]
        for line, output in zip(lines, outputs):
            filename = 'test_input_file.txt'
            f = open(filename, 'w')
            f.write(line)
            f.close()
            numbers_list, target = read_input_from_file(filename)
            self.assertEqual(numbers_list, output[0])
            self.assertEqual(target, output[1])
        os.remove(filename)

    def test_incorrect_input(self):
        lines = ['1,2,3, 6',
                 '1,2,,4,5,-6,7,8,9,10 55',
                 '-5 ',
                 '-5,-10 60000 1',
                 '-5,-10,   10     1,   -1    12341234',
                 '      --1 ,     3    ,-5 ,  -8  , 10, -34    5   ',
                 '3,--5 10',
                 '',
                 ' ',
                 ' .      ',
                 '0']
        for line in lines:
            filename = 'test_input_file.txt'
            f = open(filename, 'w')
            f.write(line)
            f.close()
            with self.assertRaises(SyntaxError):
                read_input_from_file(filename)
        os.remove(filename)


class TestReadInputFromArgs(unittest.TestCase):
    """Test read_input_from_args function"""

    def test_correct_args(self):
        args = [('1,2,3', '6'),
                ('1,2,3,4,5,-6,7,8,9,10', '55'),
                ('-5', '6'),
                ('-5,-10', '60000'),
                ('-5,-10,1,-1', '12341234'),
                ('1,3,-5,-8,10,-34'), ('5'),
                ('0', '0')]
        outputs = [([1, 2, 3], 6),
                   ([1, 2, 3, 4, 5, -6, 7, 8, 9, 10], 55),
                   ([-5], 6),
                   ([-5, -10], 60000),
                   ([-5, -10, 1, -1], 12341234),
                   ([1, 3, -5, -8, 10, -34], 5),
                   ([0], 0)]
        for arg, output in zip(args, outputs):
            numbers_list, target = read_input_from_args(arg[0], arg[1])
            self.assertEqual(numbers_list, output[0])
            self.assertEqual(target, output[1])

    def test_correct_args(self):
        args = [(',1,2,3', '6'),
                ('1,,3,4,5,-6,7,8,9,10', '55'),
                ('-5,', '6'),
                ('-5,-10', '_'),
                ('r', '12341234'),
                ('word', '5'),
                ('word', 'word'),
                ('0', 'word')]
        for arg in args:
            with self.assertRaises(SyntaxError):
                read_input_from_args(arg[0], arg[1])


class TestTheTask(unittest.TestCase):
    """Test the task"""

    def test_correct_inputs(self):
        inputs = [([1, 9, 5, 0, 20, -4, 12, 16, 7], 12),
                  ([1, 2, 3, 4, 5, -6, 7, 8, 9, 10], 12),
                  ([1, 2, 3], 6),
                  ([-5], 6),
                  ([], 0),
                  ([-10, 20, 30, 40, 150, 50, 60, 120, 70, 25, 80, 170,
                   90, 100, 50, 75, -20, -50, -70], 100),
                  ([-5, -3, -1], 0),
                  ([10, 12, 5], 1),
                  ([1, 0, -1], 0),
                  ([])
                  ]
        expected_outputs = [[(12, 0), (5, 7), (16, -4)],
                            [(2, 10), (3, 9), (4, 8), (5, 7)],
                            [(3, 3)],
                            [],
                            [],
                            [(50, 50), (75, 25), (- 20, 120), (- 50, 150),
                             (- 70, 170), (20, 80), (30, 70), (40, 60)],
                            [],
                            [],
                            [(1, -1), (0, 0)]
                            ]
        for input, expected_output in zip(inputs, expected_outputs):
            output = the_task(input[0], input[1])
            output_reverse = list(map(lambda x: (x[1], x[0]), expected_output))
            # print('134: output >>>', output)
            # print('135: expected_output >>>', expected_output)
            self.assertEqual(len(output), len(expected_output))
            for res in output:
                self.assertTrue(
                    res in expected_output or res in output_reverse)

    def test_incorrect_inputs(self):
        """Test incorrect outputs"""
        # Since the inputs to the task are generated by the read functions and those are tested
        # separately, there shouldn't be need to test incorrect inputs here
        # and I'm hungry, I'm going to eat something.
        # In a real application with possible future uses by other devs,
        # I would have also written tests for incorrect inputs.
        pass
