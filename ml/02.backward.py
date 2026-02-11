import numpy as np

def forward_backward(X, W1, b1, W2, b2, y):
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
    def softmax(z):
        c = np.max(z, axis=-1, keepdims=True) # Prevent overflow
        exp_a = np.exp(z - c)
        out = exp_a / np.sum(exp_a, axis=-1, keepdims=True)
        return out
    
    # indexing
    def cross_entropy_loss(preds, gts):
        eps = 1e-7
        batch_size = preds.shape[0]
        loss = -np.mean(np.log(preds[np.arange(batch_size), gts] + eps))
        return loss
    
    batch_size = X.shape[0]
    
    Z1 = X @ W1 + b1          # Linear 1
    A1 = np.maximum(0, Z1)    # ReLU
    Z2 = A1 @ W2 + b2         # Linear 2
    probs = softmax(Z2)
    loss = cross_entropy_loss(probs, y)
    
    dZ2 = probs.copy()
    dZ2[np.arange(batch_size), y] -= 1
    dZ2 /= batch_size

    dW2 = A1.T @ dZ2
    db2 = np.sum(dZ2, axis=0)
    dA1 = dZ2 @ W2.T   # ← W2 사용

    dZ1 = dA1 * (Z1 > 0)

    dW1 = X.T @ dZ1
    db1 = np.sum(dZ1, axis=0)
    grads = {
        'dW1': dW1,
        'db1': db1,
        'dZ1': dZ1,
        'dA1': dA1,
        'dW2': dW2,
        'db2': db2,
        'dZ2': dZ2
    }

    return loss, grads

# # one-hot encoding
# def cross_entropy_loss(preds, gts):
#     eps = 1e-7
#     batch_size = preds.shape[0]
    
#     loss = -np.sum(gts * np.log(preds+ 1e-8)) / batch_size
#     return loss



if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(3, 4)
    W1 = np.random.randn(4, 5) * 0.01
    b1 = np.zeros(5)
    W2 = np.random.randn(5, 2) * 0.01
    b2 = np.zeros(2)
    y = np.array([0, 1, 0])  # 3개 샘플의 정답 class

    loss, grads = forward_backward(X, W1, b1, W2, b2, y)
    print(f"Loss: {loss:.4f}")
    print(f"dW2 shape: {grads['dW2'].shape}")  # (5, 2)
    print(f"dW1 shape: {grads['dW1'].shape}")  # (4, 5)




def feedforward(X, W1, b1, W2, b2):
    """
    X:  (N, D)
    W1: (D, H)
    b1: (H,)
    W2: (H, C)
    b2: (C,)
    """

    # Layer 1
    z1 = X @ W1 + b1          # (N, H)
    h1 = relu(z1)             # (N, H)

    # Layer 2
    z2 = h1 @ W2 + b2         # (N, C)
    probs = softmax(z2)       # (N, C)

    return probs
