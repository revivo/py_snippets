__author__ = 'deezzy'

"""
    This is a practice rewrite of Guido's attempt in sorting 32M int in 2M memory. He uses an external file as 32M
    int storage and tempfiles to store intermediate sorted results finally combining them all.

    One can consider this as a python version of external merge sort.

    The main idea is the use of file.buffer to access the binary stream underlying the text stream file.

    http://neopythonic.blogspot.com/2008/10/sorting-million-32-bit-integers-in-2mb.html
"""

import array, heapq, sys, tempfile

# code won't work for 64 bit systems where "i" typecode does not represent 32 bit integers
assert array.array("i").itemsize == 4


def read_int_chunks_from_file(f):
    """
    This is where the performance tuning of the algorithm takes place: it reads up to 1000 integers at a time,
    and yields them one by one. I had originally written this without buffering -- it would just read 4 bytes from
    the file, convert them to an integer, and yield the result.
    But that ran about 4 times as slow!

    Note that we can't use a.fromfile(f, 1000) because the fromfile() method complains bitterly when there aren't
    enough values in the file, and I want the code to adapt automatically to however many integers are on the file.
    (It turns out we write about 10,000 integers to a typical temp file.)
    """
    while(True):
        a = array.array("i") # create array of 32 bit integers
        a.fromstring(f.read(40000))
        if not a:
            break
        for x in a:
            yield x # NOTE: this returns a generator and not the list, thus extremely memory efficient

# list to hold all iterators we create in the process to use them for merging later on
iters = []

# main reader loop
while(True):
    a = array.array("i")
    a.fromstring(sys.stdin.buffer.read(40000))
    if not a:
        break
    f = tempfile.TemporaryFile()
    array.array("i", sorted(a)).tofile(f)
    f.seek(0)
    iters.append(read_int_chunks_from_file(f))

# finally merge results
a = array.array('i')

for x in heapq.merge(iters):
    a.append(x)
    if len(a) > 1000:
        a.tofile(sys.stdout.buffer)
        del a[:]

if a:
  a.tofile(sys.stdout.buffer)