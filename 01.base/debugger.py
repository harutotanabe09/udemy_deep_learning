a = 7
b = 3

# デバックテスト
def function1(c, d):
    e = c + d
    e += c
    e += d
    return e


f = function1(a, b)
print(f)
