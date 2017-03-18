#!/usr/bin/env python
import sys, re
words = {}
r=re.compile(r"^..:.. [^\s]*>")
for f in map(lambda s:open(s.rstrip(), 'r', errors='ignore'), open('logs')):
    for line in f:
        if r.match(line):
            for word in map(str.lower, line.split()):
                    words[word] = True
print(len(words))
