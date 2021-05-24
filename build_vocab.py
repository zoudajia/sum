import read_write as rw
import re


def repl(m):
    inner_word = list(m.group(0))
    return " "+ " ".join(inner_word) +" "


def get_vocab(lines, lowercase):
    data = set()
    for line in lines:
        # 是否小写
        if lowercase == ".lower":
            line = line.lower()

        line = re.sub(r"(\W+)", repl, line)
        line = re.sub(r'\s+', " ", line)
        tmp = line.split(' ')
        
        data.update(set(tmp))

    return data

lang = "php"  # 修改语言
lowercase = ".lower"
#lowercase = ""
path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
coms = rw.read_file(path + "coms")
coms_split = rw.read_file(path + "coms.split")
funs = rw.read_file(path + "funs")
funs_split = rw.read_file(path + "funs.split")


funs_vocab = get_vocab(funs, lowercase)
funs_vocab_split = get_vocab(funs_split, lowercase)
coms_vocab = get_vocab(coms, lowercase)
coms_vocab_split = get_vocab(coms_split, lowercase)

def write_set2file(file, data):
    with open(file, 'w+') as f:
        for i in range(len(data)):
            f.write(data[i] + "\t")
            if i % 10 == 0:
                f.write('\n')
            

write_set2file(path + "funs_vocab" + lowercase,list(funs_vocab))
write_set2file(path + "funs_vocab_split"+ lowercase,list(funs_vocab_split))
write_set2file(path + "coms_vocab"+ lowercase,list(coms_vocab))
write_set2file(path + "coms_vocab_split"+ lowercase,list(coms_vocab_split))