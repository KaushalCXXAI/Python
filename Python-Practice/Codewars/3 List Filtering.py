def filter_list(l):
    nl = []
    for i in l:
        if type(i) == int:
           nl.append(i)
    return nl 

print(filter_list(filter_list([1,'a','b',0,15])))