from sklearn import datasets
from sklearn import svm
from sklearn import  metrics
import matplotlib.pyplot as plt

# 数字データ読み込み
digits = datasets.load_digits()

# データ形式の読み込み 手書き画像データのあつまり：1797
# print(digits.data)
# print(digits.data.shape)

# データの数
n = len(digits.data)

# 画像と正解データ
image = digits.images
labels = digits.target

# トレーニングデータの表示
for i in range(10):
    plt.subplot(2 , 5 , i+1)
    plt.imshow(image[i], cmap = plt.cm.gray_r,interpolation="nearest")
    plt.axis("off")
    # 正解値を表示
    plt.title("training " + str(labels[i]))
    plt.show()
