import matplotlib.pyplot as plt
import read_write as rw
import sys
sys.path.append(r'/home/zdj/work/pyvenn')
import venn


def read_vocab(file):
    data = rw.read_file(file)
    vocab = set()
    for i in data:
        vocab.update(set(i.split('\t')))
    return vocab

lang = "php"  # 修改语言
lowercase = ".lower" # 是否全小写
lowercase = ""
path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
coms = read_vocab(path + "coms_vocab" + lowercase)
coms_split = read_vocab(path + "coms_vocab_split" + lowercase)
funs = read_vocab(path + "funs_vocab" + lowercase)
funs_split = read_vocab(path + "funs_vocab_split" + lowercase)

labels = venn.get_labels([funs, funs_split, coms_split, coms], fill=['number', 'percent'])
fig, ax = venn.venn4(labels, names=['functions vocab', 'functions split vocab', 'comments split vocab', 'comments vocab'])
fig.savefig(lang + lowercase + ".pdf", format="pdf", bbox_inches='tight')