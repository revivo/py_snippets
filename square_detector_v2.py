import os
import re

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