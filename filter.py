import read_write as rw
import javalang

###############################去除代码行小于line_num的代码,注释长度小于com_len的代码
def split_lines_funs(path, suffix, line_num, com_len):
    coms = rw.load_json(path + "com" + suffix)
    funs = rw.load_json(path + "fun" + suffix)

    index = []
    error = []
    less = []
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

            if len(v.split(';')) > line_num :
                index.append(k)
            else:
                less.append(k)
        except:
            error.append(k)

    for k,v in coms.items():
        # 注释中自动生成的函数
        if len(list(javalang.tokenizer.tokenize(v))) > com_len:
            index.append(k)
        else:
            less.append(k)

    index_ = list(set(index))
    less__ = list(set(less))
    
    coms_ = {}
    funs_ = {}
    coms__ = {}
    funs__ = {}
    coms_er = {}
    funs_er = {}

    for k in index_:
        coms_[k] = coms[k]
        funs_[k] = funs[k]
    for k in less__:
        coms__[k] = coms[k]
        funs__[k] = funs[k]
    for k in error:
        coms_er[k] = coms[k]
        funs_er[k] = funs[k]
         

    rw.write_json(path + "com_morethan_.json", coms_)
    rw.write_json(path + "fun_morethan_.json", funs_)

    rw.write_json(path + "com_lessthan_.json", coms__)
    rw.write_json(path + "fun_lessthan_.json", funs__)
    
    rw.write_json(path + "com_error.json", coms_er)
    rw.write_json(path + "fun_error.json", funs_er)



# get set 函数的处理
def get_set(path, funs_name, coms_name):
    funs = load_json(path + funs_name)
    coms = load_json(path + coms_name)

    index = []
    for k,v in func_name.items():
        tmp = v.split('.')[-1]
        if re.match(r'(set\w+\s?)', tmp) or re.match(r'(get\w+\s?)', tmp):
            index.append(k)

    funs_auto = {}
    coms_auto = {}
    for k in index:
        funs_auto[k] = funs[k]
        coms_auto[k] = coms[k]
    write_json(path4 + "funs_auto.json", funs_auto)
    write_json(path4 + "coms_auto.json", coms_auto)

    for k in index:
        del funs[k]
        del coms[k]

    write_json(path + "funs_no_auto.json", funs)
    write_json(path + "coms_no_auto.json", coms)