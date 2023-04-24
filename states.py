#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
filename=sys.argv[1]
data=np.loadtxt(filename, delimiter=',', dtype=str)
print('There are ',len(data),' lines in input file')
for x in data:
  for y in data:
    if (x!=y):
      for z in data:
        if (x!=y):
          if (x!=z):
            if (y!=z):
              word=y.lower()+z.lower()
              #result of the find must be less than length of y to ensure target string is found across both sources
              #sum of the result of the find and the length of y must also exceed the length of y to ensure target string is found across both sources
              if 1 <= word.find(x.lower()) <= len(y) and word.find(x.lower())+len(x) > len(y):
                print('Concatenation of ',y.lower(),' and ',z.lower(), 'finds ',x.lower(),' at position ',word.find(x.lower()))
