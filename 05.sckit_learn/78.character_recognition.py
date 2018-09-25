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
# for i in range(10):
#     plt.subplot(2 , 5 , i+1)
#     plt.imshow(image[i], cmap = plt.cm.gray_r,interpolation="nearest")
#     plt.axis("off")
#     # 正解値を表示
#     plt.title("training " + str(labels[i]))
#     plt.show()

# サポートベクターマシン gamma C:誤認識の強度
clf = svm.SVC(gamma=0.001,C=100.0)
# サポートベクターマシンの訓練 （６割をデータ使用、４割は検証用)
clf.fit(digits.data[:n*6//10 ], digits.target[:n*6//10])

# 最後の１０個のデータを予測
# print(digits.target[-10:])
# # 予測を行う
# print(clf.predict(digits.data[-10:]))

#　残りの４割の画像、数字を読み取る
# 正解
expected = digits.target[-n*4//10:]
# 予測
predicted = clf.predict(digits.data[-n*4//10:])
# 正解率
print(metrics.classification_report(expected, predicted))
# 誤認識のマトリックス
print(metrics.confusion_matrix(expected, predicted))

# 予測と画像の対応（一部）
images = digits.images[-n*4//10:]
for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.axis("off")
    plt.imshow(images[i], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title("Guess: " + str(predicted[i]))
plt.show()