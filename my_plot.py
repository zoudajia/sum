
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


def plot_venn(lang, is_lower=True):
    #lang = "php"  # 修改语言
    if is_lower:
        lowercase = ".lower" # 是否全小写
    else:
        lowercase = ""
    path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
    coms = read_vocab(path + "coms_vocab" + lowercase)
    coms_split = read_vocab(path + "coms_vocab_split" + lowercase)
    funs = read_vocab(path + "funs_vocab" + lowercase)
    funs_split = read_vocab(path + "funs_vocab_split" + lowercase)

    labels = venn.get_labels([funs, funs_split, coms_split, coms], fill=['number', 'percent'])
    fig, ax = venn.venn4(labels, names=['functions vocab', 'functions split vocab', 'comments split vocab', 'comments vocab'])
    fig.savefig(lang + lowercase + ".pdf", format="pdf", bbox_inches='tight')
    return


def plot_venn_lower(lang):
    lowercase = ".lower" # 是否全小写
    path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
    coms_lower = read_vocab(path + "coms_vocab_split" + lowercase)
    coms_split = read_vocab(path + "coms_vocab_split")
    funs_lower = read_vocab(path + "funs_vocab_split" + lowercase)
    funs_split = read_vocab(path + "funs_vocab_split")


    labels = venn.get_labels([funs_split, funs_lower, coms_lower, coms_split], fill=['number', 'percent'])
    fig,ax = venn.venn4(labels, names=['function vocabs', 'function vocabs in lowercase', 'comment vocabs in lowercase', 'comment vocabs'])
    plt.savefig(lang + ".venn4.pdf", format="pdf", bbox_inches='tight')
    plt.close()

    labels = venn.get_labels([funs_split, funs_lower], fill=['number', 'percent'])
    fig,ax = venn.venn2(labels, names=['function vocabs', 'function vocabs in lowercase'])
    plt.savefig(lang + ".fun.pdf", format="pdf", bbox_inches='tight')
    plt.close()

    labels = venn.get_labels([coms_split, coms_lower], fill=['number', 'percent'])
    fig,ax = venn.venn2(labels, names=['comment vocabs', 'comment vocabs in lowercase'])
    plt.savefig(lang + ".com.pdf", format="pdf", bbox_inches='tight')
    plt.close()
    #plt.savefig(lang + ".lower.pdf", format="pdf", bbox_inches='tight')
    return


def get_frequence(datas):
    data = []
    for i in datas:
        fre = int(i.split('\t')[-1])
        data.append(fre)
    return data


def plot_two_as_one(lang, x_len=90):
    path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
    coms = rw.read_file(path + "vocab.coms")
    funs = rw.read_file(path + "vocab.funs")
    coms_fre = get_frequence(coms)
    funs_fre = get_frequence(funs)
    tmp = int(x_len / 3)
    import mpl_toolkits.axisartist as axisartist
    from matplotlib.pyplot import MultipleLocator
    #创建画布
    fig = plt.figure(figsize=(12, 4))

    #使用axisartist.Subplot方法创建一个绘图区对象ax
    ax1 = axisartist.Subplot(fig, 121)
    #将绘图区对象添加到画布中
    fig.add_axes(ax1)
    # 隐藏边框
    ax1.axis['top'].set_visible(False)
    ax1.axis['right'].set_visible(False)
    # 设置坐标轴箭头
    ax1.axis["bottom"].set_axisline_style("-|>", size = 1.0)
    ax1.axis["left"].set_axisline_style("->", size = 1.0)
    # ax1.set_title(label='The frequency of function words')
    ax1.set_xlabel(xlabel='Function word occurrences')
    ax1.set_ylabel(ylabel='Frequency')
    # 设置x轴刻度
    x_major_locator=MultipleLocator(3)
    ax1.xaxis.set_major_locator(x_major_locator)

    #ax1.set_ylim(0,0.3)
    ax1.set_xlim(0,x_len,3)
    
    n1, bin1, patches = ax1.hist(funs_fre, tmp, (0, x_len),density=False, color='red', label='functions', alpha=0.5, rwidth = 1)
    ax1.legend(loc='upper right')

    ax2 = axisartist.Subplot(fig, 122)
    #将绘图区对象添加到画布中
    fig.add_axes(ax2)
    # 隐藏边框
    ax2.axis['top'].set_visible(False)
    ax2.axis['right'].set_visible(False)
    # 设置坐标轴箭头
    ax2.axis["bottom"].set_axisline_style("-|>", size = 1.0)
    ax2.axis["left"].set_axisline_style("->", size = 1.0)
    ax2.set_xlabel(xlabel='Comment word occurrences')
    ax2.set_ylabel(ylabel='Frequency')
    # 设置x轴刻度
    ax2.xaxis.set_major_locator(x_major_locator)

    #ax2.set_ylim(0,0.2)
    ax2.set_xlim(0,x_len,2)
    n2, bin2, patches = ax2.hist(coms_fre, tmp, (0, x_len),density=False, color='blue', label='comments', alpha=0.5, rwidth = 1)
    ax2.legend(loc='upper right')

    fig.savefig(lang + ".frequence.pdf", format="pdf", bbox_inches='tight')
    return n1, n2, len(funs_fre), len(coms_fre)


if __name__ == "__main__":
    # execute only if run as a script
    n1, n2, b1, b2 = plot_two_as_one("java")
    print(n1, n2, b1, b2)
    #plot_venn_lower('java')
