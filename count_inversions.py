__author__ = 'deezzy'


# We will use divide and conquer paradigm from Merge sort. Merge sort naturally uncovers split inversions.
# Broad use is finding similarity in a pair of lists, e.g. list of favorite movies of you and your friend;
# forms the basis of Collaborative filtering.
#
# def count_inversions(A, n):
#     if not A: return 0
#     if len(A) == 1: return 0
#     B, x = sort_and_count_inversions(A[:len(A)/2], len(A)/2)
#   left inversions, B returns the sorted left array along with the count of inversions in variable x
#     C, y = sort_and_count_inversions(A[len(A)/2:], len(A)/2)
#   right inversions, C returns the sorted right array along with the count of inversions in variable y
#     D, z = merge_and_count_split_inversions(B, C, len(A))
#   split inversions count, D gives the sorted version of A
#     return x+y+z
#
# Approach: While doing the merge operation,
# number of split inversions is the sum of count of items in the left array when we copy item from right array.
# e.g. B = [1,3,5] and C = [2,4,6], D = [], the output array
#
# when copying 2 from C to B, we have B=[3,5], C=[2,4,6] and D=[1]. Number of items in B is 2 ==> split inversion count
# when copying 4 from C to B, we have B=[5], C=[4,6] and D=[1,2,3]. Number of items in B is 1 ==> split inversion count
# total = 3 split inversions and this exactly follows what we get from manual calculation = (3,2), (5,2) and
# (5,4) being the split inversions in the given case.
#
# Goal: implement split inversions in O(n) time so that the overall algorithm runs in O(nlogn) time


inversion_count = 0

def count_inversions(A, n):
    if n <= 1:
        return A
    B = count_inversions(A[:n/2], n/2)
    C = count_inversions(A[n/2:], n/2)
    return merge_and_count_split_inversions(B, C)


def merge_and_count_split_inversions(B, C):
    D = []  # output list
    global inversion_count
    i, j = 0, 0
    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            D.append(B[i])
            i += 1
        else:
            # this is when split inversion is getting uncovered.
            D.append(C[j])
            j += 1
            inversion_count += len(B[i:])

    if B:
        D = D + list(B[i:])
    if C:
        D = D + list(C[j:])
    return D


print count_inversions([1,3,5,2,4,6], 6)
print inversion_count
