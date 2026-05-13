import torch
import torch.nn as nn
import numpy as np

# ---- Data ----
N = 1000
coords = np.random.uniform(-1, 1, size=(N, 2))
values = np.exp(-(coords[:, 0]**2 + coords[:, 1]**2) / 0.5)


X = torch.tensor(coords, dtype=torch.float32)
# unsqueeze(1) (N, ) -> (N, 1)
y = torch.tensor(values, dtype=torch.float32).unsqueeze(1)

# ---- Model ----
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
        )

    def forward(self, x):
        return self.net(x)

model = MLP()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

# Current training is full batch, if it cause memory issue, we need to implement mini-batch
# ---- Training ----
for epoch in range(500):
    # We need to zero the gradients.
    optimizer.zero_grad()
    pred = model(X)
    loss = loss_fn(pred, y)

    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f"Epoch {epoch}: loss = {loss.item():.6f}")