import  math
import  matplotlib.pyplot as plt

# 教師データの読み込み
# 分類
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

    def reset(self):
        self.output = 0
        self.input_sum = 0

# ニューラルネットワーク(ニューロンの出力）
class NeuralNetwork:
    # 重み
    w_im = [[0.496, 0.512], [-0.501, 0.998], [0.498, -0.502]]
    w_mo = [0.121, -0.4996, 0.200]
    # ニューロンインスタンス
    #neuron = Neuron()

    #各層の入力層
    input_layer = [0.0,0.0,1.0]
    middle_layer = [ Neuron(), Neuron(),1.0]
    output_layer =  Neuron()

    # 実行・・・ニューロン
    def commit(self,input_data):
        #各層リセット
        self.input_layer[0] = input_data[0]
        self.input_layer[1] = input_data[1]

        self.middle_layer[0].reset()
        self.middle_layer[1].reset()

        self.output_layer.reset()

        # 入力層→中間層
        self.middle_layer[0].setInput(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].setInput(self.input_layer[1] * self.w_im[1][0])
        self.middle_layer[0].setInput(self.input_layer[2] * self.w_im[2][0])

        self.middle_layer[1].setInput(self.input_layer[0] * self.w_im[0][1])
        self.middle_layer[1].setInput(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].setInput(self.input_layer[2] * self.w_im[2][1])

        # 中間層→出力層
        self.output_layer.setInput(self.middle_layer[0].getOutput() * self.w_mo[0])
        self.output_layer.setInput(self.middle_layer[1].getOutput() * self.w_mo[1])
        self.output_layer.setInput(self.middle_layer[2] * self.w_mo[2])

        return self.output_layer.getOutput()

# 基準点（データの範囲を0.0-1.1の範囲に収める）
refer_point_0 = 34.5
refer_point_1 = 137.5

# ファイル読み込み
trial_data = []
trial_data_file = open("inputdata.txt","r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([float(line[0]) - refer_point_0 , float(line[1]) - refer_point_1 ,int(line[2])])
trial_data_file.close()

print (trial_data)

# ニューラルネットワークインスタンス
neural_net = NeuralNetwork()

