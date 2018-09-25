from sklearn import svm

# 株価のデータ読み込み （テキストの読み込みのみ）
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




