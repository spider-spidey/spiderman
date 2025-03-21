import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
weights_input_hidden = np.random.rand(2, 4)
weights_hidden_output = np.random.rand(4, 1)

for _ in range(10000):
    hidden_layer = sigmoid(np.dot(X, weights_input_hidden))
    output_layer = sigmoid(np.dot(hidden_layer, weights_hidden_output))

    error = y - output_layer
    d_output = error * sigmoid_derivative(output_layer)

    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer)

    weights_hidden_output += hidden_layer.T.dot(d_output) * 0.1
    weights_input_hidden += X.T.dot(d_hidden) * 0.1

print("Final Output:")
print(output_layer)
