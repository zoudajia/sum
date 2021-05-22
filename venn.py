import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import read_write as rw
import numpy as np


path = "/data/zdj/vocab/codesearchnet/java/"
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

def get_vocab(lines):
    data = {}
    for line in lines:
        data = data.update(line.split(' '))
    return data

funs_vocab = get_vocab(funs)
funs_vocab_split = get_vocab(funs_split)
coms_vocab = get_vocab(coms)
coms_vocab_split = get_vocab(coms_split)


from matplotlib.pyplot import subplots
from itertools import chain, islice
from string import ascii_uppercase
from numpy.random import choice
import venn

_, top_axs = subplots(ncols=3, nrows=1, figsize=(18, 5))
_, bot_axs = subplots(ncols=2, nrows=1, figsize=(18, 8))

dataset_dict = {"source": funs_vocab, "comment": coms_vocab, "source_split": funs_vocab_split, "comment_split": coms_vocab_split}
venn(dataset_dict, fmt="{percentage:.1f}%", cmap="plasma", fontsize=8, legend_loc="upper left", ax=chain(top_axs, bot_axs))

plt.savefig()