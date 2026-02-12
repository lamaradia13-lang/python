import torch

print("pytorch version:", torch.__version__)

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

z = x + y
print("y:", y)
print("x:", x)
print("x + y:", z)

model = torch.nn.Linear(1, 1)
los_fn = torch.nn.MSELoss
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    y_pred = model(x)
    los = los_fn(y_pred, y)
    optimizer.zero_grad()
    los.backward()
    optimizer.step

with torch.no_grad():
    new_x = torch.tensor([[4.0], [5.0]])
    predictions = model(new_x)
    print("prediction for 4 and 5:", predictions.flatten().tolist())

device = "cuda" if torch.cuda.is_available() else "cpu"
print("running on:", device)
