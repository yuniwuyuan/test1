count=0
txt=[]
def countotal(*x):
    k=x[0]
    global count
    for l in k:
        if 'auto' in l:#32个关键字查询
            count+=1
        if 'break' in l:
            count+=1
        if 'case' in l:
            count+=1
        if 'const' in l:
            count+=1
        if 'continue' in l:
            count+=1
        if 'default' in l:
            count+=1
        if 'double' in l:
            count+=1
        elif 'do' in l:
            count+=1
        if 'else' in l:
            count+=1
        if 'enum' in l:
            count+=1
        if 'extern' in l:
            count+=1
        if 'float' in l:
            count+=1
        if 'for' in l:
            count+=1
        if 'goto' in l:
            count+=1
        if 'if' in l:
            count+=1
        if 'int' in l:
            count+=1
        if 'long' in l:
            count+=1
        if 'register' in l:
            count+=1
        if 'return' in l:
            count+=1
        if 'short' in l:
            count+=1
        if 'signed' in l:
            count+=1
        if 'sizeof' in l:
            count+=1
        if 'static' in l:
            count+=1
        if 'struct' in l:
            count+=1
        if 'switch' in l:
            count+=1
        if 'typedef' in l:
            count+=1
        if 'union' in l:
            count+=1
        if 'unsigned' in l:
            count+=1
        if 'void' in l:
            count+=1
        if 'volatile' in l:
            count+=1
        if 'while' in l:
            count+=1
def main():
    file_path=input('文件地址：')
    with open(file_path, encoding='utf-8') as file_obj:
        for line in file_obj:#按行读入文件
            line = line.replace('\n',"").replace(' ',"").replace('\xa0',"")
            txt.append(line)
#print(txt)测试时检验文件是否读入成功
if __name__ == '__main__':
    main()
countotal(txt)
lines.close()
print('total num: ',count)