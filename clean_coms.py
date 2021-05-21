import re

def dc(m):
    inner = m.groups()
    return inner[1].strip()

def at_code(m):
    inner = m.groups()
    return inner[0].strip()

def at_link(m):
    inner = m.groups()
    if re.search('\.|#', inner[0]):
        tmp = re.split('\.|#', inner[0].strip())
        return tmp[-1]
    return inner[0].strip()

def clean_coms(coms):
    #(?P<name>匹配模式)，反向应用时用(?P=name）
    p = re.sub('\<(?P<type>.*)\>(.*?)\<\/(?P=type)\>', dc, coms, flags=re.S)
    p = re.sub('\<(?P<type>.*)\>(.*?)\<\/(?P=type)\>', dc, p, flags=re.S)
    p = re.sub('\{\@code(.*?)\}', at_code, p, flags=re.S)
    p = re.sub('\{\@link(.*?)\}', at_link, p, flags=re.S)
    p = re.sub('\<p\>', '', p)
    p = re.sub(r'(\/|\*|\t|\n)', ' ', p)
    p = re.sub(r'(\s+)', ' ', p)
    return p.strip()