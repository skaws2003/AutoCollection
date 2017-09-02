import tensorflow as tf

"""
This is a deep learning network for solving minigame in maplestory.
"""

"""
Graph initialization
"""
meta_path = 'D:/OneDrive/MapleData/tfrecords/Arrow_classifier.meta'
network_path = 'D:/OneDrive/MapleData/tfrecords/Arrow_classifier'

#Start
print("ArrowNet:: Loading graph...")

#Placeholder for input image
X = tf.placeholder(tf.float32,[None,28,28,3]) 

#Variables needed for convolutional layers
K = 8
L = 16
W1 = tf.Variable(tf.truncated_normal([5,5,3,K], stddev = 0.5))
B1 = tf.Variable(tf.truncated_normal([K], stddev = 0.02, mean = 0.1))
W2 = tf.Variable(tf.truncated_normal([5,5,K,L], stddev = 0.5))
B2 = tf.Variable(tf.truncated_normal([L], stddev = 0.02, mean = 0.1))

#Variables needed for densely connected layers
N = 100
P = 40
W4 = tf.Variable(tf.truncated_normal([7*7*L,N], stddev = 0.5))
B4 = tf.Variable(tf.truncated_normal([N], stddev = 0.02, mean = 0.1))
W5 = tf.Variable(tf.truncated_normal([N,P], stddev = 0.5))
B5 = tf.Variable(tf.truncated_normal([P], stddev = 0.02, mean = 0.1))
W6 = tf.Variable(tf.truncated_normal([P,4], stddev = 0.5))
B6 = tf.Variable(tf.truncated_normal([4], stddev = 0.02, mean=0.1))

#Convolutional networks
Y1 = tf.nn.relu(tf.nn.conv2d(X, W1, strides=[1,2,2,1], padding = 'SAME') + B1)
Y2 = tf.nn.relu(tf.nn.conv2d(Y1, W2, strides=[1,2,2,1], padding = 'SAME') + B2)

#Neural networks
YY = tf.reshape(Y2, shape=[-1, 7*7*L])
Y4 = tf.nn.relu(tf.matmul(YY,W4) + B4)
Y5 = tf.nn.relu(tf.matmul(Y4,W5) + B5)
Y = tf.matmul(Y5,W6) + B6

#Placeholder for the correct answer
#Y_answ = tf.placeholder(tf.float32, [None,4])

Y_softmax = tf.nn.softmax(Y)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

trained_network = tf.train.import_meta_graph(meta_path)
trained_network.restore(sess, network_path)

print("ArrowNet:: Loading success")