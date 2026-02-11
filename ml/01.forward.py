import numpy as np

def forward(X, W1, b1, W2, b2):
    """
    Args:
        X: input, shape (batch_size, input_dim)
        W1: first layer weights, shape (input_dim, hidden_dim)
        b1: first layer bias, shape (hidden_dim,)
        W2: second layer weights, shape (hidden_dim, output_dim)
        b2: second layer bias, shape (output_dim,)
    
    Returns:
        probs: softmax probabilities, shape (batch_size, output_dim)
    """
    # Linear
    z = np.matmul(X, W1)
    z = z + b1

    # LeRU
    z = np.maximum(0, z)

    # Linear
    z = np.matmul(z, W2)
    z = z + b2

    # Softmax
    c = np.max(z, axis=-1, keepdims=True) # Prevent overflow
    exp_a = np.exp(z - c)
    out = exp_a / np.sum(exp_a, axis=-1, keepdims=True)

    return out

if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(3, 4)      # batch=3, input_dim=4
    W1 = np.random.randn(4, 5)     # hidden_dim=5
    b1 = np.zeros(5)
    W2 = np.random.randn(5, 2)     # output_dim=2 (binary classification)
    b2 = np.zeros(2)

    probs = forward(X, W1, b1, W2, b2)
    print(probs.shape)  # (3, 2)
    print(probs.sum(axis=1))  # 각 row가 1.0에 가까워야 함