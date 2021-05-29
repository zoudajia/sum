# 清理代码，代码内注释
import javalang
import read_write as rw


def filter_code(code):
    '''
    去除代码内部的注释
    '''
    cl_code = ""
    try:
        tokens = javalang.tokenizer.tokenize(code)
        for i in tokens:
            cl_code = cl_code + i.value + " "
    except:
        cl_code = ""
    return cl_code


def json2file(json_name, file_name):
    import re
    data = rw.load_json(json_name)
    with open(file_name, 'w') as f:
        for k,v in data.items():
            v = filter_code(v)
            v = re.sub('\n|\t|\r', ' ', v)
            f.write(v.strip() + "\n")
    return

