import clean_coms
import re
import read_write as rw
import split_strings as ss

path = "/data/zdj/auto/codesearchnet/"


# clean
coms = rw.read_file(path + "coms")
funs = rw.read_file(path + "funs")

assert len(coms) == len(funs)

index_en = ss.filter_en(funs, coms)
index_ast = ss.filter_ast(funs)
index = list(set(index_en) | set(index_ast))

cl_funs = []
for i,v in enumerate(funs):
    if i not in index:
        v = rw.filter_code(v.strip())
        v = re.sub(r'\n|\t|\r', ' ', v)
        v = re.sub(r'\s+', ' ', v)
        cl_funs.append(v.strip() + "\n")
assert (len(index) + len(cl_funs)) == len(funs)

cl_coms = []
for i,v in enumerate(coms):
    if i not in index:
        v = clean_coms.filter_coms(v.strip()) 
        v = re.sub(r'\n|\t|\r', ' ', v)
        v = re.sub(r'\s+', ' ', v)
        cl_coms.append(v.strip() + "\n")


assert (len(index) + len(cl_coms)) == len(coms)
assert len(cl_funs) == len(cl_coms)

index_em = ss.filter_en(cl_funs, cl_coms)
for i in index_em:
    del cl_funs[i]
    del cl_coms[i]

assert (len(index_em) + len(cl_coms) + len(index)) == len(coms)
assert len(cl_funs) == len(cl_coms)

rw.write_file(path + "cl_coms", cl_coms)
rw.write_file(path + "cl_funs", cl_funs)
# split + lower

sp_funs = []
sp_coms = []

for i in cl_funs:
    sp_funs.append(ss.split_strings(i.strip()))
rw.write_file(path + "sp_funs", sp_funs)

for i in cl_coms:
    sp_coms.append(ss.split_strings(i.strip()))
rw.write_file(path + "sp_coms", sp_coms)

lw_funs = []
lw_coms = []
for i in cl_funs:
    lw_funs.append(i.lower())
rw.write_file(path + "lw_funs", lw_funs)

for i in cl_coms:
    lw_coms.append(i.lower())
rw.write_file(path + "lw_coms", lw_coms)