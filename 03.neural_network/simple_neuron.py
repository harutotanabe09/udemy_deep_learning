
# ニューロン
class Neuron:
    input_sum = 0.0

    def setInput(self,inq):
        self.input_sum += inq
        print(self.input_sum)

# ニューラルネットワーク(ニューロンの出力）
class NeuralNetwork:
    # ニューロンインスタンス
    neuron = Neuron()
    # 実行・・・ニューロン
    def commit(self,input_data):
        for data in input_data:
            self.neuron.setInput(data)

neural_net = NeuralNetwork()
total_data = [1.0,2.0,3.0]
neural_net.commit(total_data)
