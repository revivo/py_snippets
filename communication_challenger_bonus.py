# -*- coding: utf-8 -*-
__author__ = 'deezzy'

"""
Bonus question:
===============

Extend the protocol to accept an arbitrary number of valid messages.
If a message begins with a number, precisely that number of valid messages must follow. e.g.

3aaa VALID
2aaa INVALID
2ZaMbb VALID
K2aaa VALID
10aaaaaaaaaa VALID

In the case of invalid messages, output more descriptive errors.
For valid messages, output a parse tree.

How to run?
===========

python communication_challenger_bonus.py <message_expr> 
e.g. python communication_challenger_bonus.py '3aaa 2aaa 2ZaMbb K2aaa 10aaaaaaaaaa'

"""

import sys

# list that holds the parse tree for a given message, essentially a sequence of tuples.
# Stores two types of tuples: (parse_level, number_of_items_at_level) and (parse_level, parsed_character)
parse_tree = []


def parse(message, parse_level):
    """
        Returns '' if the word is valid. If invalid non-empty string is returned.
    """
    for char in message:
        if char == '':
            return ''
        if char in 'abcdefghij':
            parse_tree.append((parse_level, char))
            return message[1:]
        elif char == 'Z':
            parse_tree.append((parse_level, char))
            return parse(message[1:], parse_level+1)
        elif char in 'MKPQ':
            parse_tree.append((parse_level, char))
            sub_message = parse(message[1:], parse_level+1)
            return parse(sub_message, parse_level+1)
        elif char in str(range(9)):
            # extract digits from message string and compute the number
            num = 0
            while message[0] in str(range(9)):
                num *= 10
                num += int(message[0])
                message = message[1:]
            parse_tree.append((parse_level, num))
            # run parse on extracted message string for num times
            for x in xrange(num):
                message = parse(message, parse_level+1)
            return message
        else:
            return '# %s' % message


def is_valid_message(message):
    """
        Returns 'VALID' or 'INVALID' string
    """
    result = parse(message, 0)
    if not result:
        return 'VALID'
    else:
        if result[0] == '#':
            print "Invalid character(s): %s, in message: %s" % (result[1:], message)
        else:
            print "Extra character(s): %s, in message: %s" % (result, message)
        return 'INVALID'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        expr = sys.argv[1]

    for word in expr.split(' '):
        parse_result = is_valid_message(word)
        if parse_result == 'VALID':
            print '%s %s' % (word, parse_result)
            print "Parse tree: %s" % parse_tree
        else:
            print '%s %s' % (word, parse_result)
        print '\n'
