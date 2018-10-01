from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

# Mnistに使うデータセットをインポートする
mnist = input_data.read_data_sets('/tmp/tensorflow/mnist/input_data',
                                  one_hot=True)

# グラフの作成
x = tf.placeholder(tf.float32, [None, 784])  # 入力するPlaceholder
W = tf.Variable(tf.zeros([784, 10]))  # 重み
b = tf.Variable(tf.zeros([10]))  # バイアス
y = tf.matmul(x, W) + b  # 内積計算とバイアスの加算

# 正解ラベル用のplaceholeder
y_ = tf.placeholder(tf.float32, [None, 10])

# 損失の計算方法と、オプティマイザーを定義
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# セッションの作成と初期化
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

# 学習部(1000回学習)
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# テスト部
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                    y_: mnist.test.labels}))