import re
import read_write as rw


path = "/data/zdj/auto/codesearchnet/"

funs_name_ = rw.load_json(path + "funs_name.json")
index = []
# 匹配get set 函数
for k,v in funs_name_.items():
    name = v.split('.')[-1]
    if re.match(r'(set\w+\s?)', name) or re.match(r'(get\w+\s?)', name):
        index.append(k)

with open(path + "index", 'w') as f:
    for i in index:
        f.write(i + '\t')


coms = []
funs = []

coms_ = rw.load_json(path + "coms.json")
for k,v in coms_.items():
    if k not in index:
        v = re.sub('\n|\t|\r', ' ', v)
        coms.append(v.strip() + "\n")
rw.write_file(path + "coms", coms)

funs_ = rw.load_json(path + "funs.json")
for k,v in funs_.items():
    if k not in index:
        v = re.sub('\n|\t|\r', ' ', v)
        funs.append(v.strip() + "\n")
rw.write_file(path + "funs", funs)