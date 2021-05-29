import re


def repl(m):
    inner_word = list(m.group(0))
    return " "+ " ".join(inner_word) +" "


def df(m):
    t = m.group()
    tmp = ""
    while re.search('_',t):
        search = re.search('(_)', t)
        tmp = tmp + t[:search.start()]+" _ "
        t = t[search.end(): ]
    t = tmp + t

    tmp = ""
    while re.search(r'(\d+)', t):
        search = re.search('(\d+)', t)
        tmp = tmp + t[:search.start()] + " " + search.group()+" "
        t = t[search.end(): ]
    t = tmp + t

    while re.search(r'([^\s+][A-Z][a-z]+)', t):
        search = re.search(r'([^\s+][A-Z][a-z]+)', t)
        tmp = t[:search.start()+1] + " " + t[search.start()+1:]
        t = tmp
        tmp = ""

    while re.search(r'([a-z][A-Z]+)', t):
        search = re.search(r'([a-z][A-Z]+)', t)
        tmp = t[:search.start()+1] + " " + t[search.start()+1:]
        t = tmp
        tmp = ""
        
    return t


def split_strings(line):
    '''
    切分字符串
    '''
    p = re.sub(r"(\W+)", repl, line)
    p = re.sub(r'(\w+)', df, p)
    p = re.sub(r'(\s+)', ' ', p)
    return p.strip() + '\n'


def filter_en_json(funs, coms):
    '''
    去除空的或者非英文的代码注释对
    '''
    index = []
    pattern = re.compile(u'[^\u0000-\u007E]+', re.UNICODE)
    # 代码
    for k,v in funs.items():
        if re.search(pattern, v) or v == '':
            index.append(k)
    # 注释
    for k,v in coms.items():
        if re.search(pattern, v) or v == '':
            index.append(k)

    # 去重
    return list(set(index))

def filter_en(funs, coms):
    '''
    去除空的或者非英文的代码注释对
    '''
    index = []
    pattern = re.compile(u'[^\u0000-\u007E]+', re.UNICODE)
    # 代码
    for i,v in enumerate(funs):
        if re.search(pattern, v) or v == '\n':
            index.append(i)

    # 注释
    for i,v in enumerate(coms):
        if re.search(pattern, v) or v == '\n':
            index.append(i)

    # 去重
    return list(set(index))    


def filter_ast(funs):
    '''
    去除不能生成ast的语法错误代码
    funs: json格式
    返回key
    '''
    import javalang
    index = []
    #for k,v in funs.items():
    for k,v in enumerate(funs):
        try:
            tokens = javalang.tokenizer.tokenize(v)
            parser = javalang.parser.Parser(tokens)
            tree = parser.parse_member_declaration()
            if not hasattr(tree, 'name'):
                index.append(k)
                continue
        except:
            index.append(k)

    return list(set(index))


def get_identifier(funs):
    '''
    根据ast获取变量
    funs: lines格式
    返回key
    '''
    import javalang
    vocab = set()
    error = []
    for k,v in enumerate(funs):
        try:
            tokens = javalang.tokenizer.tokenize(v)
            for i in tokens:
                if type(i) == javalang.tokenizer.Identifier:
                    vocab.add(i.value)
        except:
            error.append(k)
    return vocab, error