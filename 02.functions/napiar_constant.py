import matplotlib.pyplot as plt
import  numpy as np
import  math

# ネイピアス関数
e = math.e
# ネイピアス関数 2.7くらい
print(e)

# 0.1刻みの -5から5
dx = 0.1
x = np.arange(-5,5, dx)

y_2 = 2 ** x
y_e = e ** x
y_3 = 3 ** x

# y = (e ~(x+dx) - e~x) /dx] 傾きが同じになる特徴を持つ
y_d = (e**(x+dx) - e**x) /dx

plt.plot(x,y_2)
plt.plot(x,y_e)
plt.plot(x,y_3)
plt.plot(x,y_d)
plt.show()
