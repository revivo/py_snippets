# -*- coding: utf-8 -*-
__author__ = 'deezzy'

"""
Built a new protocol that sends messages with a restricted syntax. Write a function
which determines whether a given message is syntactically valid or not.

Here are the rules:

There are 15 valid characters in the protocol: the lower-case characters 'a' through 'j' and the uppercase characters
'Z', 'M', 'K', 'P', and 'Q'.

Every lower-case character in isolation is a valid message, e.g., 'a' is a valid message.
If σ is a valid message then so is Zσ.
If σ and τ are valid messages then so are Mστ, Kστ, Pστ, and Qστ.

Write a function to check whether messages are valid. The input consists of a series of potential 
messages separated by whitespace and containing only
the 15 characters above.

The output consists of one line per potential messages, followed by VALID if the message is valid and INVALID if it is
invalid.

Example output:
===============

Qa INVALID
Zj VALID
MZca VALID
Khfa INVALID

How to run?
===========

python communication_challenger_1.py <message_expr> e.g. python communication_challenger_1.py 'Qa Zj MZca Khfa'

"""

import sys


def parse(message):
    """
        Returns '' if the word is valid. If invalid non-empty string is returned.
    """
    if not message:
        return '#'
    for char in message:
        if char == '':
            return ''
        if char in 'abcdefghij':
            return message[1:]
        elif char == 'Z':
            return parse(message[1:])
        elif char in 'MKPQ':
            sub_message = parse(message[1:])
            return parse(sub_message)
        else:
            return '#'


def is_valid_message(message):
    """
        Returns 'VALID' or 'INVALID'
    """
    return 'VALID' if (parse(message) == '') else 'INVALID'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        expr = sys.argv[1]

    for word in expr.split(' '):
        print '%s %s' % (word, is_valid_message(word))