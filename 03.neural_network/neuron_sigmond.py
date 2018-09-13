import  math

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
    # ニューロンインスタンス
    neuron = Neuron()
    # 実行・・・ニューロン
    def commit(self,input_data):
        for data in input_data:
            self.neuron.setInput(data)
        return  self.neuron.getOutput()

neural_net = NeuralNetwork()
#total_data = [1.0,2.0,3.0] １に近い値
# total_data = [1.0,2.0,-3.0] 0.5
total_data = [-1.0,-2.0,-3.0]
# １に近い値
print(neural_net.commit(total_data))
