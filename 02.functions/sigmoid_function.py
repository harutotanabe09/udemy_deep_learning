import matplotlib.pyplot as plt
import  numpy as np
import  math

# シグモイド関数
def sigmoid(a):
    s = 1 / (1 + e ** -a)
    return s

e = math.e
# 0.1刻みの -8から8
dx = 0.1
x = np.arange(-8,8, dx)

# 1 / (1 + e ~ -a)
y_sig = sigmoid(x)

plt.plot(x,y_sig)
plt.show()
