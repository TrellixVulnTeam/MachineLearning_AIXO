import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/python-workspace/Machine Learning/data/", one_hot=True)

print(mnist)