# -*- coding: utf-8 -*-
"""Project_code_python_2276229_이연서.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K9MuUiugmmwkKLXnHC0KT7YqqmhMyVKh
"""

import random
import matplotlib.pyplot as plt

def generate_bitstream(probability, length):
    return [1 if random.random() < probability else 0 for _ in range(length)]

def calculate_probability(bitstream):
    return sum(bitstream) / len(bitstream)

# Lengths to be considered
lengths = list(range(50, 10001, 50))

# Probabilities
p_a = 1/2
p_b = 2/3

# Lists to store probabilities for each length
prob_a_list = []
prob_b_list = []

# Generate bitstreams and calculate probabilities
for length in lengths:
    bitstream_a = generate_bitstream(p_a, length)
    bitstream_b = generate_bitstream(p_b, length)

    prob_a = calculate_probability(bitstream_a)
    prob_b = calculate_probability(bitstream_b)

    prob_a_list.append(prob_a)
    prob_b_list.append(prob_b)

# Plotting the results
plt.xticks(np.arange(0, 11000, 1000))
plt.plot(lengths, prob_a_list, label='P(A)',marker='x',markersize=3)
plt.axhline(1/2,linestyle='--')
plt.plot(lengths, prob_b_list, label='P(B)',marker='o',markersize=3)
plt.axhline(2/3,linestyle='--')
plt.xlabel('Length')
plt.ylabel('Probability')
plt.legend()

plt.show()

import random
import matplotlib.pyplot as plt
import numpy as np  # Add this line to import numpy

def generate_bitstream(probability, length):
    return [1 if random.random() < probability else 0 for _ in range(length)]

def stochastic_computing(A, B):
    return [a & b for a, b in zip(A, B)]

def calculate_probability(bitstream):
    return sum(bitstream) / len(bitstream)

# Lengths to be considered
lengths = list(range(50, 10001, 50))

# Probabilities
p_a = 1/2
p_b = 2/3

# Lists to store probabilities for each length
prob_a_list = []
prob_b_list = []
prob_c_list = []

# Generate bitstreams A and B
bitstream_a = generate_bitstream(p_a, max(lengths))
bitstream_b = generate_bitstream(p_b, max(lengths))

# Calculate probabilities for A and B
for length in lengths:
    prob_a_list.append(calculate_probability(bitstream_a[:length]))
    prob_b_list.append(calculate_probability(bitstream_b[:length]))

# Perform stochastic computing to generate C
bitstream_c = stochastic_computing(bitstream_a, bitstream_b)

# Calculate probabilities for C
for length in lengths:
    prob_c_list.append(calculate_probability(bitstream_c[:length]))

prob_c_analytic_list = [p_a * p_b] * len(lengths)

# Plotting the results
plt.plot(lengths, prob_c_list, label='stochastic approach P(C)', marker='x', markersize=3)
plt.plot(lengths, prob_c_analytic_list, label='Analytic solution', linestyle='--')
plt.xticks(np.arange(0, 10000, 1000))
plt.yticks(np.arange(0.2, 0.6, 0.05))

plt.xlabel('Length')
plt.ylabel('Probability')
plt.legend()
plt.show()