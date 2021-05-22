import read_write as rw
import javalang
import re


def filter_funs_coms(funs, coms, line_num, com_len):
    '''
    返回代码和注释长度大于设定值的key
    funs: json类型，函数
    coms: json类型，注释
    line_num: 函数行数阈值
    com_len: 注释长度阈值
    '''
    index = []
    for k,v in funs.items():
        # 代码中语句长度长度大于line_num
        if len(v.split(';')) > (line_num + 1):
            index.append(k)

    for k,v in coms.items():
        # 注释中长度大于com_len
        if len(list(javalang.tokenizer.tokenize(v))) > com_len:
            index.append(k)

    return list(set(index))




# get set 函数的处理
def get_set(funs_name):
    index = []
    for k,v in funs_name.items():
        tmp = v.split('.')[-1]
        if re.match(r'(set\w+\s?)', tmp) or re.match(r'(get\w+\s?)', tmp):
            index.append(k)

    return list(set(index))


def split_dataset(lines, a, b, c):
    '''
    自动划分数据集
    lines: 数据
    a:train
    b:valid
    c:test
    '''
    from sklearn.model_selection import train_test_split    
    train, tmp = train_test_split(lines, test_size=(b+c)/(a+b+c), random_state=42)  
    test, valid = train_test_split(tmp, test_size=b/(b+c), random_state=42)
    
    return train, valid, test


def split_auto_funs(funs, coms):
    '''
    分离get、set、构造函数及自动生成的代码
    '''
    index = []
    error = []
    for k,v in funs.items():
        try:
            tokens = javalang.tokenizer.tokenize(v)
            parser = javalang.parser.Parser(tokens)
            tree = parser.parse_member_declaration()
            if hasattr(tree, 'name'):
                func_name = str(tree.name)
            else:
                error.append(k)
                continue

            # set\get\constructor 函数
            if re.match(r'(set\w+\s?)', func_name) \
                    or re.match(r'(get\w+\s?)', func_name) \
                    or str(type(tree)).split('.')[-1][:-2] == "ConstructorDeclaration":
                index.append(k)
        except:
            error.append(k)

    for k,v in coms.items():
        # 注释中自动生成的函数
        if re.search(r'([A|a]uto[\s+|-|_]?generated)', v):
            index.append(k)

    return list(set(index)), list(set(error))

