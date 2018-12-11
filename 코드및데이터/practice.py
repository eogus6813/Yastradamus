import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from tensorflow.python.ops import nn_ops

tf.set_random_seed(777)

# train Parameters
seq_length = 2
data_dim = 16
hidden_dim = 10
output_dim = 1
learning_rate = 0.01
iterations = 1000

xy = np.loadtxt('2014dd.csv', delimiter=',')
x = xy
y = xy[:, [-1]]
#xy2 = np.loadtxt('2018dd.csv', delimiter=',')
#x2 = xy2
#y2 = xy2[:, [-1]]

dataX = []
dataY = []

for i in range(0,len(y)):
    _x = []
    tmp1 = x[i, 0:16]
    tmp2 = x[i, 16:32]
    _x.append(tmp1)
    _x.append(tmp2)
    _y = y[i]
    #print(_x, "->", _y)
    dataX.append(_x)
    dataY.append(_y)
print (dataX)

#dataX2 = []
#dataY2 = []

#for i in range(0,len(y2)):
#    _x = []
#    tmp1 = x2[i, 0:8]
#    tmp2 = x2[i, 8:16]
#    _x.append(tmp1)
#    _x.append(tmp2)
#    _y = y[i]
#    dataX2.append(_x)
#    dataY2.append(_y)

#train_size = int(len(dataY))
#test_size = len(dataY2)
#trainX, testX = np.array(dataX[0:train_size]), np.array(
#    dataX2[0:test_size])
#trainY, testY = np.array(dataY[0:train_size]), np.array(
#    dataY2[0:test_size])

# train/test split
train_size = int(len(dataY) * 0.7)
test_size = len(dataY) - train_size
trainX, testX = np.array(dataX[0:train_size]), np.array(
   dataX[train_size:len(dataX)])
trainY, testY = np.array(dataY[0:train_size]), np.array(
    dataY[train_size:len(dataY)])

# input place holders
X = tf.placeholder(tf.float32, [None, seq_length, data_dim])
Y = tf.placeholder(tf.float32, [None, 1])

# build a LSTM network
cell = tf.contrib.rnn.BasicLSTMCell(
    num_units=hidden_dim, state_is_tuple=True, activation=tf.tanh)
outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)

Y_pred = tf.contrib.layers.fully_connected(
    outputs[:, -1], output_dim, activation_fn = tf.nn.sigmoid)  # We use the last cell's output

# cost/loss
loss = tf.reduce_sum(tf.square(Y_pred - Y))  # sum of the squares
# optimizer
optimizer = tf.train.AdamOptimizer(learning_rate)
train = optimizer.minimize(loss)

# RMSE
targets = tf.placeholder(tf.float32, [None, 1])
predictions = tf.placeholder(tf.float32, [None, 1])
rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - predictions)))

cnt = []
for i in range(0,len(testY)+1):
    cnt.append(0)
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    
    # Training step
    for i in range(iterations):
        _, step_loss = sess.run([train, loss], feed_dict={
                                X: trainX, Y: trainY})
        print("[step: {}] loss: {}".format(i, step_loss))

    # Test step
    test_predict = sess.run(Y_pred, feed_dict={X: testX})
    rmse_val = sess.run(rmse, feed_dict={
                    targets: testY, predictions: test_predict})
    print("RMSE: {}".format(rmse_val))
    c = 0
    for i in range(1,len(testY)+1):
        if testY[i-1] >= 0.5 and test_predict[i-1] >= 0.5:
            c+=1
        elif testY[i-1] <= 0.5 and test_predict[i-1] <= 0.5:
            c+=1
        cnt[i] = float(c)
    for i in range(1,len(testY)+1):
        cnt[i] = cnt[i]/float(i)
        
    #print (test_predict)
    #print ("Accuracy: {}".format(float(float(cnt)/float(len(testY)))))
    # Plot predictions
    plt.plot(cnt)
    plt.xlabel("Game")
    plt.ylabel("Accuracy")
    plt.show()
