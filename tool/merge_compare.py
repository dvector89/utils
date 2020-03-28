#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Author: shiliangliang
 Date: 2020.03.26
 Desc: merge compare some candidates form files.
'''

import os, sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', nargs='+', required=True,
                    help="Files to compare")
parser.add_argument('-m', '--mark', nargs='+', required=True,
                    help="mark for files")
parser.add_argument('-o', '--output', required=True,
                    help="Output path")
args = parser.parse_args()

mark_len = max(map(len, args.mark))
args.mark = [x+'_'*(mark_len-len(x)) for x in args.mark]

contents = []
for filename in args.input:
    with open(filename) as f:
        contents.append(f.readlines())
with open(args.output, 'w') as f:
    for j in range(len(contents[0])):
        for i, m in enumerate(args.mark):
            f.write(m+':'+contents[i][j])
        f.write('\n')
