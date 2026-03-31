def lengthoflastword(s):
    words= s.stip().split()
    return len(words[-1])

s= 'hello world'
print(lengthoflastword(s))