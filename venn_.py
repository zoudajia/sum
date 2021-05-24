import read_write as rw
import sys
sys.path.append(r'/home/zdj/work/pyvenn')
import venn

def get_vocab(lines):
    data = set()
    for line in lines:
        data.update(set(line.split(' ')))
    return data

lang = "java"  # 修改语言
path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
coms = rw.read_file(path + "coms")
coms_split = rw.read_file(path + "coms.split")
funs = rw.read_file(path + "funs")
funs_split = rw.read_file(path + "funs.split")


funs_vocab = get_vocab(funs)
funs_vocab_split = get_vocab(funs_split)
coms_vocab = get_vocab(coms)
coms_vocab_split = get_vocab(coms_split)


labels = venn.get_labels([funs_vocab, funs_vocab_split, coms_vocab_split, coms_vocab], fill=['number', 'percent'])
fig, ax = venn.venn4(labels, names=['functions vocab', 'functions split vocab', 'comments split vocab', 'comments vocab'])
fig.savefig(lang + ".png")