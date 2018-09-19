import  math
import  matplotlib.pyplot as plt

#実行しても変わらない中途半端コード
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
    w_im = [[0.496,0.512] , [-0.501,0.998],[0.498,-0.502]]
    w_mo = [0.121,-0.4994,0.200]
    # ニューロンインスタンス
    #neuron = Neuron()

    #各層の入力層
    input_layer = [0.0,0.0,1.0]
    middle_layer = [ Neuron(), Neuron(),1.0]
    output_layer =  Neuron()

    # 実行・・・ニューロン
    def commit(self,input_data):
        self.neuron.reset()
        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
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


# ニューラルネットワークインスタンス
neural_net = NeuralNetwork()

# 実行
position_tokyo = [[], []]
position_kanagawa = [[], []]
for data in trial_data:
    if neural_net.commit(data) < 0.5:
        position_tokyo[0].append(data[1]+ refer_point_1)
        position_tokyo[1].append(data[0] + refer_point_0)
    else:
        position_kanagawa[0].append(data[1] + refer_point_1)
        position_kanagawa[1].append(data[0] + refer_point_0)

#プロット scatterは散布図
plt.scatter(position_kanagawa[0],position_kanagawa[1],c="red",label="Kanagawa",marker="+")
plt.scatter(position_tokyo[0],position_tokyo[1],c="blue",label="Tokyo",marker="+")

plt.legend()
plt.show()

#total_data = [1.0,2.0,3.0]
#print(neural_net.commit(total_data))
