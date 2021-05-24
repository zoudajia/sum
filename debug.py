import read_write as rw
import split_strings as ss


lang = 'java'
path = "/data/zdj/vocab/codesearchnet/" + lang + "/"

funs = rw.read_file(path + "funss")
print(len(funs))

'''
for k,v in enumerate(funs):
    if str(k) != v.split('\t')[-1].strip():
        print(k, v)
        break'''
        
print(funs[34367])
print(funs[34368])
print(funs[34369])
print(funs[34370])