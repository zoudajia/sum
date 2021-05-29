import json,json_lines,re

def load_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def write_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
    return

def read_file(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
    return data

def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.writelines(data)
    return 

def write_data_with_index(file_name, data, index):
    with open(file_name, 'w') as f:
        for i in index:
            f.writelines(data[i] + '\n')
            
def write_data_without_index(file_name, data, index):
    tmp = list(set(range(len(data))).difference(set(index)))            
    with open(file_name, 'w') as f:
        for i in tmp:
            f.writelines(data[i] + '\n') 

def filter_code(code):
    '''
    去除代码内部的注释
    '''
    cl_code = ""
    import javalang
    try:
        tokens = javalang.tokenizer.tokenize(code)
        for i in tokens:
            cl_code = cl_code + i.value + " "
    except:
        cl_code = ""
    return cl_code


def json2file(json_name, file_name, type="com"):
    data = load_json(json_name)
    import clean_coms
    import clean_code
    with open(file_name, 'w') as f:
        for k,v in data.items():
            if type == "fun":
                v = clean_code.filter_code(v)
            elif type == "com":
                v = clean_coms.filter_coms(v)
            v = re.sub('\n|\t|\r', ' ', v)
            v = re.sub('\s+', ' ', v)
            f.write(v.strip() + "\n")
    return 


def read_jsonl(path, file_name, code, nl, func_name, project, length):
    with open(path + file_name, 'rb') as f:    
        for i, item in enumerate(json_lines.reader(f)):
            key = str(i + length)
            tmp = item['code_tokens']
            tmp1 = ""
            for c in tmp:
                # python : if not c.startswith('#'): 
                # ruby: if not c.startswith('#') and not c.startswith('=begin'):
                # go javascript java: 
                if not c.startswith('//'):
                # php: if (not c.startswith('//')) and (not c.startswith('#')) and (not c.startswith('\\')):
                    tmp1 = tmp1 + c + " "
            code[key] = tmp1
            nl[key] = item['docstring']
            func_name[key] = item['func_name']
            project[key] = item['repo']
    return code, nl, func_name, project, i + length + 1


def write_set2file(file, data):
    with open(file, 'w+') as f:
        for i in range(len(data)):
            f.write(data[i] + "\t")
            if i % 10 == 0:
                f.write('\n')