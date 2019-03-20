import numpy as np
from itertools import chain
import itertools

coba = itertools.chain(range(10), range(50, 75))
trainacd = range(201, 401)
# for i in range(201, 203):
#     for j in (x for x in range(1, 601) if x not in trainacd):
#         print(i, ", ", j)

for i in range(10, 13):
    for j in range(1, 10):
        print(i, ", ", j)
