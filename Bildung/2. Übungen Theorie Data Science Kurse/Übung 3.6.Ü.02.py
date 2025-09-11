import torch
import torch.nn as nn

class NN(nn.Module):
    def __init__(self, input_size, output_size):
        super(NN, self).__init__()
        self.flatten = nn.Flatten()
        self.network = nn.Sequential(
            nn.Linear(input_size, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, output_size)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.network(x)
        return logits
