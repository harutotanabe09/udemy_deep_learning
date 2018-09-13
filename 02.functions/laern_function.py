import matplotlib.pyplot as plt
import  numpy as np

# 1次関数の描画
# xは0から10の値
x = np.arange(0,10,0.1);
print(x)
# y = 2x + 1
y = 2 * x + 1
print(y)
# 1次関数の描画
plt.plot(x,y)
plt.show()