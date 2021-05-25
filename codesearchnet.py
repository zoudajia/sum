import read_write as rw
import split_strings as ss
import sys


lang = 'java'
path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
#rw.json2file(path + "funs.json", path + "funs", 'fun')
#rw.json2file(path + "coms.json", path + "coms", 'com')

coms = rw.read_file(path + "coms")
funs = rw.read_file(path + "funs")

if len(coms) != len(funs):
    print(len(coms), len(funs))
    sys.exit()

'''
# 删除非英文注释对和空注释对
index  = ss.filter_en(funs, coms)

coms_e = []
for i,v in enumerate(coms):
    if i not in index:
        coms_e.append(v.strip()+'\n')

rw.write_file(path + "coms", coms_e)
funs_e = []
for i,v in enumerate(funs):
    if i not in index:
        funs_e.append(v.strip()+'\n')
rw.write_file(path + "funs", funs_e)
'''

#切分字符
com_split = []
for com in coms:
    com_split.append(ss.split_strings(com))
rw.write_file(path + "coms.split", com_split)

fun_split = []
for fun in funs:
    fun_split.append(ss.split_strings(fun))
rw.write_file(path + "funs.split", fun_split) 
