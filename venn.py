import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import read_write as rw
import numpy as np


path = "/data/zdj/vocab/codesearchnet/go/"
coms = rw.read_file(path + "coms")
coms_split = rw.read_file(path + "coms.split")
funs = rw.read_file(path + "funs")
funs_split = rw.read_file(path + "funs.split")

coms_vocab = []
for com in coms:
    coms_vocab = coms_vocab + com.split(' ')
coms_vocab = list(set(coms_vocab))

coms_vocab_split = []
for com in coms_split:
    coms_vocab_split = coms_vocab_split + com.split(' ')
coms_vocab_split = list(set(coms_vocab_split))

funs_vocab = []
for fun in funs:
    funs_vocab = funs_vocab + fun.split(' ')
funs_vocab = list(set(funs_vocab))

funs_vocab_split = []
for fun in funs_split:
    funs_vocab_split = funs_vocab_split + fun.split(' ')
funs_vocab_split = list(set(funs_vocab_split))


y1 = np.array(coms_vocab)
y2 = np.array(coms_vocab_split)
y3 = np.array(funs_vocab)
y4 = np.array(funs_vocab_split)

y = np.hstack(y1, y2, y3, y4)

rw.write_file(path + "vocab.matrix", y)