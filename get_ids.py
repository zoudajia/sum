import javalang
import read_write as rw
import split_strings as ss


lang = "java"  # 修改语言

path = "/data/zdj/vocab/codesearchnet/" + lang + "/"
funs = rw.read_file(path + "funs")

ids = set()
strs = set()
error = []
nums = set()
for k,v in enumerate(funs):
    try:
        tokens = javalang.tokenizer.tokenize(v)
        for i in tokens:
            if type(i) == javalang.tokenizer.Identifier:
                tmp = ss.split_strings(i.value)
                ids.update(set(tmp))
            elif type(i) == javalang.tokenizer.String:
                tmp = ss.split_strings(i.value)
                ids.update(set(tmp))
            elif type(i) in [javalang.tokenizer.BinaryInteger, javalang.tokenizer.DecimalFloatingPoint, javalang.tokenizer.DecimalInteger, javalang.tokenizer.FloatingPoint, javalang.tokenizer.HexFloatingPoint, javalang.tokenizer.HexInteger, javalang.tokenizer.Integer, javalang.tokenizer.OctalInteger]:
                nums.add(i.value)
    except:
        error.append(k)

rw.write_set2file(path + "ids", list(ids))
rw.write_set2file(path + "strs", list(strs))
rw.write_set2file(path + "nums", list(nums))