# coding:utf-8
# ��tensorflow.examples.tutorials.mnist����ģ�顣����TensorFlowΪ�˽�ѧMNIST����ǰ���Ƶĳ���

from tensorflow.examples.tutorials.mnist import input_data

# ��MNIST_data/�ж�ȡMNIST���ݡ�������������ݲ�����ʱ�����Զ�ִ������

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)



# �鿴ѵ�����ݵĴ�С

print(mnist.train.images.shape)  # (55000, 784)

print(mnist.train.labels.shape)  # (55000, 10)



# �鿴��֤���ݵĴ�С

print(mnist.validation.images.shape)  # (5000, 784)

print(mnist.validation.labels.shape)  # (5000, 10)



# �鿴�������ݵĴ�С

print(mnist.test.images.shape)  # (10000, 784)

print(mnist.test.labels.shape)  # (10000, 10)



# ��ӡ����0��ͼƬ��������ʾ

print(mnist.train.images[0, :])