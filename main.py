import torch

data = torch.load("wine-red.pt")
data = data[torch.randperm(data.shape[0])]

x, y = data[:, :-1], data[:, -1:]
x_train, y_train = x[:1000], y[:1000]
x_val, y_val = x[1000:], y[1000:]

mean = x_train.mean(0)
std = x_train.std(0)
x_train = (x_train - mean) / std
x_val = (x_val - mean) / std

torch.save(x_train, "x_train.pt")
torch.save(y_train, "y_train.pt")
torch.save(x_val, "x_val.pt")
torch.save(y_val, "y_val.pt")