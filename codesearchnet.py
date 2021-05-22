import read_write as rw
import split_strings as ss


def json2file(json_name, file_name):
    import re
    data = rw.load_json(json_name)
    with open(file_name, 'w') as f:
        for k,v in data.items():
            v = re.sub('\n|\t', ' ', v)
            f.write(v.strip() + "\n")
    return

path = "/data/zdj/vocab/codesearchnet/python/"
json2file(path + "funs.json", path + "funs")
json2file(path + "coms.json", path + "coms")

coms = rw.read_file(path + "coms")
funs = rw.read_file(path + "funs")

index  = ss.filter_en(funs, coms)

print(len(index))  # java 14814 # go 3308

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