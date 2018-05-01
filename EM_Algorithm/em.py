# coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal
from numpy import linalg as LA

data_number_1 = 100
data_number_2 = 150
data_number_3 = 200

toy_data = []
for i in range(data_number_1):
    toy_data.append(normal(50, 10))
for i in range(data_number_2):
    toy_data.append(normal(0, 5))
for i in range(data_number_3):
    toy_data.append(normal(100, 10))


toy_data = np.array(toy_data)


plt.subplot(2, 1, 1)
plt.hist(toy_data, bins=50)


def normal_pdf(x, mu, sigma):
    return (1.0 / np.sqrt(2 * np.pi * (sigma))) * np.exp(- (x - mu)**2 / sigma)


class theta():
    def __init__(self, cluster_number):
        self.pi = np.array([1.0 / cluster_number]*cluster_number)
        self.mu = np.array(np.random.rand(cluster_number) * 10.0)
        self.sigma = np.array([10.0]*cluster_number)
        self.cluster_number = cluster_number


def gamma(x, theta):
    n = len(x)
    k = theta.cluster_number
    G = np.empty((n, k))
    for t in range(n):
        for i in range(k):
            a = theta.pi[i] * normal_pdf(x[t], theta.mu[i], theta.sigma[i])
            if a < 1.0e-20:
                a = 0.0
            G[t][i] = a
        if np.sum(G[t]) == 0.0:
            G[t] = np.array([1.0 / k] * k)
        else:
            G[t] = G[t] / np.sum(G[t])
    return G


def em(x, theta_old, eps):
    delta = float("inf")
    n = len(x)
    j = 0
    cluster_number = theta_old.cluster_number
    while delta > eps:
        theta_new = theta(cluster_number)
        G = gamma(x, theta_old)
        G = G.T
        for i in range(cluster_number):
            a = np.sum(G[i])
            b = np.sum(G[i] * x)
            theta_new.pi[i] = (1.0 / n) * a
            theta_new.mu[i] = (1.0 / a) * b
            theta_new.sigma[i] = (1.0 / a) * np.sum(G[i] * (x - theta_new.mu[i]) ** 2)
        delta = LA.norm(theta_new.mu - theta_old.mu)
        theta_old = theta_new
        j += 1
    print("回った回数は", j, "回")
    return theta_new


x = toy_data
cluster_number = 4
initial_theta = theta(cluster_number)
a = em(x, initial_theta, 0.005)
for i in range(a.cluster_number):
    print("重み付けは", a.pi[i], "で N(", a.mu[i], ",", a.sigma[i], ")と推定")

x = range(-10, 120)
plt.subplot(2, 1, 2)
for i in range(a.cluster_number):
        y = [a.pi[i] * normal_pdf(x_j, a.mu[i], a.sigma[i]) for x_j in x]
        plt.plot(x, y)
plt.show()
