"""
回溯法输出一个序列的全排列
"""

a = ['a', 'b', 'c']

result = ""
def f(i,result,item):
    if i==len(item) :
        print('"'+result+'"')
        return
    
    # 第i个元素不选
    f(i+1,result,item)
    # 第i个元素选
    f(i+1,result+item[i],item)

def f1(i,result,item):
    if i == len(item):
        print('"'+result+'"')
        return
    
    # 第i个元素选
    f1(i+1, result+item[i], item)

    # 第i个元素不选
    f1(i+1, result, item)

f1(0,result,a)