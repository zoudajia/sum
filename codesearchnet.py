import javalang

import read_write as rw
import split_strings as ss

'''
path = "/data/zdj/vocab/codesearchnet/java/"
coms = rw.read_file(path + "coms")
funs = rw.read_file(path + "funs")

index  = ss.filter_en(funs, coms)

print(len(index)) # 14814
print(index[:10])
'''

""" 
切分字符
com_split = []
for i,com in enumerate(coms):
    if i not in index:
        com_split.append(ss.split_strings(com))

rw.write_file(path + "coms.split", com_split)

fun_split = []
for i,fun in enumerate(funs):
    if i not in index:
        fun_split.append(ss.split_strings(fun))

rw.write_file(path + "funs.split", fun_split) 
"""

'''
文氏图
'''
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

plt.figure()
venn2(subsets=(113428,46930,34023), set_labels=('代码词库', '注释词库'))
plt.show()
