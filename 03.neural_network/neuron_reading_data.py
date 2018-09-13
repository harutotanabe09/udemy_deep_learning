import  math
# ファイル読み込み

# シグモイド関数
def sigmoid(a):
    return 1 / (1 + math.exp(-a))

# ニューロン (setter,getter)
class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self,inq):
        self.input_sum += inq
        #print(self.input_sum)

    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return  self.output

# ニューラルネットワーク(ニューロンの出力）
class NeuralNetwork:
    # 重み
    w = [1.5,-2.5,-0.5]
    # ニューロンインスタンス
    neuron = Neuron()
    # 実行・・・ニューロン
    def commit(self,input_data):
        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
        self.neuron.setInput(input_data[2] * self.w[2])
        return self.neuron.getOutput()

# 基準点（データの範囲を0.0-1.1の範囲に収める）
refer_point_0 = 34.5
refer_point_1 = 137.5

# ファイル読み込み
trial_data = []
trial_data_file = open("inputdata.txt","r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([float(line[0]) - refer_point_0 , float(line[1]) - refer_point_1])
trial_data_file.close()
print(trial_data)

# ニューラルネットワークインスタンス
neural_net = NeuralNetwork()
#total_data = [1.0,2.0,3.0]
#print(neural_net.commit(total_data))
