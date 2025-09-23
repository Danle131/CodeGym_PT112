import itertools
instr = input("Nhập chuỗi cần nén: ")

def module_rle(chuoi):
    rle = ''
    for k, g in itertools.groupby(chuoi):
        rle += f'{len(list((g)))}{k}'
    return rle

def no_module_rle(chuoi):
    rle = ''
    dem = 1
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i + 1]:
            dem += 1
        else:
            rle += str(dem) + chuoi[i]
            dem = 1
    rle += str(dem) + chuoi[-1] 
    return rle

print(module_rle(instr))
print(no_module_rle(instr))
