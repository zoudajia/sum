import re

def dc(m):
    inner = m.groups()
    return " " + inner[1].strip() + " "

def at_word(m):
    inner = m.groups()
    if inner[1].strip() == "":
        return " "
    if re.search('\.|#', inner[1]):
        tmp = re.split('\.|#', inner[1].strip())
        return " " + tmp[-1].strip() + " "
    return " " + inner[1].strip() + " "

def filter_coms(com):
    #(?P<name>匹配模式)，反向应用时用(?P=name）
    if re.search('\<(?P<type>.*)\>(.*?)\<\/(?P=type)\>', com):
        com = re.sub('\<(?P<type>.*)\>(.*?)\<\/(?P=type)\>', dc, com, flags=re.S)
    if re.search('\{\@(\w+)(.*?)\}', com):
        com = re.sub('\{\@(\w+)(.*?)\}', at_word, com, flags=re.S)
    p = re.sub('\<p\>', '', com)
    p = re.sub(r'(\/|\*|\t|\n)', ' ', p)
    p = re.sub(r'(\s+)', ' ', p)
    return p.strip()


def get_first_line_coms(com):
    '''
    取第一行注释
    com: 字符串形式
    '''
    #v = re.sub('/|\*|\n|\t',' ', com)
    #v = re.sub('(\s+)', ' ', v)
    v = filter_coms(com)
    # 取第一行注释
    if re.search(r'(\.\s+)', v):
        v = v[:re.search(r'(\.\s+)', v).end()]
    return  v.strip() + "\n"


