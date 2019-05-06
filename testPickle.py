#
# class SimpleClass(object):
#     number = None,
#     time = None
#
#     def __init__(self, list):
#         self.number = list[0]
#         self.time = list[1]
#
# simplelist = list()
#
# count = [[1,2],
#          [3,4],
#          [5,6],
#          [7,8]]
#
# for i in range(4):
#     x = SimpleClass(count[i])
#     simplelist.append(x)
#
# for i in range(4):
#     print(simplelist[i].number, simplelist[i].time)

import pandas as pd
import numpy as np
from pandas import DataFrame
x = [[0, None, 'chaowang'],
     [1, None, 'xiaomin'],
     [2, '19940202', None]]

df = DataFrame(x)

def trans(x):
    return np.where(x==None, '<null>', x)

print(df.iloc[:,1].map(trans))
print(df.iloc[:,1])