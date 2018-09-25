from sklearn import svm

# 株価のデータ読み込み（テキストの読み込み）
stock_data = []
stock_data_file = open("stock_price.txt")
for line in stock_data_file:
    line = line.rstrip()
    stock_data.append(float(line))
stock_data_file.close()

# データ確認
# print(stock_data) ファイルの中身
count_s = len(stock_data)
# print(count_s)　カウント

# 株価の上昇率を算出　おおよそ -1.0 から 1.0に収まるように
mod_data = []
for i  in range(1,count_s):
    # 上昇率を計算（前日と当日の株価から算出）
    mod_data.append(float(stock_data[i] - stock_data[i - 1])/ float(stock_data[i-1]) * 20)
print(mod_data)
count_m = len(mod_data)
print(count_m)

# 前日までの4連続の上昇率のデータ
successive_data = []
# 正解値 価格上昇: 1 価格低下: 0
answers = []
for i in range(4, count_m):
    successive_data.append([mod_data[i-4], mod_data[i-3], mod_data[i-2], mod_data[i-1]])
    if mod_data[i] > 0:
        answers.append(1)
    else:
        answers.append(0)
# print(successive_data) # ４連続部のデータ確認
# print(answers) # 上昇か否か

# データ数
n = len(successive_data)
print (n)
m = len(answers)
print (m)

# 線形サポートベクターマシーン
clf = svm.LinearSVC()
# サポートベクターマシーンによる訓練 （データの75%を訓練に使用）
clf.fit(successive_data[:n*75//100], answers[:n*75//100])

# テスト用データ
# 正解
expected = answers[-n*25//100:]
# 予測
predicted = clf.predict(successive_data[-n*25//100:])

# 末尾の10個を比較
print (expected[-10:])
print (list(predicted[-10:]))

# 正解率の計算
correct = 0.0
wrong = 0.0
for i in range(n*25//100):
    if expected[i] == predicted[i]:
        correct += 1
    else:
        wrong += 1
print ("正解率: " + str(correct / (correct+wrong) * 100) + "%")