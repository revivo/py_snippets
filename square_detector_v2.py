__author__ = 'deezzy'

import os
import re

# You want to write an image detection system that is able to recognize different geometric shapes.
# In the first version of the system you settled with just being able to detect filled squares on a grid.
#
# You are given a grid of N×N square cells. Each cell is either white or black.
# Your task is to detect whether all the black cells form a square shape.
#
# Input
# The first line of the input consists of a single number T, the number of test cases.
#
# Each test case starts with a line containing a single integer N.
# Each of the subsequent N lines contain N characters.
# Each character is either "." symbolizing a white cell, or "#" symbolizing a black cell.
# Every test case contains at least one black cell.
#
# Output
# For each test case i numbered from 1 to T, output "Case #i: ", followed by YES or NO depending on whether or
# not all the black cells form a completely filled square with edges parallel to the grid of cells.
#
# Constraints
# 1 ≤ T ≤ 20
# 1 ≤ N ≤ 20
#
# Example
# Test cases 1 and 5 represent valid squares.
# Case 2 has an extra cell that is outside of the square.
# Case 3 shows a square not filled inside. And case 4 is a rectangle but not a square.
#
#

f_in = 'square_detector.txt'
f_out = 'square_detector_output.txt'


def process_data():
    results = {}
    data = None
    if os.path.isfile(f_out):
        os.remove(f_out)
    test_case_count = 0
    idx = 0
    arr_dim = 0
    with open(f_in, 'r') as f:
        data = f.readlines()
        test_case_count = int(data[0])
        del data[0]
        for i in xrange(test_case_count):
            if not data:
                results[i+1] = 'Case #%s: %s\n' % (i+1, 'NO')
            else:
                try:
                    arr_dim = int(data[0])
                    del data[0]
                except ValueError as ex:
                    results[i] = 'Case #%s: %s\n' % (i+1, 'NO')
                    idx = 0
                    while not data[idx].strip().isdigit():
                        del data[idx]
                    arr_dim = int(data[0])
                    del data[0]
                finally:
                    if is_square_matrix(arr_dim, data[0:arr_dim]):
                        results[i+1] = 'Case #%s: %s\n' % (i+1, 'YES')
                    else:
                        results[i+1] = 'Case #%s: %s\n' % (i+1, 'NO')
                    del data[0:arr_dim]
    write_file(results)


def is_square_matrix(arr_dim, arr):
    if sum(map(lambda item: item.count('#'), arr)) == 1:
        return True
    row_idx = 0
    while '#' not in arr[row_idx]:
        row_idx += 1
        if row_idx >= arr_dim - 1:
            return False
    all_matches = re.findall("[^#]*(#+)[^#]*", "".join(str(arr[row_idx])))

    if len(all_matches) == 1:
        str_to_check = str(all_matches[0])
        no_of_forward_rows_to_check = len(str_to_check) - 1
        match = re.search(r"(%s)" % str_to_check, arr[row_idx])
        start_pos = match.start(1)
        end_pos = match.end(1)

        for idx in xrange(no_of_forward_rows_to_check):
            row_idx += 1
            if row_idx <= arr_dim - 1:
                match = re.search(r"(%s)" % str_to_check, ''.join(arr[row_idx]))
                if not match:
                    return False
                new_start_pos = match.start(1)
                new_end_pos = match.end(1)
                if new_start_pos != start_pos and new_end_pos != end_pos:
                    return False
            else:
                return False
        if row_idx == arr_dim - 1:
            return True
        row_idx += 1
        while row_idx < arr_dim:
            if '#' in arr[row_idx]:
                return False
            else:
                row_idx += 1
    else:
        return False
    return True


def write_file(data):
    with open(f_out, 'w+') as f:
        for val in data.values():
            f.write(val)

if __name__ == "__main__":
    process_data()