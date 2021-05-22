import read_write as rw

path = "/data/zdj/vocab/codesearchnet/go/"
funs = rw.read_file(path + "vocab.funs")
funs_split = rw.read_file(path + "vocab.funs.split")

fun = []
with open(path + "matrix", 'w+') as f:
    for i in funs:
        f.write(i.split('\t')[0])
