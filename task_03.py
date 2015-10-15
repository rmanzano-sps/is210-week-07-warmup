#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""To provide the maximum, minimum, and average length of words in a speech performing
a lexicographical analysis not unlike what's used to measure reading level"""

import decimal;

def lexicographical(to_analyze):
    word_count = []
    text = to_analyze.split('\n')
    
    for line in text:
        words = line.split()
        word_count.append(len(words))
        average = decimal.Decimal(sum(word_count))/len(word_count)
    return max(word_count), min(word_count), average
