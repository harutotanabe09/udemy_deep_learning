import matplotlib.pyplot as plt
import  numpy as np
import  math

# シグモイド関数2
def sigmoid(a):
    s = 1 / (1 + e ** -a)
    return s

# シグモイド関数の微分
def d_sigmoid(a):
    d = sigmoid(a)* (1-sigmoid(a))
    return d

e = math.e
# 0.1刻みの -8から8
dx = 0.1
x = np.arange(-8,8, dx)

# シグモイド関数
y_sig = sigmoid(x)
# シグモイド関数の傾き：微分
y_dsig = (sigmoid(x + dx) - sigmoid(x)) / dx
# シグモイド関数の微分 上と同じグラフが書ける！
#dy_dsig = sigmoid(x) * (1-sigmoid(x))
dy_dsig = d_sigmoid(x)

plt.plot(x,y_sig,label = "sigmoid")
plt.plot(x,y_dsig,label = "d_sigmoid")
plt.plot(x,dy_dsig,label = "dy_sigmoid_x")
plt.legend()
plt.show()
