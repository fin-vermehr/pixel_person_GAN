import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as f
import torch.optim as optim

torch.manual_seed(1)

V_data = [1., 2., 3.]
V = torch.tensor(V_data)
print(V)

x = torch.tensor([1., 2., 3], requires_grad=True)
y = torch.tensor([4., 5., 6], requires_grad=True)
z = x + y
print(z)
print(z.grad_fn)
